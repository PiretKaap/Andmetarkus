import io
import json
import math
import pandas as pd
import numpy as np

# Data sources
PRICES_XLSX = 'Data_Sources/Hinnakiri.xlsx'
TREE_NAMES_XLSX = 'Data_Sources/Puu_nimetused_EE_ENG.xlsx'
REL_HEIGHTS_XLSX = 'Data_Sources/Suhtelised_tugikõrgused.xlsx'
VOLUME_DIST_XLSX = 'Data_Sources/Mahutabel.xlsx'


def _load_default_prices() -> dict:
    df = pd.read_excel(PRICES_XLSX)
    need = {'Sortiment', 'Hind (€/tm)'}
    if not need.issubset(df.columns):
        raise ValueError(f"Hinnakirja veerud puuduvad: {need}")
    return dict(df[['Sortiment', 'Hind (€/tm)']].values)


def _load_prices_from_xlsx_bytes(xlsx_bytes: bytes) -> dict:
    df = pd.read_excel(io.BytesIO(xlsx_bytes))
    need = {'Sortiment', 'Hind (€/tm)'}
    if not need.issubset(df.columns):
        raise ValueError(f"Üleslaetud Excel peab sisaldama veerge: {need}")
    df['Hind (€/tm)'] = pd.to_numeric(df['Hind (€/tm)'], errors='coerce')
    if df['Hind (€/tm)'].isna().any():
        raise ValueError("Veerus 'Hind (€/tm)' on mittearvulisi väärtusi.")
    if (df['Hind (€/tm)'] < 0).any():
        raise ValueError("Hinnad ei tohi olla negatiivsed.")
    return dict(df[['Sortiment', 'Hind (€/tm)']].values)


def _build_maht_hind_kokku_from_json(json_bytes: bytes) -> pd.DataFrame:
    tree_name = pd.read_excel(TREE_NAMES_XLSX)
    relative_heights = pd.read_excel(REL_HEIGHTS_XLSX)
    log_volume_distribution = pd.read_excel(VOLUME_DIST_XLSX)

    if isinstance(json_bytes, (bytes, bytearray, memoryview)):
        text = bytes(json_bytes).decode('utf-8', errors='replace')
    elif isinstance(json_bytes, str):
        text = json_bytes
    else:
        text = bytes(json_bytes).decode('utf-8', errors='replace')
    data = json.loads(text)

    stands = data.get('stands')
    if not stands:
        raise ValueError("JSON ei sisalda 'stands' massiivi.")

    rows = []
    for r in stands:
        area = r.get("total_area_ha", 0) or 0
        def rec(name_eng, h_key, d_key, v_key):
            v_ha = r.get(v_key)
            if v_ha is None:
                return
            rows.append({
                "Eraldise nr": r.get("stand_number"),
                "Puuliik": name_eng,
                "Kõrgus m": r.get(h_key),
                "Diameeter cm": r.get(d_key),
                "Pindala ha": area,
                "Tihedus m3/ha": v_ha,
                "Tagavara m3": area * v_ha
            })
        rec("Pine", "pine_bam_height_m", "pine_bam_dbh_cm", "pine_total_volume_m3_ha")
        rec("Spruce", "spruce_bam_height_m", "spruce_bam_dbh_cm", "spruce_total_volume_m3_ha")
        rec("Birch", "birch_bam_height_m", "birch_bam_dbh_cm", "birch_total_volume_m3_ha")
        rec("Other Deciduous", "other_deciduous_bam_height_m", "other_deciduous_bam_dbh_cm", "other_deciduous_total_volume_m3_ha")

    if not rows:
        raise ValueError("JSON-ist ei saadud ridu.")

    df = pd.DataFrame(rows)
    df = pd.merge(df, tree_name, left_on='Puuliik', right_on='Name_ENG', how='left')

    df['Suhteline tugikõrgus'] = np.nan
    for i, row in df.iterrows():
        name_ee = row.get('Name_EE')
        d = row.get('Diameeter cm')
        try:
            h24_val = relative_heights.loc[relative_heights['d'] == d, name_ee]
            if not h24_val.empty:
                df.at[i, 'Suhteline tugikõrgus'] = h24_val.values[0]
        except Exception:
            pass

    def _calc_h24(r):
        h = r.get('Kõrgus m')
        s = r.get('Suhteline tugikõrgus')
        if pd.notna(h) and pd.notna(s) and s != 0:
            val = int(math.ceil(h / s))
            return 16 if val < 16 else val
        return np.nan
    df['h24'] = df.apply(_calc_h24, axis=1).astype('Int64')

    def diameter_category(d):
        if pd.isna(d):
            return None
        if 5 <= d <= 52:
            return ((int(d) + 3) // 4) * 4
        if d > 52:
            return 52
        return None
    df['Diameetri klass'] = df['Diameeter cm'].apply(diameter_category).astype('Int64')

    df['Sortimendi jaotusklass'] = (
        df['Diameetri klass'].astype(str) + df['Name_EE'].astype(str) + df['h24'].astype(str)
    )

    merged = pd.merge(
        df, log_volume_distribution,
        left_on='Sortimendi jaotusklass',
        right_on='d klass+pl+h24 x m',
        how='inner'
    )

    for c in ['palk', 'peenp', 'paber', 'küte', 'jäätmed']:
        merged[c] = merged[c] * merged['Tagavara m3']

    merged = merged.drop(columns=['d klass+pl+h24 x m', 'kõrgus', 'kokku', 'Name_ENG'], errors='ignore')

    mappings = [
        ("Ma palk", ("MA","palk")),
        ("Ku palk", ("KU","palk")),
        ("Ks palk/pakk", ("KS","palk")),
        ("Teised liigid/Lv palk", ("LV","palk")),
        ("Ma peenpalk", ("MA","peenp")),
        ("Ku peenpalk", ("KU","peenp")),
        ("Ma paberipuit", ("MA","paber")),
        ("Ku paberipuit", ("KU","paber")),
        ("Ks paberipuit", ("KS","paber")),
        ("Küttepuit", (None,"küte")),
        ("Jäätmed", (None,"jäätmed")),
    ]
    out_rows = []
    for sortiment, (name_ee, col) in mappings:
        if name_ee:
            vol = merged.loc[merged["Name_EE"] == name_ee, col].sum()
        else:
            vol = merged[col].sum()
        out_rows.append({"Sortiment": sortiment, "Maht (tm)": float(vol), "Hind (€)": 0.0})

    mhk = pd.DataFrame(out_rows)
    mhk.loc[len(mhk)] = {
        "Sortiment": "Kokku",
        "Maht (tm)": float(mhk["Maht (tm)"].sum()),
        "Hind (€)": 0.0
    }
    mhk["Maht (tm)"] = mhk["Maht (tm)"].round(1)
    return mhk


def calculate_wood_prices(data: dict) -> dict:
    if data is None:
        raise ValueError("Tühjad sisendandmed.")

    costs = data.get('costs') or {}
    komplekt = float(costs.get('komplekt', 0) or 0)
    transport = float(costs.get('transport', 0) or 0)
    alghind_pct = float(costs.get('alghind', 0) or 0)

    if isinstance(data.get('xlsxFileContent'), (bytes, bytearray, memoryview)):
        prices = _load_prices_from_xlsx_bytes(data['xlsxFileContent'])
    else:
        prices = data.get('prices') or {}
        if not prices:
            prices = _load_default_prices()

    if data.get('jsonFileContent') is not None:
        mhk = _build_maht_hind_kokku_from_json(data['jsonFileContent'])
    else:
        return {
            "Maht kokku": 0.0,
            "Hind kokku": 0.0,
            "Kulud (jäätmeteta)": 0.0,
            "Tulud-kulud (jäätmeteta)": 0.0,
            "Soovituslik alghind": 0.0
        }

    def _norm(s): return str(s).strip().lower()
    alias = {
        "teised liigid/lv palk": "lv palk",
        "teised liigid paberipuit": "hb paberipuit",
    }
    prices_norm = {_norm(k): float(v) for k, v in prices.items()}

    mask = mhk["Sortiment"] != "Kokku"
    keys = mhk.loc[mask, "Sortiment"].map(_norm).map(lambda k: alias.get(k, k))
    price_series = keys.map(prices_norm).fillna(0.0)
    mhk.loc[mask, "Hind (€)"] = mhk.loc[mask, "Maht (tm)"].values * price_series.values

    hind_kokku = float(mhk.loc[mask, "Hind (€)"].sum())
    maht_kokku = float(mhk.loc[mhk["Sortiment"] == "Kokku", "Maht (tm)"].iloc[0])
    maht_jaatmeteta = float(mhk.loc[~mhk["Sortiment"].isin(["Jäätmed", "Kokku"]), "Maht (tm)"].sum())

    kulud_tm = komplekt + transport
    kulud_jaatmeteta = maht_jaatmeteta * kulud_tm
    tulud_kulud_jaatmeteta = hind_kokku - kulud_jaatmeteta
    soovituslik_alghind = tulud_kulud_jaatmeteta * (1 - alghind_pct / 100.0)

    return {
        "Maht kokku": round(maht_kokku, 1),
        "Hind kokku": round(hind_kokku, 1),
        "Kulud (jäätmeteta)": round(kulud_jaatmeteta, 1),
        "Tulud-kulud (jäätmeteta)": round(tulud_kulud_jaatmeteta, 1),
        "Soovituslik alghind": round(soovituslik_alghind, 1)
    }
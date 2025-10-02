function getNum(id, def = 0) {
  const el = document.getElementById(id);
  if (!el) return def;
  const v = parseFloat(el.value);
  return Number.isFinite(v) ? v : def;
}

function readAsBase64(file) {
  return new Promise((resolve, reject) => {
    const fr = new FileReader();
    fr.onloadend = () => resolve(String(fr.result).split(',')[1]); // strip data:...;base64,
    fr.onerror = reject;
    fr.readAsDataURL(file);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('calculate-btn');
  const results = document.getElementById('results-text');
  if (!btn || !results) return;

  btn.addEventListener('click', async () => {
    results.textContent = 'Arvutan...';

    const payload = {
      costs: {
        komplekt: getNum('komplekt', 0),
        transport: getNum('transport', 0),
        alghind: getNum('alghind', 0),
      },
      prices: {
        'Ma palk': getNum('ma_palk', 0),
        'Ku palk': getNum('ku_palk', 0),
        'Ks palk/pakk': getNum('ks_palk', 0),
        'Lv palk': getNum('lv_palk', 0),
        'Ma peenpalk': getNum('ma_peenpalk', 0),
        'Ku peenpalk': getNum('ku_peenpalk', 0),
        'Ma paberipuit': getNum('ma_paberipuit', 0),
        'Ku paberipuit': getNum('ku_paberipuit', 0),
        'Ks paberipuit': getNum('ks_paberipuit', 0),
        'Hb paberipuit': getNum('hb_paberipuit', 0),
        'Küttepuit': getNum('kutt', 0),
        'Jäätmed': getNum('jaatmed', 0),
      }
    };

    const xlsx = document.getElementById('xlsx-upload')?.files?.[0];
    const jsonf = document.getElementById('json-upload')?.files?.[0];
    if (xlsx) payload.xlsxFileContent = await readAsBase64(xlsx);
    if (jsonf) payload.jsonFileContent = await readAsBase64(jsonf);

    try {
      const r = await fetch('/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const res = await r.json();
      if (!r.ok || res.error) throw new Error(res.error || `HTTP ${r.status}`);

      // Soovitud kuvamisjärjekord
      const desiredOrder = [
        'Maht kokku',
        'Hind kokku',
        'Kulud (jäätmeteta)',
        'Tulud-kulud (jäätmeteta)',
        'Soovituslik alghind'
      ];
      // Esiteks soovitud võtmed, siis ülejäänud
      const orderedKeys = [
        ...desiredOrder.filter(k => Object.prototype.hasOwnProperty.call(res, k)),
        ...Object.keys(res).filter(k => !desiredOrder.includes(k))
      ];

      const html = orderedKeys.map(k =>
        `<div class="flex justify-between py-1">
           <span class="font-semibold">${k}:</span>
           <span>${res[k]}</span>
         </div>`
      ).join('');
      results.innerHTML = html || 'Tulemus puudub.';
    } catch (e) {
      results.innerHTML = `<span class="text-red-600">Viga: ${e.message}</span>`;
    }
  });
});
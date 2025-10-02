from flask import Flask, render_template, request, jsonify
from Forest_value_calculator import calculate_wood_prices
import base64

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')

@app.route('/')
def home():
    return render_template('Forest_value_calculator_ui.html')

@app.route('/health')
def health():
    return 'ok', 200

@app.route('/calculate', methods=['POST'])
def calculate():
    if not request.is_json:
        return jsonify({"error": "Päringu sisu peab olema JSON."}), 400

    data = request.get_json() or {}

    # Decode base64 files from the browser (if provided)
    for key in ('xlsxFileContent', 'jsonFileContent'):
        val = data.get(key)
        if isinstance(val, str) and val:
            try:
                data[key] = base64.b64decode(val)
            except Exception as e:
                return jsonify({"error": f"{key} dekodeerimine ebaõnnestus: {e}"}), 400

    try:
        result = calculate_wood_prices(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Viga arvutuse käivitamisel: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
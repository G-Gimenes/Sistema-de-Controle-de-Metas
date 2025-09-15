from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from flask_cors import CORS
from threading import Lock
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'
CORS(app)

# 1. Definir caminhos absolutos e criar pasta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
EXCEL_FILE = os.path.join(UPLOAD_FOLDER, 'meta_industria.xlsx')

lock = Lock()

# 2. Funções de data
def parse_date(val):
    if val is None or str(val).strip() == '':
        return pd.NaT
    val = str(val).strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(val, fmt).date()  # Retorna date, não datetime
        except ValueError:
            continue
    return pd.NaT

def format_date_for_excel(dt):
    if isinstance(dt, datetime):
        return dt.date()
    return dt

# 3. Rota index: cria arquivo se não existir e carrega dados
@app.route('/')
def index():
    try:
        columns = ['Data', 'Unidade', 'Tipo de Meta', 'Meta']

        # Cria Excel vazio com cabeçalhos na primeira visita
        if not os.path.exists(EXCEL_FILE):
            empty = pd.DataFrame(columns=columns)
            with lock:
                empty.to_excel(EXCEL_FILE, index=False, engine='openpyxl')

        # Lê tudo como string (preserva formato original)
        df = pd.read_excel(EXCEL_FILE, dtype=str, engine='openpyxl')
        data = df.fillna('').values.tolist()

        return render_template(
            'index.html',
            data_desossa=data,
            columns_desossa=columns,
            data_abate=[], columns_abate=[]
        )
    except Exception as e:
        return f"<h3>Erro ao carregar arquivo: {e}</h3>"

# 4. Rota save_metas: recebe JSON, converte, grava e formata no Excel
@app.route('/save_metas', methods=['POST'])
def save_metas():
    try:
        payload = request.json
        data = payload.get('data', [])
        columns = ['Data', 'Unidade', 'Tipo de Meta', 'Meta']

        df = pd.DataFrame(data, columns=columns)

        # Validação de colunas
        missing = [c for c in columns if c not in df.columns]
        if missing:
            return jsonify({'error': f'Colunas ausentes: {missing}'}), 400

        # Conversão Data e Meta
        df['Data'] = df['Data'].apply(parse_date)
        df['Meta'] = (
            df['Meta']
            .astype(str)
            .str.replace(',', '.')
            .pipe(pd.to_numeric, errors='coerce')
            .round(2)
        )

        # Grava no Excel
        with lock:
            # Salva sem índice
            df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')

            # Aplica formatação
            from openpyxl import load_workbook
            wb = load_workbook(EXCEL_FILE)
            ws = wb.active

            for idx, col_name in enumerate(columns, start=1):
                if col_name == 'Data':
                    for cell_tuple in ws.iter_cols(min_col=idx, max_col=idx, min_row=2):
                        for cell in cell_tuple:
                            cell.number_format = "DD/MM/YYYY"
                if col_name == 'Meta':
                    for cell_tuple in ws.iter_cols(min_col=idx, max_col=idx, min_row=2):
                        for cell in cell_tuple:
                            cell.number_format = "0.00"
            wb.save(EXCEL_FILE)

        return jsonify({'status': 'sucesso'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 5. Inicializa o servidor
if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar_arte():
    # Pegar dados do formulário
    empresa = request.form['empresa']
    origem = request.form['origem']
    destino = request.form['destino']
    data = request.form['data']
    valor = request.form['valor']
    
    # Criar imagem
    img = Image.new('RGB', (800, 600), color='white')
    draw = ImageDraw.Draw(img)
    
    # Tentar usar fonte padrão
    try:
        font_titulo = ImageFont.truetype("arial.ttf", 36)
        font_texto = ImageFont.truetype("arial.ttf", 24)
    except:
        font_titulo = ImageFont.load_default()
        font_texto = ImageFont.load_default()
    
    # Desenhar textos
    draw.text((50, 50), f"TRANSPORTADORA {empresa.upper()}", fill='black', font=font_titulo)
    draw.text((50, 150), f"Origem: {origem}", fill='black', font=font_texto)
    draw.text((50, 200), f"Destino: {destino}", fill='black', font=font_texto)
    draw.text((50, 250), f"Data: {data}", fill='black', font=font_texto)
    draw.text((50, 300), f"Valor: R\$ {valor}", fill='black', font=font_texto)
    
    # Salvar em memória
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='arte_transportadora.png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

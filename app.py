from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def feed():
    xml_url = "https://www.hinode.com.br/XMLData/consultores.xml"
    response = requests.get(xml_url)

    if response.status_code == 200:
        return Response(response.content, mimetype='application/xml')
    else:
        return "Erro ao buscar o XML", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

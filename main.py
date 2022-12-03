import requests
import pandas as pd
import time
import json

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)

pdf.cell(195, 10, txt = "CASOS DE COVID NO BRASIL", ln = 1, align = 'C')

header_api = {
    'User-agent': 'cliente da API'
}

datahora_atual = time.strftime('%Y-%m-%d'+'T'+'%H:%M:%S'+'Z', time.localtime())
api_site = f'https://api.covid19api.com/total/country/brazil/status/confirmed?from={datahora_atual}&to={datahora_atual}'
requisicao = requests.get(url=api_site, headers=header_api)
json_requisicao = json.loads(requisicao.text)

pdf.set_font("Arial", size=10)
for x in json_requisicao:
    pdf.cell(195, 10, txt=f'País: {x["Country"]}, Casos confirmados: {str(x["Cases"])}, Histórico por data: {x["Date"]}', ln=2, align='C')
    
pdf.output("Dados.pdf")

print("\n\nPDF Gerado!")
print("\n\nSite da API: covid19api.com\n")

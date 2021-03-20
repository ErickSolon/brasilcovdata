import requests, json, time

datahora_atual = time.strftime('%Y-%m-%d'+'T'+'%H:%M:%S'+'Z', time.localtime())

header_api = {
    'User-agent': 'cliente da API'
}

api_site = f'https://api.covid19api.com/total/country/brazil/status/confirmed?from={datahora_atual}&to={datahora_atual}'

requisicao = requests.get(url=api_site, headers=header_api)
requisicao_json = json.dumps(requisicao.text)

for x in requisicao_json:
    print('País:', x['Country'] + ' -'*2 +
     ' Casos confirmados:', str(x['Cases']) + ' -'*2 +
      ' Histórico por data:', x['Date']
    )

print("\n\nSite da API: covid19api.com\n")

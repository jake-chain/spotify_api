import csv
from files import files
import requests


def export():
    response = requests.get('https://covid19-brazil-api.now.sh/api/report/v1')
    if response.status_code != 200:
        print("Erro na consulta")
        exit()

    data = {}
    if 'data' in response.json():
        data = response.json()['data']

    with open(files.get_path("../storage/csv/teste_exportacao.csv"), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for uf in data:
            uf_data = []
            uf = dict(uf)
            for index, item in uf.items():
                uf_data.append(item)
            writer.writerow(uf_data)

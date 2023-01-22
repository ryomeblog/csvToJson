# ライブラリ設定
import csv
import json
import glob


def csvToJson(csvFileName):
    # CSVファイルの読み込み
    with open('./csv' + csvFileName, 'r', newline='', encoding='utf-8-sig') as f:
        csv_list = [row for row in csv.DictReader(f)]
    # JSONファイルへの書き込み
    with open('./json' + csvFileName.replace('.csv', '.json'), 'w', encoding='utf-8') as f:
        json.dump(csv_list, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    for fileName in glob.glob('./csv/*.csv'):
        csvToJson(fileName.replace('./csv', ''))


import pandas as pd
from pathlib import Path
from os import getcwd
import datetime

path = Path(getcwd())
print(path)
date = datetime.datetime.now().strftime('%Y%m%d_%H%M')
f_csv = open(date + '_csv_export.csv', 'w')
first_line = 'File, Sheet, Product, Region, Customer,'
title = True
for file in path.glob('*.xls'):
    print(file)
    xl_file = pd.ExcelFile(file)
    sheet = xl_file.sheet_names[0]
    df = pd.read_excel(file, sheet, header=None)
    product = df.iat[0, 0]
    region = df.iat[1, 0]
    m_1 = df.iat[3, 1]
    m_2 = df.iat[3, 2]
    m_3 = df.iat[3, 3]
    m_4 = df.iat[3, 4]
    if title:
        first_line += f'{m_1},{m_2},{m_3}, {m_4}\n'
        f_csv.write(first_line)
    title = False
    count = 4

    for i in range(count, len(df.index)):
        customer = df.iat[count, 0]
        val_1 = df.iat[count, 1]
        val_2 = df.iat[count, 2]
        val_3 = df.iat[count, 3]
        val_4 = df.iat[count, 4]
        f_csv.write(f'{file.stem},{sheet},{product},{region},{customer},{val_1},{val_2},{val_3},{val_4}\n')
        count += 1

f_csv.close()
print('\nReady!\n')

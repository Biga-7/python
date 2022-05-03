import pandas as pd
import numpy as np
from datetime import datetime, timedelta
report = pd.read_csv('/home/aslan/1.txt', delimiter = ';', header = None, usecols = range(12))
report.columns=['Номер_транзакции','Дата','Время','Тип_транзакции','Номер_POS','Номер_чека','Код_кассира','Код8','Код9','Код10','Код11','код12']
report['Дата'] = report['Дата'].apply(lambda _: datetime.strptime(_,'%d.%m.%y'))
report['Дата'] = report[' 787 Дата'].dt.strftime('%d.%m.%y')
report['Время'] = pd.to_datetime(report['Время'], format = '%H:%M:%S').dt.time
print('хоба');
Мой самый последний Задача 
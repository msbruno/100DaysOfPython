from datetime import datetime
import pandas as pd
from enum import Enum
from pandas.core.frame import DataFrame 

class Operation(Enum):
    BUY_SHARES = 1
    SELL_SHARES = 2 
    INCOME = 3

OPERATIONS = {
    'Debito': {
        'Transferência - Liquidação':  Operation.SELL_SHARES
    },
    'Credito': {
        'Transferência - Liquidação':  Operation.BUY_SHARES, 
        'Dividendo':Operation.INCOME, 
        'Rendimento':Operation.INCOME,
        'Juros Sobre Capital Próprio': Operation.INCOME,
    }
}

class TreatDataSource:

    def ini(self, data:pd.DataFrame):
        self.__original = data
        self.__temp = data.copy()
        self.__columns = ['operation', 'ticker', 'mean_price', 'quantity', 'date']

    def reset(self):
        self.__temp = self.__original

    def create_operations(self):
        for index, row in self.__temp.iterrows():
             self.__temp.loc[index, 'operation'] =  self.__treat_operation(row)

    def __treat_operation(self, row):
        operation = row['Entrada/Saída'].strip()
        sub_operation = row['Movimentação'].strip()
        return OPERATIONS[operation][sub_operation]

    def create_ticker(self):
        self.__temp['ticker'] = self.__temp['Produto'].apply(lambda value: value.split('-')[0].strip())
        
    def create_mean_price(self):
        self.__temp['mean_price'] = self.__temp['Preço unitário'].apply(lambda value: float(value))

    def create_quantity(self):
        self.__temp['quantity'] = self.__temp['Quantidade'].apply(lambda value: float(value))

    def create_date(self):
        self.__temp['date'] = self.__temp['Data'].apply(lambda value: datetime.strptime(value, "%d/%m/%Y"))

    def drop_not_used_columns(self):
        columns_to_remove  = [column for column in self.__temp.columns if column not in self.__columns]
        self.__temp.drop(columns=columns_to_remove, axis=1, inplace=True)

    def build(self)->DataFrame:
        return self.__temp
    
def read_data(path)-> pd.DataFrame:
    data = pd.read_excel(path)
    return data

path = r"data.xlsx"
data = read_data(path)
treater = TreatDataSource()
treater.ini(data)
treater.create_operations()
treater.create_ticker()
treater.create_mean_price()
treater.create_quantity()
treater.create_date()
treater.drop_not_used_columns()
result = treater.build()

expected_tickers = ['B3SA3', 'BTLG11', 'EZTC3', 'ITUB3', 'BBAS3']
quantities = [30,5,40,500,510]
mean_prices = [11.38, 97.00, 18.70, 0.02, 0.39]
dates = ['01/12/2021', '01/12/2021', '01/12/2021', '01/12/2021', '30/11/2021']
to_date = lambda value: datetime.strptime(value, "%d/%m/%Y")
dates = [to_date(value) for value in dates]

assert list(result['ticker']) == expected_tickers
assert list(result['quantity']) == quantities
assert list(result['mean_price']) == mean_prices
assert list(result['date']) == dates
assert list(result.columns) == ['operation', 'ticker', 'mean_price', 'quantity', 'date']

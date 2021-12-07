import pandas as pd
from enum import Enum 


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

    def treat_data(self, data:pd.DataFrame):
        for index, row in data.iterrows():
            data.loc[index, 'operation'] =  self.treat_operation(row)
        return data

    def treat_operation(self, row):
        operation = row['Entrada/Saída'].strip()
        sub_operation = row['Movimentação'].strip()
        return OPERATIONS[operation][sub_operation]


def read_data(path)-> pd.DataFrame:
    return pd.read_excel(path)


path = r"trades.xlsx"
data = read_data(path)
result = TreatDataSource().treat_data(data)
print(result['operation'])

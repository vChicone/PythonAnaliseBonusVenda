import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7b32e8385478b5cde5df1e4888c77904"
# Your Auth Token from twilio.com/console
auth_token  = "d9804b60ed56d11ceb0b76e91a736fdd"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
listaMeses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada arquivo:
for mes in listaMeses:
    tabelaVendas = pd.read_excel(f'{mes}.xlsx')
    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabelaVendas['Vendas'] > 55000).any():
        # Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        vendedor = tabelaVendas.loc[tabelaVendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabelaVendas.loc[tabelaVendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+5511XXXXXXXXX",
            from_="+12678438257",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

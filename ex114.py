import requests
try:
    response = requests.get('http://www.pudim.com.br')
except requests.exceptions.ConnectionError:
    print('\033[31mO site do Pudim não está acessivel no momento!\033[m')
else:
    print('\033[33mConsegui acessar o site do Pudim!\033[m')
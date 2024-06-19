import requests
from plyer import notification
from datetime import datetime

def gerar_alerta(base, etapa, nivel):
    if nivel == 1:
        titulo = "Alerta Baixo"
    elif nivel == 2:
        titulo = "Alerta Médio"
    elif nivel == 3:
        titulo = "Alerta Alto"
    else:
        titulo = "Alerta Desconhecido"
    
    mensagem = f"Falha no carregamento da base {base} na etapa {etapa}"
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    notification.notify(
        title=titulo,
        message=f"{mensagem}\nData: {data_atual}",
        timeout=10
    )

def extrair_dados_banks():
    url = "https://brasilapi.com.br/api/banks/v1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        banks = response.json()
        return banks
    except requests.RequestException as e:
        gerar_alerta("BANKS", "extração", 3)
        print(f"Erro ao extrair dados de bancos: {e}")
        return None

def extrair_dados_cep(cep):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        cep_info = response.json()
        return cep_info
    except requests.RequestException as e:
        gerar_alerta("CEP", "extração", 3)
        print(f"Erro ao extrair dados do CEP: {e}")
        return None

def extrair_dados_cnpj(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        cnpj_info = response.json()
        return cnpj_info
    except requests.RequestException as e:
        gerar_alerta("CNPJ", "extração", 3)
        print(f"Erro ao extrair dados do CNPJ: {e}")
        return None

# Exemplo de uso das funções
banks_data = extrair_dados_banks()
cep_data = extrair_dados_cep("01001000")  # Exemplo de CEP
cnpj_data = extrair_dados_cnpj("19131243000197")  # Exemplo de CNPJ

print("Dados de Bancos:", banks_data)
print("Dados do CEP:", cep_data)
print("Dados do CNPJ:", cnpj_data)


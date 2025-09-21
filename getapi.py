import requests
import json
import os
from dotenv import load_dotenv # Importa a função para carregar o .env

# Carrega as variáveis do arquivo .env
load_dotenv()

# Define valores padrão para as variáveis, caso o .env não exista
DEFAULT_BRASILAPI_URL = "https://brasilapi.com.br/api"
DEFAULT_CEP = "01001000"
DEFAULT_CNPJ = "00394460000141"
DEFAULT_MOEDA = "USD"
DEFAULT_DATA = "2024-04-18"

def buscar_dados(url_base, endpoint, identificador=""):
    """
    Realiza uma requisição GET para uma API com um endpoint e identificador.

    Args:
        url_base (str): A URL base da API (ex: "https://brasilapi.com.br/api").
        endpoint (str): O endpoint específico da API (ex: "cep/v2", "cnpj/v1").
        identificador (str, optional): O identificador a ser consultado (ex: um CEP ou CNPJ).
                                       Pode ser vazio para endpoints que não exigem um ID diretamente.

    Returns:
        dict: Um dicionário com os dados da API, ou None em caso de erro.
    """
    url = f"{url_base}/{endpoint}"
    if identificador:
        url = f"{url}/{identificador}"
    headers = {'Content-Type': 'application/json'}
    print(url)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lança uma exceção para códigos de status de erro (4xx ou 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição para {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar a resposta JSON de {url}: {e}")
        return None

if __name__ == "__main__":
    # Pega os valores do ambiente (carregados do .env)
    brasilapi_url = os.getenv("BRASILAPI_URL",DEFAULT_BRASILAPI_URL)

    # Exemplo de busca de CEP
    cep_para_buscar = os.getenv("CEP_PARA_BUSCAR",DEFAULT_CEP)
    resultado_cep = buscar_dados(brasilapi_url, "cep/v2", cep_para_buscar)

    if resultado_cep:
        print(f"Informações para o CEP {cep_para_buscar}:")
        print(json.dumps(resultado_cep, indent=4, ensure_ascii=False))
        print("-" * 40)
    else:
        print(f"Não foi possível obter informações para o CEP {cep_para_buscar}.")
        print("-" * 40)

    # Exemplo de busca de CNPJ
    cnpj_para_buscar = os.getenv("CNPJ_PARA_BUSCAR",DEFAULT_CNPJ)
    resultado_cnpj = buscar_dados(brasilapi_url, "cnpj/v1", cnpj_para_buscar)

    if resultado_cnpj:
        print(f"Informações para o CNPJ {cnpj_para_buscar}:")
        print(json.dumps(resultado_cnpj, indent=4, ensure_ascii=False))
        print("-" * 40)
    else:
        print(f"Não foi possível obter informações para o CNPJ {cnpj_para_buscar}.")
        print("-" * 40)

    # Exemplo de busca de moeda em uma data específica (USD em 2024-04-18)
    moeda_para_buscar_data = os.getenv("MOEDA_PARA_BUSCAR_DATA",DEFAULT_MOEDA)
    data_para_buscar = os.getenv("DATA_PARA_BUSCAR",DEFAULT_DATA)
    resultado_moeda_data = buscar_dados(brasilapi_url, f"cambio/v1/cotacao/{moeda_para_buscar_data}", data_para_buscar)

    if resultado_moeda_data:
        print(f"\nCotação de {moeda_para_buscar_data} em {data_para_buscar}:")
        print(json.dumps(resultado_moeda_data, indent=4, ensure_ascii=False))
    else:
        print(f"\nNão foi possível obter a cotação de {moeda_para_buscar_data} em {data_para_buscar}.")
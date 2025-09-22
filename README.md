<!-- 
  Tags: Dev
  Label: 🇧🇷 Api BrasilApi
  Description: exemplo de uso de uma Api bem usada por sistemas.
  path_hook: hookfigma.hook8
-->

# 🇧🇷 Brasil API com Python

## 📋 Visão Geral

Este projeto é um script simples em Python que utiliza a biblioteca `requests` para interagir com a **Brasil API**. Ele demonstra como buscar dados de diferentes endpoints, como **CEP**, **CNPJ** e cotações de **moeda**, utilizando variáveis de ambiente para gerenciar as configurações. É uma forma prática e segura de consumir dados públicos e de referência brasileiros.

<p align="center">
  <img src="/images/screenshot.png" alt="Exemplo de execução do script">
</p>

[Development](https://github.com/fabiuniz?tab=repositories) 

---

## 🎯 Configuração e Uso

### Pré-requisitos
Certifique-se de ter o Python instalado. O projeto também requer as bibliotecas `requests` e `python-dotenv`. Você pode instalá-las usando o `pip`:

```bash
pip install requests python-dotenv

```
### Variáveis de Ambiente
O script utiliza variáveis de ambiente para as configurações. Crie um arquivo chamado `.env` na raiz do projeto e adicione suas variáveis:

```bash

# Endereço da API
BRASILAPI_URL=[https://brasilapi.com.br/api](https://brasilapi.com.br/api)

# Valores para busca
CEP_PARA_BUSCAR=01001000
CNPJ_PARA_BUSCAR=00394460000141
MOEDA_PARA_BUSCAR_DATA=USD
DATA_PARA_BUSCAR=2024-04-18

```

Se o arquivo .env não for encontrado ou as variáveis não estiverem definidas, o script usará os valores padrão.

### Executando o Script
Para rodar o script, execute o seguinte comando no terminal:

```bash
python main.py

```

## 👨‍💻 Autor

[Fabiano Rocha/Fabiuniz](https://github.com/SeuUsuarioGitHub)


## Licence

[MIT License]

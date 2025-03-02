from fastapi import FastAPI
import requests

app = FastAPI()

# Função para buscar dados de ativos no Yahoo Finance
def get_market_data(symbol: str):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d"
    response = requests.get(url)
    data = response.json()
    if "chart" in data and "result" in data["chart"]:
        result = data["chart"]["result"][0]
        price = result["meta"].get("regularMarketPrice", "N/A")
        return {"simbolo": symbol, "preco": price}
    return {"erro": "Ativo não encontrado"}

@app.get("/preco/{simbolo}")
def obter_preco(simbolo: str):
    return get_market_data(simbolo.upper())

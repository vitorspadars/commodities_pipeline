import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

commodities = ['GC=F', 'SI=F', 'CL=F'] 

def data_commodities(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker('CL=F')
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['ticker'] = simbolo
    return dados

def all_data_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = data_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)


if __name__ == "__main__":
    dados_concatenados = all_data_commodities(commodities)
    print(dados_concatenados)
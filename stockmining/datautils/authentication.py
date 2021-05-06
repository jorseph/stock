#!/usr/bin/python
# coding=utf-8
"""
The module of fetching FinMine data
More details in https://finmind.github.io/quickstart/.
"""

import requests
import pandas as pd

URLLOGIN = "https://api.finmindtrade.com/api/v4/login"
URLDATA = "https://api.finmindtrade.com/api/v4/data"


def get_token(max_try=10):
    """Get the token."""
    parload = {
        "user_id": "jorseph",
        "password": "yoyo0418",
    }
 
    for _ in range(max_try):
        data = requests.post(URLLOGIN, data=parload).json()
        if data['msg'] == "success":
            return data['token']
    raise Exception("Faild to get token.")

def get_stock_price(stock_id, token):
    parameter = {
        "dataset": "TaiwanStockPrice",
        "data_id": stock_id,
        "start_date": "2021-04-02",
        "end_date": "2021-04-12",
        "token": token, # 參考登入，獲取金鑰
    }
    resp = requests.get(URLDATA, params=parameter)
    data = resp.json()
    data = pd.DataFrame(data["data"])
    print(data.head())
    return data
    
#TAIEX is not suitable.
def get_institutional_buy_sell(stock_id, token):
    parameter = {
        "dataset": "TaiwanStockInstitutionalInvestorsBuySell",
        "data_id": stock_id,
        "start_date": "2021-04-01",
        "token": token, # 參考登入，獲取金鑰
    }
    resp = requests.get(URLDATA, params=parameter)
    data = resp.json()
    data = pd.DataFrame(data['data'])
    print(data.head())
    
def get_all_buy_sell(token): 
    parameter = {
        "dataset": "TaiwanStockTotalInstitutionalInvestors",
        "start_date": "2021-04-01",
        "token": token, # 參考登入，獲取金鑰
    }
    resp = requests.get(URLDATA, params=parameter)
    data = resp.json()
    data = pd.DataFrame(data['data'])
    print(data.head())
    return data

if __name__ == "__main__":
    stock_id = 'TAIEX'
    token = get_token(max_try=10)
    #print(token)
    price = get_stock_price(stock_id, token)
    buysell = get_institutional_buy_sell(stock_id, token)
    total_buy_sell = get_all_buy_sell(token)
    

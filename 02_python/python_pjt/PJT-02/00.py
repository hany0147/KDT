import requests

def get_btc_krw():
    order_currency = 'BTC' 
    payment_currency = 'KRW'
    url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
    # BTC의 KRW를 불러오는 url
    
    res = requests.get(url=url).json() #해당 url을 json으로 불러오고.
    data = res['data'] #그중 data항목
    prev_closing_price = data['prev_closing_price'] # 또 그중에서 전일종가가격

    return prev_closing_price # 출력값

if __name__ == '__main__': # 이게 뭔지 모르겠다. 수업 다시 들어야함.
    print(get_btc_krw())


money = 10000
own = []

sampleStock = {
    'name':'shiwon',
    'price':900,
    'history':[0,0,0],
}

info_market = """
[[MARKET]]
1. Buy
2. Make New
3. Delete
4. Go to My Stocks
"""

info_mystocks = """
[[MYSTOCKS]]
1. Buy
2. Sell
3. Back to Main Page
4. Go to Market
"""
def ask(choice, msg):
    '''
    msg (str)
    choice ()
    '''
    ans = input(msg)

def market():
    print(f'Money: {money}')
    print(info_market)
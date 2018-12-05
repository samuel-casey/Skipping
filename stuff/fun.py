import random

new_val = 5
bought_shares = 0
money = 1000
for i in range(100):
    price_change = random.random()*int(random.choice([1.038,-1]))
    new_val = price_change+new_val
    if new_val<0:
        new_val = 0
    if price_change>0:
        bought_shares +=1
        money-=new_val
    if price_change<0 and bought_shares>=1:
        bought_shares -=1
        money+=new_val
    print("price is ", new_val, 'shares: ', bought_shares)
print('Money: ',money)
print('Shares: ', bought_shares)
print('Share price: ', new_val)
print('Share Value: ', bought_shares*new_val)
print('Total Value: ', bought_shares*new_val+money)
prices = [100, 200, 300, 400]
discounted_prices = list(map(lambda x: x-x*0.15, prices))
print(discounted_prices)
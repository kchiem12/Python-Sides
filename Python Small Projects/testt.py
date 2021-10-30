def sol(n):
	cost = n['cost_price'] * n['inventory']
	gross = n['sell_price'] * n['inventory']
	return round(gross - cost)



def main():
	print(sol({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))

main()


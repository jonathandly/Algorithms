#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = prices[1] - prices[0]
  current_min = prices[0]

  for i in range(1, len(prices)):
    if prices[i] - current_min > max_profit:
      max_profit = prices[i] - current_min

    if prices[i] < current_min:
      current_min = prices[i]

  return max_profit

# print(find_max_profit([88,218,1002,1,59,843,123,19,4500]),4499)





if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
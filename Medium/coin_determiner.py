# Have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, and return an 
# integer output that will specify the least number of coins, that when added, equal the input integer. Coins are based 
# on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11. So for example: if num is 16, 
# then the output should be 2 because you can achieve the number 16 with the coins 9 and 7. If num is 25, then the 
# output should be 3 because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins.

def CoinDeterminer(num):
  if num < 5:
    return num
  # The strategy we use here is to subtract 11 from num as many times as possible, then 9, then 7, then 5, then 1.  
  # The only cases where this won't work is with remainders of 14 and 15. In the case of 14, this method will give 4 
  # (11 + 3 * 1), but we could've done it in 2 (9 + 5), and in the case of 15, this method will give 5 (11 + 4 * 1), 
  # but we could've done it in 3 (9 + 5 + 1). These cases are dealt with in the if block on lines 18-19.
  coins = [11, 9, 7, 5, 1]
  remainder = num
  count = 0
  for n in coins:
    if 2 < remainder < 5:
      return count + 1 if remainder == 3 else count + 2
    if n <= remainder:
      count += remainder // n
      remainder = remainder % n
      if remainder == 0:
        return count

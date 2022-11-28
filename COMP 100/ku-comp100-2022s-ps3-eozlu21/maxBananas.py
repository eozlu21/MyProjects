def maxBananas(money, price, price_p, total_bananas = 0, current_peels = 0):
  # your code here
  if money < price:
    return total_bananas
  else:
    new_peels = money // price
    total_bananas += new_peels
    current_peels += new_peels
    money %= price
    money += current_peels // price_p
    current_peels %= price_p
    return maxBananas(money, price, price_p, total_bananas, current_peels)


    



if __name__ == "__main__":

  money = int(input("Enter money: "))
  price = int(input("Enter price: "))
  price_p = int(input("Enter price_p: "))

  print(maxBananas(money, price, price_p)) # pass your arguments in ...

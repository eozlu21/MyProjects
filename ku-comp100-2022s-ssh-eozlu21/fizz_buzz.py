def fizz_buzz(limit):
  for i in range(limit):
    if i % 3 == 0:
      print('fizz')
    if i % 5 == 0:
      print('fizz')
    if i % 3 and i % 5:
      print(i)

def main():
    fizz_buzz(10)

## We will fix the following issues:
# Main is never called
# Starts at 0 instead of 1
# Prints “fizz” and “buzz” on separate lines for multiples of 15
# Prints “fizz” for multiples of 5
# Uses a hard-coded argument of 10 instead of taking a command-line argument
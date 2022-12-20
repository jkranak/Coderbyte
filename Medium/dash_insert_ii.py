# Have the function DashInsertII(str) insert dashes ('-') between each two odd numbers and insert asterisks ('*') between each two even numbers in str.

def DashInsertII(num):
  num_str = str(num)
  result = ''
  for i in range(len(num_str) -1):
    # We insert nothing if either a number or the number after is 0 or if one of the two numbers is odd and the other even
    if num_str[i] == '0' or num_str[i + 1] == '0' or int(num_str[i]) % 2 != int(num_str[i + 1]) % 2:
      result += num_str[i]
    else:
      fill_str = '-' if int(num_str[i]) % 2 == 1 else '*'
      result += num_str[i] + fill_str

  # Our for loop stops before the last number, so we add that on here
  return result + num_str[-1]

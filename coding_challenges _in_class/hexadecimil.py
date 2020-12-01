# generates a random hexadecimal color value  ie random_hex() => #f0667A  up to 6 char, 0-9 A-f , with #
import random

def random_hex():
    abc_li = list(range(0,10)) + list('ABCDEF')
    hex_li = []
    for i in abc_li:
        hex_li.append(str(random.sample(hex_li, 6))
    return '#' + ''.join(hex_li)

print(random_hex())

#ryans answer

# Write a program that generates a random hexadecimal color value
# IE: random_hex() => '#F0667A'
# Up to 6 characters, 0-9, A-F, Leading '#'
import random as r
def random_hex():
  hex_val = list(range(10)) + list("ABCDEF")
  final_hex = []
  i = 1
  while i <= 6:
    final_hex.append(str(hex_val[r.randint(0, 15)]))
    i += 1
  return "#" + "".join(final_hex)
  # return r.sample(hex_val, 6)
print(random_hex())
    

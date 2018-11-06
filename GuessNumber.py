import random

a=(random.randint(1,30))
bingo = False
b = 0
print("guess the number i think(1-30): ")

while bingo == False:

  b=int(input())

  if a>b:
    print"too small"
  elif a==b:
    print "bingo"
    bingo = True
  else:
    print"too large"

import random
def display(room):
 print(room)
room=[
      [1,0,1,0],
      [1,1,0,0],
      [0,1,0,1],
      [0,0,1,1],

      ]

print("all dirty ")
display(room)
x=0
y=0
while x<4:
      while y<4:
          room[x][y]=random.choice([0,1])
          y+=1
          x+=1
          y=0

          print("before cleaning dirts ")
          print(room)

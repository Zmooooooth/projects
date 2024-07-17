list = ["Bananas","Apples",2,3,4]
for i in list:
    print(i)
print("meow\n" * 3,end="")

while True:
    i = int(input("Give a number for n: "))
    if i > 0:
        break
counter = 0
while counter < i:
    print("meow")
    counter = counter + 1

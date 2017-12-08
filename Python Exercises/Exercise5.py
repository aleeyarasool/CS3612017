#While loop to find the first 20 numbers divisible by 5,7 and 11
number = 0
x = 11

while number < 20:
    if (x%5==0 or x%7==0 or x%11==0):
        print(x)
        number +=1
    x+=1    


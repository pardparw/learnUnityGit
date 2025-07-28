import math

a = float(input("Enter x : "))
x = a
if a > 99:
    x = ((2*(math.pow(a,3)))  - (a/(math.sqrt((a+1))))  )
elif a > 0 and a <= 99:
    x = ((3*(math.pow(a,2))) - (math.pow((1-a), 2)))
elif a == 0:
    x = a
elif a < 0:
    x = math.sqrt( (math.pow(a,2) + 1) )
print(f"f({a:.2f}) = {math.ceil(x)}")

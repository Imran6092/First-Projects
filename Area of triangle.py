a= int(input("Length of side A"))
b= int(input("Length of side B"))
c= int(input("Length of side C"))

p=(a+b+c)
s= p/2

area= (s*(s-a)*(s-b)*(s-c))**0.5

print("The Area of the triangle is:", area)
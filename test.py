num = 7458
numc = num
sum = 0
arr = []
arr2 = arr
new = 0
newnum = 0
newnum2 = 0
while num!=0:
    p = num%10
    arr.append(p)
    sum = sum + p
    new = new * 10 + p
    num = int(num/10)

arr2.sort()
for element in arr2:
    newnum = newnum *10 + element
arr3 = arr2
arr4 = arr3[::-1]
for elements in arr4:
    newnum2 = newnum2 * 10 + elements
print("Given Number = ",numc)
print("Is Even number:(Given Number) ",numc % 2 == 0)
print("All the digits are ",arr) 
print("Sum of all digits are = ",sum)
print("Reverse number of the given number is = ",new)
print("Is Even number:(Reverse number) ",new % 2 == 0)
print("Lowest number from the digits",newnum)
print("Highst number from the digits",newnum2)
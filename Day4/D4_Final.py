a = 1 + 2j
b = 2 + 4j
print('Arthimatics of complex No')
print('Addition', a + b)
print('Subtraction =', a - b)
print('Multiplication =', a * b)
print('Division =', a / b)
#print('Division =', a % b)

#Research on range() functions and its parameters. Create a markdown cell
print("Python range() example")
print("Get numbers from range 0 to 10")

for i in range(10): 
    print(i, end =" ") 
print("\n") 
for i in range(8): 
    print(i, end = " ") 
print("\n") 
for i in range(2, 7): 
    print(i, end =" ") 
print() 

# using range to print number 
# divisible by 3 
for i in range(3, 10, 3): 
    print(i, end = " ") 
print() 

for i in range(0, 10, 2): 
    print(i, end =" ") 
print() 


for i in range(10, 2, -2): 
    print(i, end =" ") 
print() 

element = range(10)[0] 
print("First element:", element) 
  
element = range(10)[-1] 
print("Last element:", element) 
  
element = range(10)[4] 
print("Fifth element:", element) 

#Consider two numbers. Perform their subtraction and if the result of subtraction is greater than
#25, print their multiplication result else print their division result.

num1 = 28
num2 = 100
print("Value of num1  and num2: ", num1,num2)
temp = num1-num2
if (temp > 25):
   temp=num1*num2
   print("Value of temp: ", temp)
else:
    temp=num1/num2
    print("Value of temp: ", temp)

#Question 4:
#Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the
#result as "square of that number minus 2".
myList = [ 2,3,6,4,7,8,9,10,12,30 ]
lengt=len(myList)
#print (lengt)
for i in range(lengt-1):
    if ((myList[i]) % 2) == 0:
        print("{0} is divisible by 2".format((myList[i])))
        #templist[i]= ((myList[i])*2)-2)
        #print(templist)

    else:
        print("{0} is Odd".format((myList[i])))
    
   # print(myList[i])


#Question 4:
#Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the
#result as "square of that number minus 2".
myList = [ 2,3,6,4,7,8,9,10,12,30 ]
lengt=len(myList)
#print (lengt)
for i in range(lengt-1):
    if ((myList[i]) % 2) == 0:
        print("{0} is divisible by 2".format((myList[i])))
        #print("square of ((myList[i]) * 2) - 2".format((myList[i])*2 -2))
        print ( ((myList[i]) * 2) - 2)
   # else:
    #    print("{0} is not  divisible by 2".format((myList[i])))
    
   # print(myList[i])

#Question 5:
#Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that
#number is divided 2.

myList1 = [ 2,3,6,4,7,8,9,10,12,30 ]
lengt1=len(myList1)
#print (lengt1)
for i in range(lengt1-1):
    if ((myList1[i]) % 2) == 0 and (myList1[i]) > 7:
        print("{0} is divisible by 2 and greater than 7".format((myList1[i])))
        print (myList1[i])
   # else:
    #    print("{0} is not  divisible by 2".format((myList[i])))
    
   # print(myList[i])
    

    
    


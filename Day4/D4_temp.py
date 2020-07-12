#complex numbers don’t support comparison operators like <, >, <=, => and it will through TypeError message
a = 1 + 2j
b = 2 + 4j
print('Arthimatics of complex No')
print('Addition', a + b)
print('Subtraction =', a - b)
print('Multiplication =', a * b)
print('Division =', a / b)
#print('Division =', a % b)

#Research on range() functions and its parameters. Create a markdown cell and write in your own
#words (no copy-paste from google please) what you understand about it. Implement a small
#program of your choice on the same.
#Python range() Basics :
#start: integer starting from which the sequence of integers is to be returned
#stop: integer before which the sequence of integers is to be returned.
#The range of integers end at stop – 1.
#step: integer value which determines the increment between each integer in the sequence


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

#Question 5:
#Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that
#number is divided 2.
    

    
    


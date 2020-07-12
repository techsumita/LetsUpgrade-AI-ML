
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
    

    
    


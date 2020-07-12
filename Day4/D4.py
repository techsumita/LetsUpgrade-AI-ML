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



#Write a Python program to find the first 20 non-even prime natural numbers.

lower = 0
upper = 20

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
 # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
    else:
        print(num)

def isPalindrome(string):
 left_pos = 0
 right_pos = len(string) - 1
 
 while right_pos >= left_pos:
    if not string[left_pos] == string[right_pos]:
        return False
 left_pos += 1
 right_pos -= 1
 return True
print(isPalindrome('aza'))
def areAnagram(str1, str2):  
    # Get lengths of both strings  
    n1 = len(str1)  
    n2 = len(str2)  
  
    # If lenght of both strings is not same, then  
    # they cannot be anagram  
    if n1 != n2:  
        return 0
  
    # Sort both strings  
    str1 = sorted(str1) 
    str2 = sorted(str2) 
  
    # Compare sorted strings  
    for i in range(0, n1):  
        if str1[i] != str2[i]:  
            return 0
  
    return 1
  
str1 = "test"
str2 = "estt"
if areAnagram(str1, str2):  
    print ("The two strings are anagram of each other") 
else:  
    print ("The two strings are not anagram of each other") 
  

string = "ana"
flag = 0

length = len(string)
for i in range(length):
    if(string[i] != string[length - i - 1]):
        flag = 1
        break

if(flag == 0):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")
   
 
   
def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)

print(is_anagram('anagram','nagaram'))
print(is_anagram('cat','rat'))

ini_string = "Dr. Darshan Ingle @AI-ML Trainer"
  
# printing initial string 
print ("initial string : ", ini_string) 
  
# function to demonstrate removal of characters 
# which are not numbers and alphabets using re 
getVals = list([val for val in ini_string if val.isalnum()]) 
result = "".join(getVals) 

# printing final string 
print ("final string", result) 

x = result.lower()

print("final string in lower case",x)
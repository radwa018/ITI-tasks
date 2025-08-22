#1
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
#2
def generate_array(length, start):
    arr = []
    for i in range(length):
        arr.append(start + i)
    return arr
print(generate_array(5, 10))  

#3
arr = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print("Ascending order:", sorted(arr))
print("Descending order:", sorted(arr, reverse=True))
#4
def fizzbuzz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return str(n)

for i in range(1, 16):
    print(fizzbuzz(i))
#5
def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    return s == s[::-1]
word = input("Enter a word: ")
if is_palindrome(word):
    print("Palindrome ")
else:
    print("Not Palindrome")
#6
def longest_alphabetical_substring(s):
    longest = current = s[0]
    for i in range(1, len(s)):
        if s[i] >= s[i-1]:  
            current += s[i]
            if len(current) > len(longest):
                longest = current
        else:
            current = s[i]  
    return longest

s = input("enter a string: ")
print("longest substring in alphabetical order is:", longest_alphabetical_substring(s))

    
#Write your code below this line ๐
def prime_checker(number):
  prime_number = True
  for i in range(2, number):
    if number % i == 0:
      prime_number = False
  if prime_number == True:
    print(f"The number {number} is a prime number")
  else:
    print(f"The number {number} is not a prime number")
  

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input(f"Select a number to see if it's prime: "))
prime_checker(number=n)




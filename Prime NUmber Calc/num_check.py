def prime_check(num):
  is_prime = True
  for n in range(2,num):
    if num%n==0:
      is_prime = False
  if is_prime==True:
    print(f"{num} is a prime number.")
  else:
    print(f"{num} is not a prime number.")

def factors_check(num):
  factors=[]
  for n in range(1,num+1):
    if num%n==0:
      factors.append(n)
  print(factors)   
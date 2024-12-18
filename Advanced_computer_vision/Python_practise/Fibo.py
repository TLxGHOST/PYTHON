def recur_fibo(n):
    '''This is just a doc string to make the user experince '''
    if n <= 1:
       return n
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       
# set=set()
# print(type(set))
# set.add(5)
# print(set)
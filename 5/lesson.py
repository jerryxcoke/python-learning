 # read to file
file = open('helloka.txt', 'r')
file.read()
file.readline()
file.close()
 # write to file
file_h = open("testfile.txt", "w")
file_h.write("This is a test")
file_h.write("To add more lines.")
file_h.close()

# fib while loop
nterms = 10
n1 = 0
n2 = 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#recursive fibonacci
def recursive_fibo(n):
   if n <= 1:
        return n
   else:
       result = (recursive_fibo(n-1) + recursive_fibo(n-2))
       return result

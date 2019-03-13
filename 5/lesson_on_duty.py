text = "Andrea Anagyon okos, Peti meg ugyes matekbol"

def isCharacterA(char):
    return char is 'a' or char is 'A'

def isSame(char1, char2):
    return char1 is char2 or char1 == char2.upper()

num = 0
for char in text:
    if isSame(char, 'a'):
        num += 1
print(num)

# while fibonacci
nterms = 5
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




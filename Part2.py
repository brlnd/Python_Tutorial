#Chapter 4: More Control Flow Tools
#From previous chapter we have seen how to use "while": Fibonacci serie
a, b = 0, 1
while b<10:
    print(b)
    a, b = b, a+b
    
#If I want the number on the same line, I can use the following code, the argument end avoid to change the line
a, b = 0, 1
while b<30:
    print(b, end=',')
    a, b = b, a+b
#4.1 The if statement. Write now a code which allows use to interact with the user
x = int(input("Please enter a positive integer: "))
if x<0:
    x=0
    print("Since the integer is negative it was changed to 0")
elif x==0:
    print('Zero')
elif x>0:   # In alternative can use else:
    print('The number you choose is', x)

#4.2 For statement. Like foreach or forvalues in stata
#measure some string
words = ['casa', 'zucchina', 'ruttolibero']
for w in words:
    print(w, len(w))
#Suppose now I want to modify my list: I want to replicate words shorter that a given threshold
for w in words[:]:  # Loop over a slice copy of the entire list, otherwise the loops is infinite.
    if len(w) < 6:
        words.insert(0, w)
#4.3 range(a,b,c) function a=begin of interval b=end c=step
#use range to print the words contained in our vector
for i in range(len(words)):
    print(words[i], end=', ')

#4.4 break and continue statements
#break interrupt the loop if some condition is verified. Suppose I want to look for prime numbers in an interval
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n, 'equals', x, '*', n//x)
            break #if the condition hold for a number x then the loop break
    else: #n%x != 0 for every x --> prime + else is referred to the for cycle, not the if one
        print(n, ' is a prime number')
#Try to make a basic program that, once I insert an integer number he returns me if is prime or not
n=int(input("Give me an integer number and I'll tell you if it's prime. The number is: "))
for x in range(2,n):
    if n%x==0:
        print(n, "is not a prime number")
        break
else:
        print(n, "is a prime number")
    
#continue: if a condition is verified, do something and the pass to the following command
#pass: skip a command useful when I want to define something as a class or a function but I don't know yet what to write --> pass

#4.6 Defining function
#Define a function which returns if a number is prime or not
def prime(n):
    for x in range(2,n):
        if n%x==0:
            print(n, "is not a prime number")
            break
    else:
            print(n, "is a prime number")

prime(53)

#Define a function which returns the prime n number of the Fibonacci series
def Fib(n):
    a, b = 0,1
    while a<n:
        print(a, end=', ')
        a, b = b, a+b

Fib(37)

#BUt previous one is technically a procedure, functions have a return in their definition
def Fib2(n):
    a, b = 0,1
    result = []
    while a<n:
        result.append(a) #method that appends to the vector result a value, equivalent to result = result + [a]
        a, b = b, a+b
    return result
#A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type.
fib37 = Fib2(37)

#4.7 More on defining Functions
#Default argument values
def ask_ok(prompt, retries=4, reminder= 'Ritenta e sarai più fortunato!'):
    while True: #means that it continues to repeat the operation, like an infinite loop
        ok=input(prompt)
        if ok in ('yes', 'ye', 'y'):
            return True
        if ok in ('nope', 'nop', 'no', 'n'):
            return False
        retries = retries -1
        if retries <0:
            raise ValueError('Invalid response user')
        print(reminder)
#Alternative: Keyboard arguments
# print(my_function.__doc__) print the description of a function you make it using """ ... """
#my_function.__annotations__ print the not to a function
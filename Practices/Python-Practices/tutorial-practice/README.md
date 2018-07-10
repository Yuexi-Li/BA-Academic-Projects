
This tutorial notebook is used for python review.

# The Python Tutorial

## 1.Why python?
    

1. Compare to C/C++/Java, the usual write/complie/re-complie cycle is much more fast. 
2. Python is more simple to use, offering much more structure and support for large programs than shell scripts or batch files can offer.
1.  Python allows you to split your program into modules that can be reused in other Python programs. It comes with a large collection of standard modules that you can use as the basis of your programs — or as examples to start learning to program in Python.

4. Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:

> -   the high-level data types allow you to express complex operations in a single statement;
>-   statement grouping is done by indentation instead of beginning and ending brackets;
>-   no variable or argument declarations are necessary. 




## 2. Informal introduction

### 1.Numbers

**Basic calculation**


```python
17/3
```




    5.666666666666667




```python
17//3 # floor division discards the fractional part 
```




    5




```python
17 % 3  # the % operator returns the remainder of the division
```




    2



**Powers**


```python
2 ** 7  # 2 to the power of 7
```




    128



In interactive mode, the last printed expression is assigned to the variable `_`


```python
tax = 12.5 / 100
```


```python
price = 100.50
```


```python
price * tax
```




    12.5625




```python
price + _
```




    113.0625




```python
round(_,2)
```




    113.06



###  2. Strings

**Basic String output**
> 1. Escape quotes using the backlash `\`
> 2. Create new line using `\n`
> 3. Add `r` before the first quote to read as raw strings
> 4. String literals can span multiple lines. One way is using triple-quotes: `"""..."""` or `'''...'''`. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. 


```python
'doesn\'t'  # use \' to escape the single quote...
```




    "doesn't"




```python
"doesn't"  # ...or use double quotes instead
```




    "doesn't"




```python
print('C:\some\name')  # here \n means newline!
```

    C:\some
    ame



```python
print(r'C:\some\name')  # note the r before the quote
```

    C:\some\name



```python
# End of lines are automatically included in the string
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    


**Concatenation**
> 5. Strings can be concatenated (glued together) with the `+` operator, and repeated with `*`:
> 6. Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
> 7. This only works with two literals though, **not with variables or expressions** :
    but they can concatenate with `+`



```python
3 * 'un' + 'ium'   # Repeat three times and concatenated with ium
```




    'unununium'




```python
'Py'  'thon'       #Automatically concatenated 
```




    'Python'




```python
# So, this feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
      'to have them joined together.')
text
```




    'Put several strings within parentheses to have them joined together.'




```python
#This only works with two literals though, not with variables or expressions :
prefix= 'py'
prefix 'thon'
```


      File "<ipython-input-39-d0af82720f88>", line 3
        prefix 'thon'
                    ^
    SyntaxError: invalid syntax




```python
#Can be concatenated with + esperession
prefix= 'py'
prefix +'thon'
```




    'python'



**String indexing, slicing**
> 1. Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one.

> 2. Indices may also be negative numbers, to start counting from the right:

> Note that since -0 is the same as 0, negative indices start from -1.

> 1. Note how the **start** is always included, and the **end always excluded**. This makes sure that 
`s[:i] + s[i:]` is always equal to `s `


```python
word='Python'
```


```python
word[0]==word[-6]  # Both index the first character 'P'
```




    True




```python
word[0:2]  # characters from position 0 (included) to 2 (excluded)
```




    'Py'




```python
word[2:5]  # characters from position 2 (included) to 5 (excluded)
```




    'tho'




```python
word[-1]
```




    'n'



**Others** 

> Python strings cannot be changed — they are **immutable**.Therefore, assigning to an indexed position in the string results in an error

>If you need a different string, you should create a new one


```python
word[0] ='J'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-60-98aaa973c227> in <module>()
    ----> 1 word[0] ='J'
    

    TypeError: 'str' object does not support item assignment



```python
'J' + word[1:]
```




    'Jython'



### 3. Lists  (mutable!)
**Basics**  
Python knows a number of **compound** data types, used to group together other values.  
The most **versatile** is the list, which can be written as a list of comma-separated values (items) between square brackets.   
Lists might **contain items of different types**, but usually the items all have the same type.

**Indexing and slicing**
> 1. Like strings (and all other built-in sequence type), lists can be indexed and sliced:
> 2. All slice operations return a new list containing the requested elements. This means that the following slice returns a **new (shallow) copy** of the list:
> 3. Lists also support operations like concatenation:


```python
#1. Can be indexed and sliced
squares = [1, 4, 9, 16, 25]
squares[0]
```




    1




```python
# 2. the slice operation return a new list (shallow) copy of the list
squares[-3:]
```




    [9, 16, 25]




```python
# 3. Support concatenation
squares[-3:] + [36, 49, 64, 81, 100]
```




    [9, 16, 25, 36, 49, 64, 81, 100]



**List is mutable!**  
> 1. lists are a mutable type, i.e. it is possible to change their content:
> 1. Can add new items at the end of the list, by using the append() method (we will see more about methods later):
> 1. **Remove** the list item can be achieved by assign null to the certain elements
> 1. Can be nested


```python
# 1. Mutable! change the content
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4**3
```




    64




```python
cubes[3]= _    #replace the wrong value
cubes
```




    [1, 8, 27, 64, 125]




```python
#2. add new items at the end of the list
cubes.append(3)
cubes
```




    [1, 8, 27, 64, 125, 3]




```python
# 3. delete the 'd', 'e'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```


```python
letters[3:5]=[]   # replace with null and remove them
letters
```




    ['a', 'b', 'c', 'f', 'g']




```python
# clear the list by replacing all the elements with an empty list
letters=[]
letters
```




    []




```python
# Nested list
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
```


```python
>>> x[0][0]
```




    'a'



### Programming example


```python
>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```

    0
    1
    1
    2
    3
    5
    8





    8



This example introduces several new features.

> The first line contains a **multiple assignment**:
    the variables `a and b` simultaneously get the new values `0 and 1`.  On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.

> The while loop executes as long as the condition (here: a < 10) remains true. In Python, like in C, any non-zero integer value is true; zero is false. The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false. 

>The body of the loop is **indented**: indentation is Python’s way of grouping statements. 

>The keyword argument `end` can be used to avoid the newline after the output, or end the output with a different string:



```python
#The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...

```

    0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

## 3. More Control flows

### 1. `While` statement
The while loop executes as long as the condition remains true.

### 2. `If` statement
> There can be **zero or more** elif parts, and the else part is **optional**. The keyword `elif` is short for `else if`, and is useful to avoid excessive indentation. An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.


```python
x= int(input("Please enter an integer : "))
if x<0:
    x=0
    print ('Negative changed to Zero')
elif x==1:
    print ('Single')
elif x==0:
    print ('Zero')
else:
    print ('more')
```

    Please enter an integer : -2
    Negative changed to Zero


### 3. `for` statement
> Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement **iterates over the items of any sequence (a list or a string)**, in the order that they appear in the sequence. For example (no pun intended):


```python
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']     #iterate over the items of any sequence! list or string
>>> for w in words:
...     print(w, len(w), end='; ')
```

    cat 3; window 6; defenestrate 12; 

> If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you **first make a copy**.  
>**Iterating over a sequence does not implicitly make a copy.** The slice notation makes this especially convenient:  
>With for `w in words`:, the example would attempt to create an infinite list, inserting defenestrate over and over again.
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12

```python
#The above chunk is Wrong which falls into a dead loop. 

#1.Should used this way to create a copy first.
for w in words[:]:  # Loop over a slice copy of the entire list.
     if len(w) > 6:
         words.insert(-1, w)
#Same with to create a new copy then to iterate

new_words=words[:]
for w in new_words:  # Loop over a slice copy of the entire list.
     if len(w) > 6:
         words.insert(-1, w)
```


```python
words
```




    ['cat',
     'window',
     'defenestrate',
     'defenestrate',
     'defenestrate',
     'defenestrate']



### 4. The `Range()` function
 to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
 > 1. Range function can be used as `range(4)` to give 4 values, start with 0
 > 2. Range function can be used to start certain number `range(3,6)`   start at another number
 > 3. Range function can be used to step over certain number `range(2,10,2)` to specify a different increment (even negative; sometimes this is called the ‘step’):


```python
# 1.Start with 0, and gives 5 values
for i in range(5):
     print(i, end=',')
```

    0,1,2,3,4,


```python
# 2.Start with 3, and gives 3 values
for i in range(3,6):
     print(i, end=',')
```

    3,4,5,


```python
# 3. To step over certain number // to specifiy different increment 2
for i in range(2,10,2):
     print(i, end=',')
```

    2,4,6,8,


```python
#To iterate over the indices of a sequence, you can combine range() and len() as follows:
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i], end='; ')
```

    0 Mary; 1 had; 2 a; 3 little; 4 lamb; 

### 5. `break` and `continue` Statements, and `else` Clauses on Loops
>The break statement, like in C, breaks out of the innermost enclosing `for` or `while` loop.   

>It is executed when the loop terminates through exhaustion of the list (with `for`) or when the condition becomes false (with `while`), but not when the loop is terminated by a `break` statement. This is exemplified by the following loop, which searches for prime numbers:

> Break the entire loop  
> Return the whole function   
> Continute to the next iteration  
> Pass the current line

***Check on the prime number**


```python
#Prime number program 
for n in range (2,15):
    divisible= False 
    for x in range (2,n):
        if n%x==0:
            divisible=True 
            print (n,'equals', x,'*', n//x)
            break  # break the entire loop
    if divisible==False:
        print (n,'is a prime number') 
```

    2 is a prime number
    3 is a prime number
    4 equals 2 * 2
    5 is a prime number
    6 equals 2 * 3
    7 is a prime number
    8 equals 2 * 4
    9 equals 3 * 3
    10 equals 2 * 5
    11 is a prime number
    12 equals 2 * 6
    13 is a prime number
    14 equals 2 * 7



```python
# Prime number program
for n in range (2,15):
    for x in range (2,n):
        if n%x==0:
            print (n,'equals', x,'*', n//x)
            break
    else:   #else in here belongs to the for loop, not the if statement
        print (n,'is a prime number')
```

    2 is a prime number
    3 is a prime number
    4 equals 2 * 2
    5 is a prime number
    6 equals 2 * 3
    7 is a prime number
    8 equals 2 * 4
    9 equals 3 * 3
    10 equals 2 * 5
    11 is a prime number
    12 equals 2 * 6
    13 is a prime number
    14 equals 2 * 7


>When used with a loop, the `else` clause has more in common with the else clause of a try statement than it does that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs. For more on the try statement and exceptions, see Handling Exceptions.

>The `continue` statement, also borrowed from C, continues with the **next iteration** of the loop:


```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue  # continues with the next iteration of the loop
...     print("Found a number", num)
```

    Found an even number 2
    Found a number 3
    Found an even number 4
    Found a number 5
    Found an even number 6
    Found a number 7
    Found an even number 8
    Found a number 9


### 6. `Pass` Statements
This is commonly used for creating minimal classes:


```python
>>> class MyEmptyClass:
...     pass
```

Another place pass can be used is as a `place-holder` for a `function` or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The `pass` is silently ignored:


```python
>>> def initlog(*args):
...     pass   # Remember to implement this!
```

### 7. Defining Functions

#### **1. Basics**

> 1. Make a habit on writting doc strings 
>
> 2. **????** The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced. 

**Call by value**  
> 3. The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using **call by value** (where the value is always an **object reference, not the value of the object**). When a function calls another function, a new local symbol table is created for that call.  

**Renaming mechanism**  
>4. A function definition introduces the function name in the current symbol table. The value of the function name has a type that is recognized by the interpreter as a user-defined function. This value can be **assigned to another name which can then also be used as a function**. This serves as a general renaming mechanism:

Fibonacci series to an arbitrary boundary


```python
#1. Basics
def fib(n):
    """Print a Fibonacci series up to n."""   # make a habit on writing doc string
    a,b= 0 ,1
    while a< n: 
        print(a, end=' ')
        a,b=b, a+b
    print()
```


```python
fib(20)
```

    0 1 1 2 3 5 8 13 



```python
# 2. Renaming mechanism
fun= fib
fun(23)
```

    0 1 1 2 3 5 8 13 21 


**Return on value**
> Coming from other languages, you might object that fib is not a function but a procedure since it doesn’t return a value. In fact, even functions without a return statement do return a value, albeit a rather boring one. This value is called` None (it’s a built-in name)`. Writing the value None is normally suppressed by the interpreter if it would be the only value written. You can see it if you really want to using print()  

>1. Return a list of results


```python
print(fib(12))
```

    0 1 1 2 3 5 8 
    None



```python
#Return a list of results
def fib_2(n):
    """Return a list containing the Fibonacci series up to n."""
    result=[]
    a,b= 0 ,1
    while a< n: 
        result.append(a)
        a,b=b, a+b
    return result
```


```python
fib_2(20)
```




    [0, 1, 1, 2, 3, 5, 8, 13]



This example, as usual, demonstrates some new Python features:
> <li> The return statement returns with a value from a function. return without an expression argument returns `None`. Falling off the end of a function also returns None.   
    
**Method object**
> <li> The statement `result.append(a)` calls a method of the list object result.
> <li> A **method** is a function that **‘belongs’** to an object and is named `obj.methodname`, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type. Different types define different methods. Methods of different types may have the same name without causing ambiguity. (It is possible to define your own object types and methods, using classes, see Classes) The method append() shown in the example is defined for `list objects`; it adds a new element at the end of the list. In this example it is equivalent to `result = result + [a]`, but more efficient.

#### 2. Defining Functions


```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """Reponse chatbox program"""
    while True:
        ok=input(prompt)
        if ok in ('y','Y','Yes','yes'):
            return True
        if ok in ('N','n','No','Nope'):
            return False
        else: 
            retries-=1
            if retries<0:
                raise ValueError('invalid user response')
        print(reminder)         
```


```python
ask_ok('Ok to overwrite the file',2, 'Come on, only "Yes" or "No"')
```

    Ok to overwrite the file1
    Come on, only "Yes" or "No"
    Ok to overwrite the file2
    Come on, only "Yes" or "No"
    Ok to overwrite the fileN





    False



><li> The default values are evaluated at the point of function definition in the defining scope  
><li> **Important warning:** The default value is evaluated only once. **Non-primitive: This makes a difference when the default is a mutable object such as a `list, dictionary, or instances of most classes`.** For example, the following function accumulates the arguments passed to it on subsequent calls:


```python
#Call by value, assign the value of i to arg
i=5
def f(arg=i):     
    print(arg)  #Arg equals to 5

i=6   #even though i=6, is not effective in the defining scope, so the f()=5 still
f()
```

    5



```python
#Important warning example: Call by reference, assign the value to the mutable object
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

    [1]
    [1, 2]
    [1, 2, 3]


>If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:


```python
def f(a, L=None):
    L=[]
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
```

    [1]
    [2]
    [3]


** *Reference vs Copy**
> <li> In python, the primitive are defined as float, string, bool and int. Pass value by copy. Only change the copy value.   
> <li> Non-premitive as example of class,set, list, dict.  Pass value by reference. So it will change the value of the initial object. 


```python
#w in here is the string element in list, so it pass value by copy. Did not change the value of words.
words=['cat', 'window', 'defenestrate', 'defenestrate']
for w in words:  # Loop over a slice copy of the entire list.
    w='dog'

words
```




    ['cat', 'window', 'defenestrate', 'defenestrate']




```python
# index back to the origin words so
for i in range(len(words)): 
    words[i]='dog'
words 
```




    ['dog', 'dog', 'dog', 'dog']




```python
class Dog:
    def __init__(self):
        self.val='dog'
dogs=[Dog(),Dog(),Dog()]  # create three new obejects of class Dog, and put in the dogs list
for d in dogs:
    print(d.val)
    d.val='cat'
    
for d in dogs:
    print(d.val)
    
```

    dog
    dog
    dog
    cat
    cat
    cat



```python
dog=Dog()   #creation, definition , instantiation  Create a object dog; dog is a reference of Dog()
dogs=[dog,dog,dog]   # The dogs list contains three references of one object.  
for d in dogs:
    print(d.val)
#pass the value 'cat' to the object dog (reference), so the following print statement gives three 'cat'.
dogs[1].val='cat'  
for d in dogs:
    print(d.val)
```

    dog
    dog
    dog
    cat
    cat
    cat


#### 3. Keyword Argument `kwarg`
><li>Functions can also be called using keyword arguments of the form `kwarg=value`. For instance, the following function  
><li>In a function call, **keyword arguments must follow positional arguments**. All the keyword arguments passed must **match 
** one of the arguments accepted by the function (e.g. actor is not a valid argument for the parrot function), and their order is not important. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No argument may receive a value more than once. 



```python
#voltage here is positional, the other three is optional
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'): 
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```


```python
parrot(2300)
```

    -- This parrot wouldn't voom if you put 2300 volts through it.
    -- Lovely plumage, the Norwegian Blue
    -- It's a stiff !



```python
#Here’s an example that fails due to this restriction:
parrot()                     # required argument missing  
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument  
parrot(110, voltage=220)     # duplicate value for the same argument  
parrot(actor='John Cleese')  # unknown keyword argument  
```


      File "<ipython-input-324-ecb6a6062a39>", line 3
        parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
                           ^
    SyntaxError: positional argument follows keyword argument



`**name` = dictionary  
>When a final formal parameter of the form `**name` is present, it receives a `dictionary`  containing **all keyword arguments** except for those corresponding to a formal parameter.   

**`*name`** = tuple
>This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a `tuple` containing the **positional arguments** beyond the formal parameter list. (*name must occur before **name.) 




```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```


```python
cheeseshop("Limburger",    #Kind positional argument
           "It's very runny, sir.",  #tuple
           "It's really very, VERY runny, sir.", #tuple
           shopkeeper="Michael Palin",  #dictionary
           client="John Cleese",        #dictionary
           sketch="Cheese Shop Sketch") #dictionary
```

    -- Do you have any Limburger ?
    -- I'm sorry, we're all out of Limburger
    It's very runny, sir.
    It's really very, VERY runny, sir.
    ----------------------------------------
    shopkeeper : Michael Palin
    client : John Cleese
    sketch : Cheese Shop Sketch


#### 4. Arbitrary Argument lists
>Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a `tuple` (see Tuples and Sequences). Before the variable number of arguments, `zero or more normal` arguments may occur.

>Normally, these `variadic` arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the `*args parameter are ‘keyword-only’ arguments`, meaning that they can only be used as keywords rather than positional arguments.


```python
#  *arg means keyword-only argument
>>> def concat(*args, sep="/"): 
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
>>> concat("earth", "mars", "venus", sep=".")
```




    'earth.mars.venus'



#### 5. Unpacking argument lists
>The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments.  
>For instance, the built-in `range(`) function expects separate `start and stop arguments`. If they are not available separately, write the function call with the `*-operator` to unpack the arguments out of a list or tuple:

>In the same fashion, dictionaries can deliver keyword arguments with the `**-operator`:


```python
args = (3, 6)
```


```python
list(range(*args))
```




    [3, 4, 5]




```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
```


```python
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
```


```python
parrot(**d)
```

    -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !


#### 6. lambda expressions

>Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: `lambda a, b: a+b`. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

>pass a small function as an argument:


```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
```




    [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]



#### 7.Documentation   `function.__doc__`


Here are some conventions about the content and formatting of documentation strings.  

>The first line should always be a **short, concise summary** of the object’s purpose. This line should begin with a **capital letter and end with a period**.  

>If there are more lines in the documentation string, the **second** line should be **blank**, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.  

>The Python parser does not strip indentation from multi-line string literals in Python, so tools that process documentation have to strip indentation if desired. This is done using the following convention. 
>>The **first non-blank line after the first line of the string** determines the amount of indentation for the entire documentation string. (We can’t use the first line since it is generally adjacent to the string’s opening quotes so its indentation is not apparent in the string literal.) Whitespace “equivalent” to this indentation is then stripped from the start of all lines of the string. Lines that are indented less should not occur, but if they occur all their leading whitespace should be stripped. Equivalence of whitespace should be tested after expansion of tabs (to 8 spaces, normally).  


```python
def my_function():
    """Do nothing, but document it.
    
No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
```

    Do nothing, but document it.
        
    No, really, it doesn't do anything.
        


#### 8.Function annotation   `myfunction.__annotations__`

Annotations are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on any other part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation. Return annotations are defined by a literal `->`, followed by an expression, between the parameter list and the colon denoting the end of the def statement. The following example has a positional argument, a keyword argument, and the return value annotated:


```python
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
```

    Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
    Arguments: spam eggs





    'spam and eggs'



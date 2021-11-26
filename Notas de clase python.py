 #funcion tipo
>>> type(1)
<class 'int'>
>>> type(1.3)
<class 'float'>


#escribir una 'cadena' sin hacer la distincion con ( '' / "" ) producira un error 

>>> type(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined

######

#hacer la distincion volvera cualquier variable en una cadena, por ende se clasificara como 'str'

>>> type('a')
<class 'str'>
>>> type('1')
<class 'str'>


##palabras_reservadas = ['and', 'continue', 'else', 'for', 'import', 'not', 'raise', 'assert', 'def', 'except', 'from',
                       'in', 'or', 'return', 'break', 'del', 'exec', 'global', 'is', 'pass', 'try', 'class', 'elif',
                       'finally', 'if', 'lambda', 'print', 'while', 'as']


>>> #concadenacion de cadena no conmuta
>>> x='a'
>>> z='b'

#recordar que la funcion de igualdad esta dada por ' == ', si se usa ' = ' producira error

>>> x+z=z+x
  File "<stdin>", line 1
    x+z=z+x
    ^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

#por otro lado observamos que gracias a los boleanos se nota que las operaciones de cadenas o concadenaciones NO conmutan

>>> x+z==z+x
False
>>>


>>> #Funcion id; la funcion id toma una variable y le asigna un valor entero unico para dicha variable:

>>> id(39)
1688997266864

>>> # OJO: en la funcion id las 'str' se deben denotar con comillas

>>> id(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'g' is not defined

#la forma correcta es:

>>> id('g')
1689003123696
>>>

>>> #Fncion int; toma un valor y lo convierte de ser posible a un entero

>>> int(93.78787)
93
>>> int(21)
21

>>> #funcion float; toma un valor y de ser posible lo vuerlve un valor tipo float

>>> float(2)
2.0
>>> float(2.19821)
2.19821

>>> #funcion str; toma una variable y de ser posible lo vuerlve un valor tipo str o cadena de palabras
>>> str(38)
'38'

#ojo, aqui las variables tipo str tambien deben denotarse con comillas a pesar de la funcion de la operacion str

>>> str(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'g' is not defined

#forma correcta

>>> str('g')
'g'

>>> #Python dispone de un módulo matemático que proporciona la mayoría de las funciones matemáticas habituales.

>>> import math

>>>#podemos asignar una variable tipo str para abreviar la funcion math:


>>> import math as m 
>>> import math as y

>>> # sin y las otras funciones trigonométricas (cos, tan, etc.) toman sus argumentos en radianes.



>>> #Añadir una funcion nueva
>>> #se define  una funcion

>>>  def NOMBRE( LISTA DE PARAMETROS ):
           SENTENCIAS  

>>> def DP(h):        #h es el parametro este puede ser determinado por cualquier variable alfabetica
...     print(h,h)
...

# en la linea de codigo se define la funcion DP con argumento 'h'; la sentencia al ejecutar dicha funcion sobre una variable es hacer 'print(h,h)' teniendo como resulado h h

>>> DP(8) 
8 8

>>> DP('h') #recordar que las tipo str deben ir diferenciadas por lass comillas
h h

# defino otra funcion para ilustrar 

>>> def DL(h):
...     print(h)
...     print(h)
...     print(h)
...

>>> DL(8)
8
8
8
>>>


>>> def PL(p1,p2):
...     cat=p1+p2      #PREGUNTAR SOBRE LAS 'VARIABLES Y PARAMETROS LOCALES DE UNA FUNCION'
...     DL(cat)
...
>>> C1= "Die Jesu domine, "
>>> C2="Dona eis requiem."
>>> PL(C1,C2)
Die Jesu domine, Dona eis requiem.
Die Jesu domine, Dona eis requiem.
Die Jesu domine, Dona eis requiem.







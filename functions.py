#Understanding Functions

#return multiple args
'''
def myfunc():
	return 'Hello','World','Python'


a,b,c = myfunc()
print a
print b
print c

x = myfunc()
'''

#default args
#default params should be at end
'''
def defargs(loc,name='Awantik',gender='male'):
	print loc,name

defargs('Bangalore','Bombay')
defargs('Mumbai')
'''

#variable args
'''
def varargs(*args):
	for arg in args:
		print arg,

varargs('bangalore','Thursday')
varargs('Mumbai')
'''
'''
def varargs(loc='Mumbai',*args):
	for arg in args:
		print arg,
	print loc

varargs('bangalore','Thursday','Mumbai')
varargs('Mumbai','India')
'''
'''
def unpack(name,loc,gender):
	print name,loc,gender

l = ['Awantik','Bangalore','awantikdas@gmail.com']

unpack(*l)
'''

#Keyword based arguments
'''
def kwargsfunc(name,loc,gender='female'):
	print name,loc,gender

kwargsfunc(name='awantikdas',loc='bangalore')
'''

db = {'name':'Awantik','loc':'Bangalore','age':30}
'''
def kwargs(l,m,n,*args,**kwargs):
	print l
	print args
	print kwargs

kwargs('CISCO','Bangalore','Awantik',day='Thursday',loc='bangalore')
'''

def revkwargs(name,loc,age):
	print name,loc,age

revkwargs(**db)






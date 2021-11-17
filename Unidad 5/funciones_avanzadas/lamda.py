# ##############################################
# Recursión ####
# ##############################################
def func1(a, b, c):return a + b + c

print(func1(1, 2, 3))	
print('',end='\n################\n' )	

func2 = lambda a,b,c: a+b+c 
	
print(func2(1, 2, 3))	
print('',end='\n################\n' )	
	
func3 =(lambda a= 4, b= 5, c= 6 :a+b+c)
	
print(func3(1, 2, 3))	
print('',end='\n################\n' )	

input()
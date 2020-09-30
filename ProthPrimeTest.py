# Python3 program to check for Prime Proth number 

n = int(input("Enter a number: "))  

# Funtion to Check power of two 
def isPowerOfTwo(n): 
		
	return (n and (not(n & (n - 1)))) 
	
def ProthPrime(n):
    if n > 1:  
       for i in range(2,n):  
           if (n % i) == 0:  
               print(n,"is not a prime number")   
               break  
       else:  
           print(n,"is a prime number")  
             
    else:  
       print(n,"is not a prime number")

# Function to check if the given number is Proth number or not

def isProthNumber( n): 

	k = 1
	
	while(k < (n//k)): 
		
		# check if k divides n or not 
		if(n % k == 0): 

			# Check if n / k is power of 2 or not 
			if(isPowerOfTwo(n//k)): 
					return True
		
		# update k to next odd number 
		k = k + 2	
	
	'''
	If we reach here means there exists no value of K 
	Such that k is odd number 
	and n / k is a power of 2 greater than k
	'''
	return False
		
# Check n for Proth Number 
if(isProthNumber(n-1)):
    ProthPrime(n)
                 
else: 
	print(n,"is not a Proth number"); 

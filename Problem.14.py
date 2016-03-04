#problem 14 -	Longest Collatz sequence
#This solution uses brute force unfortunately
# You could potentially check if the number has already been in a previous sequence and then add currentChainLength 
# to the chain length of the matched number (although this would be faster would take up more memory)
currentNumber=0
currentChainLength=0
largestChainLength=0
lclStartNumber=0

for i in range(2,1000000):
    currentNumber=i
    currentChainLength=0
    while currentNumber!=1:
        if currentNumber%2==0:
            currentNumber=currentNumber/2
        else:
            currentNumber=(3*currentNumber)+1
        currentChainLength+=1
        if currentChainLength>largestChainLength:
            largestChainLength=currentChainLength
            lclStartNumber=i
print(lclStartNumber)
            
        
    
    

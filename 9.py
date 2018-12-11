def findSum(A, B): 
    ans = 0; 
  
    # Iterate from 1 to A && 
    # evaluating and adding i % B. 
    for i in range(1, A + 1): 
        ans += (i % B); 
  
    return ans; 
  
# Driver Code 
A = 20;  
B = 2; 
print(findSum(A, B)); 

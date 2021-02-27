def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort() #first we shall sort the array 
	
	
	left = 0
	right = len(array) - 1
	
	
	while (left<right):
		
		answer = array[left] + array[right]
		
		if answer == targetSum:
			return [array[left],array[right]]
		
		elif (answer < targetSum):
			left+= 1
			
		elif (answer > targetSum):
			right-= 1
		
		
		
	
			
	return []
		

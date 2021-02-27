def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort() #first we shall sort the array 
	
	
	left = 0 #starting index of the array
	right = len(array) - 1 #last index of the array
	
	
	while (left<right): #while we don't reach the middle
		
		answer = array[left] + array[right] # check the sum of first and last number
		
		if answer == targetSum: #if they are equal then all good.
			return [array[left],array[right]] #return
		
		elif (answer < targetSum): # if the answer is falling short then obviosuly increment left as we sorted the array 
			left+= 1
			
		elif (answer > targetSum): # if the anser is greater than move down from right.
			right-= 1
		
		
		
	
			
	return []
		

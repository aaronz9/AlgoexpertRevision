def isValidSubsequence(array, sequence):
    # Write your code here.
    arrayIndex = 0 #array index should be 0
	seqIndex = 0 #sequence index should be 0
	
	# while both don't reach out of bounds
	while arrayIndex < len(array) and seqIndex < len(sequence):
		
		#if match is found increment
		if array[arrayIndex] == sequence[seqIndex]:
			seqIndex+= 1
		#move the index further	
		arrayIndex+= 1
	
	#return the length of the sequence
	return seqIndex == len(sequence)



-----------------Solution2------------------------------------------

def isValidSubsequence(array, sequence):
    # Write your code here.
	arrayIndex = 0 #make this the index of the array
	sequenceIndex = 0 #make this index of the sequence
	
	for i in array: #make a for loop
		
		if sequenceIndex == len (sequence): # if lenghts are same come out
			break
		
		if sequence[sequenceIndex] == i: # if match is found increment
			sequenceIndex += 1
		else:
			
			arrayIndex += 1 #of increase the length of the array 
		
	#return length of sequence
	return sequenceIndex == len(sequence)
			
	

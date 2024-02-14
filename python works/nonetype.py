def fun():
    a=100
    
print(fun())
#it returns none





from collections import Counter


def find_dup_char(input):
    WC = Counter(input)
    print(WC)# now create dictionary using counter method
	         # which will have strings as key and their
	         # frequencies as value
    for letter, count in WC.items():
		        if (count > 1):       # Finding no. of occurrence of a character
	                                  # and get the index of it.
			           print(letter,count)

	
	
	
	
# Driver program
if __name__ == "__main__":
	input = 'geeksforgeeks'
	find_dup_char(input)
    
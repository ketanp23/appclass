tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

#tuple elements
#abcd->0,786->1,2.23->2,john->3,70.2->4
# Total elements are 5


print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 1st to 2nd considering we start from 0 being abcd 
print (tuple[2:])       # Prints elements starting from 2nd element considering we start from 0 being abcd
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple
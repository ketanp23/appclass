list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

#list elements
#abcd->0,786->1,2.23->2,john->3,70.2->4
# Total elements are 5

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 1st to 2nd considering we start from 0 being abcd 
print (list[2:])      # Prints elements starting from 2nd element considering we start from 0 being abcd
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists
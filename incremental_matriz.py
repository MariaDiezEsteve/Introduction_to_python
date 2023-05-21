"""
Create a matrix list n x n
    it's going to build the list for us and in this case, it's going to build a list that contains multiple lists inside of it.
[
    [ 0, 1, 2, 3, 4],
    [ 1, 2, 3, 4, 5],
    [ 2, 3, 4, 5, 6],
    [ 3, 4, 5, 6, 7],
    [ 4, 5, 6, 7, 8],
]
"""

 #nested = matriz anidada.

def manual_incrementring_matrix(n): #we created a function and the function takes in how many items that you want the matrix to be,  each one of those nested lists will contain the same number of items and that's doing exactly what we're asked to do right up here.
    
    #matrix n x n
    matrix = [[ None for y in range(n)] for x in range(n)] #I'll say none for y in range and then I'm going to pass in the range which is going to be n so this is going to allow us to build a set of empty values and it's going to define exactly how many it's going to create for us.
    #Print:
    """
    [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]
    """
    #we are looking to increment the count
    counter = 0
    
    
    
    for idx, el in enumerate(matrix):
        #nested for loop so I can say four and I need to keep track of the index and so we can do that by saying for idx which is just short for index. 
        #  loop over from 1 to 5. I want you to go through this five times and then for each time I want you to assign the value of none and then I want you to go and do that again for the parent structure and that's how we were able to create five elements just like this or n elements and then go inside and create 5 elements or n elements inside each one of those items from there we created a counter set it equal to zero because this was kind of the trick we were able to use because the counter is the way we are able to increment our values.
        #for idx which is just short for index.
        for nested_idx, nested_el in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx
           
            #we use the enumerate function or we cast the matrix so that we could use this cool little trick where we can grab the index and we could loop over and have access to the element
        counter += 1
    
    
    return matrix

print(manual_incrementring_matrix(5))




    

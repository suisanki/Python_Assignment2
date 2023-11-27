def flatten(input_list):
    #Check if input is a list
    if type(input_list) != list:
        raise ValueError("Input is not a list.")
    #Base case where list is empty
    if input_list == []:
        return input_list
    
    """If first element of the list is a list, apply 'flatten' to it, 
    and apply 'flatten' to rest of the list recursively."""
    if isinstance(input_list[0], list):
        return flatten(input_list[0]) + flatten(input_list[1:])
    
    """"If first element of the list is not list, return it and apply 'flatten'
    to rest of the list recursively. First element should be selected as 
    [:1] rather than [0] because there will be int+list TypeError when 
    connecting the results from recursion."""
    return input_list[:1]+ flatten(input_list[1:])

if __name__ == "__main__":
    try:
        print(flatten())
    
    except ValueError as msg:
        print(msg)
    
    except TypeError:
        print("Required argument missing. Enter a list.")
    

        


def find_index_of_components():
    
    #Long lines of error handling, trying to make errors more understandable.
    input_str = input("Enter a list of integers: ")
    
    if input_str == "":
        raise ValueError("Input list is empty. Try again.\n")
    
    if input_str[0] != "[" or input_str[-1] != "]":
        raise ValueError("Input is not a list. Try again.\n")
    
    """Here comes inefficient nested for loop. I know this is not ideal, but
    please take this part as a practice to handle error with easy to 
    understand error messages."""
    input_str = input_str[1:-1].split(",")
    for component in input_str:
        for char in component:
            if not(47 < ord(char) < 58):
                raise ValueError("The list contains non-integer value. Try again.\n")
    
    input_list = [int(x) for x in input_str]
            
    target_str = input("Enter a target integer: ")
    
    if target_str == "":
        raise ValueError("Target is empty. Try again.\n")
    
    for char in target_str:
        if not(47 < ord(char) < 58):
            raise ValueError("Target is not an integer. Try again.\n")
        
    target = int(target_str)
    
    if target_str == "":
        raise ValueError("Target is empty. Try again.\n")
        
    target = int(target_str)
    
    #Calculation part. Applying blute force
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            #Avoid picking up same indice
            if i == j:
                continue
          
            if input_list[i]+input_list[j] == target:
               print([i,j])
               return 
    #Print -1 if there is no pair that adds up to target
    print(-1)
    return

if __name__ == "__main__":
    while True:
        try:
            find_index_of_components()
            break
        
        except ValueError as msg:
            print(msg)


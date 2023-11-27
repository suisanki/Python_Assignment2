def integefier():
    in_str = input("Please input number: ")
    neg_flag = False
    integer = 0
    
    #Raise error if the input is empty.
    if in_str == "":
        raise ValueError("Input is empty. Try again.\n")
    
    #Set a flag to see if the input is positive or negative
    if in_str[0] == "+" or in_str[0] == "-":
        if in_str[0] == "-":
            neg_flag = True
        
        #Get rid of + or - sign.
        in_str = in_str[1:]
    
    """If each component of the string is a number, change it to decimal
    Unicode and subtract 48 to make it same int number. Multiply by power
    of tens to keep degree information."""
    for i in range(len(in_str)):
        char_index = len(in_str)-i-1
        
        if 47 < ord(in_str[char_index]) < 58:
            integer = integer + (10**i)*(ord(in_str[char_index])-48) 
        
        #If a component is not a number, raise an error
        else:
            raise ValueError("Invalid character detected. Try again.\n")       
    
    #Make the number negative if the flag is True.
    if neg_flag == True:
        integer = -integer
    
    print(integer)
    print(type(integer))
    return

if __name__ == "__main__":
    while True:
        try:
            integefier()
            break
    
        except ValueError as msg:
            print(msg)    
                
            
        
        
        
        

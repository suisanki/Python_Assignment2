def longest_consecutive_zeros():
    in_str = input("Please input series of 0 and 1: ")
    counter = 0
    counter_counter = []
    i = 0
    
    #check if input is empty
    if in_str == "":
        raise ValueError("Input is empty. Try again.\n")
    
    while i < len(in_str):
        #If chr is '0', increment counter
        if in_str[i] == "0":
            counter += 1
            i = i+1
        
        #If chr is '1', append result of counter to list and reset counter
        elif in_str[i] == "1":
            counter_counter.append(counter)
            counter = 0
            i = i+1
        
        #Raise error if there is any chr other than '0' or '1'
        else:
            raise ValueError("Input other than 0 or 1 detected. Try again.\n")
            break
    
    #Clean up the counter. This is needed when in_str ends with 0s
    counter_counter.append(counter)
    
    print(max(counter_counter))
    return

if __name__ == "__main__":
    while True:
        try:
            longest_consecutive_zeros()
            break
        
        except ValueError as msg:
            print(msg)
        
    
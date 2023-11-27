def find_index_of_components():
    input_str = input("Enter a list of integers: ")
    
    if input_str == "":
        raise ValueError("Input list is empty. Try again.\n")
    
    if input_str[0] != "[" or input_str[-1] != "]":
        raise ValueError("Input is not a list. Try again.\n")
    
    """Again, this is an inefficient nested for loops. I know it is inefficient
    but wanted to practice how to prepare for and handle errors."""
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
    #Copy input list
    sorted_input = [x for x in input_list]
    #Sort input list
    sorted_input.sort()
    i = 0
    j = len(input_list)-1
    sum = 0
    
    """Add smallest and biggest numbers of input list. If the result is smaller
    than the target, swap the smallest to second smallest. If the result is 
    bigger than the target, swap the biggest with second biggest, and continue
    till there is a match. This suppose to be O(n/2) so more efficient."""
    while i < len(input_list) and j > 0:
        sum = sorted_input[i] + sorted_input[j]
        
        if sum == target:
            ans1 = input_list.index(sorted_input[i])
            input_list[ans1] = None
            
            ans2 = input_list.index(sorted_input[j])
            
            print([ans1,ans2])
            return 
        
        elif sum > target:
            j = j-1
        
        elif sum < target:
            i = i+1
    
    #Return -1 if there is no such a pair
    print(-1)
    return 

if __name__ == "__main__":
    while True:
        try:
            find_index_of_components()
            break
        
        except ValueError as msg:
            print(msg)


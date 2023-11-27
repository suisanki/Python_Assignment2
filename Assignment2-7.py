def stair(n):
    #Raising error for irregular input
    if type(n) != int:
        raise ValueError("Input is not an integer.")
    
    """As analysed in the video, counting number of ways to climb up
    n-step stairs with 1 or 2 steps is equal to calculating n+1th number
    of a Fibonacci sequence. So simple Fibonacci recursion code will do.""" 
    if n in [0,1]:
        return 1
    return stair(n-2) + stair(n-1)

if __name__ == "__main__":
    try:
        print(stair())
    
    except ValueError as msg:
        print(msg)
    
    except TypeError:
        print("Required argument missing. Enter an integer.")

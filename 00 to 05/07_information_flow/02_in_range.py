def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:  
        return True
    return False

def main():
    
    print(in_range(5, 1, 10))  
    print(in_range(0, 1, 10))  
    print(in_range(10, 1, 10)) 

if __name__ == '__main__':
    main()

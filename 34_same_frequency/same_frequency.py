def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1 = str(num1)
    num2 = str(num2)

    nums1 = set(num1)
    for num in nums1:
        if str(num1).count(num) != num2.count(num):
            return False
        
    nums2 = set(num2)
    for num in nums2:
        if num1.count(num) != num2.count(num):
            return False
        
    return True
def edit_dict(my_dict, my_list):
    for i in my_list:
        if my_dict.get(i) != None:
            my_dict.pop(i)
    
    return my_dict
    
def isAnagram(str1, str2):
    """
    :type str1: str
    :type str2: str
    :return type: bool
    """
    for i in str1:
        for j in str2:
            if i == j:
                str1 = str1.replace(i, '')
                str2 =str2.replace(j, '')
        
    if str1 and str2 != '':
        return False
    else:
        return True
        
def twoSum(nums, target):
    newlist = []
    for i in range(0, len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                newlist.append(i)
                newlist.append(j)
                return newlist
                
    return newlist

def unique (in_list=[]):
    empty_list=[]
    for el in in_list: 
        if el not in empty_list:
            empty_list.append(el)
    return empty_list
        

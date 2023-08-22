def common_elements(list1,list2):
    set1=set(list1)
    set2=set(list2)
    common_element=set1.intersection(set2)
    result_list=list(common_element)
    return result_list
list1=[1,2,3,4,2]
list2=[3,4,5,2,4]
result=common_elements(list1,list2)
print("output will be:",result)

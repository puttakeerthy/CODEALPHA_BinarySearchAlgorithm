from array import *
def Binary_search(l,start,end,item):
    if(end>=start):
        middle=(start+end)//2
        if l[middle]==item:
            return middle
        elif item<l[middle]:
            return Binary_search(l,start,middle-1,item)
        else:
            return Binary_search(l,middle+1,end,item)
    else:
        return -1
    
print("*****ENTER ELEMENTS WITH SEPERATED BY CAMMAS******\n")
print("-------------------------------------------------------\n")
list=[int(x) for x in input("enter list elements").split(',')]
list.sort()
search_key=int(input("ENTER SEARCH ELEMENT:"))
print("\nTHE GIVEN LIST OF ELEMENTS:")
print(list)
i=Binary_search(list,0,len(list)-1,search_key)
if i!=-1:
    print("Element searched is FOUND at the index",i,"of given list")
else:
    print("Element searched is NOT FOUND in the given list!")


#I won't be making the explanations made in
#find_kth_book_1 function again so this will just focus
#on the differences between the first one and the second
#one.
#In this version instead of decreasing the problem by
#either size1/2 or size2/2 we will decrease all arrays
#by k/2. Therefore we will be comparing the k/2th element
#instead of the middle ones. Juts like before we have
#to change the value of k since in every recursion step
#the size of array is changing as well. The decrease amount
#before was either m1-1 or m2-1 but this time it is k/2
#so in each step we have to decrease k by k/2. Note that
#we can't really just say k=k/2 since for example 5/2=2
#but 5-5/2=3 etc(Trust me i tried that and couldn't figure out
#why it wasn't working since i was thinking in normal math...).
#This approach comes with other problems of course. Such as
#array sizes not being enough for the k/2th index so we have
#to check that for every array in each step. We can't just
#take len(arr) because we are actually decreasing the size
#by changing the start values so the correct size value
#will be end-start.And if the array size is not enough
#we of course can't compare the k/2th element since the
#array doesn't have that many. So we will instead compare the
#last element of that array with the k/2th element of the other.
#If both sizes are enough we simply just increase the starting
#index of smaller one since the value can never be at its
#left half.
#The main benefit here is that instead of decreasing the array
#in each step by size1/2 or size2/2 we simply keep decreasing it
#by k/2 in each step. This way the time complexity is dependent
#on k instead of array sizes. So it is O(logk).


def find_kth_book_2(arr1,arr2,k):
    return find_kth_book_2_helper(arr1,arr2,0,0,len(arr1),len(arr2),k)

def find_kth_book_2_helper(arr1,arr2,start1,start2,end1,end2,k):
    if(start1==end1):
        return arr2[start2+k-1]
    if(start2==end2):
        return arr1[start1+k-1]
    
    size1=end1-start1
    size2=end2-start2
    #print(start1,end1,"-",start2,end2,"--",k)
    if(k>size1+size2 or k <= 0):
        return "error"
    
    if(k==1):
        if(arr1[start1]<arr2[start2]):
            return arr1[start1]
        else:
            return arr2[start2]
    
    sliceP=k//2
    #print(sliceP)
    if(sliceP> end1-start1):
        
        if(arr1[end1-1]<arr2[start2+sliceP-1]):
            #print("here1",start2+start1-end1+k-1)
            return arr2[start2+start1-end1+k-1];
        else:
            #print("here2")
            return find_kth_book_2_helper(arr1,arr2,start1,start2+sliceP,end1,end2,k-sliceP)
    
    if(sliceP> end2-start2):
        
        if(arr2[end2-1]<arr1[start1+sliceP-1]):
            #print("here3")
            return arr1[start1+start2-end2+k-1];
        else:
            #print("here4")
            return find_kth_book_2_helper(arr1,arr2,start1+sliceP,start2,end1,end2,k-sliceP)
        
    else:
        
        if(arr1[sliceP+start1-1]<arr2[sliceP+start2-1]):
            #print("here5")
            return find_kth_book_2_helper(arr1,arr2,start1+sliceP,start2,end1,end2,k-sliceP)
        else:
            #print("here6")
            return find_kth_book_2_helper(arr1,arr2,start1,start2+sliceP,end1,end2,k-sliceP)
        
        
m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_2(m,n,4)
print(book)
#Output: oop
book = find_kth_book_2(m,n,6)
print(book)
#Output: systemsprogramming
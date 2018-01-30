#Since we are asked to find the kth element in 2 SORTED
#arrays we don't have to worry about sorting and
#can assume in which half the element has to be.
#If it is smaller than the element we are comparing it with
#then it means that the element we are looking for is at
#the left half of the array.
#Just like in binary search we will slice the arrays into
#2 halves at each step. The main problem here is deciding
#which array will be sliced and what part of it will be
#thrown away. As explained before we can know what part will
#be thrown away by simply comparing it with the middle element.
#The index for the middle element might be different for each
#array so we need different middle indexes for each of them.
#This function only takes 2 arrays so we will have 2.
#Imagine these arrays as merged in sorted way, in that case if we
#compare k with sum of m1 and m2(also equal to (size1+size2)/2)
#we can know  if it is in the left half or right half ! So we
#know which part to throw away. After that we need to know
#which array will be sliced(Note that the slicing is made by
#either increasing the start(throw left) or decreasing
#the end(throw right)). To decide that we simply need to
#compare both of their middle elements. For example
#if k is greater than the middle index of the merged
#array and arr1 has greater value on middle index than
#arr2 then it means that the kth element can never be
#at the left part of arr2 so just throw that away!
#Of course if we are going to get rid of a part of array
#then it means that the total size for the merged array will
#be changed therefore the index of the kth element will
#be changed too.To prevent that from happening we simply
#change the value of k according to the changes made to
#the size. In the example before we were getting rid of
#left part of arr2 by increasing the start by m2+1 so we
#just need to decrease k by the same amount.
#After that we make a recursive call. This means that we
#are creating a new subproblem with decreased size
#(decreased by half of one of the arrays). This goes on until
#the base case is reached.
#Since this works just like binary search which has the
#time complexity of O(logn) this function has the time
#complexity of O(logn+logm) since we are slicing only 1
#array in each step.
#PS:n is the size of first array and m is the size of second.

import sys


#def mergeArrays(arr,arr2):
    
#    res=[]
#    i=iter(arr2)
#    j=i.__next__()
#    for k in arr:
#        while (j<k):
#            res.append(j)
#            j=i.next()
#        res.append(k)
#    res.append(j)
#    res.extend(it)
#    return res

#print(mergeArrays(m,n))

def find_kth_book_1(arr1,arr2,k):
    if(k>0):
        return find_kth_book_1_helper(arr1,arr2,0,0,len(arr1),len(arr2),k-1)
    


def find_kth_book_1_helper(arr1,arr2,start1,start2,end1,end2,k):
    #print("- -",end1,start1,end2,start2,k)
    if(start1==end1):
        return arr2[start2+k]
    if(start2==end2):
        return arr1[start1+k];
    
    m1=(end1-start1)//2
    m2=(end2-start2)//2
    #print(m1,m2,end1,start1,end2,start2,k)
    if(m1+m2<k):
        if(arr1[start1+m1]>arr2[start2+m2]):
            return find_kth_book_1_helper(arr1,arr2,start1,start2+m2+1,end1,end2,k-m2-1)
        else:
            return find_kth_book_1_helper(arr1,arr2,start1+m1+1,start2,end1,end2,k-m1-1)
    else:
        if(arr1[start1+m1]>arr2[start2+m2]):
            return find_kth_book_1_helper(arr1,arr2,start1,start2,start1+m1,end2,k)
        else:
            return find_kth_book_1_helper(arr1,arr2,start1,start2,end1,start2+m2,k)

m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book = find_kth_book_1(m,n,4)
print(book)
#Output: oop
book = find_kth_book_1(m,n,6)
print(book)
#Output: systemsprogramming



#book = find_kth_book_1_helper(m,n,0,0,len(m),len(n),3)
#print(book)
    
#print("a">"c")
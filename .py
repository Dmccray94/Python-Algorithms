# question 1

words = ['this' , 'is', 'a', 'sentence', '.']

def swaps(alist, a, b, c, d, e):
    alist[a],alist[b],alist[c],alist[d],alist[e] = alist[e],alist[d][::-1],alist[c][::-1],alist[b][::-1],alist[a][::-1]
    return alist

print(swaps(words, 0,1,2,3,4))

# question 2

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def wordcount(alist):
    alist_split = alist.split(" ")
    count = {}
    for word in alist_split:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return sorted(count.items())
            
(wordcount(a_text))

# question 3 

def linearSearch(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i

linearSearch([1,3,5,7,9,11,13], 13)

# question 4 Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of “F” greater than or equal to 2 returns “Outage”, anything below returns “Power”
# Example Input: ['T', 'F', 'F', 'F']
# Example Output: “Outage”

def outage(l_street):
    x = l_street.count('F')
    if x >= 2:
        print("outage")
    else:
        print("Power")
                
l_street = ['T', 'F', 'F', 'F']
outage(l_street)

def outage2(l_street):
    f_counter = 0
    for letter in l_street:
        if letter == "F":
            f_counter += 1
    if f_counter >=2:
        print("outage")
    else:
        print("power")
        
outage2(l_street)
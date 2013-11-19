def subset_sum_recursive(numbers,target,partial):
    s = sum(partial)

    #check if the partial sum is equals to target
    if s >= target: 
        print "sum(%s)=%s"%(partial,target)
    if s >= target:
        return # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum_recursive(remaining,target,partial + [n]) 

def subset_sum(numbers,target):
    #we need an intermediate function to start the recursion.
    #the recursion start with an empty list as partial solution.
    subset_sum_recursive(numbers,target,list())

if __name__ == "__main__":
    subset_sum([28.79,25.46,4.03,16.66,14.81,2.46,7.79],51)


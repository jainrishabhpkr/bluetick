def missing_ranges(arr, lower , upper) : 

    arr_len = len(arr)
    
    seen = [False]*upper


    for i in range(arr_len) :
      if (arr[i] < upper and arr[i] >= lower) :
        seen[arr[i]] = True
     
    i = lower
    ans = []
    while (i < upper) :
     
      if (seen[i] == False) :
       
        j = i + 1
        while (j < upper and seen[j] == False) :
          j += 1

        p = j - 1
        if(i + 1 == j) :   
          ans.append(str(i))
         
        else :
            x = str(i)+"->"+str(p)
            ans.append(x)
     
        # Update u
        i = j
       
      else :
        i += 1

    return ans

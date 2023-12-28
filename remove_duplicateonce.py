def remove(num,target):
    res = ""
    count = 1
    for i in num:
        if i==target:
            if count==1:
                count+=1
            elif count!=1:
                res += i
        else:
            res+=i
    return res

print(remove("1231","1"))
      


            
        

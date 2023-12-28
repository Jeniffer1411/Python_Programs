def pass_check(s):
    if len(s)>=8:
        return any(i.isupper() for i in s) and any(i.isdigit() for i in s) and any(i.islower() for i in s) and any(not i.isalpha() and not i.isdigit() for i in s)
    else:
        return False
    
s = "Santhosh984#"
print(pass_check(s))

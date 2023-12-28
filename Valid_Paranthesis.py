def isValid(s):
    stack = []
    l = set("({[")
    r = set(")}]")
    key = {"]":"[",")":"(","}":"{"}
    for i in s:
        if i in l:
            stack.append(i)
        if i in r:
            if not stack:
                return False
            elif stack.pop() != key[i]:
                return False
            else:
                continue
    if not stack:
        return True
    else:
        return False

print(isValid("()([)]"))

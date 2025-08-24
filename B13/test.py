def check(check1):
    diem = 0
    for test in check1:
        if test == "(":
            diem += 1
        elif test == ")":
            diem -= 1
        if diem < 0:
            return False
    return diem == 0
            
# test
print(check("()(("))
print(check("()"))
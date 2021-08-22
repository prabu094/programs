'''
input=modify_variable
output=modifyVariable'''


def fun1(s):
  def fun2(s):
        v=[]
        for i in s:
            if i.isupper()!=True:
                v.append(i)
            elif i.isupper()==True:
                v.append(('_'+i.lower()))
        return(''.join(v))
    def fun3(s):
        v=s.split('_')
        n=[v[0]]
        for i in range(1,len(v)):
            n.append(v[i].title())
        return(''.join(n))
    for i in s:
        if i.isupper()==True:
            return(fun2(s))
        elif i=="_":
            return(fun3(s))
print(fun1(input()))
def fun1(s):
    def fun2(s):
        v=[]
        for i in s:
            if i.isupper()!=True:
                v.append(i)
            elif i.isupper()==True:
                v.append(('_'+i.lower()))
        return(''.join(v))
    def fun3(s):
        v=s.split('_')
        n=[v[0]]
        for i in range(1,len(v)):
            n.append(v[i].title())
        return(''.join(n))
    for i in s:
        if i.isupper()==True:
            return(fun2(s))
        elif i=="_":
            return(fun3(s))
print(fun1(input()))

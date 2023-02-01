def myAtoi(s):

        num=""
        x="+"
        check=0
        checked=0
        for i in range(len(s)):
            if s[i].isnumeric():
                num=num+s[i]
                checked=1
            elif s[i]=="-":
                x="-"
            elif s[i]==".":
                result(num,x)
            elif checked==0:

                if s[i]!="-" and s[i]!=" ":
                
                    check=s[i]
                    if check.isnumeric()==False:
                        checked+=1
                        return 0
            
        if num=="":
            return 0
        res=int(num)        
        if int(num)>2147483647:
            if x=="-":
                res=2147483648
            else:
                res=2147483647
        if x=="-":
            return -res
        return res
s="hello 1234"
print(myAtoi(s))
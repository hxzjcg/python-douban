import re


def IfLong(Massage):
    ans=""
    if len(Massage)==0:
        return ans
    else:
        ans=str(Massage[0])
    return ans
def Dta_book(M):
    ans = ""
    if len(M) == 0:
        return ans
    else:
        ans = str(M[0])
        if len(ans) > 20:
            ans=re.sub('[^\u4e00-\u9fa5]+', '', ans)
    return ans

def Dta_author(Ma):
    ans = ""
    if len(Ma) == 0:
        return ans
    else:
        ans=str(Ma[0])
        ans=ans.replace("("," ")
        ans=ans.replace(")"," ")
        ans=re.sub('[^\u4e00-\u9fa5]+', ',', Ma[0])
    return ans


def delete(strs):
    ans=''
    index=0
    for x in strs:
        x=re.sub('[^\u4e00-\u9fa5]+', '', x)
        if "展开全部" in x :
            x=""
        if index<len(strs):
            ans=ans+x+","
        else:
            ans=ans+x+"。"
    return ans

def yuanwen(yuanwen):
    ans=''
    if len(yuanwen)==0:
        return ans
    else:
        ans=str(yuanwen[0])
        ans=ans.replace("("," ")
        ans=ans.replace("\n","")
        return ans
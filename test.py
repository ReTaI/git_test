string=input()
if(string!=""):
    maxlen=0
    for i in range (0,string.__len__()):
        left=i
        right=i+1
        len=0
        while(left>=0) and (right<string.__len__()) and (string[left]==string[right]):
            len+=1
            if(len>maxlen):
                maxlen=len
                longest=string[left:right+1]
            left-=1
            right+=1
    for i in range (0,string.__len__()):
        left=i-1
        right=i+1
        len=0
        while(left>=0) and (right<string.__len__()) and (string[left]==string[right]):
            len+=1
            if(len>maxlen):
                maxlen=len
                longest=string[left:right+1]
            left-=1
            right+=1
    print(longest)
else:
    exit(1)
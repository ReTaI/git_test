string=input()
maxlen=0
for l in range (0,string.__len__()):
    k=0
    len=0
    while(l-k>=0) and (l + k < string.__len__()):
        if string[l-k]==string[l+k]:
            len+=1
            if(len>maxlen):
                maxlen = len
                longest=string[l-k:l+k+1]
        k=k+1
print(longest)
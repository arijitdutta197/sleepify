import pandas as pd
import re

df=pd.read_excel("test.xlsx")

def modify_rating_cols(col):
    dcol=[]
    for i in range(len(df)):
        temp=df.loc[i,col]
        num=re.search("[0-3]", temp)
        dcol.append(int(num[0]))
    return dcol


def modify_time_cols(col):
    dcol=[]
    for i in range(len(df)):
        s=str(df.loc[i,col])
        temp=''
        #print(temp)
        if not temp:
            temp= re.findall("[0-9][0-9]*:[0-9][0-9]*",s)
        if not temp:
            temp= re.findall("[0-9][0-9]*\.[0-9][0-9]*",s)
        if not temp:
            temp= re.findall("[0-9][0-9]*",s)
        dcol.append(temp[-1])
        #print(i,temp,df.loc[i,1.0],sep="\t\t\t")
    #print(type(dcol1[0]))
    for i in range(len(dcol)):
        if ':'not in dcol[i] and '.' not in dcol[i]:
            dcol[i]=dcol[i]+":00"
        elif ':' not in dcol[i]:
            #ind=dcol1[i].index('.')
            ind=dcol[i].replace('.',':',1)
            dcol[i]=ind
    return dcol


dcol1_0=[i for i in modify_time_cols(1.0)]
dcol3_0=[i for i in modify_time_cols(3.0)]
dcol5_1=[i for i in modify_rating_cols(5.1)]
dcol5_2=[i for i in modify_rating_cols(5.2)]
dcol5_3=[i for i in modify_rating_cols(5.3)]
dcol5_4=[i for i in modify_rating_cols(5.4)]
dcol5_5=[i for i in modify_rating_cols(5.5)]
dcol5_6=[i for i in modify_rating_cols(5.6)]
dcol5_7=[i for i in modify_rating_cols(5.7)]
dcol5_8=[i for i in modify_rating_cols(5.8)]
dcol5_9=[i for i in modify_rating_cols(5.9)]
dcol6_0=[i for i in modify_rating_cols(6.0)]
dcol7_0=[i for i in modify_rating_cols(7.0)]
dcol8_0=[i for i in modify_rating_cols(8.0)]
dcol9_0=[i for i in modify_rating_cols(9.0)]

print(dcol3_0)


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
        if not temp:
            temp= re.findall("[0-9][0-9]*:[0-9][0-9]*",s)
        if not temp:
            temp= re.findall("[0-9][0-9]*\.[0-9][0-9]*",s)
        if not temp:
            temp= re.findall("[0-9][0-9]*",s)
        dcol.append(temp[-1])
    for i in range(len(dcol)):
        if ':'not in dcol[i] and '.' not in dcol[i]:
            dcol[i]=dcol[i]+":00"
        elif ':' not in dcol[i]:
            ind=dcol[i].replace('.',':',1)
            dcol[i]=ind
    return dcol

def modify_minute_cols(col):
    dcol=[]
    for i in range(len(df)):
        s = str(df.loc[i,col])
        temp = re.findall("[0-9]*[0-9]",s)
        dcol.append(int(temp[-1]))
        if dcol[i]>120:
            dcol[i]=120
    return dcol

def modify_hour_cols(col):
    dcol=[]
    for i in range(len(df)):
        s = str(df.loc[i,col])
        s = s.replace('.',':')
        temp=[]
        if ':' in s:
            temp = re.findall("[0-9][0-9]*",s)
            temp[0]=int(temp[0])
            temp[1]=int(temp[1])
            if temp[1] >= 10:
                temp[0] = temp[0]+(temp[1]/60)
            else:
                temp[0] = temp[0]+0.1*temp[1]
        else:
            temp = re.findall("[0-9][0-9]|[0-9]",s)
            for j in range(len(temp)):
                temp[j]=int(temp[j])
                if temp[j] >= 10 and j%2 != 0:
                    temp[j] = temp[j]/60
            if len(temp) > 1 and temp[1] <= 1:
                temp[0] = temp[0]+temp[1]
            elif len(temp) > 1:
                temp[0]=max(temp)
        dcol.append(temp[0])
    return dcol

dcol1_0 = modify_time_cols(1.0)
dcol2_0 = modify_minute_cols(2.0)
dcol3_0 = modify_time_cols(3.0)
dcol4_0 = modify_hour_cols(4.0)
dcol5_1 = modify_rating_cols(5.1)
dcol5_2 = modify_rating_cols(5.2)
dcol5_3 = modify_rating_cols(5.3)
dcol5_4 = modify_rating_cols(5.4)
dcol5_5 = modify_rating_cols(5.5)
dcol5_6 = modify_rating_cols(5.6)
dcol5_7 = modify_rating_cols(5.7)
dcol5_8 = modify_rating_cols(5.8)
dcol5_9 = modify_rating_cols(5.9)
dcol6_0 = modify_rating_cols(6.0)
dcol7_0 = modify_rating_cols(7.0)
dcol8_0 = modify_rating_cols(8.0)
dcol9_0 = modify_rating_cols(9.0)



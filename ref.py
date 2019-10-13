import pandas as pd
import re

df=pd.read_excel("test2.xlsx")

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


"""data = []
data.append(modify_time_cols(1.0))
data.append(modify_minute_cols(2.0))
data.append(modify_time_cols(3.0))
data.append(modify_hour_cols(4.0))
data.append(modify_rating_cols(5.1))
data.append(modify_rating_cols(5.2))
data.append(modify_rating_cols(5.3))
data.append(modify_rating_cols(5.4))
data.append(modify_rating_cols(5.5))
data.append(modify_rating_cols(5.6))
data.append(modify_rating_cols(5.7))
data.append(modify_rating_cols(5.8))
data.append(modify_rating_cols(5.9))
data.append(modify_rating_cols(6.0))
data.append(modify_rating_cols(7.0))
data.append(modify_rating_cols(8.0))
data.append(modify_rating_cols(9.0))

df1 = pd.DataFrame(data)
df1 = df1.transpose()
print(df1)"""
##########################################################################
#final data setting

#this method converts string time to integer time for col1.0 and gives it in 24 hrs format considering person sleeps befor 6 am
#data1 = modify_time_cols(1.0) 
def get_hour_min_sleep_time(data1):
    dcol=[]
    for i in range(len(data1)):
        ind = data1[i].index(':')
        if ind == 1:
            h = int(data1[i][0])
        else:
            h = int(data1[i][0]+data1[i][1])
        if h == 12:
            h = 0
        elif h>6 and h<12:
            h = h+12    
        
        if len(data1[i])-ind == 2:
            m = 10*int(data1[i][ind+1])
        else:
            m = 10*int(data1[i][ind+1])+int(data1[i][ind+2])
            
        dcol.append([h,m])
        #print(ind,data1[i],dcol[i],h,m)
    #print(dcol)
    return dcol

#this method converts string time to integer time for col3.0 and gives it in 24 hrs format considering person wakes up after 3am
#data1 = modify_time_cols(3.0) 
def get_hour_min_awake_time(data1):
    dcol=[]
    for i in range(len(data1)):
        ind=data1[i].index(':')
        if ind == 1:
            h = int(data1[i][0])
        else:
            h = int(data1[i][0]+data1[i][1])
        if h > 12 and h<=3:
            h = h+12
            
        if len(data1[i])-ind == 2:
            m = 10*int(data1[i][ind+1])
        else:
            m = 10*int(data1[i][ind+1])+int(data1[i][ind+2])
    
        dcol.append([h,m])
        #print(ind,data1[i],dcol[i],h,m)
    #print(dcol)
    return dcol
    #print(ind,data1[i],h,m)

#creating components
c1 = dcol9_0
def comp2(col1,col2):
    dcol1=[]
    dcol2=[]
    for i in range(len(df)):
        if col1[i] <= 15:
            dcol1.append(0)
        elif col1[i] > 15 and col1[i]<=30:
            dcol1.append(1)
        elif col1[i] > 30 and col1[i]<=60:
            dcol1.append(2)
        else:
            dcol1.append(3)
        
        dcol2.append(dcol1[i]+col2[i])
        #print(col1[i],col2[i],dcol1[i],dcol2[i],end=' ')
        if dcol2[i] == 0:
            dcol2[i] = 0
        elif dcol2[i] == 1 or dcol2[i] == 2:
            dcol2[i] = 1
        elif dcol2[i] == 3 or dcol2[i] == 4:
            dcol2[i] = 2
        else:
            dcol2[i] = 3
        #print(dcol2[i],type(dcol2[i]))
    return dcol2

def comp3(col):
    dcol=[]
    for i in range(len(df)):
        if col[i] > 7:
            dcol.append(0)
        elif col[i] > 6 and col[i] <=7:
            dcol.append(1)
        elif col[i] > 5 and col[i] <=6:
            dcol.append(2)
        else:
            dcol.append(3)
        #print(col[i],dcol[i])
    return(dcol)
def comp4(col1,col2,col3):
    dcol1 = get_hour_min_sleep_time(col1)
    dcol2 = get_hour_min_awake_time(col2)
    dcol3 = []
    for i in range(len(df)):
        if dcol2[i][0] < dcol1[i][0]:
            h = dcol2[i][0] + (24 - dcol1[i][0])
        else:
            h = dcol2[i][0] - dcol1[i][0]
        m = round((dcol2[i][1] - dcol1[i][1])/60 ,2)
        t = h+m
        #h_bed.append(t)
        sleep_eff = col3[i]/t
        if sleep_eff >= 0.85:
            dcol3.append(0)
        elif sleep_eff >= 0.75 and sleep_eff < 0.85:
            dcol3.append(1)
        elif sleep_eff >= 0.65 and sleep_eff < 0.75:
            dcol3.append(2)
        else:
            dcol3.append(3)
    return dcol3
        #print(dcol1[i],dcol2[i],col3[i],t,sleep_eff,dcol3[i])
    #for i in range(len(df)):
        #print(dcol1[i],dcol2[i],h_bed[i],)

def comp5(col1, col2, col3, col4, col5, col6, col7, col8):
    dcol = []
    for i in range(len(df)):
        summ = col1[i] + col2[i] + col3[i] + col4[i] + col5[i] + col6[i] + col7[i] + col8[i]
        if summ == 0:
            dcol.append(0)
        elif summ > 0 and summ <= 8:
            dcol.append(1)
        elif summ > 8 and summ <= 16:
            dcol.append(2)
        else:
            dcol.append(3)
        #print(i,summ,dcol[i])
    return dcol

c6 = dcol6_0

def comp7(col1, col2):
    dcol = []
    for i in range(len(df)):
        summ = col1[i] + col2[i]
        if summ == 0:
            dcol.append(0)
        elif summ > 0 and summ <= 2:
            dcol.append(1)
        elif summ > 2 and summ <= 4:
            dcol.append(2)
        else:
            dcol.append(3)
        #print(i,summ,dcol[i])
    return dcol

def gpsqi_col(fin_comps):
    l=[]
    for i in range(len(df)):
        l.append(fin_comp[0][i]+fin_comp[1][i]+fin_comp[2][i]+fin_comp[3][i]+fin_comp[4][i]+fin_comp[5][i]+fin_comp[6][i])
    return l

def my_score_col(gpsqi):
    l=[]
    for sc in gpsqi:
        if sc<=5:
            l.append(1)
        elif sc>5 and sc<=10:
            l.append(2)
        elif sc>10 and sc<=15:
            l.append(3)
        else:
            l.append(4)
    return l

fin_comp = []
fin_comp.append(dcol9_0)
fin_comp.append(comp2(dcol2_0,dcol5_1))
fin_comp.append(comp3(dcol4_0))
fin_comp.append(comp4(dcol1_0,dcol3_0,dcol4_0))
fin_comp.append(comp5(dcol5_2, dcol5_3, dcol5_4, dcol5_5, dcol5_6, dcol5_7, dcol5_8, dcol5_9))
fin_comp.append(dcol6_0)
fin_comp.append(comp7(dcol7_0,dcol8_0))
fin_comp.append(gpsqi_col(fin_comp))
#l=gpsqi_col(fin_comp)
fin_comp.append(my_score_col(fin_comp[7]))
#fin_comp.insert(0,my_score_col(l))

fin_df = pd.DataFrame(fin_comp)
fin_df = fin_df.transpose()
fin_df.columns = ['C1','C2','C3','C4','C5','C6','C7','C8','C9']
#fin_df.columns = ['C1','C2','C3','C4','C5','C6','C7','C8']
#print(dcol6_0)
print(fin_df.loc[0:,])
#comps = fin_df.to_excel (r'/home/arijit/sleepify', index = None, header=True)
outputFile = "comps.xlsx"
#fin_df.to_excel(outputFile, index=None, header=True)
fin_df.to_csv("comps.csv", index=None, header=False)


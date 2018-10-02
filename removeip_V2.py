
# coding: utf-8

# In[1]:


import pandas as pd
from cyberpandas import IPArray
from cyberpandas import ip_range
#import pandas_ip as ip


# In[6]:


#initial parameters 
FilePath='./M3 raw-data/Q3/CHT/M3_part15/2/CSV/en/vulnerabilities.csv'
FilePathCt='./M3 raw-data/Q3/CHT/M3_part15/2/CSV/ct/vulnerabilities.csv'
startIP='10.0.14.1'
endIP='10.0.14.255'

#print(FilePath,'\n',FilePathCt)
df = pd.read_csv(FilePath)
dfCt=pd.read_csv(FilePathCt)
print('The dataframe shape(En,Ct) are',df.shape,dfCt.shape)
#print(df.size)
print('=========================')
print('The first 5 En\'s data are\n',df.head())
print('=========================')
print('The first 5 Ct\'s data are\n',dfCt.head())


# In[15]:


def RemoveIP(raw_df,IP_columns_position,StartIP,EndIP):
    #convert data type  from object to ip arrary 
    ColumnsNameOfIP=raw_df.columns[IP_columns_position]
    #print(ColumnsNameOfIP)
    raw_df[ColumnsNameOfIP]=IPArray(raw_df[ColumnsNameOfIP])
    ipar=raw_df[ColumnsNameOfIP]
    removeIParray=[]
    i=0
    #remove En part IP
    for ip in ipar:
        if ip not in ip_range(StartIP,EndIP):
            removeIParray.append(i)
            print('drop num of index=',i,',IP =',ip)
        i=i+1
    #print(removeIParray)   
    new_df=raw_df.drop(removeIParray)
    return new_df


# main function
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Remove IP or IP range you want.')
    parser.add_argument("-s", "--start-ip", metavar="", help="remove form IP", default="127.0.0.1")
    parser.add_argument("-e", "--end-ip", metavar="", help="remove  IP", default="127.0.0.1")
    parser.add_argument("-f", "--file-read", metavar="", help="remove form IP", default="127.0.0.1")
new_df=RemoveIP(df,0,start_ip,end_ip)
new_dfCt=RemoveIP(dfCt,0,startIP,endIP)
print('before and after rows(en)=',df.shape[0],new_df.shape[0])
print('before and after rows(ct)=',dfCt.shape[0],new_dfCt.shape[0])

#export to file
new_df.to_csv('vulnerabilities_en.csv', index = False)
new_dfCt.to_csv('vulnerabilities_ct.csv', index = False)


#df.to_csv('/AfterRemoveIP/Q3/CHT/M3_part15/2/CSV/en/vulnerabilities.csv', index = False)



# coding: utf-8

# In[1]:

import argparse
import pandas as pd
from cyberpandas import IPArray
from cyberpandas import ip_range
#import pandas_ip as ip


# In[6]:

'''
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
'''

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
    print('''

        | |  | \ | |     | | | | | \ / |  | \ | |   | | | |        | |  | |  | \ 
        | |__| | | |---- | | | | | | | |  | | \ \   / / | |----    | |  | |__|_/ 
        |_|  \_\ |_|____ |_| |_| |_| \_|__|_/  \_\_/_/  |_|____   _|_|_ |_|      

        Author:Dio

        example: (If you only need to keep 10.1.1.0/24,and column 0 is IP's filed)

        python removeip_V2.py -s 10.1.1.1 -e 10.1.1.255 -f 0 -r './M3 raw-data/Q3/CHT/M3_part15/2/CSV/en/vulnerabilities.csv' -w 'vulnerabilities_en.csv'
        ''')
    parser = argparse.ArgumentParser(description='leave IP or IP range you want to keep.')
    parser.add_argument("-s", "--start-ip", metavar="", help="start form IP", default="127.0.0.1")
    parser.add_argument("-e", "--end-ip", metavar="", help="end of IP", default="127.0.0.1")
    parser.add_argument("-f", "--specific-field", metavar="", help="which field include IP",type=int, default="0")
    parser.add_argument("-r", "--file-read", metavar="", help="the file you want to remove/keep certain IP", default="")
    parser.add_argument("-w", "--file-write", metavar="", help="save path", default="")
    args = parser.parse_args()

    df = pd.read_csv(args.file_read)
    #print(df.tail())
    new_df=RemoveIP(df,args.specific_field,args.start_ip,args.end_ip)
    print('before rows=',df.shape[0],'\nafter rows=',new_df.shape[0])

#export to file
    new_df.to_csv(args.file_write, index = False)
    print('success!!')


#df.to_csv('/AfterRemoveIP/Q3/CHT/M3_part15/2/CSV/en/vulnerabilities.csv', index = False)


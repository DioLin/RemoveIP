
# coding: utf-8

import argparse
import pandas as pd
from cyberpandas import IPArray,ip_range


def RemoveIP(raw_df,IP_columns_position,StartIP,EndIP,IParr):
    #convert data type  from object to ip arrary 
    ColumnsNameOfIP=raw_df.columns[IP_columns_position]
    iplist=IPArray(IParr)
    #print(ColumnsNameOfIP)
    raw_df[ColumnsNameOfIP]=IPArray(raw_df[ColumnsNameOfIP])
    ipar=raw_df[ColumnsNameOfIP]
    removeIParray=[]
    i=0
    #remove En part IP
    for ip in ipar:
        if ip not in ip_range(StartIP,EndIP) and ip not in iplist:
            removeIParray.append(i)
            print('drop num of index=',i,',IP =',ip)
        i=i+1
    #print(removeIParray)   
    new_df=raw_df.drop(removeIParray)
    return new_df


# main function
if __name__ == '__main__':
    print('''

         ______   ______  _________   ______   _     _   ______   _____  ______  
        | |  | \ | |     | | | | | \ / |  | \ | |   | | | |        | |  | |  | \ 
        | |__| | | |---- | | | | | | | |  | | \ \   / / | |----    | |  | |__|_/ 
        |_|  \_\ |_|____ |_| |_| |_| \_|__|_/  \_\_/_/  |_|____   _|_|_ |_|      
                                                                         

        Author:Dio 
        Version:0.3
        example: (If you only need to keep 10.1.1.0/24,and column 0 is IP's filed)

        python removeip_V2.py -s 10.1.1.1 -e 10.1.1.255 -f 0 -r 'vulnerabilities.csv' -w 'vulnerabilities_en.csv'
        or 
        python removeip_V2.py -i 'keepIPlist.csv' -f 0 -r 'vulnerabilities.csv' -w 'vulnerabilities_en.csv'
        ''')
    parser = argparse.ArgumentParser(description='leave IP or IP range you want to keep.')
    parser.add_argument("-s", "--start-ip", metavar="", help="start form IP", default="0.0.0.0")
    parser.add_argument("-e", "--end-ip", metavar="", help="end of IP", default="0.0.0.0")
    parser.add_argument("-i", "--ip-list", metavar="", help="read IP list in csv", default="")
    parser.add_argument("-f", "--specific-field", metavar="", help="which field include IP address,default vaule is columns 0'th",type=int, default="0")
    parser.add_argument("-r", "--file-read", metavar="", help="the file you want to remove/keep certain IP", default="")
    parser.add_argument("-w", "--file-write", metavar="", help="save path", default="")
    args = parser.parse_args()

#read raw csv data
    df = pd.read_csv(args.file_read)
#read iplist file
    if args.ip_list:
        df_iplist=pd.read_csv(args.ip_list)
    else:
        df_iplist=[]
    new_df=RemoveIP(df,args.specific_field,args.start_ip,args.end_ip,df_iplist)
    print('before rows=',df.shape[0],'\nafter rows=',new_df.shape[0])

#export to file
    new_df.to_csv(args.file_write, index = False)
    print('success!!')



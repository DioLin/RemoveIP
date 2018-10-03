# RemoveIP
For CSV file
只保留csv檔某段IP，移除其他列
'''

        | |  | \ | |     | | | | | \ / |  | \ | |   | | | |        | |  | |  | \ 
        | |__| | | |---- | | | | | | | |  | | \ \   / / | |----    | |  | |__|_/ 
        |_|  \_\ |_|____ |_| |_| |_| \_|__|_/  \_\_/_/  |_|____   _|_|_ |_|      

        Author:Dio

        example: (If you only need to keep 10.1.1.0/24,and column 0 is IP's filed)

        python removeip_V2.py -s 10.1.1.1 -e 10.1.1.255 -f 0 -r './M3 raw-data/Q3/CHT/M3_part15/2/CSV/en/vulnerabilities.csv' -w 'vulnerabilities_en.csv'
        '''


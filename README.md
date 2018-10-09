# RemoveIP
For CSV file
只保留csv檔某段IP，移除其他列


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
        
        usage: removeip_V3.py [-h] [-s] [-e] [-i] [-f] [-r] [-w]

        leave IP or IP range you want to keep.

        optional arguments:
          -h, --help            show this help message and exit
          -s , --start-ip       start form IP
          -e , --end-ip         end of IP
          -i , --ip-list        read IP list in csv
          -f , --specific-field 
                                which field include IP address,default vaule is
                                columns 0'th
          -r , --file-read      the file you want to remove/keep certain IP
          -w , --file-write     save path
        


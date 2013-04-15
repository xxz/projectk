'''
Created on Apr 1, 2013

@author: talos
'''

from config import PKConfig


if __name__ == '__main__':

    configure_file = PKConfig('D:\workspace\projectk\config.xml')
    parameter = configure_file.PK_parse_config()
    
    #define source file and destination file
    data_file = open(parameter['SOURCE_PATH'])
    output_file = open(parameter['DESTINATION_PATH'], "w")

    #initial the var
    data_content = list()
    rows = ''

    #load file to memory
    while 1 :
        temp_content = data_file.readlines(10000)        
        if not temp_content :
            break  
        data_content = data_content + temp_content
        
    #for the data
    for line in data_content:        
        rows += line.strip().replace('\n', '').strip().replace('CREATE ', '\n CREATE ')
    data = rows.splitlines()
    data.pop()

    output_file.writelines(data)
    

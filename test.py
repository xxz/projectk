'''
Created on Apr 1, 2013

@author: talos
'''

from data import k_data

if __name__ == '__main__':
    
    output_file = open("output", "w")

    
    test  = k_data
    data_content = list()
    lines = ''
    line=''
    
    data_file = open('/home/talos/workspace/data')
    while 1 :
        temp_content = data_file.readlines(10000)        
        
        if not temp_content :
            break
        
        data_content = data_content + temp_content
     
    print data_content[5]
        
    #for line in data_content:
     #   line.strip().replace('\n', '').strip()#.replace('CREATE ', '\n CREATE ')
      #  lines += line
        
    #lines.replace('\n', '')
    
    #print lines    
    
    #datas  = list(lines)
    #datas = lines.rstrip().split('\n')
    #datas = lines.partition('CREATE')
    #datas = lines.split('CREATE')
    #datas = lines.splitlines()
    
    #print lines
    #print len(datas)
    #print datas
    
    #output_file.writelines(lines)
    
    print 'done'

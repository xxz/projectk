'''
Created on 2013-4-14

@author: Talos
'''

try:
    from lxml import etree
except ImportError:
    print 'error in import etree'

class PKConfig():
    '''
    classdocs
    '''
    PK_config_path = 'config.xml'
    PK_parameter = {}

    def __init__(self, PK_config_path):
        '''
        Constructor
        '''
        self.PK_config_path = PK_config_path
        
    def PK_parse_config(self):
        tree  =  etree.parse(self.PK_config_path)
        root = tree.getroot()
        for child in root:
            self.PK_parameter[child.tag] = child.text
        return self.PK_parameter
    
    def PK_showinfo(self):
        print self.PK_config_path
        for key in self.PK_parameter:
            print 'key=%s, value=%s' % (key, self.PK_parameter[key])

#===============================================================================
# if __name__ == '__main__':
#     config = PKConfig('config.xml')
#     config.PK_parse_config()
#     config.PK_showinfo()
#===============================================================================

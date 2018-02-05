# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 04:40:42 2018

@author: Tijs
"""

import datetime
                
class LogbookLine:
    """
    A logbook line
    """
    
    def __init__(self,entry,timestamp=None):
        
#        assert type(entry)==str,  "'entry' should be a string"
        
        if timestamp is None:
            timestamp = datetime.datetime.now()
        else:
            assert type(timestamp)==datetime.datetime,  "'timestamp' should be a datetime.datetime"

        self.entry = entry
        self.timestamp = timestamp
        
    def __str__(self):
        
        object_string = ''
        object_string += '('+self.timestamp.strftime('%Y-%m-%d %H:%M:%S')+') '
        object_string += self.entry
        
        return object_string
    
class Logbook:
    """
    A logbook
    """
    
    def __init__(self,first_entry=None,first_timestamp=None):
        
        if first_entry is None:
            self.lines = []
        else:
            self.lines = [LogbookLine(first_entry,first_timestamp)]
            
    def __str__(self):
        
        object_string = ''
        for line in self.lines:
            object_string += str(line)+'\n'
            
        return object_string
        
    def __len__(self):
        
        return len(self.lines)
            
    def append(self,entry,timestamp=None):
                
        self.lines.append(LogbookLine(entry,timestamp))
        
#%% Test code
        
if __name__=='__main__':
    
    logline = LogbookLine('entry',datetime.datetime.now())
    print(logline)
    
    logbook = Logbook()
    print(logbook)
    logbook.append('first entry')
    print(logbook)
    logbook.append('second entry',datetime.datetime(2018,1,1,12,25,33))
    print(logbook)
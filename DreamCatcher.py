# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 04:40:42 2018

@author: Tijs
"""

from Logbook import Logbook
                
class Dream:
    """
    <Dream> objects are the elemental objects that the DreamCatcher is catching.
    """
    
    def __init__(self,dreamweb,ID=0,content='',parent=None):
                        
        self._dreamweb = dreamweb    
        self._ID = ID
        self._content = content
        self._parent = parent
        self._children = []
        self._links = []
        if isinstance(parent,int):
            self._logbook = Logbook('<Dream> ID='+str(self.ID)
                                +' (parent='+str(self.parent)+') created')
        else:
            self._logbook = Logbook('<Dream> ID='+str(self.ID)+' created')
        
    def __str__(self):
        
        object_string = ''
        object_string += 'DreamWeb: '+self.dreamweb.name+'\n'
        object_string += 'ID: '+str(self.ID)+'\n'
        object_string += 'Content: '+self.content+'\n'
        object_string += 'Parent: '+str(self.parent)+'\n'
        object_string += 'Children: '+str(self.children)+'\n'
        object_string += 'Links: '+str(self.links)+'\n'
        object_string += 'No. of logbook lines: '+str(len(self.logbook))+'\n'
        
        return object_string
        
    def create_child(self,content=''):
        """
        Create a child <Dream> object.
        """    
        self.dreamweb.add(content,parent=self.ID)
        
    def create_sibling(self,content=''):
        """
        Create a sibling <Dream> object (same parent).
        """     
        self.dreamweb.add(content,parent=self.parent)
        
    def detach(self,other):
        """
        Detach <Dream> from a parent or child <Dream>.
        """
        pass
        
    def link_to(self,other):
        """
        Link to another <Dream> object.
        """
        self.dreamweb.link(self.ID,other)
        
    def unlink(self,other):
        """
        Remove link to another <Dream> object.
        """   
        self.dreamweb.unlink(self.ID,other)
    
    @property
    def dreamweb(self):
        """
        Returns dreamweb to which <Dream> belongs.
        """
        return self._dreamweb
    
    @property    
    def ID(self):
        """
        Returns <Dream> ID.
        """        
        return self._ID
        
    @property    
    def content(self):
        """
        Returns <Dream> content.
        """
        return self._content
        
    @content.setter    
    def content(self,new_content):
        """
        Changes <Dream> content to new_content.
        """
        self._content = new_content
        
    @property    
    def parent(self):
        """
        Returns <Dream> parent.
        """
        return self._parent
        
    @property    
    def children(self):
        """
        Returns list of <Dream> children.
        """
        return self._children
        
    @property
    def links(self):
        """
        Returns list of <Dream> links.
        """
        return self._links
        
    @property
    def logbook(self):
        """
        Returns <Dream> logbook.
        """
        return self._logbook
        
class DreamWeb:
    """
    A <DreamWeb> object is a collection of <Dream>s.
    """
    
    def __init__(self,name='',description=''):
        
        self.name = name
        self.description = description
        self.dreams = []
        self.IDs = []
        self.logbook = Logbook('<DreamWeb> name=\''+self.name+'\' created')    
    
    def __str__(self):
        
        object_string = ''
        object_string += 'Name: '+self.name+'\n'
        object_string += 'Description: '+self.description+'\n'
        object_string += 'No. of dreams: '+str(self.count())+'\n'
        object_string += 'No. of logbook lines: '+str(len(self.logbook))+'\n'
        
        return object_string
    
    def add(self,content='',parent=None):
        """
        Adds a new <Dream> object to the <DreamWeb>.
        """
        
        new_ID = len(self.dreams)
        self.dreams.append(Dream(self,new_ID,content,parent))
        self.IDs.append(new_ID)
        
        if isinstance(parent,int):
            self.dreams[parent].children.append(new_ID)
            self.dreams[parent].logbook.append('<Dream> child='+str(new_ID)+' created')
            self.logbook.append('<Dream> ID='+str(new_ID)
                                +' (parent='+str(parent)+') added')
        else:
            self.logbook.append('<Dream> ID='+str(new_ID)+' added')
            
    def remove(self,ID):
        """
        Remove a <Dream> object from the <DreamWeb>.
        
        NOTE: the <Dream> is not really removes, but only its reference in the IDs list.
        """
        
        self.IDs.remove(ID)
        
        print('Warning: <Dream> removed, but <Logbook>s not updated!')
            
    def detach(self,parent,child):
        """
        Detach parent <Dream> from child <Dream>.
        """
        pass
    
            
    def link(self,ID1,ID2):
        """
        Links two <Dream> objects together.
        """
        
        link_already_exists = self.dreams[ID1].links.count(ID2) > 0
        
        if not link_already_exists:
            self.dreams[ID1].links.append(ID2)
            self.dreams[ID1].logbook.append('Link to <Dream> ID='+str(ID2)+' created')
            self.dreams[ID2].links.append(ID1)
            self.dreams[ID2].logbook.append('Link to <Dream> ID='+str(ID1)+' created')
            self.logbook.append('<Dream>s ID='+str(ID1)+' and ID='+str(ID2)+' linked')
            
    def unlink(self,ID1,ID2):
        """
        Remove link between two <Dream> objects.
        """
        pass
    
    def count(self):
        """
        Returns the number of <Dream> objects in the <DreamWeb>.
        """
        
        return len(self.IDs)
    
    def get_dreams(self):
        """
        Returns a list of all <Dream> objects in the <DreamWeb>.
        """
        
        return [self.dreams[ID] for ID in self.IDs]
    
    def get_links(self):
        """
        Returns a list of all links between <Dream> objects contained in the <DreamWeb>.
        """
        pass

#%% TEST code
    
if __name__=='__main__':
    
    dreamweb = DreamWeb('Everything?','Yes, everything!')
    print(dreamweb)
    print(dreamweb.logbook)    
    
    dreamweb.add('This is my first idea')
    print(dreamweb.dreams[0])
    print(dreamweb.dreams[0].logbook)
    
    dreamweb.add('This is my second idea')
    print(dreamweb.dreams[1])
    print(dreamweb.dreams[1].logbook)
    
    dreamweb.add('This is my third idea',1)
    print(dreamweb.dreams[1])
    print(dreamweb.dreams[1].logbook)
    print(dreamweb.dreams[2])
    print(dreamweb.dreams[2].logbook)
    print(dreamweb)
    print(dreamweb.logbook)
    
    dreamweb.dreams[2].create_child('This is my fourth idea')
    print(dreamweb.dreams[2])
    print(dreamweb.dreams[2].logbook)
    print(dreamweb.dreams[3])
    print(dreamweb.dreams[3].logbook)
    print(dreamweb)
    print(dreamweb.logbook)
    
    dreamweb.link(0,3)
    print(dreamweb.dreams[0])
    print(dreamweb.dreams[0].logbook)
    print(dreamweb.dreams[3])
    print(dreamweb.dreams[3].logbook)
    print(dreamweb)
    print(dreamweb.logbook)
    
    dreamweb.dreams[1].link_to(3)
    dreamweb.dreams[3].link_to(1)
    print(dreamweb.dreams[1])
    print(dreamweb.dreams[1].logbook)
    print(dreamweb.dreams[3])
    print(dreamweb.dreams[3].logbook)
    print(dreamweb)
    print(dreamweb.logbook)
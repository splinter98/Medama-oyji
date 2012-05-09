from defaultdict import DefaultDict
import os

class Config(DefaultDict):
   __slots__=[]
   def __init__(self, path=".animedb_config"):
      self['path'] = os.path.abspath(path)
      DefaultDict.__init__(self)
      self.load()

   def load(self):
      try:
         f=open(os.path.abspath(self['path']),'r')
         for line in f:
            line=line.strip()
            if line.startswith('#'):
               continue
            key,value=line.split('=',1)
            self[key]=value
         f.close()
      except IOError:
         self['error']=1
         self['errormsg']="Config File Does not Exist"

   def save(self):
      f=file(os.path.expanduser(self['path']),'w')
      for key in self:
         f.write(str(key)+'='+str(self[key])+'\n')
      f.close()

class DefaultConfig(Config):
   def load(self):
      print 'using Default Config'
      self['ScanFolder']='Unsorted'
      self['aPuser'] = '<Delete this and enter Username Here>'
      self['aPpassword'] = '<Delete this and enter password here>'
      self['aPdburl'] = 'sqlite://%s/anidb.sqlite?user=a&password=p'%os.path.dirname(self['path'])[0]
      self['aPsession'] = None
      self['aPdbfmask'] = '71F8C3E900'
      self['aPdbamask'] = 'B020C000'
      self['aPfolder'] = "Unsorted"

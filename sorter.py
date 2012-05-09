import os

from yapsy.PluginManager import PluginManager

from cparser import Parser
from config import Config, DefaultConfig

class MiscParser(Parser):
   def __init__(self):
      Parser.__init__(self)
      self.miscLoc = "Misc"
      self.moves = []

   def ScanFile(self, File):
      return {"Misc": File}

   def SortFile(self, Info, File):
      filename = os.path.basename(File)
      self.moves.append([File, os.path.abspath(os.path.join(self.miscLoc, filename))])
      return self.moves[-1][1]

   def commit(self):
      for old,new in self.moves:
         print "Moving %s to %s" % (old, new)
      self.moves = []

def main():
   configpath = ".animedb.config"
   config = Config(configpath)
   if config['error']:
      print "No Config file found - using default config"
      print "please edit %s to include your anidb username and pass" % config['path']
      config=DefaultConfig(configpath)
      config.save()
      raise IOError

   manager = PluginManager(categories_filter={"Parsers": Parser}, plugin_info_ext="parser")
   manager.setPluginPlaces(["plugins"])
   manager.collectPlugins()

   parsers = []
   for plugin in manager.getPluginsOfCategory("Parsers"):
    parsers.append(plugin.plugin_object)
   parsers.append(MiscParser())

   for parser in parsers:
      parser.setdb("db.sqlite", "sqlite")
      parser.setconfig(config)

   for root,dirs,files in os.walk(os.path.abspath(config['ScanFolder'])):
      for filename in files:
         name = os.path.join(root,filename)
         print "Parsing: %s" % name
         for parser in parsers:
            catalogue = []
            Info = parser.ScanFile(name)
            if Info:
               location = parser.SortFile(Info, name)
               catalogue.append((location, Info))
               if catalogue:
                  parser.Catalogue(catalogue)
               break
      for parser in parsers:
       parser.commit()

if __name__ == "__main__":
   main()

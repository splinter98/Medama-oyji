from yapsy.IPlugin import IPlugin


class Parser(IPlugin):
   def ScanFile(self, File):
      """Called to scan the file and return a dict if it matches (empty if not)"""
      return {}

   def SortFile(self, Info, File):
      """Called to place the file in a sensible place"""
      return File

   def Catalogue(self, catalogue):
      """take a dict of File and Infos and place the data in a db"""
      pass

   def commit(self):
      """do any post actions"""
      pass

   def setdb(self, db, dbtype):
      self.db = db
      self.dbtype = dbtype

   def setconfig(self, config):
      self.config = config
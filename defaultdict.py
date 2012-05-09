
class DefaultDict(dict):
	__slots__=['default']
	def __init__(self,default=None):
		super(DefaultDict,self).__init__()
		self.default=default
	
	def __getitem__(self,key):
		try:
			return dict.__getitem__(self,key)
		except:
			return self.default
	
	def get(self,key,*args):
		if not args:
			args=(self.default,)
		return dict.get(self,key,*args)

class ListDict(object):
	"""
	With ListDict integers are indexes and strings are keys.
	"""
	def __init__(self,values=None):
		self.order=[]
		self.values={}
		if not values:
			values=[]
		for key,name in values:
			self.append((key,name))
	
	def __len__(self):
		return len(self.order)
	
	def __repr__(self):
		return "ListDict(%s,%s)"%(repr(self.order),repr(self.values))
		#return '{%s}'%(', '.join(['%s: %s'%(repr(key),repr(value)) for key,value in self.iteritems()]))
	
	def append(self,item):
		key,value=item
		if not isinstance(key,basestring):
			raise TypeError,"ListDict keys must be strings"
		if key not in self.order:
			self.order.append(key)
		self.values[key]=value
	
	def __getitem__(self,index):
		if isinstance(index,int):
			return self.order[index]
		elif isinstance(index,basestring):
			return self.values[index]
		else:
			raise TypeError,"ListDict indices must be either integers or strings"
	
	def __setitem__(self,key,value):
		if isinstance(key,int):
			key=self.order[key]
			self.values[key]=value
		elif isinstance(key,basestring):
			self.append((key,value))
		else:
			raise TypeError,"ListDict indices must be either integers or strings"
	
	def __delitem__(self,key):
		self.remove(key)
	
	def index(self,item):
		return self.order.index(item)
	
	def remove(self,key):
		if isinstance(key,int):
			index=key
			key=self.order[index]
		elif isinstance(index,basestring):
			index=self.order.index(key)
		else:
			raise TypeError,"ListDict indices must be either integers or strings"
		del self.order[index]
		del self.values[key]
	
	def iteritems(self):
		for key in self.order:
			yield (key,self.values[key])
	
	def items(self):
		return [(key,self.values[key]) for key in self.order]
	
	def iterkeys(self):
		for key in self.order:
			yield key
	
	def keys(self):
		return self.order[:]
	
	def itervalues(self):
		for key in self.order:
			yield self.values[key]
	
	def values(self):
		return [self.values[key] for key in self.order]


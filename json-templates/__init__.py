import json
import re
import sys

class JsonTemplater:


#-----------------------------------------------------------------------
 def __init__(self): 
  self.isdone = False
  self.template = None
  self.var_regex = re.compile("\{\{\ [a-zA-Z0-9_]+\ \}\}")
  self.arr_regex = re.compile("\{\%\ [a-zA-Z0-9_]+\ \%\}")

#-----------------------------------------------------------------------
 def is_iterable(obj):
  try:
   iter(obj)
   return True
  except:
   return False
   
#-----------------------------------------------------------------------
 def loads(self,json_str):
  try:
   self.template = json.loads(json_str)
  except Exception as ex:
   return (False, "Unable to parse json! {}".format(ex))
  
  return (True,self.template)

#-----------------------------------------------------------------------
 def load(self,path):
  if sys.path.isfile(path) and path.lower().endswith("json"):
   try:
    self.template = json.load(path)
   except Exception as ex:
    return (False, "Unable to parse json! {}".format(ex))
  else:
   return (False, "{} is not JSON file")
  
  return (True,self.template)
  
#-----------------------------------------------------------------------
 def generate(self,keyvalue):
  targetNodes = self.template
  
  #for k,v in targetNodes.items():
  # if is_iterable(v):
  return (False, "WIP")
    
    

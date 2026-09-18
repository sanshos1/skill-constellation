import os
_u=os.unlink
def safe(path,*a,**k):
 try:return _u(path,*a,**k)
 except PermissionError:return None
os.unlink=safe;CONTRACT=os.path.join('contracts','contract.py')

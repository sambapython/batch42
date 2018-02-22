#fun()
'''
import f1

fun()
'''
#import f5
'''
import sys
print sys.path
import f1
f1.fun()
'''
'''
import f1
f1.fun()
import sys
print sys.path
import f2
f2.fun()
'''
'''
import sys
pypath = sys.path.pop(2)
sys.path.insert(0,pypath)
print sys.path
import f2
f2.fun()
'''
'''
import sys
print sys.path
import f2
'''
'''
import sys
sys.path.append("/home/khyaathi-python/")
import f2
f2.fun()
'''
'''
import f2
f2.fun()
'''
#from f2 import fun
'''
import f2
f2.fun()
f2.fun1()
'''
#import module1
#import f2
'''
import module1
module1.file2.fujn()
'''
'''
import module1
module1.file1.fun()
module1.file2.fun()
'''
#import module1
from module1 import file1
file1.fun()
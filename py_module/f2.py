
print "name attribute value:",__name__
def fun():
	print "this is fun in f2 in current working directory"


if __name__ == "__main__":
	def fun1():
		print "this is fun1 in f2"
	fun1()
	print "name attribute",__name__
	print "this is f2 operations"
	fun()
	print "other statements in f2"
	print "program ended for f2"

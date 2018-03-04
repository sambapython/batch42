import logging
#logging.error("info before config")
logging.basicConfig(level=logging.DEBUG, 
    filename="log.txt",
    format="%(asctime)s=>%(levelname)s==>%(message)s")
print "program started"
logging.info("program started")
a=raw_input("Enter a number:")
logging.info("a value taken")
b=raw_input("Enter b number:")
logging.info("b value entered")
print "a=%s, b=%s"%(a,b)
logging.debug("a=%s, b=%s"%(a,b))
try:
    a=float(a)
    logging.info("a converted well")
    b=float(b)
    logging.info("b converted well")
    print "after conversion a=%s, b=%s"%(a,b)
    logging.debug("after conversion a=%s, b=%s"%(a,b))
    res=a/b
    print "res=",res
    logging.debug("res=%s"%res)
except ZeroDivisionError as err:
    print err
    print "b value should not zero."
    logging.error("b value should not zero.")
except ValueError as err:
    print err
    print "expecting only digits got alphabets"
    logging.error("expecting only digits got alphabets")
except Exception as err:
    print "some issue"
    print "ERROR:",err
    logging.error(err)
print "other statements in program"
print "program ended"
logging.info("progrm ended")
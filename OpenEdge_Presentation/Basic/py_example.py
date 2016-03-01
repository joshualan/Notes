# Python Equivalent for OpenEdge query:
# for each Customer where
#   SalesRep = pInput:
#   if Balance > CreditLimit then
#   Balance = Balance + 0.05.
# end.

import config 
import MySQLdb as mdb

salesrep = raw_input("Enter the Sales Representative's Employee Number: ")

# This is the part that's probably where the equivalency starts
# Transactional scoping
try:
    db = mdb.connect('localhost', 'root', config.password, 'classicmodels')
    cur = db.cursor()
    cur.execute("UPDATE customers \
                 SET BALANCE = BALANCE + 0.05 \
                 WHERE SALESREPEMPLOYEENUMBER = %s AND BALANCE > CREDITLIMIT",
                (salesrep,))
    
    db.commit()
    print "{} rows updated".format(cur.rowcount)
except:
    db.rollback()
    print "Query failed"
finally:
    if cur:
        cur.close()
    if db:
        db.close()


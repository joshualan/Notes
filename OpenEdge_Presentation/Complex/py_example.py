import config 
import MySQLdb as mdb

try:
    db = mdb.connect('localhost', 'root', config.password, 'classicmodels')
    cur = db.cursor()

    # Join on 4 tables
    # We do an outer join the Employees, Customers, Orders, and OrderDetails tables
    # And then sort out all the orders where we are processing orders and the order
    # contains a specific product
    cur.execute('select \
                 employees.lastName, employees.firstName, customers.customerName, \
                 orders.orderNumber, orderdetails.priceEach \
                 from employees join customers on customers.salesRepEmployeeNumber = employees.employeeNumber \
                                join orders on orders.customerNumber = customers.customerNumber \
                                join orderdetails on orderdetails.orderNumber = orders.orderNumber \
                                where orders.status = "In Process" and orderdetails.productCode = "S24_2300";')
    
    print "{} rows found".format(cur.rowcount)
except:
    print "Query failed"
finally:
    if cur:
        cur.close()
    if db:
        db.close()

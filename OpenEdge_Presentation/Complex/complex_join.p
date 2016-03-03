DEF VAR dt1 AS DATE INITIAL 09/19/1999.

FOR EACH salesrep,
    EACH customer OF salesrep,
    // An alternate version of this statement is:
    // EACH customer WHERE cust.salesrep = salesrep.salesrep,
        EACH order OF customer WHERE Order.OrderStatus = "Ordered" OR
        (Order.OrderStatus = "Shipped" AND INTERVAL(order.shipdate, dt1, "months") <= 1),
            EACH orderline OF order WHERE orderline.itemnum = 14:
                // You can access any field from the joined record.
                DISPLAY 
                    SalesRep.Repname FORMAT "x(10)"
                    Customer.NAME
                    order.ordernum 
                    orderline.price.
END.

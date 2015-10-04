hrs = raw_input("Enter Hours:")
h = float(hrs)
rate=10.50
if hrs < 40:
    pay=hours*rate
    print "the pay is:", pay
else:
    pay = 40 * rate + (h-40)*1.5*rate
    print "the pay is:", pay

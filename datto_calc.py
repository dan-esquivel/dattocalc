#user entry

winservers = 0
winservers = float(input("Enter the quantity of general Windows Servers: "))
linux = 0
linux = float(input("Enter the quantity of Linux servers: "))
sql = 0
sql = float(input("Enter the quantity of SQL servers: "))
exchange = 0
exchange = float(input("Enter the quantity Exchange servers: "))
data = 0
data = float(input("Enter the amount of data being protected in GB: "))
billrate = 165
billrate = float(input("Enter the billing rate: "))

#base PM cost
basepm = 3

#base project cost
baseproj = 18
monbase = 0

#base winserver - normal hours
winnextday = winservers

#base winserver - after hours
wincutover = winservers * 1.5

#add linux servers
linuxnextday = linux
linuxcutover = linux * 1.5
linuxprem = linux * 0.5

#add sql servers
sqlnextday = sql
sqlcutover = sql * 1.5
sqlprem = sql * 0.5

#add exchange servers
exchangenextday = exchange
exchangecutover = exchange * 1.5
exchangeprem = exchange * 0.5

#data size variable costs
if (data <= 500):
	monbase = 8

elif (data > 500 and data <= 1000):
	monbase = 10

elif (data > 1000 and data <= 2000):
	monbase = 12

elif (data > 2000 and data <= 3000):
	monbase = 15

#restricted values
if (winservers > 30):
	print("This opportunity cannot be used with this calculator.  Please submit a custom peer review.")
if (linux > 5):
	print("This opportunity cannot be used with this calculator.  Please submit a custom peer review.")
if (sql > 4):
	print("This opportunity cannot be used with this calculator.  Please submit a custom peer review.")
if (exchange > 4):
	print("This opportunity cannot be used with this calculator.  Please submit a custom peer review.")
if (data > 3000):
	print("This opportunity cannot be used with this calculator.  Please submit a custom peer review.")

#output
normalhours = (basepm + baseproj + monbase + winnextday + linuxnextday + linuxprem + sqlnextday + sqlprem + exchangenextday + exchangeprem)
afterhours = (exchangecutover + wincutover + linuxcutover + sqlcutover)
initcost = (normalhours * billrate) + (afterhours * billrate)
riskprem = 0
totalcost = 0
if (linux < 1 and sql < 1 and exchange < 1):
	riskprem = 0.05
	totalcost = initcost + (initcost * riskprem)
elif (linux >= 1):
	riskprem = 0.10
	totalcost = initcost + (initcost * riskprem)
elif (sql >= 1):
	riskprem = 0.10
	totalcost = initcost + (initcost * riskprem)
elif (exchange >= 1):
	riskprem = 0.10
	totalcost = initcost + (initcost * riskprem)
elif (linux >= 1 and exchange >= 1 or sql >= 1):
	riskprem = 0.15
	totalcost = initcost + (initcost * riskprem)
elif (exchange >= 1 and linux >= 1 or sql >= 1):
	riskprem = 0.15
	totalcost = initcost + (initcost * riskprem)
elif (sql >= 1 and exchange >= 1 or linux >= 1):
	riskprem = 0.15
	totalcost = initcost + (initcost * riskprem)
elif (linux >= 1 and exchange >= 1 and sql >= 1):
	riskprem = 0.20
	totalcost = initcost + (initcost * riskprem)

print("Total cost is $", "%.2f" % totalcost)
print("Total hours are #", "%.2f" % (totalcost / billrate) )


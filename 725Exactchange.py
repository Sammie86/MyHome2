#User input
amount=int(input())

#calculate change
dlr=int(amount/100)
amount=amount%100
qtr=int(amount/25)
amount=amount%25
dme=int(amount/10)
amount=amount%10
nkl=int(amount/5)
amount=amount%5
pny=int(amount)

#Print the results
if dlr==1:
   print("1 Dollar")
if dlr>1:
   print(dlr,"Dollars")
if qtr==1:
   print("1 Quarter")
if qtr>1:
   print(qtr,"Quarters")
if dme==1:
   print("1 Dime")
if dme>1:
   print(dme,"Dimes")
if nkl==1:
   print("1 Nickel")
if nkl>1:
   print(nkl,"Nickels")
if pny==1:
   print("1 Penny")
if pny>1:
   print(pny,"Pennies")
if dlr<1 and qtr<1 and dme<1 and nkl<1 and pny<1:
   print("No change")
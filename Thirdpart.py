# Part b
def find(in_date):
   #Dictionary to convert months into integers
   mon_to_num = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
              "August":8,"September":9,"October":10,"Novenber":11,"December":12}
   try:
      yy = in_date.split(",")[-1].strip() #Split by "," and take last part as the year
      month = in_date.split(",")[0].split()[0] #Split by ',' and then by the blank space for month
      dd = in_date.split(",")[0].split()[-1] #Split by ',' and then by the blank space for day
      mm = mon_to_num[month] #Convert month to integer
      int(yy)
      int(dd)
      return str(mm)+"/"+dd+"/"+yy #Return result
   except:
      return ""

with open("inputDates.txt") as f: #Read file
   for x in f.readlines():  #loop line by line
      if x.strip() != "-1": #Check if -1 is entered
         print(find(x.strip())) #print result
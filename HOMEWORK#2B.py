#Second part of my coding
def find(in_date):

   #Use dictionary to change months to integers
   mon_to_num = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
              "August":8,"September":9,"October":10,"Novenber":11,"December":12}

   try:
        yy = in_date.split(",")[-1].strip() #Please split by "," and  also take last part as the year
        month = in_date.split(",")[0].split()[0] #Please split by ',' and also by the blank space for month
        dd = in_date.split(",")[0].split()[-1] #Please split by ',' and also by the blank space for day
        mm = mon_to_num[month] #Change month to integer
        return str(mm)+"/"+dd+"/"+yy #Pease return result
   except:
       with open("inputDates.txt") as f: #Please read file
    for x in f.readlines(): #Please loop line by line
        if x.strip()!="-1": #Please check if -1 is entered

            print(find(x.strip())) #please print result
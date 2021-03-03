#First part of my coding
def find(in_date):

   #Use dictionary to change months to integers
   mon_to_num = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
              "August":8,"September":9,"October":10,"Novenber":11,"December":12}


   yy = in_date.split(",")[-1].strip() #Please split by "," and  also take last part as the year
   month = in_date.split(",")[0].split()[0] #Please split by ',' and also by the blank space for month
   dd = in_date.split(",")[0].split()[-1] #Please split by ',' and also by the blank space for day
   mm = mon_to_num[month] #Change month to integer
   return str(mm)+"/"+dd+"/"+yy #Pease return result

while True: #infinite loop
   inp= input() #Please take input from user
   if inp == "-1": #Please Check if input is -1
      break #Please breaks out of the loop


   print(find(inp)) #Function call
import csv

mycsv = csv.reader(open('./jester-data-2.csv'))
writer=csv.writer(open('./ratings.csv','wb'))
writer.writerow(['UserID','MovieID','Rating'])
for row in mycsv:
    user=row[0]
    count=1
    for rating in row[1:]:
        list=[]
        list.append(user)#userID
        list.append(count)#movieID
        list.append(rating)
        writer.writerow(list)
        count+=1
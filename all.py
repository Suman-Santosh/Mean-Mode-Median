import csv
from collections import Counter
with open("HeightWeight.csv", newline='')as f:
    csvReader=csv.reader(f)
    fileData=list(csvReader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))
n=len(newData)
total=0
for x in newData:
    total+=x
mean=total/n
print (mean)
newData.sort()
if n%2==0:
    median1=float(newData[n//2])
    median2=float(newData[n//2-1])
    median=(median1+median2)/2
else:
    median=newData[n//2]
print (median)
n=len(newData)
data=Counter(newData)
modForRange={
 "50-60":0, 
 "60-70":0, 
 "70-80":0
}
for Height, Occurence in data.items():
    if 50<float(Height)<60:
        modForRange["50-60"]+=Occurence
    elif 60<float(Height)<70:
        modForRange["60-70"]+=Occurence
    elif 70<float(Height)<80:
        modForRange["70-80"]+=Occurence
modRange, modOccurence= 0, 0
for range, Occurence in modForRange.items():
    if Occurence>modOccurence:
        modRange, modOccurence=[int(range.split("-")[0]), int(range.split("-")[1])], Occurence
mod=float((modRange[0]+modRange[1])/2)
print (mod)
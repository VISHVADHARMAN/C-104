import csv
with open('D:/C-104/height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
    file_data.pop(0)
    #Sorting data to get the height of people
    new_data=[]
    for i in range(len(file_data)):
        n_num=file_data[i][1]
        new_data.append(float(n_num))
    
    #Getting the mean
    n=len(new_data)
    new_data.sort()
    #total=0
    #for x in new_data:
        #total+=x

    #mean=total/n
    #print("Mean/Average is: "+str(mean))

    #Using floor division to get the nearest number to whole number
    #Floor division is shown by //
    
    if n%2==0:
        #Getting the first number
        median1=float(new_data[n//2])
        #Getting the second number
        median2=float(new_data[n//2-1])
        #Getting mean of those numbers
        median=(median1+median2)/2
    else:
        median=new_data[n//2]
        print(n)
    print("Median is: "+str(median))

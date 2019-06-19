#Python script for analyzing the financial records of a company.
#Import modules
import os
import csv

# Reading the data
csvpath = os.path.join('.', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# (1) Loop to compute (1) Total Months and (2) Profits.
    meses=0  
    profit=0
    c=[] 
    for row in csvreader:
        meses=meses+1
        profit=profit + int(row[1])
        c.append(int(row[1]))
        
# Loop to compute (1) changes and (2) the average of the changes. 
    change=[]      
    for i in range(0, (meses-1)):    
        change.append(c[i+1]-c[i])
    
    media=sum(change)/len(change)
    
# Loops para encontrar indices de  filas máximas y mínimas
    
    k=0
    mini=[]
    maxi=[]
    maxval=max(change)
    minval = min(change)
    indmax = [j for j, w in enumerate(change) if w == maxval]
    indmin = [i for i, v in enumerate(change) if v == minval]

# Volvemos a leer el CSV para poder loopear sobre sus filas. 
# Por alguna razón esto no es posible sino se vuelve a leer!!
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# Extraemos la fecha del máximo y del mínimo en un loop sobre las filas
    for row in csvreader:
        if k==(indmin[0]+1):
           mini.append(row[0])
        if k==(indmax[0]+1):
           maxi.append(row[0])   
        k=k+1  

# Guardamos en un string las fechas de los minimos y
# maximos cambios concatenadas con sus respectivos valores.       
    minimo= str(mini[0]) + " " + "($ "+ str(change[indmin[0]])+")"
    maximo= str(maxi[0]) + " " + "($ "+ str(change[indmax[0]])+")"

#Storing results as strings
Tmeses="Total Months: " + str(meses)
Tprofits="Total: $ "+ str(profit)
promedioC="Average Change: $ "+ str(media)
Gincrease="Greatest Increase in Profits: " + maximo
Gdecrease="Greatest Decrease in profits: " + minimo


#Printing to terminal
print("                            ")
print("Financial Analysis")
print("----------------------------")
print(Tmeses)
print(Tprofits)
print(promedioC)
print(Gincrease)
print(Gdecrease)

# Exporting a text file with the results.
# Specify the file to write to
output_file = os.path.join("PyBank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w', newline='') as datafile:

    # Initialize csv.writer
    writer = csv.writer(datafile)

    # Write the first row (column headers)
    writer.writerow(["Finacial analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([Tmeses])
    writer.writerow([Tprofits])
    writer.writerow([promedioC])
    writer.writerow([Gincrease])
    writer.writerow([Gdecrease])

    
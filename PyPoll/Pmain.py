#Python script for helping a small, rural town modernize its vote-counting process.
#Import modules
import os
import csv

# Reading the data
csvpath = os.path.join('.', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# (1) Loop to compute  total nummber of votes and identify cadidates
    votes=0  
    candidates=["Khan"] 
    for row in csvreader:
        votes=votes+1
        k=0
        for i in candidates:
            if i !=	row[2]:
               k=k
            else:
                k=k+1
        if k == 0:
            candidates.append(row[2])

# Counting votes for each candidate   
# Adentro del 1er loop de candidatos volvemos a leer el CSV para poder loopear sobre sus filas. 
# Por alguna razón esto no es posible sino se vuelve a leer!!  
  
    votesC = [] 
    for candidate in candidates: 
        votes=0
        with open(csvpath, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            csv_header = next(csvreader)   
            for row in csvreader:  
                if row[2] == candidate:
                    votes=votes+1
            votesC.append(votes)        
    Totalvotes=sum(votesC)    

#loop to compte porcentajes de votación para cada candidato
    porcentajes=[]
    n=0
    for candidate in candidates: 
        porcentajes.append(int(100*votesC[n]/Totalvotes))
        n=n+1

#loop para hacer una lista de listas con los resultados
resultado=[]
m=0
maxi=max(porcentajes)
winner="Li"
for candidate in candidates: 
    resultado.append([candidate+":", str(porcentajes[m])+"%", "("+str(votesC[m])+")"])
    if maxi == porcentajes[m]:
       winner=candidate
    m=m+1

# The winner of the election based on "majority voting" is:

i=0
print("                            ")
print("Election Results")
print("----------------------------")
print("Total votes: "+ str(Totalvotes))
print("----------------------------")
for candidate in candidates: 
    print(resultado[i])
    i=i+1
print("----------------------------")
print("Winner: " + winner)
print("----------------------------")

# Exporting a text file with the results.
# Specify the file to write to
output_poll = os.path.join("PyPoll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_poll, 'w', newline='') as datafile:

    # Initialize csv.writer
    writer = csv.writer(datafile)
    x=0
    
    # Write the first row (column headers)
    writer.writerow(["Election results"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total votes: "+ str(Totalvotes)])
    writer.writerow(["----------------------------"])
    for candidate in candidates: 
        writer.writerow(resultado[x])
        x=x+1
    writer.writerow(["----------------------------"])
    writer.writerow(["Winner: " + winner])
    writer.writerow(["----------------------------"])
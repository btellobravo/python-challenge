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
    

    


 

# The winner of the election based on "majority voting" is:



print(str(votes))
print(candidates)  
print(votesC)

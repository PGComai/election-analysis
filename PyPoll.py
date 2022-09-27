#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data to retrieve
# 1. total number of votes cast
# 2. complete list of candidates
# 3. percentage each candidate got
# 4. total number each candidate got
# 5. winner


# In[2]:


import datetime as dt
import csv
import os


# In[24]:


file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

t_votes = 0
options = []
c_votes = {}
winner = ''
win_count = 0
win_percent = 0
c_results = ''

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
        
    headers = next(file_reader)
    
    for row in file_reader:
        t_votes += 1
        
        c_name = row[2]
        
        if c_name not in options:
            options.append(c_name)
            c_votes[c_name] = 0
        
        c_votes[c_name] += 1
    
    for c in options:
        votes = c_votes[c]
        vote_percent = float(votes) / float(t_votes) * 100
        
        c_results += (f'{c}: {vote_percent:.1f}% ({votes:,})\n')
        
        if votes > win_count and vote_percent > win_percent:
            win_count = votes
            win_percent = vote_percent
            winner = c
            
    winner_sum = (
    
    f'------------------------\n'
        
    f'Winner: {winner}\n'
        
    f'Winning Vote Count: {win_count:,}\n'
        
    f'Winning Percentage: {win_percent:.1f}%\n'
        
    f'------------------------\n'
    
    )
    
    print(winner_sum)
    
    #print(t_votes)
    #print(options)
    #print(c_votes)
    
    
with open(file_to_save, 'w') as txt_file:
    
    election_results = (
    
    f'\nElection Results\n'
        
    f'--------------------------\n'
        
    f'Total Votes: {t_votes:,}\n'
        
    f'--------------------------\n'
    
    )
    
    print(election_results)
    print(c_results)
    
    txt_file.write(election_results)
    txt_file.write(c_results)
    txt_file.write(winner_sum)



# In[ ]:





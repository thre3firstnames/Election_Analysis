# Data to retrieve
# 1. Total number of votes cast
# 2. A Complete list of candidates who recieved votes
# 3. Percentage of votes each candidate recieved
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote

#open a file
# file_variable = open(filename, mode)
    # MODES
    #"r" to read
    #"w" open a file and write to it (will overwrite OR create a new file)
    #"x" Open a file for creation (if it does not exist, one will be created)
    #"a" Open and file and append -- data will only be added to the file, not overwritten
    #"+" Open a filed for reading/writing

# indicate the file to load
# file_to_load = 'Resources\election_results.csv'

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # To do: perform analysis.
#     print(election_data)

#IMPORTING THE MODULES
import csv
import os

#INDICATING WHERE THE FILE IS, OPENING IT, and USING THE DATA
#assign variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable for the file to save and the path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Declare vote counter
total_votes=0

#Candidate Options and votes
candidate_options = []
#declare empty vote dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the results and read
with open(file_to_load) as election_data:
    #To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)
 
    #print header row
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #Add to total vote count
        total_votes +=1
        

    #PGet Candidate Names
        candidate_name = row[2]
    #Add Candidate Names to options list with only unique values
        if candidate_name not in candidate_options:
            #Add unique names to list
            candidate_options.append(candidate_name)
            #track the vote count per candidate
            candidate_votes[candidate_name]=0
            #increase votes by one with each instance of candidate name
        candidate_votes[candidate_name] += 1

#save results to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end = "")
    #save final vote count to text file
    txt_file.write(election_results)


    #loop through candidate options to get names and vote percentage
    for candidate_name in candidate_votes:
    #retrieve voates of the candidate from candidate_votes dictionary
        votes = candidate_votes[candidate_name]
    #calculate percentage of the vote cout
        vote_percentage = float(votes) / float(total_votes) * 100
    #print each candidate and the percentage of the votes using f-string formatting
        # print(f"{candidate_name}: recieved {vote_percentage:.1f}% fo the total vote.")
    
        #determine the winning vote cound and candidate
        #determine if the vote count that was caldulated is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if the vote count IS greater than the winning count and the percentage is greater than the winning percentage, set the winning count equal to votes and percetnage equal to percentage
            winning_count = votes
            winning_percentage = vote_percentage
        #set the winning count equal to the winning candidate name in the for loop
            winning_candidate = candidate_name

        #print to terminal
        # print(f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")

        #Candidate results details 
        candidate_results = (f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #write the results to the textfile
        txt_file.write(candidate_results)



#format winning candidate summary for output
    winning_candidate_summary = (    
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    #Save winner info to the text file
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)




# CREATING FILES IN EXISTING FOLDERS
    # #create a filename variable to a direct or indirect path where the files to be located 
    # file_to_save = os.path.join("Analysis", "election_analysis.txt")
    # #use the open function in "W" mode to open a file and write data to the file
    # open(file_to_save, "w")

# ADDING CONTENT TO FILES
    # #create a variable to a direct or indirect path to file
    # file_to_save = os.path.join("Analysis", "election_analysis.txt")
    # #use open statement ot open the file as a text file
    # outfile = open(file_to_save, "w")
    # #wite data to the file
    # outfile.write("Hello World")
    # #close the file
    # outfile.close()

# ADDING CONTENT TO FILES - REFACTOR
# #create a variable to a direct or indirect path to file
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# #Use with statement to open the file and save as a text file
# with open(file_to_save, "w") as txt_file:
#     #write data to the file
#     txt_file.write(
#         "Counties in the Election\n"
#         #Is there a simpler way to repeat characters without typing them so many times? Formula?
#         "-----------------------------\n"
#         "Arapahoe\nDenver\nJefferson")

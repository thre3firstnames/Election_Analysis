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

#open the results and read
with open(file_to_load) as election_data:
    #To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)
 
    #print header row
    headers = next(file_reader)
    print(headers)
 
    #   # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)




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

# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The iwnner of the election based on popular vote



# add our dependencies
import csv
import os

# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")


# initialize total vote counter
total_votes = 0

# candidate options variable
candidate_options = []

# declare an empty dictionary to keep votes for each candidate
candidate_votes ={}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    # the variable file_reader is referencing the file object which is stored in memory
    ## to pull the data out of the file object we can iterate through the file_reader variable and print each row
    ## including the headers, or column names

    # print the header row
    headers = next(file_reader)
   #print(headers)

    # print each row in the csv file
    for row in file_reader:
        #print(row)

        # add to the total vote count
        total_votes +=1

        # print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            # add it to candidate_options
            candidate_options.append(candidate_name)
        
            # begin tracking candidate's vote count
            candidate_votes[candidate_name]=0

        #add a vote to that candidate's count, align with if statement
        candidate_votes[candidate_name] +=1

# save the results to our text file
with open(file_to_save, "w") as txt_file:

#print the final vote count to the terminal
    election_results = (
        f"\nElection Restults\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n"
    )        
    print(election_results, end="")
    # save the final vote count to the text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
            # retrieve the vote count of a candidate
                votes = candidate_votes[candidate_name]

            #calculate the percentage of votes
                vote_percentage = float(votes)/float(total_votes)*100

            #create if statement to determine winning vote count and candidate
            ## 1. determine if the votes are greater than the winning count
                if (votes>winning_count) and (vote_percentage>winning_percentage):
            
                # 2. if true then set winning_count = votes and winning_percent = vote_percentage
                    winning_count = votes
                    winning_percentage = vote_percentage

                # 3. set the winning_candidate equal to the candidate's name
                    winning_candidate = candidate_name

                
            #align with if statemtent  
            #print("------------------------\n")  
                candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                print(candidate_results)

                #save the candidate results to the txt file
                txt_file.write(candidate_results)

                
            
        #output results for winner
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        )
    print(winning_candidate_summary)

    #save winning candidate summary in txt file
    txt_file.write(winning_candidate_summary)

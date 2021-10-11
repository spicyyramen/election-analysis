
""" #How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))

# total voes in the election
total_votes = int(input("What is the total votes in the election?"))

#Calculate the percentage of votes you received
percentage_votes = (my_votes / total_votes)*100

print("I received "+ str(percentage_votes)+"% of the total votes.") """
#---------------------------------------------------------------------------------------


counties = ["Arapahoe", "Denver", "Jefferson"]


""" if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties")  

# compound membership and logical operation
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.") """

#--------------------------------------------------------------------------------------
# practice implementing a for loop by iterating through list of counties
""" for county in counties:
    print(county)

# practice with numbers
numbers=[0,1,2,3,4]
for num in numbers:
    print(num)

# can get same output by using range function
for num in range(5):
    print(num)

# indexing to iterate through a list
#       if list contains strings, need to get the length of the list as an integer for the range fx

for i in range(len(counties)):
    print(counties[i]) """

 # dictionary for counties and voters
counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

# to get ony the keys from a dictionary using for loop, write like iterating over list or tuple
for county in counties_dict:
    print(county)

# can also use the keys method to iterate over a dictionary to get the keys
for county in counties_dict.keys():
    print(county)

# to get the values of a dictionary
for voters in counties_dict.values():
    print(voters)
print("------------------------------------------")

# another way
print(counties_dict["Arapahoe"])
print("------------------------")

""" for county in counties:
    print(county)
print("-----------------------------------------")

# making a for loop to print nums
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)
print("-----------------------------------------")

# another way to print nums using range function
for num in range(5):
    print(num)
print("-------------------------------------") """

# to iterate through list of strings using indexes, need to get list length
for i in range(len(counties)):
    print(counties[i])
print("===========================================")     

# get the key-value pairs of a dictionary
for county, voters in counties_dict.items():
    print(county,voters)

print("==============")
print("==================")

#practice, turn key-value pairs into full sentences

for county, voters in counties_dict.items():
    print(county + " county has " +str(voters)+ " registered voters.")

print("-------------------")

# to print each dictionary in voting_data, use standard format for iterating over list with for loops

voting_data=[{"county":"Arapahoe", "registered_voters":4222829},
                {"county":"Denver", "registered_voters":463353},
                {"county":"Jefferson", "registered_voters": 432438}]
                

#for county_dict in voting_data:
   # print(county_dict)

# iterate over the list using the range function
for i in range(len(voting_data)):
    print(voting_data[i])
print("==================")


# get the values from a list of dictionaries
## to retrieve ONLY the values from each dictionary in the list of dicts we need NESTED 4loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
print("------------------------")

# how would you retrieve the # of voters from each dictionary?
for county_dict in voting_data:
    print(county_dict['registered_voters'])
print("==========")

# if you only want to print county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

print("----------------------")

#printing formats
## easier to use fstrings for concatenation 

""" # original code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes/total_votes)*100
print("I received " + str(percentage_votes)+"% of the total votes.")

print("--====--====--==--=====-=--==--==--")
#edited code to use fstrings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes/total_votes * 100}% of the total votes.") """


# using f strings with dictionaries
""" for county, voters in counties_dict.items():
    print(county + " county has " +str(voters)+ " registered voters.") """

print("--====--====--==--=====-=--==--==--")
##rewrite with fstring
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

""" print("---===---===---===---===---===")
#multi line f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of cotes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes/total_votes*100}% of the total votes. "
)

print(message_to_candidate) """


# formatting floating point decimals
""" f'{value:{width}.{precision}}' """

# redo with float formatting

print("---------------------------")
""" candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of cotes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes/total_votes*100:.2f}% of the total votes. "
)

print(message_to_candidate) """

print("=============================")


# using dependencies
# import the datetime class from the datetime module
import datetime
#use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()
#print the present time
print("The time right now is ",now)

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if counties[3] != 'Jefferson':
#     print(counties[2])

# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapagoe and El Paso are in the list of counties")
# else:
#     print("Arapahoe or El Paso is not in the list of counties")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties")
# else:
#     print("Arapahoe or El Paso is not in the list of counties")

# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties")

# for county in counties:
#     print(county)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

# counties_tuples = ("Arapahoe","Denver","Jefferson")

# for county in counties_tuples:

#       print(counties)


# # DICTIONARIES
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# #F-STRINGS
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# for county in counties_dict:
#     print(county)

#Using the Keys to define outputs
# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# Get value for a specific key
# print(counties_dict["Arapahoe"])

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

# for county, voters in counties_dict.items():
#     print(county, voters)

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# # for county_dict in voting_data:
# #     print(county_dict)

# # for i in range(len(voting_data)):

# #       print(voting_data[i]['county'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)      
#     #PRINTING the number of voters
#     # print(county_dict['registered_voters'])\
#     print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#MULTI_LINE F STRINGS
    # candidate_votes = int(input("How many votes did the candidate get in the election? "))
    # total_votes = int(input("What is the total number of votes in the election? "))
    # message_to_candidate = (
    #     f"You received {candidate_votes:,} number of votes. "
    #     f"The total number of votes in the election was {total_votes:,}. "
    #     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

    # print(message_to_candidate)

#SKILL DRILL 3.2.A
    # counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

    # for county, voters in counties_dict.items():
    #     print(f"{county} has {voters:,} registered voters.")

# SKILL DRILL 3.2.B
voting_data = [
    {"county":"Arapahoe", "registered_voters": 422829}, 
    {"county":"Denver", "registered_voters": 463353}, 
    {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} has {county_dict['registered_voters']:,} registered voters.")


#counties = ["Arapahoe", "Denver", "Jefferson"]
#if "El Paso" in counties or "Arapahoe" in counties:
    #print("El Paso or Arapahoe are relevant counties")
#else:
    #print("El Paso or Arapahoe aren't relevant counties")


#for county in counties:
    #print(county)

#for i in range(len(counties)):
    #print(counties[i])

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for x in counties_dict:
    #print(x)

#for county in counties_dict:
    #print(counties_dict[county])

#for voters in counties_dict.values():
    #print(voters)


#for county, voters in counties_dict.items():
    #print(county, "has", voters, "registered voters!")

#voting_data = [{"County": "Arapahoe", "Registered Voters": 422829},
               #{"County": "Denver", "Registered Voters": 463353},
               #{"County": "Jefferson", "Registered Voters": 432438}]

#for i in range(len(voting_data)):
    #print(voting_data[i])

#for counties_data in voting_data:
    #for value in counties_data.values():
        #print(value)

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#my_votes = int(input("How many votes did you get in the election?"  ))
#total_votes = int(input("How many total were in the election?"  ))
#print(f"I received {(my_votes / total_votes) * 100}% of the total votes.")

candidate_votes = int(input("How many votes did the candidate get in the election?  "))
total_votes = int(input("What is the total number of votes in the election?  "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election is {total_votes}."
    f"You received {(candidate_votes / total_votes) * 100:.2f}% of the total votes. Congradulations!! "
)

print(message_to_candidate)
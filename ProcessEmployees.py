"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file
file = open("employee_data.csv", "r")
data = csv.reader(file)


# create an empty dictionary
dictionary = {}

# use a loop to iterate through the csv file
for line in data:
    # check if the employee fits the search criteria
    if line[4] == "CSR":
        print(
            "CSR Name: ",
            line[1],
            " ",
            line[2],
            "Current Salary: $",
            format(int(line[5]), ".2f"),
        )
        key = str(line[1]) + str(line[2])
        dictionary[key] = int(line[5]) * 1.1


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout

for key in dictionary:
    print("CSR Name: ", key, "New Salary: $" + format(dictionary[key], ",.2f"))

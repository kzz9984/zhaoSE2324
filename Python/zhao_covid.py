"""
Name: Kevin Zhao
Date: 12/04/23

File: zhao_covid.py

Purpose: Read a text file with data for the number of COVID-19 cases by state
         as of Saturday, May 24, 2020. Display the data in a table and
         calculate the average number of COVID-19 cases per state.
"""

def main():

    # Read txt file and add contents to lists: states & cases
    f = open("covid19_txt.txt", 'r')        # Open txt file for reading
                                            # and assign it to file object "f"
    
    states = []                             # States list
    cases = []                              # Cases list

    for line in f:                          # Iterate through each line in file
        line = line.split(',')              # Split each line at comma
        states.append(line[0].strip())      # Strip ws and \n & append state to states
        cases.append(line[1].strip())       # Strip ws and \n & append case count to cases
    

    # Calculate average number of cases per state
    sumCases = 0                            # Sum of all cases

    for c in range(len(cases)):             # Iterate over cases list
        if c == 0:                          # First entry is the title "COVID-19 CASES"
            pass                            # so skip (pass) it
        else:                               
            sumCases += int(cases[c])       # Sum all numerical values in cases
                                            # (must convert to numeric type)
    
    avgCases = sumCases / (len(cases) - 1)  # Cases includes 57 entries (1st is column title)
                                            # Count only the 56 numeric ones


    # Display results in table
    print("{0:^10}{1:^14}".format(states[0], cases[0]))

    for s in range(len(states)):
        if s == 0:                          # First entry is column title so skip it
            pass
        else:
            print("{0:^10}{1:<14}".format(states[s], cases[s]))
    
    print("The average number of COVID-19 cases per state is: {0:.0f}".format(avgCases))


main()
# module for implementing cyk algorithm using table filling method
from modules.cfg_to_cnf import get_set_of_production

# variable to store the table
TRIANGULAR_TABLE = {}

# function to check if the string is accepted by the cfg
def is_accepted(inputString):
    global TRIANGULAR_TABLE
    # make sure the table is empty before starting
    TRIANGULAR_TABLE.clear()
    # get the set of production from module cfg_to_cnf
    prodRules = get_set_of_production()
    # initialize the table
    for i in range(1,len(inputString)+1):
        for j in range(i, len(inputString)+1):
            TRIANGULAR_TABLE[(i,j)] = []
    # iteration O(n^3)
    for i in reversed(range(1, len(inputString)+1)):
        for j in range(1, i+1):
            # when index i == j
            if (j == j + len(inputString) - i):
                tempList = []
                # find the production rule that has the terminal
                for key, value in prodRules.items():
                    for val in value:
                        if (val == inputString[j-1]):
                            tempList.append(key)
                # add the production rule to the table
                TRIANGULAR_TABLE[(j, j + len(inputString) - i)] = tempList
            # when index i != j
            else:
                # list to store the result of concatenation + union
                tempList = []
                # list to store the production rule (left hand side)
                resultList = []
                # compare most k pair of previously computed
                for k in range(len(inputString) - i):
                    first = TRIANGULAR_TABLE[(j,j+k)]
                    second = TRIANGULAR_TABLE[(j+k+1,j+len(inputString) - i)]
                    # concatenate
                    for fi in first:
                        for se in second:
                            if (fi+se not in tempList):
                                # union
                                tempList.append(fi+se)
                # find the production rule that has the concatenated string
                for key, value in prodRules.items():
                    for val in value:
                        if (val in tempList and key not in resultList):
                            resultList.append(key)
                # add the production rule to the table
                TRIANGULAR_TABLE[(j,j+len(inputString) - i)] = resultList
    # check if the start symbol is in the last cell
    if "T" in TRIANGULAR_TABLE[(1, len(inputString))]:
        return True
    else:
        return False

# function to get the table
def get_triangular_table():
    global TRIANGULAR_TABLE
    return TRIANGULAR_TABLE


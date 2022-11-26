# module to convert cfg to cnf
from itertools import permutations
from string import ascii_uppercase, ascii_lowercase

RESULT = {}
TERMINAL_LIST = list(ascii_lowercase)
VARIABLE_LIST = list(ascii_uppercase)

# function to check if there is S in the RHS
def is_contain_s_in_rhs():
    global RESULT
    for val in RESULT.values():
        for i in val:
            if ("S" in i):
                return True
    return False

# function to check if there is epsilon in the RHS
def is_contain_epsilon():
    global RESULT
    for key, val in RESULT.items():
        for i in val:
            if ("ε" in i):
                return True
    return False

# function to remove epsilon or null production
def remove_cascading_epsilon(k):
    global RESULT
    for key, val in RESULT.items():
        valList = []
        for i in val:
            if (k in i):
                epsilon = "ε"
                nonEpsilon = []
                for j in i:
                    if (j != k):
                        nonEpsilon.append(j)
                repeat = i.count(k)
                tempList = []
                for j in range(repeat+1):
                    tempStr = ""
                    for l in range(j):
                        tempStr += epsilon
                    for l in nonEpsilon:
                        tempStr += l
                    for l in range(repeat - j):
                        tempStr += k
                    permuList = permutations(tempStr)
                    for z in permuList:
                        tempList.append("".join(z))
                numberPostList = []
                nonEpsilonPost = []
                for j in range(len(i)):
                    if (i[j] == k):
                        numberPostList.append(j)
                    else:
                        nonEpsilonPost.append(j)
                for j in tempList:
                    isAcc = True
                    for l in numberPostList:
                        if not (j[l] == k or j[l] == epsilon):
                            isAcc = False
                    for l in nonEpsilonPost:
                        if not (j[l] == i[l]):
                            isAcc = False
                    if isAcc:
                        valList.append(j)
        for i in valList:
            if (i not in val):
                val.append(i)
        RESULT[key] = val

# function to check if there is two or more variables in the RHS
def is_two_more_in_rhs():
    global RESULT
    for key, val in RESULT.items():
        for i in val:
            if (len(i) > 2):
                return True
    return False

# function to remove if there is two or more variables in the RHS
def remove_two_more_in_rhs(k):
    global RESULT
    tempStr = "".join(RESULT[k])
    for key, val in RESULT.items():
        for i in val:
            if len(i) > 2 and tempStr in i:
                newStr = i.replace(tempStr, k)
                val.remove(i)
                val.append(newStr)

# function to check if there is terminal and variable in the RHS
def is_contain_terminal_variable():
    global RESULT
    global VARIABLE_LIST
    global TERMINAL_LIST
    for key, val in RESULT.items():
        for i in val:
            if len(i) == 2:
                if (i[0] in VARIABLE_LIST and i[1] in TERMINAL_LIST
                        or i[0] in TERMINAL_LIST and i[1] in VARIABLE_LIST):
                    return True
    return False

# function to remove if there is terminal and variable in the RHS
def remove_contain_terminal_variable(k):
    global RESULT
    tempStr = "".join(RESULT[k])
    for key, val in RESULT.items():
        for i in val:
            if (tempStr in i):
                if (str(key) != str(k)):
                    newStr = i.replace(tempStr, k)
                    val.remove(i)
                    val.append(newStr)

# main function to convert cyk to cnf
def get_set_of_production():
    global RESULT
    global VARIABLE_LIST
    global TERMINAL_LIST
    RESULT.clear()
    # read file and make dictionary
    f = open("./set_of_production.txt", "r", encoding="utf-8")
    for line in f:
        temp = line.splitlines()
        for i in temp:
            res = i.split(" ")
            for j in res:
                if (j == "|" or j == "→"):
                    res.remove(j)
            for j in res:
                if res[0] in RESULT.keys():
                    if (j != res[0]):
                        tempValue = RESULT[res[0]]
                        if (j not in tempValue):
                            tempValue.append(j)
                        RESULT[res[0]] = tempValue
                else:
                    RESULT[res[0]] = res[1:]
    # check if start symbol S is occur in the RHS
    if is_contain_s_in_rhs():
        RESULT["T"] = ["S"]
    # check if there is epsilon or null production and remove it
    while (is_contain_epsilon()):
        for key, val in RESULT.items():
            for i in val:
                if (len(i) > 1 and "ε" in i):
                    temp = i.replace("ε", "")
                    if (temp not in val):
                        val.append(temp)
                    val.remove(i)
                    RESULT[key] = val
                if (len(i) == 1 and i == "ε"):
                    val.remove(i)
                    remove_cascading_epsilon(key)
                    RESULT[key] = val
    # remove unit production
    listKey = list(RESULT.keys())
    for key in RESULT.keys():
        for k in listKey:
            if k in RESULT[key]:
                if key == k:
                    RESULT[key].remove(k)
                else:
                    RESULT[key].remove(k)
                    RESULT[key].extend(RESULT[k])
    # replace each production that has length more than 2
    keyList = ["X", "Y", "Z", "P", "Q", "R", "V"]
    while (is_two_more_in_rhs()):
        saverI = ""
        for key, val in RESULT.items():
            for i in val:
                if (len(i) > 2):
                    saverI = i[-2:]
        RESULT[keyList[0]] = [saverI]
        remove_two_more_in_rhs(keyList.pop(0))
    # replace each production that has terminal and variable in the RHS
    while is_contain_terminal_variable():
        saverI = ""
        for key, val in RESULT.items():
            for i in val:
                if len(i) == 2:
                    if (i[0] in VARIABLE_LIST and i[1] in TERMINAL_LIST
                            or i[0] in TERMINAL_LIST and i[1] in VARIABLE_LIST):
                        if i[0] in TERMINAL_LIST:
                            saverI = i[0]
                        else:
                            saverI = i[1]
        RESULT[keyList[0]] = [saverI]
        remove_contain_terminal_variable(keyList.pop(0))
    # return the dictionary
    return RESULT

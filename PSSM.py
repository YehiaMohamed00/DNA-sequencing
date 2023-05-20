import math

def print_table(table, str1, str2):
    counter = 0
    print("{:5s}".format(str("pos")), end="| ")
    for col in str1:
        print("{:5s}".format(col), end="| ")
    for row in range(len(table)):
        for col in table[row]:
            if counter % len(str1) == 0:
                print()
                print("{:5s}".format(str(str2[row])), end="| ")
            print("{:5s}".format(str(col)), end="| ")
            counter += 1
    print("\n"+"________"*len(str1), "\n\n")

def PSSM(strings, str_to_match):
    # formation of row headers
    str2 = ""
    for col in range(len(strings[0])):
        for row in range(len(strings)):
            if strings[row][col] in str2:
                continue
            str2 += strings[row][col]
    ########################################
    # formation of column headers
    str1 = ""
    for col in range(len(strings[0])):
        str1 += str(col + 1)
    ########################################
    # creation of PSSM table
    table = []
    for row in range(len(str2)):
        temp = []
        # given the value of "--" in order to avoid
        # taking a log of 0 which crashes the program
        # it denotes it hasn't occured at that position
        # in any of the input strings
        for col in range(len(str1)):
            temp.append("--")
        table.append(temp)
    ########################################
    # Step 1: Raw Frequency Table
    current_col, out = [], ""
    for col in range(len(strings[0])):
        for row in range(len(strings)):
            current_col.append(strings[row][col])
        # in a separate loop because it is dependent
        # on the previous loop (current_col)
        for roww in range(len(str2)):
            calc = current_col.count(str2[roww]) / len(current_col)
            if calc == 0:
                continue
            table[roww][col] = calc
        current_col.clear()
    print_table(table, str1, str2)
    ########################################
    # Step 2: Normalize Values
    for row in range(len(table)):
        avg = 0
        # two for loops because the second for is dependent on
        # the final result of the avg value

        # this loop for evaluating the avg of this row
        for col in range(len(table[0])):
            try:
                avg += float(table[row][col]) / len(table[0])
            except:
                pass
        # this loop for normalizing values of the table
        for col in range(len(table[0])):
            try:
                table[row][col] = round(float(table[row][col]) / avg, 2)
            except:
                pass
    print_table(table, str1, str2)
    ###########################################
    # Step 3: Convert to probability value
    for row in range(len(table)):
        for col in range(len(table[0])):
            try:
                table[row][col] = round(math.log2(float(table[row][col])), 2)
            except:
                pass
    print_table(table, str1, str2)
    ###########################################
    # Step 4: Match a new sequence to PSSM
    total_score = 0
    # adds up all matching character scores
    # of the string to be matched from the
    # PSSM table
    for i, j in zip(str_to_match, range(len(str_to_match))):
        total_score += table[str2.index(i)][str1.index(str(j + 1))]
    print(f'==> Total Match Score of "{str_to_match}" = {total_score}')

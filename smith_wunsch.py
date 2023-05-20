import random
import matrix

def string_weight(text):
    weight = []
    for character in text:
        weight.append(ord(character))
    return weight


class Cell(object):
    def __init__(self):
        self.value = 0
        self.prev = ""

def smith_wunsch(str1, str2, config: dict):
    str1 = " " + str1
    str2 = " " + str2
    ###################################################
    if config["scoring"] == "pam":
        pam = matrix.given_matrices_inserter("pam250.txt")[1]
        pam_order = "G A V L I P S T D E N Q K R H F Y W M C B Z X".replace(" ", "")
    elif config["scoring"] == "blosum":
        blosum = matrix.given_matrices_inserter("blosum45.txt")[1]
        blosum_order = "A R N D C Q E G H I L K M F P S T W Y V B J Z X".replace(" ", "")
    ###################################################
    table = []
    # table preparation
    for ii in range(len(str2)):
        temp = []
        for jj in range(len(str1)):
            temp.append(Cell())
        table.append(temp)

    # table preparation for row1 and col 1 in needleman_wunsch
    if config["algo"] == "needleman_wunsch":
        for col in range(1, len(str1)):
            table[0][col].value = col * config["gap"]
            table[0][col].prev += "←"
        for row in range(1, len(str2)):
            table[row][0].value = row * config["gap"]
            table[row][0].prev += "↑"

    # smith_waterman specific variables to keep track of
    # max value and position(s) of the max value
    mx = 0
    mx_ndx = []
    for row in range(1, len(str2)):
        for col in range(1, len(str1)):
            # calculations for both
            up = table[row - 1][col].value + config["gap"]
            left = table[row][col - 1].value + config["gap"]
            if config["type"] != "protein":
                if str1[col] == str2[row]:
                    diag = table[row - 1][col - 1].value + config["match"]
                else:
                    diag = table[row - 1][col - 1].value + config["mismatch"]
            else:
                if config["scoring"] == "pam":
                    diag = (
                        table[row - 1][col - 1].value
                        + pam[pam_order.index(str1[col])][pam_order.index(str2[row])]
                    )
                elif config["scoring"] == "blosum":
                    diag = (
                        table[row - 1][col - 1].value
                        + blosum[blosum_order.index(str1[col])][blosum_order.index(str2[row])]
                    )

            # updating the cell value with the proper method
            # for that specific algorithm
            if config["algo"] == "needleman_wunsch":
                tmp = max(diag, up, left)
            else:
                tmp = max(diag, up, left, 0)
            table[row][col].value = tmp

            # this section is responsible for keeping
            # track of the max value position(s) in
            # smith_waterman
            if config["algo"] != "needleman_wunsch":
                if mx < tmp:
                    mx = tmp
                    mx_ndx = [[row, col]]
                elif mx == tmp:
                    mx_ndx.append([row, col])

            # if is used to all sources of the evaluated
            # value at hand and updating the prev string
            # which is used later to traceback table
            if tmp == diag:
                table[row][col].prev += "↖"
            if tmp == up:
                table[row][col].prev += "↑"
            if tmp == left:
                table[row][col].prev += "←"

    # this section is only for printing the
    # produced "VALUES" table
    counter = 0
    # prints str1 as column headers
    print("{:4s}".format(str()), end="| ")
    for j in str1:
        print("{:4s}".format(j), end="| ")
    # prints str2 row headers as well as
    # every cell in the table
    for i in range(len(table)):
        for j in table[i]:
            if counter % len(str1) == 0:
                print()
                print("{:4s}".format(str(str2[i])), end="| ")
            print("{:4s}".format(str(j.value)), end="| ")
            counter += 1
    print()
    print()

    # this section is only for printing the
    # produced "ARROWS" table
    print("{:4s}".format(str()), end="| ")
    for j in str1:
        print("{:4s}".format(j), end="| ")
    for i in range(len(table)):
        for j in table[i]:
            if counter % len(str1) == 0:
                print()
                print("{:4s}".format(str(str2[i])), end="| ")
            print("{:4s}".format(str(j.prev)), end="| ")
            counter += 1
    print()
    print()
    ######################################################
    # this section is responsible for the traceback

    # we don't care about the max value in needleman
    # we always start from the bottom right
    if config["algo"] == "needleman_wunsch":
        mx_ndx = [[ii, jj]]

    # 1st loop: for multi-path evaluation
    # 2nd loop: for multiple start position (smith_waterman)
    # 3rd loop: for printing alignment
    # 4th loop: for tracing back the arrows and forms alignment
    avg_len = int((len(str1) + len(str2))/ 2)
    dic = {}
    for i in range(avg_len*150):
        out1, out2 = "", ""; path = []
        for count in mx_ndx:
            row, col = count[0], count[1]
            while row != -1:
                while col != -1:
                    # stopping condition for smith_waterman
                    condition = (table[row][col].value != 0 and table[row][col].prev != "")
                    if config["algo"] == "needleman_wunsch":
                        # stopping condition for needleman_wunsch
                        condition = table[row][col].prev != ""
                    if condition:
                        l = list(table[row][col].prev)
                        random.shuffle(l)
                        shuffled_prev = ''.join(l)
                        if shuffled_prev[0] == "↖":
                            out1 += str1[col]
                            out2 += str2[row]
                            row -= 1
                            col -= 1
                            path.append("↖")
                        elif shuffled_prev[0] == "↑":
                            out1 += "-"
                            out2 += str2[row]
                            row -= 1
                            path.append("↑")
                        elif shuffled_prev[0] == "←":
                            out1 += str1[col]
                            out2 += "-"
                            col -= 1
                            path.append("←")
                    else:
                        break
                out1 = out1[::-1]
                out2 = out2[::-1]
                total_weight = str(string_weight(out1) + string_weight(out2))
                if total_weight not in dic.keys():
                    print("\n" + out1 + "\n" + out2 + "\n" + str(path[::-1]))
                    dic[total_weight] = [out1, out2]
                break

    # prints the max value and its position(s)
    if config["algo"] != "needleman_wunsch":
        print("\nmax value =", mx, "at", mx_ndx)

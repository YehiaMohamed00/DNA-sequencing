import random
# seq.s are same length in consensus



def sum_consensus(strings:list):
    characters, current_col, result, counts, out = [], [], [], {}, ""
    # 1st loop: for looping every column and assemble
    # consensus sequence
    # 2nd(a) loop: for fetching the column characters
    # 2nd(b) loop: for evaluating the most repeated
    #               character in the current column
    for col in range(len(strings[0])):
        # 2nd(a)
        for row in range(len(strings)):
            current_col.append(strings[row][col])
            if strings[row][col] in characters:
                continue
            characters.append(strings[row][col])
        # 2nd(b)
        for k in characters:
            if current_col.count(k) in counts.keys():
                continue
            # only last most repeated character wins
            counts[current_col.count(k)] = k
        # append the most repeated character at this
        # position to the output consensus alignment
        out += counts[max(counts.keys())]
        # print(counts)
        # print(result)
        # print(current_col)
        # print(characters)
        counts.clear(); result.clear(); current_col.clear(); characters.clear()
    # print(out)
    return out

def threshold_consensus(strings: list, threshold=20 / 100):
    characters, current_col, result, out = [], [], [], ""

    # 1st loop: for looping every column and assemble
    # consensus sequence
    # 2nd(a) loop: for fetching the column characters
    # 2nd(b) loop: for evaluating the character over
    #              threshold in the current column
    for col in range(len(strings[0])):
        # 2nd(a)
        for row in range(len(strings)):
            current_col.append(strings[row][col])
            if strings[row][col] in characters:
                continue
            characters.append(strings[row][col])
        # 2nd(b)
        for k in characters:
            # if passes the threshold add to consensus sequence
            # last character wins
            if (current_col.count(k) / len(current_col)) >= threshold:
                result.append(k + " " + str(current_col.count(k)))
                out += k
                break

        # if no character bypasses threshold then
        # it is undetermined and denoted by "?"
        if len(result) == 0:
            out += "?"
        # print(result)
        # print(current_col)
        # print(characters)
        result.clear(); current_col.clear(); characters.clear();
    # print(out)
    return out

def get_all(func, strs, thrshld=50/100):
    # done is used to collect all consensus sequences
    done = []
    for i in range(len(strs) * 150):
        # shuffles strings to make the last character different
        # theoretically gets all possible arrangements
        random.shuffle(strs)
        try:
            # if the threshold is provided run threshold consensu
            out_now = func(strs, thrshld)
        except TypeError:
            # in case not then run sum consensus
            out_now = func(strs)
        if out_now in done:
            continue
        done.append(out_now)

    # prints all consensus sequences evaluated
    print(f'There are ( {len(done)} ) consensus alignments')
    for i, j in enumerate(done):
        print("{:4s}".format(str(i+1)), end=": ")
        print(j)

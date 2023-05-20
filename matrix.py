def given_matrices_inserter(filename):
    try:
        data = open(filename, "r")
        dimensions = data.readline()
        try:
            n = int(dimensions)
        except ValueError:
            print("Wrong file")
            exit()
        letters = data.readline()
        letters = letters.replace("\n", "")
        letters_arr = letters.split(" ")
        # print(letters_arr)
        score_matrix = []
        for ii in range(n):
            temp = []
            for jj in range(n):
                temp.append(0)
            score_matrix.append(temp)
        for i in range(0, n):
            arr = data.readline().split(" ")
            for j in range(0, n):
                # print(arr[j])
                # score_matrix[i][j] = float(arr[j])
                score_matrix[i][j] = int(arr[j])
        # print("Chosen matrix:")
        # print(score_matrix)
        score_m = score_matrix
        return letters_arr, score_m
    except FileNotFoundError:
        print("There is no matrix file.")
        exit()

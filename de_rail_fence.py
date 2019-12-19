import re
def dekripsi_cipher(pesan, kunci):
    msg = pesan
    rails = kunci

    # removing white space from message
    # msg = msg.replace(" ", "")

    # creating an empty matrix
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(msg)):
            railMatrix[row].append('.')
        # inner for
    # for

    # testing the matrix
    # for row in railMatrix:
    #     for column in row:
    #         print(column, end="")
    #     print("\n")
    #     # inner for
    # # for

    # putting letters of message one by one in the matrix in zig-zag
    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
                # inner if
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else

    # testing the matrix with message in zig-zag
    # for row in railMatrix:
    #     for column in row:
    #         print(column, end="")
    #     print("\n")
    #     # inner for
    # # for

    # reordering the matrix
    ordr = 0
    for i in range(rails):
        for j in range(len(msg)):
            temp = railMatrix[i][j]
            if re.search("\\.", temp):
                # skipping '.'
                continue
            else:
                railMatrix[i][j] = msg[ordr]
                ordr += 1
            # if-else
        # inner for
    # for

    # testing matrix reorder
    for i in railMatrix:
        for column in i:
            print(column, end="")
        #inner for
        print("\n")
    # for

    # putting reordered matrix into decrypted text string to get decrypted text
    check = 0
    row = 0
    decryp_text = ""
    for i in range(len(msg)):
        if check == 0:
            decryp_text += railMatrix[row][i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            decryp_text += railMatrix[row][i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else
    # for

    # decryp_text = re.sub(r"\.", "", decryp_text)
    # print("Hasil Dekripsi: {}".format(decryp_text))
    return decryp_text


if __name__ == "__main__":
   dekripsi_cipher()
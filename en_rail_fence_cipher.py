def enkripsi(pesan, kunci):
    msg = pesan
    key = kunci
    # msg = input("Masukkan kalimat : ").upper()
    # key = int(input("Masukkan kunci : "))
    # msg = msg.replace(" ", "")
    arr = []
    for i in range(key):
        arr.append([])
    for baris in range(key):
        for kolom in range(len(msg)):
            arr[baris].append('.')


    baris = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            arr[baris][i] = msg[i]
            # print (arr[baris][i])
            baris += 1
            if baris == key:
                check = 1
                baris -= 1

        elif check == 1:
            # print (baris)
            baris -= 1
            arr[baris][i] = msg[i]
            # print (arr[baris][i])
            if baris == 0:
                check = 0
                baris = 1


    for baris in arr:
        for kolom in baris:
            print(kolom, end="")
        print("\n")

    enkripsi = ""
    for i in range(key):
        for j in range(len(msg)):
            enkripsi += arr[i][j]

    enkripsi = enkripsi.replace(".","")
    # print("Hasil Enkripsi : ",(enkripsi))
    return enkripsi


if __name__ == "__main__":
    enkripsi()

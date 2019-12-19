from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import de_rail_fence
import en_rail_fence_cipher
from de_rail_fence import dekripsi_cipher
from en_rail_fence_cipher import enkripsi




def enkripsiAES(plainteks):
    size = 16
    pad = "{"
    padding = lambda s: s + (size - len(s) % size) * pad
    cipher = AES.new(hkey, AES.MODE_ECB)
    # print (cipher)
    result = cipher.encrypt(padding(plainteks).encode('utf-8'))
    # nonbyte = result.decode('unicode-8')
    # print (nonbyte)
    # print (result)
    return result

def dekripsiAES(cipher):
    pad = "{"
    decipher = AES.new(hkey, AES.MODE_ECB)
    plaintext = decipher.decrypt(cipher).decode('utf-8')
    # print (plaintext)
    pad_index = plaintext.find(pad)
    result = plaintext[:pad_index]
    # print (result)
    return result

if __name__ == "__main__":
    msg = input ("MASUKKAN TEKS YANG AKAN DI ENKRIPSI = ")
    # msg = "I love Python More Than Ever Always with You Forever"
    key = int(input("Masukkan Kunci : "))
    sandi = "PassWord123"
    hash_obj = SHA256.new(sandi.encode('utf-8'))
    hkey = hash_obj.digest()
    # print (hkey)
    # print (len(hkey))
    EnkripsiRF = enkripsi(msg ,key)
    print ("Hasil Enkripsi Rail Fence Cipher = ",EnkripsiRF)
    Enkripsi = enkripsiAES(EnkripsiRF)
    print ("Hasil Enkripsi AES = ", Enkripsi)
    print ("Hasil Enkripsi AES (non byte) = ", Enkripsi)
    print ('\n\n')

    # dekripsi
    Dekripsi = dekripsiAES(Enkripsi)
    print ("Hasil Dekripsi AES = ", Dekripsi)
    plaintext = dekripsi_cipher(Dekripsi, key)
    print ("Hasil Dekripsi Rail Fence Cipher = ", plaintext)





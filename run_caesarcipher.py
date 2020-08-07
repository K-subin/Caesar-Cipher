import File_IO_lib
import caesarcipher_lib

#==== txt 파일 읽기 ====
my_content = File_IO_lib.ReadFile('시저암호/my_text.txt')
print('[plain_text]')
print(my_content)

#==== 읽어온 파일을 시저암호로 암호화 ====
key = 13
my_cipher = caesarcipher_lib.Caesar_encrypt(key, my_content)

#==== 암호화 파일 쓰기 ====
File_IO_lib.WriteFile('시저암호/my_cipher.txt', my_cipher)

print('[Cipher_text]')
print(my_cipher)

#==== 암호화 파일을 시저암호로 복호화 ====
my_new_text = caesarcipher_lib.Caesar_decrypt(key, my_cipher)

#==== 복호화 파일 쓰기 ====
File_IO_lib.WriteFile('시저암호/my_new_text.txt', my_new_text)

print('[Recovered_text]')
print(my_new_text)

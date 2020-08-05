import caesarcipher_lib
import os, sys

#==== 파일 입출력 ====
os.chdir('시저암호')
in_file = 'my_text.txt'
print('Working directory:',os.getcwd())

if not os.path.exists(in_file):
    print("file %s does not exist." %(in_file))
    sys.exit()
InFileObj = open(in_file)
my_content = InFileObj.read()
InFileObj.close()
print('[plain_text]')
print(my_content)

#==== 시저암호 암호화 ====
key = 13
my_cipher = caesarcipher_lib.Caesar_encrypt(key, my_content)

out_file = 'my_cipher.txt'
if os.path.exists(out_file):
    print('This will overwrite the file %s. (C)ontinue or (Q)uit' %(out_file))
    response = input('--->')
    if not response.lower().startswith('c'):
        sys.exit()
OutFileObj = open(out_file, 'w')
OutFileObj.write(my_cipher)
OutFileObj.close()

in_file = 'my_cipher.txt'
print('Working directory:',os.getcwd())

if not os.path.exists(in_file):
    print("file %s does not exist." %(in_file))
    sys.exit()
InFileObj = open(in_file)
my_cipher = InFileObj.read()
InFileObj.close()
print('[Cipher_text]')
print(my_cipher)

#==== 시저암호 복호화 ====
key = 13
my_new_text = caesarcipher_lib.Caesar_decrypt(key, my_cipher)

out_file = 'my_new_text.txt'
print('Working directory:',os.getcwd())

if os.path.exists(out_file):
    print('This will overwrite the file %s. (C)ontinue or (Q)uit' %(out_file))
    response = input('--->')
    if not response.lower().startswith('c'):
        sys.exit()
OutFileObj = open(out_file, 'w')
OutFileObj.write(my_new_text)
OutFileObj.close()
print('[Recovered_text]')
print(my_new_text)
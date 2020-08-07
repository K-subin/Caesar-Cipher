import caesarcipher_lib
import EngDic_lib
import os, sys

# 암호화 된 text 가져오기
os.chdir('시저암호')
in_file = 'my_cipher.txt'

print('Working directory:',os.getcwd())

if not os.path.exists(in_file):
    print("file %s does not exist." %(in_file))
    sys.exit()
InFileObj = open(in_file)
my_cipher = InFileObj.read()
InFileObj.close()
print('[Cipher text]')
print(my_cipher)

# EncDiic_lib을 이용하여 빈도조사를 통해 올바른 key 찾기
percentEngWords, key, recovered_msg = 0, 0, 0
for possible_key in range(0, 26):
    possible_recovered_msg = caesarcipher_lib.Caesar_decrypt(possible_key, my_cipher)
    possible_percentEngWords = EngDic_lib.percentEnglishWords(possible_recovered_msg)*100
    if (possible_percentEngWords > percentEngWords):
        key, percentEngWords, recovered_msg = possible_key, possible_percentEngWords, possible_recovered_msg

print('[Recovered text]')
print("key #%2s : %s (Englisg word : %5.1f%%)" %(key, recovered_msg, percentEngWords))

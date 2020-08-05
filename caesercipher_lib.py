lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 시저암호 함수
def Caeser_encrypt(key, plain_msg):
    cipher_msg = ''
    for symbor in plain_msg:
        if symbor in upper_alphabet:
            symbor_idx = upper_alphabet.find(symbor)
            cipher_msg = cipher_msg + upper_alphabet[(symbor_idx + key) % len(upper_alphabet)]
        elif symbor in lower_alphabet: # 소문자인 경우
            symbor_idx = lower_alphabet.find(symbor)
            cipher_msg = cipher_msg + lower_alphabet[(symbor_idx + key) % len(lower_alphabet)]
        else:
            cipher_msg = cipher_msg + symbor
    return cipher_msg

def Caeser_decrypt(key, cipher_msg):
    recovered_msg = ''
    for symbor in cipher_msg:
        if symbor in upper_alphabet:
            symbor_idx = upper_alphabet.find(symbor)
            recovered_msg = recovered_msg + upper_alphabet[(symbor_idx - key) % len(upper_alphabet)]
        elif symbor in lower_alphabet: # 소문자인 경우
            symbor_idx = lower_alphabet.find(symbor)
            recovered_msg = recovered_msg + lower_alphabet[(symbor_idx - key) % len(lower_alphabet)]
        else:
            recovered_msg = recovered_msg + symbor
    return recovered_msg

#--------------------------------------------------------------------

# test main함수
def main():
    plain_msg = "This is a plaintext message to be encrypted."
    key = 3
    cipher_msg = Caeser_encrypt(key, plain_msg)
    print('PLAINTEXT =', plain_msg)
    print('CIPHERTEXT =', cipher_msg)
    recovered_msg = Caeser_decrypt(key, cipher_msg)
    print('RECOVEREDTEXT =', recovered_msg)

# rnun main()
if __name__ == '__main__':
    main()

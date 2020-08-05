lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 시저암호 함수
def Caesar_encrypt(key, plain_msg):
    cipher_msg = ''
    for symbol in plain_msg:
        if symbol in upper_alphabet:
            symbol_idx = upper_alphabet.find(symbol)
            cipher_msg = cipher_msg + upper_alphabet[(symbol_idx + key) % len(upper_alphabet)]
        elif symbol in lower_alphabet: # 소문자인 경우
            symbol_idx = lower_alphabet.find(symbol)
            cipher_msg = cipher_msg + lower_alphabet[(symbol_idx + key) % len(lower_alphabet)]
        else:
            cipher_msg = cipher_msg + symbol
    return cipher_msg

def Caesar_decrypt(key, cipher_msg):
    recovered_msg = ''
    for symbol in cipher_msg:
        if symbol in upper_alphabet:
            symbol_idx = upper_alphabet.find(symbol)
            recovered_msg = recovered_msg + upper_alphabet[(symbol_idx - key) % len(upper_alphabet)]
        elif symbol in lower_alphabet: # 소문자인 경우
            symbol_idx = lower_alphabet.find(symbol)
            recovered_msg = recovered_msg + lower_alphabet[(symbol_idx - key) % len(lower_alphabet)]
        else:
            recovered_msg = recovered_msg + symbol
    return recovered_msg

#--------------------------------------------------------------------

# test main함수
def main():
    plain_msg = "This is a plaintext message to be encrypted."
    key = 10
    cipher_msg = Caesar_encrypt(key, plain_msg)
    print('PLAINTEXT =', plain_msg)
    print('CIPHERTEXT =', cipher_msg)
    recovered_msg = Caesar_decrypt(key, cipher_msg)
    print('RECOVEREDTEXT =', recovered_msg)

# rnun main()
if __name__ == '__main__':
    main()

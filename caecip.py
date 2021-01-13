alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
start ="yes"
while start =="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def encrypt(text,shift):
        text_list =[]
        cipher =[]
        caesar=[]
        for letter in text:
            text_list.append(letter)
        for i in text_list:
            shifted_pos =alphabet.index(i)
            shifted_pos +=shift
            caesar +=alphabet[shifted_pos]
            caesar_text =""
            for text in caesar:
                caesar_text+=text
            shifter_pos =0
        print(caesar_text)
    def decrypt(text,shift):
        text_list =[]
        cipher =[]
        for letter in text:
            text_list.append(letter)
        for i in text_list:
            shifted_pos =alphabet.index(i)
            shifted_pos -=shift
            cipher +=alphabet[shifted_pos]
            cipher_text =""
            for text in cipher:
                cipher_text +=text
            shifter_pos =0
        print(cipher_text)           
    if direction=="encode":
        encrypt(text,shift)
    elif direction =="decode":
        decrypt(text,shift)
    else:
        print("Invalid Input")
    start =input("Do you want to continue \p Type yes or no ")            

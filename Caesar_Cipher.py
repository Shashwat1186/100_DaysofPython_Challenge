
def encrypt(shift, text):
    encrypted = ""
    for char in text :
        if (ord(char)+shift) <= ord('z') and char.isalpha():
            encrypted += chr(ord(char)+shift)
        elif char.isalpha() :
            encrypted += chr(ord(char)+shift - 26)
        else :
            encrypted += char
    print(f"Here is the encoded result: {encrypted}")
def decrypt(shift, text):
    decrypted = ""
    for char in text :
        if (ord(char)-shift) >= ord('a') and char.isalpha():
            decrypted += chr(ord(char)-shift)
        elif char.isalpha() :
            decrypted += chr(ord(char)- shift + 26)
        else :
            decrypted += char
    print(f"Here is the decoded result: {decrypted}")
def caesar():
    print("""           
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝        
""")
    direction = input("Type 'encode ' to encrypt, 'decode' to decrypt: \n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%26
    if direction == "encode":
        encrypt(shift, text)
    elif direction == "decode":
        decrypt(shift, text)
    else :
        print("Incorrect input")
restart = True
caesar()
while restart :
    restart_input = input("Type 'yes' if you want to go again. Otherwise, type 'no\n").lower()
    if restart_input != "yes" :
        restart = False
        break
    caesar()
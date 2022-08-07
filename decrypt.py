with open ('msg.enc','r') as file:
    secret = file.read()

ct = bytes.fromhex(secret)
plaintext = ''

for i in ct:
    for j in range(33,126):
        if ((123 * j + 18) % 256) == i:
            plaintext += chr(j)
            break

print(plaintext)
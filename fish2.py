# genereert random sterke wachtwoorden
import random
import string
# dit script genereert een wachtwoord van 18 karakters
word_length = 18
# list van nummer, letters en speciale karakters
components = [string.ascii_letters, string.digits, "!@#$%&"]
# maakt ze in een list
chars = []
for clist in components:
  for item in clist:
    chars.append(item)
def generate_password():
  # slaat het wachtwoord op 
  password = []
  # kiest een random karakter en stop het in het wachtwoord
  for i in range(word_length):
    rchar = random.choice(chars)
    password.append(rchar)
  # return het wachtwoord
  return "".join(password)
# print het wachtwoord
print(generate_password())
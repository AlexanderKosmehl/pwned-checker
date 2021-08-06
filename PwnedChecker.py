from hashlib import sha1
import requests

input = input("Input String: ")
hash = sha1(input.encode("utf-8")).hexdigest().upper()
print(input + " : " + hash)

hash_responses = requests.get("https://api.pwnedpasswords.com/range/" + hash[:5]).text.split("\r\n")
for response in hash_responses:
    password_hash = response.split(":")
    if password_hash[0] == hash[5:]:
        print(input + " has been found " + password_hash[1] + " times!")


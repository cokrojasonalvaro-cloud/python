user = "Jason"
password = "APple123"
nama = input("\nWhat is your name?")
while nama != user:
    print("Intruder, report to the security center")
    nama = input("\nWhat is your name?")
pw = input("\nInput password!")
while password != pw:
    print("Wrong password!, try again!")
    pw = input("\nInput password!")
print("Access granted")
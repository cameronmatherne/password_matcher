

import hashlib

brokenFile = []
counter = 0
hashFile = open("MyShadow.txt", 'r')

for line in hashFile:
    y = line.split("$")
    brokenFile.append(y)
    counter += 1

passwords = open("rockyou_500Thousand.txt", 'r')
passList = []
salt = "RT"

dummyList = []

for line in passwords:
    dummyList.append(line.strip('\n'))
    password = salt+line.strip('\n')
    hashedPass = hashlib.md5(password.encode()).hexdigest()
    passList.append(hashedPass)

i = 0
listOfHashes = []
amtOfHashes = 0

# place only the hashes in their own list
while i <= (counter-1):
    temp = brokenFile[i][3]
    hashVal = temp[0:32]
    listOfHashes.append(hashVal)
    i += 1
    amtOfHashes += 1

success = 0
listLength = len(dummyList)

# create a blank list of 9 spaces to fill with the cracked passwords
crackedPasswords = []
for i in range(len(listOfHashes)):
    crackedPasswords.append(" ")

# iterate through every one of the 9 hashes
for i in range(len(listOfHashes)):
    j = 0

    # iterate through every one of the 500,000 hashes, for each of the 9 passwords
    for j in range(len(passList)):
        if listOfHashes[i] == passList[j]:
            success += 1
            crackedPasswords[i] = dummyList[j]
        j += 1

print()
print("Name     Salt               Hash                  Password")
print("----------------------------------------------------------------")
for i in range(len(brokenFile)):
    print(brokenFile[i][0].strip(':') + "   " + brokenFile[i][2] + "   "+ listOfHashes[i] + "   " + crackedPasswords[i])

failure = amtOfHashes - success
print()
print("Number of hashes tested: " + str(amtOfHashes))
print("Cracked passwords: " + str(success))
print("Unknown passwords: " + str(failure))

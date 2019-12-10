import csv, subprocess, platform, os, random, string

osys = platform.system()
running = True
meny = 0
chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars2 = "0123456789"
chars3 = "!#/()=#"
row = ""

def getFileLocation():
    working = False
    while working == False:
        print('Skriv sökvägen till CSV filen.')
        csvLocation = input("csv: ")
        if os.path.isfile(csvLocation) == False:
            print("Filen existerar inte, vänligen testa igen.")
        elif os.path.isfile(csvLocation) == True:
            print("Filen existerar.")
            working = True
            return csvLocation
        else:
            print("gg")

def passwordGen(length=8):
    password = ''
    password += random.choice(chars1).lower()
    password += random.choice(chars1)
    password += random.choice(chars2)
    password += random.choice(chars3)
    for c in range(length-4):
        cat = random.randint(1,4)
        if cat == 1:
            password += random.choice(chars1).lower()
        elif cat == 2:
            password += random.choice(chars1)
        elif cat == 3:
            password += random.choice(chars2)
        else:
            password += random.choice(chars3)
    password = ''.join(random.sample(password, len(password)))

    return password

def addUser(opsy = osys, returnedValue = 0):
    generatedPass = passwordGen()
    if opsy == 'Linux' or opsy == 'Linux2':
        cmd = f'sudo useradd --password "{generatedPass}" -c "{row["first_name"]} {row["last_name"]}" -m {row["first_name"]}.{row["last_name"]}' #useradd --password Lösenord -c “Shrek Ogre” -m S.Ogre
        print(cmd)
        returnedDelValue = subprocess.call(cmd, shell=True)
    else:
        cmd = f'New-ADUser -Name "{row["first_name"]} {row["last_name"]}" -GivenName "{row["first_name"]}" -Surname "{row["last_name"]}" -SamAccountName "{row["SamAccountName"]}" -AccountPassword (ConvertTo-SecureString "{generatedPass}" -AsPlainText -force) -passThru -ChangePasswordAtLogon $True'
        print(cmd)
        returnedValue = subprocess.call(['powershell', cmd])
    if returnedValue >= 1:
        print(f"Något gick fel.\nReturned Value: {returnedValue}")

def deleteUser(opsy= osys, returnedDelValue = 0):
    if opsy == 'Linux' or opsy == 'Linux2':
        print(delRow)
        print(f'Deleting {delRow["delete_user"]}')
        cmd = f'sudo userdel {delRow["delete_user"]}'
        print(cmd)
        returnedDelValue = subprocess.call(cmd, shell=True)
    else:
        cmd = f'Remove-ADUser -Identity {delRow["delete_user"]} -Confirm:$false'
        print(f'Tar bort konto {delRow["delete_user"]}')
        returnedDelValue = subprocess.call(['powershell', cmd])
    if returnedDelValue >= 1:
        print(f"Något gick fel.\nReturned Value: {returnedDelValue}")

print(f'Välkommen,\nDu kör operativsystemet {osys}.\nNotera: Denna kod fungerar endast för Linux och Windows.')

while running:
    if meny == 0: #Meny
        try:
            print("\nMeny\nLägg till användare [1]\nRadera användare [2]\nAvsluta [3]")
            meny = int(input("Val: "))
            if  meny == 0 or meny >= 4:
                print("Välj ett av de tillgänliga alternativen.")
                meny = 0
        except:
            print("Välj ett av de tillgänliga alternativen.")
            meny = 0
    if meny == 1: #Add User
        correctCSVLocation = getFileLocation()
        with open (correctCSVLocation, newline='') as csvFile:
            readFile = csv.DictReader(csvFile)
            for row in readFile:
                addUser()
        meny = 0

    if meny == 2: #Remove User
        correctCSVLocation = getFileLocation()
        with open (correctCSVLocation, newline='') as csvFileDel:
            delReadFile = csv.DictReader(csvFileDel)
            for delRow in delReadFile:
                deleteUser()
        meny = 0

    if meny == 3: #Exit
        running = False
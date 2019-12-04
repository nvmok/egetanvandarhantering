import os, csv, random, string

# def getFileLocation():
#     print('Skriv sökvägen till CSV filen.')
#     csvlocation = input("csv: ")
#     if os.path.isfile(csvlocation) == False:
#         print("Filen existerar inte, vänligen testa igen.")
#         getFileLocation()
#     elif os.path.isfile(csvlocation) == True:
#         print("Filen existerar.")
        
#         correctcsvlocation = csvlocation
#     else:
#         print("gg")
    
#     return correctcsvlocation

# # print(getFileLocation())
# with open ('MOCK_DATA.csv', newline='') as csvfile:
#     readFile = csv.DictReader(csvfile)
#     for row in readFile:
#         print(f'{row["first_name"]} with ID:  {row["id"]}')
chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars2 = "0123456789"
chars3 = "!#/()=#"
def passgen():
    password = ''
    password += random.choice(chars)
    password += random.choice(chars1)
    password += random.choice(chars2)
    password += random.choice(chars3)
    for c in range(4):
        cat = random.randint(1,4)
        if cat == 1:
            password += random.choice(chars)
        elif cat == 2:
            password += random.choice(chars1)
        elif cat == 3:
            password += random.choice(chars2)
        else:
            password += random.choice(chars3)
    return password

test = f'asdasd test {passgen()}   -123123'
print(test)

# var1 = 'jonas'
# var2 = 'är'
# var3 = 'fin'
# def test():
#     spremo = f'testet{var1}{var2}{var3}'
#     return spremo
# print(test())
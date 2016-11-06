#This will keep the database
birthdays = {}

#This will help you to find out and
#Update the database
while True:
    #This will take input from user
    print('Enter a name: (blank to quit)')

    #keep in mind input is casesensetive
    #so, 'Biddrup' and 'biddrup' is different from each other
    name = input()

    #If input '', then loop will be terminated
    if name == '':
        break
    #Will make each input as uppercase
    newname = name.upper()

    #This will check the name in databse or not
    if newname in birthdays:
        
        #If the input in databse, this will print
        print (birthdays[newname] + ' is the birthday of ' + newname)

    else:
        print('I do not hav ethe information for ' + newname)

        #This will take info under that name
        print('What is the birthday')
        baby = input()
        birthdays[newname] = baby

        #And, databse is updated now
        print('Birthdays database updated')

#Your complete birthday list
for k, v in birthdays.items():
    print(k + '  : ' + str(v))

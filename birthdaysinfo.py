#This wii keep the database
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
    #This will check the name in databse or not
    if name in birthdays:
        #If the input in databse, this will print
        print (birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not hav ethe information for ' + name)
        #This will take info under that name
        print('What is the birthday')
        baby = input()
        birthdays[name] = baby
        #And, databse is updated now
        print('Birthdays database updated')

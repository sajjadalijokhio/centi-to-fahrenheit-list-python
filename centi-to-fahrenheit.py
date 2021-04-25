#taking list as an input from user which containes centigrade temprature and using lambda function convert it into fahrenheit
try:
    centi = [] #defined empty list

    while True: #take input from user till the condition is true
        centi.append(eval(input("Enter temprature in degree centigrade: ")))

# if the input is not-integer, just print the list converted into fahrenheit
except:
    fahrenheit = list(map(lambda x: (x * 1.8) + 32, centi)) #convert each centi member into fahrenheit
    print()

    #using for loop printing the tempratures w.r.t conversion
    for i in range(0, len(centi)):
        print("{} degree centigrade is equal to {} fahrenheit.".format(centi[i], fahrenheit[i]))

Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]

city = input("enter a city name:")

if city in Australia:
    print("{} is in Australia".format(city))
elif city in UAE:
    print("{} is in UAE".format(city))
elif city in India:
    print("{} is in India".format(city))
else:
    print("{} is not in the list".format(city))

import requests


base_url="http://api.openweathermap.org/data/2.5/forecast?"
api_key = "12e30bac05ff8b5c1f2adf2be1c7be2b"
city =input("Entrer votre ville.")
units = "metric"
lang="fr"
url = base_url + "&lang=" + lang + "appid=" + api_key + "&q=" + city + "&units=" + units


response=requests.get(url).json()

temp0=response["list"][0]["main"]["temp"]
ressentie0=response["list"][0]["main"]["feels_like"]
dt0=response["list"][0]["dt_txt"]
wind0=response["list"][0]["wind"]["speed"]
description0=response["list"][0]["weather"][0]["description"]


temp10=response["list"][10]["main"]["temp"]
ressentie10=response["list"][10]["main"]["feels_like"]
dt10=response["list"][10]["dt_txt"]
wind10=response["list"][10]["wind"]["speed"]
description10=response["list"][10]["weather"][0]["description"]


temp15=response["list"][15]["main"]["temp"]
ressentie15=response["list"][15]["main"]["feels_like"]
dt15=response["list"][15]["dt_txt"]
wind15=response["list"][15]["wind"]["speed"]
description15=response["list"][15]["weather"][0]["description"]


temp20=response["list"][20]["main"]["temp"]
ressentie20=response["list"][20]["main"]["feels_like"]
dt20=response["list"][20]["dt_txt"]
wind20=response["list"][20]["wind"]["speed"]
description20=response["list"][20]["weather"][0]["description"]


temp30=response["list"][30]["main"]["temp"]
ressentie30=response["list"][30]["main"]["feels_like"]
dt30=response["list"][30]["dt_txt"]
wind30=response["list"][30]["wind"]["speed"]
description30=response["list"][30]["weather"][0]["description"]


temp39=response["list"][39]["main"]["temp"]
ressentie39=response["list"][39]["main"]["feels_like"]
dt39=response["list"][39]["dt_txt"]
wind39=response["list"][39]["wind"]["speed"]
description39=response["list"][39]["weather"][0]["description"]


print(dt0)
print("Temperature :",temp0, "C°")
print("Ressentie :", ressentie0, "C°")
print("La vitesse du vent est de :", wind0 ,"m/s")
print("Le temps est :",description0)

print(dt10)
print("Temperature :",temp10, "C°")
print("Ressentie :", ressentie10, "C°")
print("La vitesse du vent est de :", wind10, "m/s")
print("Le temps est :",description10)

print(dt15)
print("Temperature :",temp15, "C°")
print("Ressentie :", ressentie15, "C°")
print("La vitesse du vent est de :", wind15, "m/s")
print("Le temps est :",description15)

print(dt20)
print("Temperature :",temp20, "C°")
print("Ressentie :", ressentie20, "C°")
print("La vitesse du vent est de :", wind20, "m/s")
print("Le temps est :",description20)

print(dt30)
print("Temperature :",temp30, "C°")
print("Ressentie :", ressentie30, "C°")
print("La vitesse du vent est de :", wind30, "m/s")
print("Le temps est :",description30)

print(dt39)
print("Temperature :",temp39, "C°")
print("Ressentie :", ressentie39, "C°")
print("La vitesse du vent est de :", wind39, "m/s")
print("Le temps est :",description39)


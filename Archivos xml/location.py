from geopy.geocoders import Nominatim

answer = "si"
while answer == "si" or answer == "Si":
    geoLoc = Nominatim(user_agent="GetLoc")

    latitude = float(input("latitud: "))

    longitude = float(input("longitud: "))

    location_name = geoLoc.reverse(str(latitude)+","+str(longitude))

    print(location_name.address)

    answer = input("Desea realizar otra busqueda: ")
    if answer == "no" or answer == "No":
        break
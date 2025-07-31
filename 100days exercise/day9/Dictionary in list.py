from pprint import pprint

travel_log=[
    {
        "conutry":"France",
        "vists":2,
        "cites":["paris","Lille","Dijon"],
    },
    {
        "conutry":"India",
        "vists":1,
        "cites":["chennai","mumbai","Delhi"],
    }
]
# country = input("Enter the country to add")
# visited = int(input(f"Enter the {country} visited"))
# cites = [input(f"Enter the visited {country} cites")]
# print(country, visited, cites)

def add_new_country(country,visited,cites):
    new_log={}
    new_log = {
        "country": country,
        "visits": visited,
        "cites": cites
        }
    travel_log.append(new_log)


add_new_country("russia",2,"paris")
pprint(travel_log)
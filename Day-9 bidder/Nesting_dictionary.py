travel_log ={
    "frances": 
        {"cities": ["Paris", "Parcia"],
         "total_visits":5},
    "Germany": 
        {"cities":["Berlin","MagiPara"]},
    "Bangladesh": 
        ["Dhaka", "Ctg"]
}

travel_logs =[
    {
        "country":"France",
        "cities": ["Paris", "Parcia"],
        "total_visits":5
    },
    {
        "country":"Germany",
        "cities": ["Garis", "Garcia"],
        "total_visits":55
    }
]

def new_country(country_visited , cities_visited , total_visits):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = cities_visited
    new_country["total_visits"] = total_visits
    travel_logs.append(new_country)
new_country("Russia",["Mos","res"] , 5)
print(travel_logs)
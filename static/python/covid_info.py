url = "https://covid-193.p.rapidapi.com/statistics?country={}".format(arg)

headers = {
    "x-rapidapi-key": "f3c7547811mshb7e5680d6a29edcp1387fcjsncb14f156c54a",
    "x-rapidapi-host": "covid-193.p.rapidapi.com",
}

response = requests.request("GET", url, headers=headers)
new_dict = json.loads(response.text)

dict1 = new_dict["response"]

dict2 = dict1[0]
dict3 = dict2["cases"]
new_cases = dict3["new"]
active_cases = dict3["active"]
critical_cases = dict3["critical"]
recovered = dict3["recovered"]
cases_per1mill = dict3["1M_pop"]
total_cases = dict3["total"]

deaths = dict2["deaths"]

deaths_per1mill = deaths["1M_pop"]

new_deaths = deaths["new"]

total_deaths = deaths["total"]

day = dict2["day"]
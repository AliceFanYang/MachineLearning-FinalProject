import requests

api_key = "12c3359bc69c96ac440e62d8d521d5919f6eb842"

# could later read in a file of zip codes

#zips = [06110, 06107]

# first creaet a dictionary matching state name to state id
parameters = {"get": "NAME",
              "for": "state"}
r = requests.get("http://api.census.gov/data/2014/acs5?key=" + \
                 api_key, params = parameters)
#print(r.text)

states_json = r.json()[1:]
names_to_states_dict = dict(map(lambda x: [x[0], x[1]], r.json()[1:]))#{name: state for name, state in r.json[1:]}
#print(names_to_states_dict["Alabama"])

#The list taken in will assume the order is: [state_name, zip]
zips = [["Massachusetts", "01067"], ["Connecticut", "06110"]]

for name, zip_code in zips:
    parameters = {"get": "P0010001",#"DP04_0104M,DP05_0032E,DP03_0062E,DP04_0047E",
    #total pop | white pop | income, total householdsmedian household income
    #not sure what the difference between E and M is
                  "for": "zip code tabulation area:" + zip_code,
                  "in": "state:" + names_to_states_dict[name]}
    r = requests.get("http://api.census.gov/data/2010/sf1?key=" + \
                 api_key, params = parameters)

    print(r.text)

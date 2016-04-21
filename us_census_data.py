import requests

api_key = "12c3359bc69c96ac440e62d8d521d5919f6eb842"

# first creaet a dictionary matching state name to state id
#parameters = {"get": "NAME",
#              "for": "state"}
#r = requests.get("http://api.census.gov/data/2014/acs5?key=" + \
#                 api_key, params = parameters)
#states_json = r.json()[1:]
#names_to_states_dict = dict(map(lambda x: [x[0], x[1]], r.json()[1:]))

 
# The list taken in will assume the order is: [state_name, zip]
# could later read in a file of zip codes
zips = ["10029", "94040"]#[["Massachusetts", "01067"], ["Connecticut", "06110"]]

for zip_code in zips: #name, zip_code in zips:
    # pulled from the 2010 census data based on a tutorial Alice gave me from
    # the data visualization class that works
    #parameters2010 = {"get": "P0010001,P0080003",
    #              "for": "zip code tabulation area:" + zip_code,
    #              "in": "state:" + names_to_states_dict[name]}

    # total pop
    # white pop not hispanic not latino
    # average household size
    # median household income
    # median household income white homeowner
    # median household income asian homeowner
    # http://api.census.gov/data/2014/acs5/variables.html
    # http://api.census.gov/data/2014/acs5/examples.html
    #print(names_to_states_dict[name])
    parameters = {"get":"B01001_001E,B01001H_001E,B25010_001E,B19013_001E,B19013A_001E,B19013D_001E",
                  "for": "zip code tabulation area:" + zip_code}#,
                  #"in": "state:" + names_to_states_dict[name]}
				
    r = requests.get("http://api.census.gov/data/2014/acs5?key=" + \
                 api_key, params = parameters)

    print(r.text)

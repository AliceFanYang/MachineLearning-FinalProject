import os
import json
import csv

def extractStarBucksData():

	starbucksData = []

	currentPath = os.getcwd()
	path = currentPath + '/yelp_academic_dataset_business.json'

	with open(path, 'r') as data_file:  
		for line in data_file:
			businessData = json.loads(line)
			if businessData['name'] == 'Starbucks':
				starbucksData.append(businessData)

				# create starbucks info
				starbucksDict = {}
				#starbucksDict['starbucks_business_id'] = businessData['business_id'].encode('utf-8')
				print businessData['business_id'].encode('utf-8')
				#starbucksDict['avg_stars'] = businessData['stars']
				#starbucksDict['median_hours_open'] = businessData['business_id']

				if 'Wi-Fi' in businessData['attributes'].keys():
					if businessData['attributes']['Wi-Fi'] == "no":
						starbucksDict['has_wifi'] = 0
					else:
						starbucksDict['has_wifi'] = 1
				
				# starbucksDict['price_range'] = businessData['business_id']
				# starbucksDict['has_outdoor_seating'] = businessData['business_id']
				# starbucksDict['has_lot_parking'] = businessData['business_id']
				# starbucksDict['has_street_parking'] = businessData['business_id']
				# starbucksDict['has_credit_card_pay'] = businessData['business_id']
				# starbucksDict['is_wheelchair_accessible'] = businessData['business_id']

				#starbucksDict['num_similar_restaurants'] = businessData['business_id']


	convertStarbucksDataToCSV(starbucksData)


def convertStarbucksDataToCSV(starbucksData):
	# http://stackoverflow.com/questions/3086973/how-do-i-convert-this-list-of-dictionaries-to-a-csv-file-python
	keys = starbucksData[0].keys()
	with open('starbucks.csv', 'wb') as output_file:
		dict_writer = csv.DictWriter(output_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(starbucksData)


extractStarBucksData()
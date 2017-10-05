# Hypothesis_PoC
### Description
This is a python script that uses Hypothesis and Unittest that includes 2 simple tests. Tests will call google api reverse geocoding by providing lat and lng values. The first test will use Hypothesis to generate valid sets of coordinates and the second test will generate invalid sets of coordinates. Tests will make http API call and verify that the response for valid coordinates is  `OK` or `ZERO_RESULTS` and for invalid coordinates is `INVALID_REQUEST`. Hypothesis will randomly generate values for the given conditions in @given and will generate no more than max_examples values given in @settings. Hypothesis will also execute my custom examples provided in each @example. For positive scenarios script uses Hypothesis to generate coordinates in decimals between -90 and 90 for lat and -180 and 180 for lng. For negative scenarios it generates values outside of that range and will generate one of 3 scenarios - lat only invalid, lng only invalid, or both lat and lng invalid.

### Setup 

1. Install Python 2.7.14
2. Install additional libraries from the Command window with the following commands:
  1.  `pip install unittest`
  2.  ` pip install hypothesis`
3. Get google api key to use for Reverse Geocoding (Address Lookup) https://developers.google.com/maps/documentation/javascript/get-api-key
4. Download and edit python script by inserting your API key instead of `API_KEY_GOES_HERE`

### Execution
To run the script, open command window and navigate to the location of the python script. Then run the following command: 
`python ./test.py`

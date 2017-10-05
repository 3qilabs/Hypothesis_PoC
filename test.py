from hypothesis import given, settings, example
from hypothesis.strategies import decimals, one_of, tuples

import unittest
import requests
import json
import hypothesis


class TestGeocode(unittest.TestCase):
    api_key = "API_KEY_GOES_HERE"
    #this test will generate lat and lng some random integers or decimals that are valid and send a request
    # the response should be OK or ZERO_RESULTS if there is no address for the location
    @settings(max_examples=20, deadline=5000, timeout=hypothesis.unlimited)
    @given(decimals(min_value=-90, max_value=90) ,decimals(min_value=-180, max_value=180))
    @example(90,180)
    @example(-90,180)
    @example(90,-180)
    @example(-90,-180)
    def test_positive_flow(self, lat, lng):
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," +str(lng) + "&key=" + TestGeocode.api_key
        print "\nlat=" + str(lat) + "\nlng=" +str(lng) 
        print url
        r = requests.get(url) #got response into r
        b = json.loads(r.content) #parsed response as dictionary
        self.assertTrue((b['status'] == 'ZERO_RESULTS') or (b['status'] =='OK'), "Status is not OK or ZERO_RESULTS, status is: " + b['status'] + "\n using url: " + url  )
        print b['status']

    #this test will generate lat and lng. some random integers or decimals that are not valid  and send a request
    #the response should be INVALID_REQUEST
    @settings(max_examples=20, deadline=5000, timeout=hypothesis.unlimited)
    @given(one_of(tuples(one_of(decimals(allow_nan=False, allow_infinity=False,min_value=91),decimals(allow_nan=False, allow_infinity=False,max_value=-91)) ,one_of(decimals(allow_nan=False, allow_infinity=False,min_value=181),decimals(allow_nan=False, allow_infinity=False,max_value=-181))),tuples(decimals(min_value=-90, max_value=90),one_of(decimals(allow_nan=False, allow_infinity=False,min_value=181),decimals(allow_nan=False, allow_infinity=False,max_value=-181))),tuples(one_of(decimals(allow_nan=False, allow_infinity=False,min_value=91),decimals(allow_nan=False, allow_infinity=False,max_value=-91)) ,decimals(min_value=-180, max_value=180))))
    @example((90.00000001,180))
    @example((-90.0000001,180))
    @example((90,-180.00000001))
    @example((-90,-180.00000001))
    @example(("",180))
    @example((90,""))
    def test_negative_flow(self, arg):
        lat = arg[0]
        lng = arg[1]
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," +str(lng) + "&key=" + TestGeocode.api_key
        print "\nlat=" + str(lat) + "\nlng=" +str(lng) 
        print url
        r = requests.get(url) #got response into r
        b = json.loads(r.content) #parsed response as dictionary
        self.assertTrue((b['status'] =='INVALID_REQUEST'), "Status is not INVALID_REQUEST, status is: " + b['status'] + "\n using url: " + url  )
        print b['status']
        
if __name__ == '__main__':
    unittest.main()
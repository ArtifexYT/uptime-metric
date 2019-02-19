  checking for new data...
import httplib, urllib, time, random
 
# the following 4 are the actual values that pertain to your account and this specific metric
api_key = '32c83590-8198-47f6-990d-c4396f3abd9a'
page_id = 'djp8vk59r4vq'
metric_id = 'gc80d08g3ylx'
api_base = 'api.statuspage.io'
 
# need 1 data point every 5 minutes
# submit random data for the whole day
total_points = (60 / 5 * 24)
for i in range(total_points):
  ts = int(time.time()) - (i * 5 * 60)
  value = random.randint(0, 99)
  params = urllib.urlencode({'data[timestamp]': ts, 'data[value]': value})
  headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "OAuth " + api_key}
 
  conn = httplib.HTTPSConnection(api_base)
  conn.request("POST", "/v1/pages/" + page_id + "/metrics/" + metric_id + "/data.json", params, headers)
  response = conn.getresponse()
 
  print "Submitted point " + str(i + 1) + " of " + str(total_points)
  time.sleep(1)

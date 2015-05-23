import urllib2, sys
import rauth
import ConfigParser

inifile = ConfigParser.ConfigParser()
inifile.read("config/secrets.ini")

def search_params(term, location):
  params = {}
  params["term"] = term
  params["location"] = location
  params["limit"] = "10"
  return params

def get_restaurants(params):
  consumer_key = inifile.get("yelp", "consumer_key")
  consumer_secret = inifile.get("yelp", "consumer_secret")
  access_token = inifile.get("yelp", "access_token")
  access_token_secret = inifile.get("yelp", "access_token_secret")

  session = rauth.OAuth1Session(
      consumer_key = consumer_key,
      consumer_secret = consumer_secret,
      access_token = access_token,
      access_token_secret = access_token_secret)

  request = session.get("http://api.yelp.com/v2/search", params=params)

  data = request.json()
  session.close()

  return data

def main():
  term = sys.argv[1]
  location = sys.argv[2]
  params = search_params(term, location)
  response = get_restaurants(params)
  restaurants_info = response["businesses"]
  restaurant_names = []
  for restaurant_info in restaurants_info:
    restaurant_name = restaurant_info["name"]
    print restaurant_name

if __name__ == "__main__":
  main()

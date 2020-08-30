import urllib.request
import json
import configip

def Lookup(ip):

	response = urllib.request.Request("http://v2.api.iphub.info/ip/{}".format(ip))
	response.add_header("X-Key", configip.API_KEY)

	try:
		response = json.loads(urllib.request.urlopen(response).read().decode())
	except:
		return False # In the case of an error, pass all IP's to avoid blocking innocents

	return response.get("block") # Defaults to None if failed to get block value

import urllib2
import urllib
import json
import subprocess

def getRequest():
	url = raw_input('insert here : ')
	urlData = urllib2.urlopen(url)
	loadJson = json.load(urlData)

	prettyJson = json.dumps(loadJson, indent=4)

	pbcopy(prettyJson)

def postRequest():
	url = 'http://103.43.44.111/user/register-user'
	params = {'key': 'value'}

	data = urllib.urlencode(params)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	
	jsonResponse = json.load(response)
	jsonDump = json.dumps(jsonResponse, indent=4)

	print jsonDump

def pbcopy(data):
	p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
	p.stdin.write(data)
	p.stdin.close()
	retcode = p.wait()
	return retcode

def main():
	getRequest()

main()
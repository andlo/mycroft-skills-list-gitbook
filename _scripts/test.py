
import urllib3

def get_api(url):
    USER='andlo'
    API_TOKEN='ef77171c9449656ca7bfb3bfe082ef2238e5b102'
    GIT_API_URL='https://api.github.com'
    try:
        request = urllib3.Request(GIT_API_URL + url)
        base64string = base64.encodestring('%s/token:%s' % (USER, API_TOKEN)).replace('\n', '')
        request.add_header("Authorization", "Token %s" % base64string)
        result = urllib2.urlopen(request)
        result.close()
    except:
        print('Failed to get api request') 
    

print(get_api("/search/repositories?q='Mycroft'in:readme+'Mycroft'in:description+'Mycroft'in:name+archived:false"))

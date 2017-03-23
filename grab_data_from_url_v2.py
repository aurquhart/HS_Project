

import urllib.parse
import urllib.request

url = 'https://trackobot.com/profile/history.json?username=still-gnoll-6604&token=ekojyJx_c68FJpkVfavn'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data, headers)

print(req)


#response = urllib.request.urlopen(req)
#the_page = response.read()


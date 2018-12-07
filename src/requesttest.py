from urllib import request
import json
import ssl

def test():
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        file = open('../support/key.key', 'r')
        key = file.read()
        file.close()
    except:
        assert False

    url = 'https://www.googleapis.com/youtube/v3/search?part=id&q=jfla&type=video&key={0}'.format(key)
    req = request.urlopen(url)

    assert req.getcode() == 200

    read = req.read()
    result = json.loads(read)
    for temp in result['items']:
        assert '' != temp['id']['videoId']
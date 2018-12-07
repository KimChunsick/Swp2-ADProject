from urllib import request
import json
import ssl

def main():
    context = ssl._create_unverified_context()
    try:
        file = open("../support/key.key", 'r')
        key = file.read()
        file.close()
    except:
        assert False

    test(context, key)

def test(context, key):
    url = "https://www.googleapis.com/youtube/v3/search?part=id&q=jfla&type=video&key={0}".format(key)
    req = request.urlopen(url, context=context)

    assert req.getcode() == 200

    read = req.read()
    result = json.loads(read)
    for temp in result["items"]:
        print(temp["id"]["videoId"])

if __name__ == "__main__":
    main()
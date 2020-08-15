def getMap(mapLocation):
    import requests
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config.get('GOOGLE', 'STATICMAPKEY')
    url = "https://maps.googleapis.com/maps/api/staticmap?"

    center = str(mapLocation)
    zoom = 9

    r = requests.get(url + "center=" + center + "&zoom=" +
                    str(zoom) + "&size=800x800 &key=" +
                                api_key + "&sensor=false")

    # wb mode is stand for write binary mode
    f = open('map.png', 'wb')

    # r.content gives content,
    # in this case gives image
    f.write(r.content)

    # close method of file object
    # save and close the file
    f.close()
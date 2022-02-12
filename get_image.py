import requests
from PIL import Image, ImageQt
from io import BytesIO


def get_image(ll, spn, map_type="map", add_params=None):
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": map_type
    }
    if isinstance(add_params, dict):
        map_params.update(add_params)
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    image = Image.open(BytesIO(response.content))
    file_name = 'map.png'
    image.save(file_name)
    #image_qt = ImageQt.ImageQt(image)
    return file_name


if __name__ == '__main__':
    a = get_image('37.620070,55.753630', '0.002,0.002')
    a.show()
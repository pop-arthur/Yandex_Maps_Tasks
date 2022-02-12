import requests
from PIL import Image
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
    return Image.open(BytesIO(response.content)).show()


if __name__ == '__main__':
    a = get_image('37.620070,55.753630', '0.002,0.002')
    a.show()
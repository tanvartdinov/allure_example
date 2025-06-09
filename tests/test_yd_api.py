import requests

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

# def test_create_folder_success(headers, temp_folder):
#     response = requests.put(BASE_URL, headers=headers, params={'path': f'disk:/{temp_folder}'})
#     assert response.status_code in [201, 409]
#
#
# def test_create_existing_folder(headers, create_and_cleanup_folder):
#     folder = create_and_cleanup_folder
#     response = requests.put(BASE_URL, headers=headers, params={'path': f'disk:/{folder}'})
#     assert response.status_code == 409
#
#
# def test_create_folder_invalid_path(headers):
#     response = requests.put(BASE_URL, headers=headers, params={'path': 'disk://///'})
#     assert response.status_code == 404
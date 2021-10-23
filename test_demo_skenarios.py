import requests
import json
BASE_URL = 'https://api.skenarios.com/api/v1/portfolio/4116/building'
token = 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MzQ1NTE2OTksImp0aSI6ImhTZ2VQMTdMeW51aGg0RlNMb3NLY0dZWEZWZUZyM0ZlIiwiYXVkIjoiYXBpLnNrZW5hcmlvcy5jb20iLCJpc3MiOiJza2VuYXJpb3MuY29tIiwic3ViIjoiaWxqYSt0ZXN0LWVuZ2luZWVyQHNrZW5hcmlvbGFicy5jb20iLCJ1c2VyTmFtZSI6ImlsamErdGVzdC1lbmdpbmVlckBza2VuYXJpb2xhYnMuY29tIiwiZW1haWwiOiJpbGphK3Rlc3QtZW5naW5lZXJAc2tlbmFyaW9sYWJzLmNvbSIsInNrZW5hcmlvc1VzZXJJZCI6Mjg3NCwib3JnYW5pemF0aW9uSWQiOjE0NTd9.OrI_7MMx0q5tBGwKJPyCablDDi-B0u5P0dpdSO6w3aDdudmoqnWZCty5WTSqFsZd7mzH0un8zKSaoKC-JRcs0Q'
building_id = 'buildingId'
header = {
    "Authorization": "Bearer {}".format(token),
    "Content-Type": "application/json",
    }
header_invalid_token = {
    "Authorization": "Bearer {}".format('Invalid_Token'),
    "Content-Type": "application/json",
    }

debug = False


def test_log(message):
    if debug:
        print(message)


def test_success_message(msg):   # This method will excute when the testcase sucess
    print('\n******  '+msg + '   ******' + '\n' + 'TEST PASSED --- OK\n' + '************'  )


def test_failure_message(msg):   # This method will excute when the testcase fail
    print( '\n******  '+msg + '   ******')
    print('TEST FAILED --- NOK')


def test_get_buildings_with_valid_token():
    test_case_name = "Get building with valid token"
    response= requests.get(BASE_URL, headers=header)
    response_json=response.json()
    test_log(response.status_code)
    test_log(response_json)
    if response.status_code == 200:
        test_success_message(test_case_name)
    else:
        test_failure_message(test_case_name)


def test_get_buildings_with_invalid_token():
    test_case_name= "Get building with invalid token"
    response= requests.get(BASE_URL, headers=header_invalid_token)
    response_json=response.json()
    test_log(response.status_code)
    test_log(response_json)
    if response.status_code == 401:
        test_success_message(test_case_name)
    else:
        test_failure_message(test_case_name)


def test_get_buildings_without_token():
    test_case_name= "Get building without token"
    response= requests.get(BASE_URL)
    response_json=response.json()
    test_log(response.status_code)
    test_log(response_json)
    if response.status_code == 401:
        test_success_message(test_case_name)
    else:
        test_failure_message(test_case_name)


def test_create_building_with_new_id():
    test_case_name="Create building with new ID"
    with open('json_data.json', "r") as f:
        data = json.loads(f.read())
        response_create = requests.post(BASE_URL, headers=header, json=data)
        test_log(response_create.status_code)
        test_log(response_create.json())
        if response_create.status_code == 201:
            test_success_message(test_case_name)
        else:
            test_failure_message(test_case_name)


def test_create_building_with_existing_id():
    test_case_name="Create building with existing ID"
    with open('json_data.json', "r") as f:
        data = json.loads(f.read())
        response_create = requests.post(BASE_URL, headers=header, json=data)
        test_log(response_create.status_code)
        test_log(response_create.json())
        if response_create.status_code == 400:
            test_success_message(test_case_name)
        else:
            test_failure_message(test_case_name)


def test_create_building_with_invalid_token():
    test_case_name="Create building with invalid token"
    with open('json_data.json', "r") as f:
        data = json.loads(f.read())
        response_create = requests.post(BASE_URL, headers=header_invalid_token, json=data)
        test_log(response_create.status_code)
        test_log(response_create.json())
        if response_create.status_code == 401:
            test_success_message(test_case_name)
        else:
            test_failure_message(test_case_name)


def test_create_building_without_token():
    test_case_name="Create building without token"
    with open('json_data.json', "r") as f:
        data = json.loads(f.read())
        response_create = requests.post(BASE_URL, json=data)
        test_log(response_create.status_code)
        test_log(response_create.json())
        if response_create.status_code == 401:
            test_success_message(test_case_name)
        else:
            test_failure_message(test_case_name)


def test_delete_building_with_valid_id():
    test_case_name = "Delete building with valid ID"
    response = requests.get(url=BASE_URL, headers=header)
    json_response= response.json()
    response_buildingid= json_response['models'][0]['buildingId']
    test_log(json_response)
    test_log(json_response['models'][0]['buildingId'])
    response_delete = requests.delete(url=BASE_URL+'/'+response_buildingid, headers=header)
    test_log(response_delete.status_code)
    if response_delete.status_code == 204:
        test_success_message(test_case_name)
    else:
        test_failure_message(test_case_name)


def test_delete_building_with_invalid_id():
    test_case_name="Delete building with invalid ID"
    response = requests.get(url=BASE_URL, headers=header)
    json_response= response.json()
    response_buildingid= json_response['models'][0]['buildingId']
    test_log(json_response)
    test_log(json_response['models'][0]['buildingId'])
    response_delete = requests.delete(url=BASE_URL+'/'+"InvalidBuildingID", headers=header)
    test_log(response_delete.status_code)
    if response_delete.status_code == 404:
        test_success_message(test_case_name)
    else:
        test_failure_message(test_case_name)


def test_delete_building_without_token():
    test_case_name = "Delete building without token"
    response = requests.get(url=BASE_URL, headers=header)
    json_response= response.json()
    response_building_id= json_response['models'][0]['buildingId']
    response_delete = requests.delete(url=BASE_URL+'/'+"InvalidBuildingID")
    test_log(response_delete.status_code)
    test_log(response.status_code)
    test_log(response_building_id)
    if response_delete.status_code == 401:
        test_success_message(test_case_name)
    else:
        test_failure_message(test_case_name)


def test_delete_building_with_invalid_token():
    test_case_name = "Delete building with invalid Token"
    response = requests.get(url=BASE_URL, headers=header_invalid_token)
    test_log(response.status_code)
    if response.status_code == 401:
        test_success_message(test_case_name)
    else:
        test_failure_message(test_case_name)


test_get_buildings_with_valid_token()
test_get_buildings_with_invalid_token()
test_get_buildings_without_token()
test_create_building_with_new_id()
test_create_building_with_existing_id()
test_create_building_with_invalid_token()
test_create_building_without_token()
test_delete_building_with_valid_id()
test_delete_building_with_invalid_id()
test_delete_building_with_invalid_token()
test_delete_building_without_token()

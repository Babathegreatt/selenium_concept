import requests
from assertpy import assert_that
import json

class TestPetStoreAPI:
    END_POINT = "https://petstore.swagger.io/v2"


    # def generate_token(self):
    #         header_dic = {"api-token": "application/json"}
    #         response = requests.post(url=, headers=header_dic)
    #         return response.json()["token"]


    def test_add_valid_pet(self):
        resource ="/pet"
        json_body = json.load(open("../test_data/add_pet.json"))
        header_dic = {"Content-Type":"application/json"}
        response = requests.post(url=TestPetStoreAPI.END_POINT + resource,headers=header_dic,json=json_body)
        print(response.json())
        assert_that(200).is_equal_to(response.status_code)
        assert_that(json_body["id"]).is_equal_to(response.json()["id"])

    def test_update_valid_pet(self):
        resource = "/pet"
        json_body = json.load(open("../test_data/add_pet.json"))
        header_dic = {"Content-Type": "application/json"}
        response = requests.put(url=TestPetStoreAPI.END_POINT + resource,headers=header_dic, json=json_body)
        print(response.json())
        assert_that(200).is_equal_to(response.status_code)
        assert_that(json_body["name"]).is_equal_to(response.json()["name"])


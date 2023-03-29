import requests
from assertpy import assert_that


class TestPetStoreAPI:
    END_POINT = "https://petstore.swagger.io/v2"


    """Request to fetch valid pet ID"""
    def test_find_valid_pet_by_id(self):
        pet_id = 5001
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(200).is_equal_to(response.status_code)
        assert_that("cat-901").is_equal_to(response.json()["category"]["name"])
        print(response.json())
        print(response.status_code)

    """Get-Query parameter - to fetch """
    def test_find_pet_by_valid_status(self):
        status = "sold"
        resource = f"/pet/findByStatus?status={status}"
        response = requests.get(TestPetStoreAPI.END_POINT+resource)
        # print(response.status_code)
        # print(response.json())
        # print(len(response.json()))
        # print(response.json()[0])

        #Validating all pet details received have status - sold
        for i in range(0,len(response.json())):
            print(response.json()[i]["id"])
            print(response.json()[i]["status"])
            assert_that(status).is_equal_to(response.json()[i]["status"])



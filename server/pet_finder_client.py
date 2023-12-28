from typing import  Dict, Any, List
import requests

from models.animal import Animal


class PetFinderClient:
    def __init__(self, client_id: str, client_secret: str):
        self.base_url = "https://api.petfinder.com/v2"
        self.headers = {
            "reset" : "Bearer ",
            "Authorization": "Bearer "
        }
        self.client_id = client_id
        self.client_secret = client_secret

    def _get_access_token(self):
        # will be accessed every time needing new data
        response = requests.post(
            self.base_url + "/oauth2/token",
            data={"grant_type": "client_credentials"},
            auth=(self.client_id, self.client_secret),
        )
        return response.json()["access_token"]
    
    def get_animal_types(self) -> List[str]:
        # return the avaliable animal types on petfinder
        try:
            self.headers["Authorization"] = self.headers["reset"] + self._get_access_token()
            response = requests.get(
                url=self.base_url + "/types",
                headers=self.headers,
            ).json()["types"]
            types = [item["name"] for item in response]
            return types
        except Exception as e:
            raise Exception(f"failed to get animal types due to error: {e}")
    
    def get_animals(self, type: str, page: int) -> tuple[Dict[str, Any], list[Animal]]:
        try:
            self.headers["Authorization"] = self.headers["reset"] + self._get_access_token()
            response = requests.get(
                url=self.base_url + "/animals",
                headers=self.headers,
                params={
                    "type": type,
                    "page": page,
                }
            ).json()
            animals = [
                Animal(**{key: val for key,val in animal.items() if key != 'description'} | {'description': animal['description'] if animal['description'] else "no description"})
                for animal in response["animals"]
            ]
            # works: this uses dictionary unpacking
                # print({**{key: val for key, val in animal.items() if key != 'description'},'description': animal['description'] if animal['description'] else 'what?'})

            # not work: the key 'description' exists in animal. Even though the value is None, it is still valid. Therefore, the substitute value "what!!" is never inputed
                # print({**{key: val for key, val in animal.items() if key != 'description'},'description': animal.get('description','what!!')})
                # print({key: val for key, val in animal.items() if key != 'description'} | {'description': animal.get('description','what!!')})


            return (response['pagination'], animals)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get animals by type {type}, error: {e}")

    
    def get_animal(self, type: str, page: int, id: int) -> Animal:
        # return the animal with the specific id
        try:
            self.headers["Authorization"] = self.headers["reset"] + self._get_access_token()
            response = requests.get(
                url=self.base_url + "/animals/"+str(id),
                headers=self.headers,
            ).json()['animal']
            # return Animal(**response)
            return Animal(**{key: val for key,val in response.items() if key != 'description'} | {'description': response['description'] if response['description'] else "no description"})
            # return Animal(**{**{key: val for key, val in response.items() if key != 'description'},'description': response['description'] if response['description'] else 'no description'})
            
        except Exception as e:
            raise Exception(f"Failed to get animal with id {id}. Error: {e}")


# should be saved in a secure place

# client_id = "Umcqw6TWPCwhteNyMqJNLJEeasrecM3RcTHZRJQWQjwBfzgzl9"
# client_secret = "lw1oCR5FgETXi6y2YEzmj2WZ1TVE6sGkIdy6E0o8"

# pet_finder_client = PetFinderClient(client_id=client_id, client_secret=client_secret)
# animals = pet_finder_client.get_animals(type="dog", page=2)


# class Animal:
#     name: str
#     breed: str
#     type: str

# List[Animal]

# json.loads()
# json.dumps()

# 1. python as backend service
# a. create pet finder client
# b. create some api endpoints using fast api
# c. python virtual environment
# 2. JS as frontend
# a. services.js contains all the backend calls -> call backend service
# fetch(
# "https://jsonplaceholder.typicode.com/users")
#             .then((res) => res.json())
#             .then((json) => {
#                 this.setState({
#                     items: json,
#                     DataisLoaded: true
#                 });
#             })
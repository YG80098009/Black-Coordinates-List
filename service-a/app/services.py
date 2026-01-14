import requests

class Routs:
    
    @staticmethod
    def cleaning_data(dict_json):
        dict = {"query": dict_json["query"],
            "lat": dict_json["lat"],
            "lon": dict_json["lon"]}
        return dict
    


    @staticmethod
    def send_to_server_b(clean_data):
        respons = requests.post(f"http://localhost:8001/store/{clean_data}")
        return respons
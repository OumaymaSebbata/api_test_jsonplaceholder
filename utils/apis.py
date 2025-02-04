import requests



class APIs:
    BASE_URL="https://jsonplaceholder.typicode.com"
    
    def apis(method,endpoint,json_body):
        url=f"{APIs.BASE_URL}/{endpoint}"
        headers = {"Accept":"application/json"}
        response = requests.request(method=method,url=url,params=None,headers=headers,auth=None,json=json_body)
        

        return response


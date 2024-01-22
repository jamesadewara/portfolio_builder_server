from django.http import JsonResponse
from django.views import View
import requests

class RecommendationSystemView(View):
    def get(self, request, *args, **kwargs):
      
        # Your logic to fetch data or process here
        data = {'message': 'Hello, this is your API!'}
        return JsonResponse(data)

# url = 'http://your-django-server.com/api/endpoint'

# # Make a GET request
# response = requests.get(url)

# # Check the status code
# if response.status_code == 200:
#     # Successful request, handle the response
#     data = response.json()  # Assuming the response is in JSON format
#     print(data)
# else:
#     # Handle the error
#     print(f"Error: {response.status_code}")
    


# url = 'http://your-django-server.com/api/endpoint'
# data = {'key': 'value'}
# headers = {'Content-Type': 'application/json'}

# response = requests.post(url, json=data, headers=headers)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}")


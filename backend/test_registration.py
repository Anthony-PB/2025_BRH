# test_registration.py
import requests
import json

def test_registration():
    url = "http://127.0.0.1:8000/api/users/register/"
    data = {
        "email": "newuser@example.com",
        "password": "testpass123",
        "password_confirm": "testpass123", 
        "first_name": "New",
        "last_name": "User",
        "display_name": "NewUser"
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201:
            print("Registration successful!")
            token = response.json().get('token')
            print(f"Auth Token: {token}")
        else:
            print("Registration failed!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_registration()
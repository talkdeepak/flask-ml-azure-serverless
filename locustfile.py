from locust import HttpUser, between, task
import random
import json

class AppUser(HttpUser):
    wait_time = between(5, 15)
    
    host = "https://flask-ml-azure-webapp.azurewebsites.net:443"

    @task
    def index(self):
        self.client.get("/")

    @task
    def prediction(self):

        """
        """
        payload={
            "CHAS": {"0": random.randint(0,1)},
            "RM":{"0": random.uniform(1.0, 10.0)},
            "TAX":{"0": random.uniform(50.0, 1000.0)},
            "PTRATIO":{"0": random.uniform(3.0, 50.0)},
            "B":{"0": random.uniform(5.0, 1000.0)},
            "LSTAT":{"0": random.uniform(1.0, 9.5)}
        }

        response = self.client.post("/predict", json=payload)
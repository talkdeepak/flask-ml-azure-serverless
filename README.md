
[![Python application test with Github Actions](https://github.com/talkdeepak/UdacityAzureDevOps2/actions/workflows/main.yml/badge.svg)](https://github.com/talkdeepak/UdacityAzureDevOps2/actions/workflows/main.yml)

# OverView
This project is Python Flask application hosted in Azure DevOps which can predict housing price in a particular area. it depends upon Machine Learning model SKLearn.

## Environment

Python 3.7

# Architecture

![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/f5addef5-2a63-4a29-af17-45ea3d750a5e)

https://app.diagrams.net/#G1R9vl7V4p922r-4v5t5xgKWXc1UBgJkuu![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/485bf699-2b5d-4c64-aa08-a65ca8cfcf3b)

## Project planning 

* A Trello board is created for all the task with different swimlanes. We can track the progress with this board.
* Follow this link to Trello Board : https://trello.com/b/0P1zCeYx/sprint1-duacitypoject2![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/f043c582-cde7-4f51-b2d9-63e4447fa1d2)
* Also for spreadheetplanning we are using google sheets for this project  : https://docs.google.com/spreadsheets/d/1zC-Li3UpKbEmmkAHVjaiMbXY2Eg50ugrBOtR9uOl3B4/edit#gid=1348135932![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/995c7ee4-eb17-4c18-a25b-a9a62bef8292)

## Requirement and dependencies
* Azure Account ( I have used free account)
* SSH key from GitHub

## How to Get Started
* Go to Azure Cloud shell from (top right corner after login to portal.azure.com)
* Create SSH keys for accessing the GitHub repo
  ```
  ssh -keygen -t rsa
  ```
 * Copy the public key file : rsa.pub file
* Add the public key content to your Github account in Settings --> SSH key) . This allows to open or clone the repo from cloud shell without entering the credentials.
* now Clone the repo in cloud shell

  ```
  git clone git@github.com:talkdeepak/UdacityAzureDevOps2.git

  ```
  ## Create the python virtual environment using following commands

  ```
  python3 -m venv ~/.devops
  source ~/.devops/bin/activate

  ```

  
  
  



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

  ## Run the make file

  ```
  make all

  ```

  * This will run the the test against your code similar to the screenshot below :

   ![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/03d4d58d-b136-4a60-820e-1c5b23a2f871)

  # How to set up Git Hub Actions

  * Go to the GitHub and login your account
  * Go to Actions in the Code Repo -> New Workflow -> And Set up the workflow
  * I used this following code for the workflow file

      ```

      name: Python application test with Github Actions

      on: [push]
      
      jobs:
        build:
      
          runs-on: ubuntu-latest
      
          steps:
          - uses: actions/checkout@v2
          - name: Set up Python 3.8
            uses: actions/setup-python@v1
            with:
              python-version: 3.8
          - name: Install dependencies
            run: |
              make install
          - name: Lint with pylint
            run: |
              make lint
          - name: Test with pytest
            run: |
              make test

      ```
* Commit the changes in the yaml file
> This would basically trigger the build job as specified in the worflow file above
> Starts the build job and install the dependencies
> and then Lint with pylint
### Output would look similar to this below 

![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/094fc1c5-fb0b-4361-bd62-019630133676)


## Configure the Azure pipeline

* This could be different for different type of Azure subscription
* I used the free subsction account from Azure but that has limitation , that It can not run the parallel jobs that means in this free account you can not run the build agent and instead have to build you own.
* If you want to try using the Azure provided agent when you build the pipeline in azure DevOps ( Free subscription) it throws error and asks you to request microsoft to open it for your free account, which generally is done in 2-3 days.
* I choose to build my self hosted agent (VM or agent server myself) and then Build the pipeline.

### Basic requirement :   
Make sure that you have a WebApp already registered / created for you in azure portal, if not use the following step. Note : Web App name should be unique for you

```
az webapp up --name flask-ml-azure-webapp --resource-group DeepakRG --sku B1 --logs --runtime "PYTHON:3.9"

```
## Seting up the server takes some steps which is basically 

1. Set up the DevOps Organisation
2. In Organiszation Settings  : Allow public project
3. Create Service Connection
 ![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/daeada3a-c331-4e8e-88d4-0f8ff0cbc8d6)

4. Add a Agent Pool

   ![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/2df471b0-ca79-4591-a500-d455baa83f3f)

5. Create Agent Pool

![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/af7443a8-6f14-4c21-82e0-ca6b7a7b125a)

6. Create a VM and Configure it ( Follow official steps from Microsoft)on Azure and associate with Agent pool we create in last step.
7. ![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/4c3c0eaf-34dd-4722-bb84-b02239243d0b)

## Running the Deploy pipeline after configure 

* When you make any change in the code in your repo in GitHub and Commit it.
* it will trigger the build and deploy. this depends upon the steps mentioned in the azure.pipelines.yml file

* Successful Build looks like this in the Azure DevOps 

![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/a171617d-9a70-4791-aafc-6e6abd579a9b)

* On Successful deploy Application can checked in the browser :
  ![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/5c0cd607-3251-45f8-9a8b-0e2f8b034010)

  
* Testing the Application deployed
  > SSH to the WebApp in my case : it is https://flask-ml-azure-webapp.azurewebsites.net/  on potal
  > Run the command make_predict_azure_app
  > Result is as shown below . The out json
  > ![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/98c42e84-1300-4b1f-891a-7ad40e57bf65)

### Logs for the app can be seen here 
https://flask-ml-azure-webapp.scm.azurewebsites.net/api/logs/docker![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/240781cb-899e-4003-b716-6dd3c8e7311a)

* or it can be streamed with this command

  ```
  az webapp log tail -n flask-ml-azure-serverless

  ``` 
  ![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/0466af6a-db18-48c2-8d30-c00eaf75f279)

### Load Testing with Locust

* It is way to load test your application by smilating the hitting of endpoint
* I did this test from my local machine by hitting the end point using locust. To Do this follow steps below :
   
> First install the Locust , I did locally using this command. Make sure you have Python installed first. 
```
pip install locust
```
> Create the locust file as below  and then run the command to test as below
 ```
locust -f locustfile.py

```
![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/8c73a444-3d92-451c-be81-7eaa019e9ff6)


> Load test result form Locust

![image](https://github.com/talkdeepak/flask-ml-azure-serverless/assets/29501818/8c7cf751-782d-4a80-b2ce-c89bec686b28)




      

  
  


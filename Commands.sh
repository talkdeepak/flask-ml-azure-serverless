git clone "git@github.com:talkdeepak/flask-ml-azure-serverless.git"
cd ./flask-ml-azure-serverless.git
git pull
make all
az webapp up --name flask-ml-azure-webapp --resource-group DeepakRG --sku B1 --logs --runtime "PYTHON:3.9"

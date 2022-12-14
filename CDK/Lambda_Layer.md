# This file contains the commands to create CDK virtual Environment and create Lambda Layer

### Create CDK Environment
##### init command creates a new Python CDK Project
```
cdk init sample-app --language python
```

##### Activate virtual Environment
```
source .venv/bin/activate
```
##### Install the required python modules
```
pip install -r requirements.txt
```
##### Once done, you can deploy the CDK stack, it will create a cloudformation changeset and further create the AWS infrastructure
```
cdk deploy
```
##### To teardown the infrastructure, use destroy command as follows:
```
cdk destroy
```


### Commands to create Lambda Layer
```
mkdir layers
cd layers
pip install requests -t layers/
pip install bs4 -t layers/
```

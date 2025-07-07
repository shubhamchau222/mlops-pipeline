## Commands Required for the projcet 

# UV comands
```bash
# create the env 
uv venv --python==3.12 venv 

# Activate the env
venv/Scripts/activate 

# to deactivate the env 
deactivate

```

# create git repo 

```bash
# local git initialization
$ git init 

# to connect git remote to your local
$ git remote add origin <your git repo link here>

# pull the content from git to local
$ git pull origin main 

```

## create the dagshub account and connect git repo to it
 
```
# process 
1. Go to: https://dagshub.com/dashboard
2. Create > New Repo > Connect a repo > (Github) Connect > Select your repo > Connect
3. Copy experiment tracking url and code snippet. (Also try: Go To MLFlow UI)
4. pip install dagshub & mlflow
```

## to create project strucuture (Optional)
link : https://github.com/drivendataorg/cookiecutter-data-science

```bash 

$ uv pip install cookiecutter 

$ cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science

## create the project Structures
```
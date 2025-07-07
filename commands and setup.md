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

# create the dagshub account and connect git repo to it
 
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

# Setup Mlflow on dagshub (optional you can set on aws as well)

-------------------------Setup MLFlow on Dagshub---------------------------
8. Go to: https://dagshub.com/dashboard
9. Create > New Repo > Connect a repo > (Github) Connect > Select your repo > Connect
10. Copy experiment tracking url and code snippet. (Also try: Go To MLFlow UI)
11. pip install dagshub & mlflow

12. Run the exp notebooks
13. git add - commit - push

14. dvc init
15. create a local folder as "local_s3" (temporary work)
16. on terminal - "dvc remote add -d mylocal local_s3"

17. Add code to below files/folders inside src dir:

## doenv 

```python
# Environment variables go here, can be read by `python-dotenv` package:
#
#   `src/script.py`
#   ----------------------------------------------------------------
#    import dotenv
#
#    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
#    dotenv_path = os.path.join(project_dir, '.env')
#    dotenv.load_dotenv(dotenv_path)
#   ----------------------------------------------------------------
#
# DO NOT ADD THIS FILE TO VERSION CONTROL!


```

## DVC Commands 

```bash

#1) Initialize DVC (if not done already)

$ dvc init
$ git add .dvc .gitignore
$ git commit -m "Initialize DVC"

#2) Add Data to DVC

$ dvc add data/raw/train.csv
```
commands summary

```bash 
dvc init
dvc add data/raw/train.csv
git add data/raw/train.csv.dvc .gitignore
git commit -m "Track dataset"
dvc remote add -d origin https://dagshub.com/<user>/<repo>.dvc
dvc remote modify origin --local auth basic
dvc remote modify origin --local user <dagshub-username>
dvc remote modify origin --local password <dagshub-token>
dvc push
git push origin main
```

```bash
# dvc to track the dataset

git init
dvc init
cp ../data/experimental/data.csv .
dvc add data.csv
git add data.csv.dvc .gitignore
git commit -m "Initial version"

# Change 1
echo "new_value,999" >> data.csv
dvc add data.csv && git add data.csv.dvc
git commit -m "Added new row"

# Change 2
# (Remove row using shell commands)
dvc add data.csv && git add data.csv.dvc
git commit -m "Removed row"

# Revert
git checkout <initial_commit_hash>
dvc checkout

# check the commit history
git log 
```
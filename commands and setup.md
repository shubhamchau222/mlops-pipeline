# 🚀 Project Setup Guide (with UV, Git, DVC, and MLflow on DAGsHub)

---

## 📦 Environment Setup with `uv`

```bash
# Create a virtual environment using Python 3.12
uv venv --python=3.12 venv

# Activate the environment
venv/Scripts/activate

# Deactivate the environment
deactivate
```

---

## 🗃️ Git Repository Setup

```bash
# Initialize a local Git repository
git init

# Add remote origin
git remote add origin <your-git-repo-url>

# Pull existing content from remote
git pull origin main
```

---

## 🌐 Connect GitHub Repository to DAGsHub

1. Go to: [https://dagshub.com/dashboard](https://dagshub.com/dashboard)
2. Click: **Create > New Repo > Connect a repo**
3. Choose **GitHub > Connect > Select your repo > Connect**
4. Copy the **MLflow tracking URL** and code snippet
5. Install dependencies:

   ```bash
   pip install dagshub mlflow
   ```

---

## 🧱 (Optional) Create Project Structure with Cookiecutter

🔗 Template: [cookiecutter-data-science](https://github.com/drivendataorg/cookiecutter-data-science)

```bash
uv pip install cookiecutter

cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
```

---

## 📊 MLflow Setup on DAGsHub

1. Setup MLflow through DAGsHub (same repo connect process as above)
2. Use the experiment tracking snippet in your code
3. Run experiment notebooks and track runs in the DAGsHub MLflow UI
4. Commit and push:

   ```bash
   git add .
   git commit -m "Add MLflow experiment"
   git push origin main
   ```

---

## 📁 Example `.env` Usage (Optional)

```python
# Inside your script (e.g., src/script.py)
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)
```

> ⚠️ **Note:** Do **not** add `.env` to version control!

---

## 🧰 DVC Setup & Workflow Guide

### ✅ 1. Initialize DVC

```bash
dvc init
git add .dvc .gitignore
git commit -m "Initialize DVC"
```

---

### 📂 2. Add & Track Dataset

```bash
dvc add data/raw/train.csv
git add data/raw/train.csv.dvc .gitignore
git commit -m "Track training dataset"
```

---

### 🌐 3. Configure Remote (DAGsHub)

```bash
# Optional: local remote
dvc remote add -d mylocal local_s3

# DAGsHub remote config
dvc remote add -d origin https://dagshub.com/<username>/<repo>.dvc
dvc remote modify origin --local auth basic
dvc remote modify origin --local user <dagshub-username>
dvc remote modify origin --local password <dagshub-token>

# Push tracked data and Git commits
dvc push
git push origin main
```

---

### 🔁 4. Dataset Versioning Workflow

```bash
# Copy dataset
cp ../data/experimental/data.csv .

# Initial tracking
dvc add data.csv
git add data.csv.dvc .gitignore
git commit -m "Initial version"

# ➕ Add new data
echo "new_value,999" >> data.csv
dvc add data.csv
git add data.csv.dvc
git commit -m "Added new row"

# ➖ Remove data manually, then:
dvc add data.csv
git add data.csv.dvc
git commit -m "Removed row"

# 🔄 Revert to original
git checkout <initial_commit_hash>
dvc checkout

# 📜 View history
git log
```

---

### ⚙️ 5. DVC Pipelines

```bash
# Re-run DVC pipeline stages
dvc repro

# Untrack folder from Git (if tracked previously)
git rm -r --cached 'data/raw'
git commit -m "Stop tracking data/raw"
```

---

### ☁️ 6. Connect DVC with AWS S3

```bash
# 1. Create IAM user + S3 bucket
# 2. Install required tools
pip install "dvc[s3]" awscli

# 3. (Optional) Clear old remotes
dvc remote list
dvc remote remove <name>

# 4. Set AWS credentials
aws configure

# 5. Add remote storage
dvc remote add -d myremote s3://<your-bucket-name>
```

---


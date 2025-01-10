# SQL_Query_Generator_LLM_App

## Project Overview:
SQL query generator project can generate sql queries with proper explaination that anyone can understand easily. This application is very effective that allow user to generate SQL query based on the prompts.

## Technology used:
1. Python
2. LLM- Google Gemimi Pro
3. Streamlit

## How to Run?

### Step 01: Clone the repository

```bash
Project repo: https://github.com/
```
### STEP 02- Create a conda environment after opening the repository

```bash
conda create -n sql python=3.11 -y
```

```bash
conda activate sql
```


### STEP 03- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Google API credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```

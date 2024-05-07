# [dataMate](https://github.com/PRANJALRANA11/datamate) 💬📊



DataMate is your  data assistant. A conversational interface for your data where you can load, clean, transform, and visualize without a single line of code.

## Demo

https://github.com/PRANJALRANA11/datamate/assets/129268721/29098247-4e6a-4d56-8f35-0f70eac88411


Note: Demo above is `Gemini-pro/vision`, which sends the conversation to Google AI API. . Model can hallucinates answer or even can produce bugs



### ⇒ *[Try it now! Hosted public environment is live! (Click Here)](pranjalrana11.github.io/datamate-csr/)* ⇐




## Features
- [x] Persistent Juptyer kernel backend for data manipulation during conversation
- [x] Natural language chat, visualizations/plots, and direct download of data assets
- [x] Load multiple tables directly into the chat
- [x] Search for data and load CSVs directly from github
- [x] Export data as html file
- [ ] WIP: Rollback kernel state when undo ~using `criu`~ (re-execute all cells)
- [ ] TODO: Support for more data sources (e.g. SQL, S3, PySpark etc.)


## Things you can ask DataMate
- [x] Load data from a URL
- [x] Clean data by removing duplicates, nulls, outliers, etc.
- [x] Join data from multiple tables into a single output table
- [x] Visualize data with plots and charts
- [x] Ask whatever you want to your very own  code-interpreter

## Quickstart

To install locally.

### 1. Clone the repository
```bash
git clone https://github.com/PRANJALRANA11/datamate
```
###  2. Create a branch
```bash
git checkout -b temp
```
### 3. copy the .env.example to .env
```bash
cp .env.example .env
```
### 4. install the dependancies
```bash
pip install -r requirements.txt
```
### 5. activate the virtual environment
```bash
.venv/scripts/activate
```
### 6. Run Uvicorn and access localhost:8000/docs
```bash
Uvicorn app:app --reload
```






## Contributions

Contributions are welcome! Feel free to submit a PR or open an issue.




### Technologies used in the project:

  fastapi
  Jupyter Kernels
  Google Cloud
  Gemini pro

### 🛡️ License

This project is licensed under the MIT





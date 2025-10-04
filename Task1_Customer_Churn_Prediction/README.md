# Customer Churn Prediction (Task 1)
Project: Customer Churn Prediction for Rhombix Technologies internship task.

## Overview
This is a simple, beginner-friendly churn prediction project using the public Telco Customer Churn dataset.
The Jupyter notebook performs data download, cleaning, EDA, model training (Logistic Regression & Random Forest),
evaluation, and saves model artifacts. It is designed to be easy to run and adapt.

## Structure
```
Task1_Customer_Churn_Prediction/
├── data/                            # place dataset here if you download manually
├── notebooks/
│   └── churn_prediction.ipynb       # main notebook
├── src/
│   ├── data_preprocessing.py        # helper functions
│   ├── model_training.py            # training & evaluation functions
│   └── visualization.py             # plotting helpers
├── README.md
├── requirements.txt
└── .gitignore
```

## How to run
1. Clone your repo locally and extract this bundle into `D:/Haseeb/Programming/RhombixTechnologies_Tasks03/Task1_Customer_Churn_Prediction/`
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows PowerShell
   source venv/bin/activate  # macOS / Linux
   pip install -r requirements.txt
   ```
3. Open the notebook `notebooks/churn_prediction.ipynb` in Jupyter and run all cells.
   The notebook will download the dataset from a public GitHub raw URL automatically.
4. Commit the files to your Git repo and push.

## Notes
- Dataset download requires internet when running the notebook.
- No sensitive data is included.

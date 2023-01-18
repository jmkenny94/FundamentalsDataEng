##Import required Libraries

import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd

##Create function that reads in the data.csv file and writes it out to JSON
def CSVToJson():
    df=pd.read_csv('C:\Users\jmken\Desktop\FundamentalsDataEng/data.CSV')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.JSON', orient='records')

#Next to implement airflow portion of the pipeline
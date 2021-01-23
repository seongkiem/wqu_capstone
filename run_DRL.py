# common library
import pandas as pd
from model.models import *
import os


def run_model() -> None:
    """Train the model."""

    # read and preprocess data
    preprocessed_path = "preprocessing/data/full_data.csv"
    if os.path.exists(preprocessed_path):
        data = pd.read_csv(preprocessed_path, index_col=0)
        data['datadate']=pd.to_datetime(data['datadate']).dt.strftime('%Y-%m-%d')
        #print(data.dtypes)
        
        print(len(data['datadate'].unique()))#1693
        #print('The number of tickers in study = ',len(data.tic.unique()))#91
        #print(data.head())
        #print(data.size)#5392205[1693 rows x 35 columns x 91 tickers]
        
        # 2015/10/01 is the date that validation starts
        # 2016/01/01 is the date that real trading starts
        # unique_trade_date needs to start from 2014/01/01 for validation purpose
        unique_trade_date = data[(data.datadate >= '2014-01-01')&(data.datadate <= '2020-12-17')].datadate.unique()
        #unique_trade_date = data[(data.datadate > 20151001)&(data.datadate <= 20200707)].datadate.unique()
        print(unique_trade_date)
        
        # rebalance_window is the number of months to retrain the model
        # validation_window is the number of months to  validation the model and select for trading
        rebalance_window = 63
        validation_window = 63
        
        
        ## Ensemble Strategy
        run_ensemble_strategy(df=data, 
                              unique_trade_date= unique_trade_date,
                              rebalance_window = rebalance_window,
                              validation_window=validation_window)
             
        #_logger.info(f"saving model version: {_version}")
    else:
        print("File is not exist.")

if __name__ == "__main__":
    run_model()

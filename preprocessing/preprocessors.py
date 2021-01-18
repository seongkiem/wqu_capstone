import numpy as np
import pandas as pd
import yfinance as yf
from stockstats import StockDataFrame as Sdf
from config import config

def data_split(df,start,end):
    """
    split the dataset into training or testing using date
    :param data: (df) pandas dataframe, start, end
    :return: (df) pandas dataframe
    """
    data = df[(df.datadate >= start) & (df.datadate < end)]
    data=data.sort_values(['datadate','tic'],ignore_index=True)
    #data  = data[final_columns]
    data.index = data.datadate.factorize()[0]
    return data

def calculate_price(df):
    """
    calcualte adjusted close price, open-high-low price and volume
    :param data: (df) pandas dataframe
    :return: (df) pandas dataframe
    """
    data = df.copy()
    data['tic']=data['Ticker']
    data['ajexdi']=data['Adj Close']/data['Close']
    data['adjcp'] = data['Adj Close']
    data['open'] = data['Open'] * data['ajexdi']
    data['high'] = data['High'] * data['ajexdi']
    data['low'] = data['Low'] * data['ajexdi']
    data['volume'] = data['Volume']
    data['datadate'] = data.index

    data = data[['datadate', 'tic', 'adjcp', 'open', 'high', 'low', 'volume']]
    data = data.sort_values(['tic', 'datadate'], ignore_index=True)
    return data

def add_vix(df,start,end):
    data = df.copy()
    df_vix=yf.download('^VIX', start=start, end=end)
    df_vix['datadate']=df_vix.index
    df_vix['vix_open']=df_vix['Open']
    df_vix['vix_high']=df_vix['High']
    df_vix['vix_low']=df_vix['Low']
    df_vix['vix_close']=df_vix['Close']
    #data=pd.merge(data, df_vix[['vix_open','vix_high','vix_low','vix_close']], left_index=True, right_index=True)
    data = data.merge(df_vix[['datadate','vix_open','vix_high','vix_low','vix_close']], on='datadate')
    return data

def add_major_indices(df,start,end):
    data = df.copy()
    df_sse=yf.download('000001.SS', start=start, end=end)
    df_sse['datadate']=df_sse.index
    df_sse['sse_close']=df_sse['Close']
    
    df_hsi=yf.download('^HSI', start=start, end=end)
    df_hsi['datadate']=df_hsi.index
    df_hsi['hsi_close']=df_hsi['Close']
    
    df_asx=yf.download('^AXJO', start=start, end=end)
    df_asx['datadate']=df_asx.index
    df_asx['asx_close']=df_asx['Close']
    
    df_nikkei=yf.download('^N225', start=start, end=end)
    df_nikkei['datadate']=df_nikkei.index
    df_nikkei['nikkei_close']=df_nikkei['Close']
    
    df_kospi=yf.download('^KS11', start=start, end=end)
    df_kospi['datadate']=df_kospi.index
    df_kospi['kospi_close']=df_kospi['Close']
    
    df_sti=yf.download('^STI', start=start, end=end)
    df_sti['datadate']=df_sti.index
    df_sti['sti_close']=df_sti['Close']
    
    df_nzx=yf.download('^NZ50', start=start, end=end)
    df_nzx['datadate']=df_nzx.index
    df_nzx['nzx_close']=df_nzx['Close']
    
    df_twi=yf.download('^TWII', start=start, end=end)
    df_twi['datadate']=df_twi.index
    df_twi['twi_close']=df_twi['Close']
    
    df_bse=yf.download('^BSESN', start=start, end=end)
    df_bse['datadate']=df_bse.index
    df_bse['bse_close']=df_bse['Close']
    
    df_ftse=yf.download('^FTSE', start=start, end=end)
    df_ftse['datadate']=df_ftse.index
    df_ftse['ftse_open']=df_ftse['Open']
    
    df_stoxx=yf.download('^STOXX50E', start=start, end=end)
    df_stoxx['datadate']=df_stoxx.index
    df_stoxx['stoxx_open']=df_stoxx['Open']
    
    df_dax=yf.download('^GDAXI', start=start, end=end)
    df_dax['datadate']=df_dax.index
    df_dax['dax_open']=df_dax['Open']
    
    df_cac=yf.download('^FCHI', start=start, end=end)
    df_cac['datadate']=df_cac.index
    df_cac['cac_open']=df_cac['Open']
    
    df_moex=yf.download('IMOEX.ME', start=start, end=end)
    df_moex['datadate']=df_moex.index
    df_moex['moex_open']=df_moex['Open']
    
    data = data.merge(df_sse[['datadate','sse_close']], how='left', on='datadate')
    data = data.merge(df_hsi[['datadate','hsi_close']], how='left', on='datadate')
    data = data.merge(df_asx[['datadate','asx_close']], how='left', on='datadate')
    data = data.merge(df_nikkei[['datadate','nikkei_close']], how='left', on='datadate')
    data = data.merge(df_kospi[['datadate','kospi_close']], how='left', on='datadate')
    data = data.merge(df_sti[['datadate','sti_close']], how='left', on='datadate')
    data = data.merge(df_nzx[['datadate','nzx_close']], how='left', on='datadate')
    data = data.merge(df_twi[['datadate','twi_close']], how='left', on='datadate')
    data = data.merge(df_bse[['datadate','bse_close']], how='left', on='datadate')
    data = data.merge(df_ftse[['datadate','ftse_open']], how='left', on='datadate')
    data = data.merge(df_stoxx[['datadate','stoxx_open']], how='left', on='datadate')
    data = data.merge(df_dax[['datadate','dax_open']], how='left', on='datadate')
    data = data.merge(df_cac[['datadate','cac_open']], how='left', on='datadate')
    data = data.merge(df_moex[['datadate','moex_open']], how='left', on='datadate')
    return data

def add_technical_indicator(df):
    """
    calcualte technical indicators
    use stockstats package to add technical inidactors
    :param data: (df) pandas dataframe
    :return: (df) pandas dataframe
    """
    stock = Sdf.retype(df.copy())

    stock['close'] = stock['adjcp']
    unique_ticker = stock.tic.unique()

    vlm_delta = pd.DataFrame()
    up_boll = pd.DataFrame()
    low_boll = pd.DataFrame()
    wr_14 = pd.DataFrame()
    wr_250 = pd.DataFrame()
    sma_5 = pd.DataFrame()
    sma_10 = pd.DataFrame()
    sma_21 = pd.DataFrame()
    sma_63 = pd.DataFrame()
    sma_250 = pd.DataFrame()
    rsv = pd.DataFrame()
    atr = pd.DataFrame()
    vr = pd.DataFrame()
    kdjk = pd.DataFrame()
    cr = pd.DataFrame()
    macd = pd.DataFrame()
    rsi = pd.DataFrame()
    cci = pd.DataFrame()
    dx = pd.DataFrame()

    #temp = stock[stock.tic == unique_ticker[0]]['macd']
    for i in range(len(unique_ticker)):
        ## volume delta against previous day
        temp_vlm_delta = stock[stock.tic == unique_ticker[i]]['volume_delta']
        temp_vlm_delta = pd.DataFrame(temp_vlm_delta)
        vlm_delta = vlm_delta.append(temp_vlm_delta, ignore_index=True)
        # upper bolling
        temp_up_boll = stock[stock.tic == unique_ticker[i]]['boll_ub']
        temp_up_boll = pd.DataFrame(temp_up_boll)
        up_boll = up_boll.append(temp_up_boll, ignore_index=True)
        # lower bolling
        temp_low_boll = stock[stock.tic == unique_ticker[i]]['boll_lb']
        temp_low_boll = pd.DataFrame(temp_low_boll)
        low_boll = low_boll.append(temp_low_boll, ignore_index=True)
        # 10 days WR
        temp_wr_14 = stock[stock.tic == unique_ticker[i]]['wr_14']
        temp_wr_14 = pd.DataFrame(temp_wr_14)
        wr_14 = wr_14.append(temp_wr_14, ignore_index=True)
        # 250 days WR
        temp_wr_250 = stock[stock.tic == unique_ticker[i]]['wr_250']
        temp_wr_250 = pd.DataFrame(temp_wr_250)
        wr_250 = wr_250.append(temp_wr_250, ignore_index=True)
        # sma 5 days
        temp_sma_5 = stock[stock.tic == unique_ticker[i]]['close_5_sma']
        temp_sma_5 = pd.DataFrame(temp_sma_5)
        sma_5 = sma_5.append(temp_sma_5, ignore_index=True)
        # sma 10 days
        temp_sma_10 = stock[stock.tic == unique_ticker[i]]['close_10_sma']
        temp_sma_10 = pd.DataFrame(temp_sma_10)
        sma_10 = sma_10.append(temp_sma_10, ignore_index=True)
        # sma 21 days
        temp_sma_21 = stock[stock.tic == unique_ticker[i]]['close_21_sma']
        temp_sma_21 = pd.DataFrame(temp_sma_21)
        sma_21 = sma_21.append(temp_sma_21, ignore_index=True)
        # sma 63 days
        temp_sma_63 = stock[stock.tic == unique_ticker[i]]['close_63_sma']
        temp_sma_63 = pd.DataFrame(temp_sma_63)
        sma_63 = sma_63.append(temp_sma_63, ignore_index=True)
        # sma 250 days
        temp_sma_250 = stock[stock.tic == unique_ticker[i]]['close_250_sma']
        temp_sma_250 = pd.DataFrame(temp_sma_250)
        sma_250 = sma_250.append(temp_sma_250, ignore_index=True)
        # rsv
        temp_rsv = stock[stock.tic == unique_ticker[i]]['rsv_14']
        temp_rsv = pd.DataFrame(temp_rsv)
        rsv = rsv.append(temp_rsv, ignore_index=True)
        # atr
        temp_atr = stock[stock.tic == unique_ticker[i]]['atr_14']
        temp_atr = pd.DataFrame(temp_atr)
        atr = atr.append(temp_atr, ignore_index=True)
        # vr
        temp_vr = stock[stock.tic == unique_ticker[i]]['vr_14']
        temp_vr = pd.DataFrame(temp_vr)
        vr = vr.append(temp_vr, ignore_index=True)
        # kdj - k
        temp_kdjk = stock[stock.tic == unique_ticker[i]]['kdjk']
        temp_kdjk = pd.DataFrame(temp_kdjk)
        kdjk = kdjk.append(temp_kdjk, ignore_index=True)
        # cr
        temp_cr = stock[stock.tic == unique_ticker[i]]['cr']
        temp_cr = pd.DataFrame(temp_cr)
        cr = cr.append(temp_cr, ignore_index=True)
        ## macd
        temp_macd = stock[stock.tic == unique_ticker[i]]['macd']
        temp_macd = pd.DataFrame(temp_macd)
        macd = macd.append(temp_macd, ignore_index=True)
        ## rsi
        temp_rsi = stock[stock.tic == unique_ticker[i]]['rsi_14']
        temp_rsi = pd.DataFrame(temp_rsi)
        rsi = rsi.append(temp_rsi, ignore_index=True)
        ## cci
        temp_cci = stock[stock.tic == unique_ticker[i]]['cci_14']
        temp_cci = pd.DataFrame(temp_cci)
        cci = cci.append(temp_cci, ignore_index=True)
        ## adx
        temp_dx = stock[stock.tic == unique_ticker[i]]['dx_14']
        temp_dx = pd.DataFrame(temp_dx)
        dx = dx.append(temp_dx, ignore_index=True)

    df['vlm_delta'] = vlm_delta
    df['up_boll'] = up_boll
    df['low_boll'] = low_boll
    df['wr_14'] = wr_14
    df['wr_250'] = wr_250
    df['sma_5'] = sma_5
    df['sma_10'] = sma_10
    df['sma_21'] = sma_21
    df['sma_63'] = sma_63
    df['sma_250'] = sma_250
    df['rsv'] = rsv
    df['atr'] = atr
    df['vr'] = vr
    df['kdjk'] = kdjk
    df['cr'] = cr
    df['macd'] = macd
    df['rsi'] = rsi
    df['cci'] = cci
    df['adx'] = dx

    return df

def add_turbulence(df):
    """
    add turbulence index from a precalcualted dataframe
    :param data: (df) pandas dataframe
    :return: (df) pandas dataframe
    """
    turbulence_index = calculate_turbulence(df)
    df = df.merge(turbulence_index, on='datadate')
    df = df.sort_values(['datadate','tic']).reset_index(drop=True)
    return df

def calculate_turbulence(df):
    """calculate turbulence index based on dow 30"""
    # can add other market assets
    
    df_price_pivot=df.pivot(index='datadate', columns='tic', values='adjcp')
    unique_date = df.datadate.unique()
    # start after a year
    start = 252
    turbulence_index = [0]*start
    #turbulence_index = [0]
    count=0
    for i in range(start,len(unique_date)):
        current_price = df_price_pivot[df_price_pivot.index == unique_date[i]]
        hist_price = df_price_pivot[[n in unique_date[0:i] for n in df_price_pivot.index ]]
        cov_temp = hist_price.cov()
        current_temp=(current_price - np.mean(hist_price,axis=0))
        temp = current_temp.values.dot(np.linalg.inv(cov_temp)).dot(current_temp.values.T)
        if temp>0:
            count+=1
            if count>2:
                turbulence_temp = temp[0][0]
            else:
                #avoid large outlier because of the calculation just begins
                turbulence_temp=0
        else:
            turbulence_temp=0
        turbulence_index.append(turbulence_temp)
    
    
    turbulence_index = pd.DataFrame({'datadate':df_price_pivot.index,
                                     'turbulence':turbulence_index})
    return turbulence_index

def data_preprocessing()-> None:
    sp100 = pd.read_csv('data/s&p100_before_tesla.csv',encoding = "ISO-8859-1")
    tickers=[]
    
    excl=['PM','V','CHTR','GM','KMI','FB','ABBV','PYPL','KHC','DOW']
    
    for ticker in sp100.iloc[:,0]:
        if ticker not in excl:
            tickers.append(ticker)
        
    #print(sp100.iloc[:,0].head())
    print(len(tickers))
    
    # set the start date and end date
    start='2007-04-01'
    end='2020-12-18'# tesla was included in the S&P 500 after this date
    
    df=yf.download(tickers[0], start=start, end=end)
    df['Ticker']=tickers[0]
    
    for ticker in tickers[1:]:
        df_0=yf.download(ticker, start=start, end=end)
        df_0['Ticker']=ticker
        df=df.append(df_0)
    
    df_new=calculate_price(df)
    df_new=add_vix(df_new,start,end)
    df_new=add_major_indices(df_new,start,end)
    df_new=add_technical_indicator(df_new)
    df_new=add_turbulence(df_new)
    print('Extracting data to excel file.')
    df_new.to_csv("data/full_data.csv")
    
if __name__ == "__main__":
    data_preprocessing()
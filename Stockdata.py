from alpha_vantage.timeseries import TimeSeries
from Config import Configuration
import pandas as pd
import ast



class DataFeed:
    def __init__(self):
        self.name = "BDME"
        self.Company = Configuration().GetData()['CompanyList1']
        self.APIKEYS = Configuration().GetData()['APIKEYDICT']
        print (self.APIKEYS[1])

    # to get ticket names (data we have) / Company_names
    def Feed_IntraDay(self):
        collectionname = 'IntraDay'
        for com in self.Company:
            print (com)
            try:
                ts = TimeSeries(key=self.APIKEYS[1], output_format='pandas')
                data, meta_data = ts.get_intraday(com, interval='1min',outputsize="full")
                # RWmongo.WriteValue(collectionname, com, data.to_dict())
                # print (data)
                return data
            except ValueError:
                print('Company Ignor due to high service call')


    def Feed_Daily(self):
        collectionname = 'Daily'
        for com in self.Company:
            try:
                ts = TimeSeries(key=self.APIKEYS[1], output_format='pandas')
                data, meta_data = ts.get_daily(com, outputsize="full")
                return data
            except ValueError:
                print('Company Ignor due to high service call')


    def Feed_Weekly(self):
        collectionname = 'Weekly'
        for com in self.Company:
            try:
                ts = TimeSeries(key=self.APIKEYS[1], output_format='pandas')
                data, meta_data = ts.get_weekly(com)
                #RWmongo.WriteValue(collectionname, com, data.to_dict())
                #print (data)
                return data
            except ValueError:
                print('Company Ignor due to high service call')


    def Feed_Monthly(self):
        collectionname = 'Monthly'
        for com in self.Company:
            try:
                ts = TimeSeries(key=self.APIKEYS[1], output_format='pandas')
                data, meta_data = ts.get_monthly(com)
                #RWmongo.WriteValue(collectionname, com, data.to_dict())
                #print (data)
                return data
            except ValueError:
                print('Company Ignor due to high service call')


#Debug
#DataFeed().Feed_IntraDay()
#DataFeed().Feed_Daily()
#DataFeed().Feed_Weekly()
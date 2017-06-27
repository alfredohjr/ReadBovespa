import pandas as pd

def read_Bovespa(File):
    '''
    this function convert file "COTAHIST_AXXX" to DataFrame
    '''

    deli = [2,8,2,12,3,12,10,3,4,13,13,13,13,13,13,13,5,18,18,13,1,8,7,13,11,4]

    df = pd.read_fwf(File,widths=deli,header=None)

    df = df.rename(columns={0:'tipreg',1:'data',2:'codbdi',3:'codneg',4:'tpmerc',5:'nomres'
                       ,6:'especi',7:'prazot',8:'modref',9:'preabe',10:'premax'
                      ,11:'premin',12:'premed',13:'preult',14:'preofc',15:'preofv',16:'totneg',17:'quatot'
                      ,18:'voltot',19:'preexe',20:'indopc',21:'datven',22:'fatcot',23:'ptoexe',24:'codisi',25:'dismes'
                      })
    df = df.drop(df.index[[0,df.index.max()]])

    df['data'] = pd.to_datetime(df['data'])

    return df

def convert_to_decimals(x):
    return float(x[:-2] + '.' + x[-2:])

def read_Bovespa(File):
    '''
    this function convert file "COTAHIST_AXXX" to DataFrame
    '''

    import pandas as pd
    
    deli = [2,8,2,12,3,12,10,3,4,13,13,13,13,13,13,13,5,18,18,13,1,8,7,13,11,4]

    df = pd.read_fwf(File,widths=deli,header=None,converters={9:convert_to_decimals,
                                                              10:convert_to_decimals,
                                                              11:convert_to_decimals,
                                                              12:convert_to_decimals,
                                                              13:convert_to_decimals,
                                                              14:convert_to_decimals,
                                                              15:convert_to_decimals,
                                                              18:convert_to_decimals,
                                                              19:convert_to_decimals,
                                                                })

    df = df.rename(columns={0:'tipreg',1:'data',2:'codbdi',3:'codneg',4:'tpmerc',5:'nomres'
                       ,6:'especi',7:'prazot',8:'modref',9:'preabe',10:'premax'
                      ,11:'premin',12:'premed',13:'preult',14:'preofc',15:'preofv',16:'totneg',17:'quatot'
                      ,18:'voltot',19:'preexe',20:'indopc',21:'datven',22:'fatcot',23:'ptoexe',24:'codisi',25:'dismes'
                      })
    df = df.drop(df.index[[0,df.index.max()]])

    df['data'] = pd.to_datetime(df['data'])
    df['datven'] = pd.to_datetime(df['datven'])
    df['preabe'] = pd.to_numeric(df['preabe'])
    df['premax'] = pd.to_numeric(df['premax'])
    df['premin'] = pd.to_numeric(df['premin'])
    df['premed'] = pd.to_numeric(df['premed'])
    df['preult'] = pd.to_numeric(df['preult'])
    df['preofc'] = pd.to_numeric(df['preofc'])
    df['preofv'] = pd.to_numeric(df['preofv'])
    df['voltot'] = pd.to_numeric(df['voltot'])
    df['preexe'] = pd.to_numeric(df['preexe'])
    
    return df

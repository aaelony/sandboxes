import numpy as np
import pandas as pd

def random_df(nrows=5):
    """
    Generate random data and return a pandas dataframe.
    
    Categorical, integer, poisson, and normally distributed data generated.
    """
    df = pd.DataFrame(
        {'gender': [np.random.choice(['M','F']) for i in range(nrows)],
         'colors': [np.random.choice(['red','orange', 'yellow','green','blue','indigo', 'violet']) for i in range(nrows)],
         'age' : np.random.randint(low=18, high=80, size= nrows, dtype=int),
         'visit_date' : [np.random.choice(pd.date_range(start='2020-01-01', end=date.today() )) for i in range(nrows)],
         'visits' : np.random.default_rng().poisson(lam=1.0, size=nrows),
         'paidamt' : np.random.default_rng().normal(loc=100.0, scale=90.0, size=nrows).round(decimals=2)
        })
    return df


random_df(nrows = 100)

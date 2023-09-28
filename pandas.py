import pandas as pd



D={'PANDAS':['When we have to work on Tabular data,'
             'we prefer the pandas module.',
            'The powerful tools of pandas are Data frame and Series.',
            'Pandas consume more memory.',
            'Pandas have a better performance when the number of rows is 500K or more.',
            'Indexing of the pandas series is very slow as compared to numpy arrays.',
            'Pandas have 2d table object called DataFrame.',
            'It was developed by Wes McKinney and was released in 2008.',
            'It is used in a lot of organizations like Kaidee, Trivago, Abeja Inc. , and a lot more.',
            'It has a higher industry application.',],
  'NUMPY':['When we have to work on Numerical data, we prefer the numpy module.',
          'Whereas the powerful tool of numpy is Arrays.',
          'Numpy is memory efficient.',
          'Numpy has a better performance when number of rows is 50K or less.',
          'Indexing of numpy arrays is very fast.',
          'Numpy is capable of providing multi-dimensional arrays.',
          'It was developed by Travis Oliphant and was released in 2005.',
          'It is being used in organizations like Walmart Tokopedia, Instacart, and many more.',
          'It has a lower industry application.'
          ]
  }

P=pd.DataFrame(D) 
print(P)

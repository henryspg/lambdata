import pandas as pd
import datetime


class StateAbbreviation:
    """
    This 1st class is to convert the name of US states to its abbreviation and vice versa.
    """

#     Start with the dictionary
    state_to_abbreviation = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Washington DC': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }
    
    
    def __init__(self):
        return



    def get_abbreviation_from_state(self, state):
        """ This code is to convert from state name to state abbreviation  """        
        return self.state_to_abbreviation.get(state, state+ " does not exist. Please put in a valid state")



    def get_state_from_abbreviation(self, abbreviation):
        """ This code is to convert from abbreviation to state name """
        
#         Make the dictionary in reversed order
        abbreviation_to_state = {v: k for k, v in self.state_to_abbreviation.items()}
        return abbreviation_to_state.get(abbreviation, abbreviation+" does not exist. Please put in a valid abbreviation")

    

    
class DateExtract:
    """
    This 2nd class is related to a 'date' conversion.
    """    
    
    def __init__(self):
        return
    
    def date_extract(self, df_with_date_column):
        """
        This code is about the function to extract year, month, and day from a 'date' column.
        sample: df = pd.DataFrame({'date': ['2018-08-09 11:10:55','2019-03-02 13:15:21']})
        """
        df=df_with_date_column.copy()
    
        df['year'] = pd.DatetimeIndex(df['date']).year
        df['month'] = pd.DatetimeIndex(df['date']).month
        df['day'] = pd.DatetimeIndex(df['date']).day
    
        return df
from pprint import pprint
import pandas as pd

def service(data, sortingData):

    # columns to = list
    mappingPd = pd.DataFrame(data[0:])
    mappingPdResult = mappingPd.values.tolist()


    # mapping to df
    df = pd.DataFrame(mappingPdResult[1:], columns=mappingPdResult[0])

    return df

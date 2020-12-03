import pandas as pd
from pathlib import Path

def write_average(input_filepath, output_filepath):
    df = pd.read_csv(input_filepath, header = None)

    pd.to_numeric(df, errors = 'coerce')

    average = df.mean(axis = 0, skipna = True)
    average_T = pd.DataFrame(average).T

    return average_T.to_csv(output_filepath, header = None, index = None)

write_average("test_csv.csv", "output.csv")
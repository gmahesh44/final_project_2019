import pandas as pd
import numpy as np
def test_hiv():
    data = pd.read_csv("/Users/gmahesh/final_project_2019/data_coded.csv")
    assert data["YEAR"].dtypes == np.int64
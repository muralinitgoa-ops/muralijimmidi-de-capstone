import pandas as pd
from src.etl.transform import transform_data


def sample_df():
    data = {
        "id": [1, 2],
        "name": ["A", "B"],
        "age": [25, 35],
        "salary": [50000, 60000],
    }
    return pd.DataFrame(data)


def test_salary_increase():
    df = sample_df()
    result = transform_data(df)

    assert round(result.loc[0, "salary"], 2) == 55000
    assert round(result.loc[1, "salary"], 2) == 66000


def test_age_group():
    df = sample_df()
    result = transform_data(df)

    assert result.loc[0, "age_group"] == "Young"
    assert result.loc[1, "age_group"] == "Senior"


def test_no_nulls():
    df = sample_df()
    result = transform_data(df)

    assert result.isnull().sum().sum() == 0
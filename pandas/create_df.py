import os

import pandas as pd


def main():
    # create series from dictionary
    sr_from_dict = pd.Series(
        {"hokkaido": "sapporo", "aomori": "aomori", "iwate": "morioka"}
    )
    print(sr_from_dict)

    # create series from list
    sr_from_list = pd.Series(
        ["hokkaido", "aomori", "iwate"], index=["sapporo", "aomori", "morioka"]
    )
    print(sr_from_list)

    # create dataframe by specifying columns
    df_from_col = pd.DataFrame(
        data={
            "prefecture": ["hokkaido", "aomori", "iwate"],
            "prefectural capital": ["sapporo", "aomori", "morioka"],
            "population": [5130000, 1200000, 1180000],
        }
    )
    print(df_from_col)

    # create dataframe by specifying rows
    df_from_row = pd.DataFrame(
        data=[
            ["hokkaido", "sapporo", 5130000],
            ["aomori", "aomori", 1200000],
            ["iwate", "morioka", 1180000],
        ],
        index=["1", "2", "3"],
        columns=["prefecture", "prefectural capital", "population"],
    )
    print(df_from_row)

    # create dataframe from csv
    example_csv_path = os.path.dirname(__file__) + "/example.csv"
    df_from_csv = pd.read_csv(example_csv_path)
    print(df_from_csv)


if __name__ == "__main__":
    main()

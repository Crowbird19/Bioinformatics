import pandas as pd
from chembl_webresource_client.new_client import new_client


def main():

    target = new_client.target
    target_query = target.search("diabetes")
    target_df = pd.DataFrame.from_dict(target_query)
    # print(target_df.head())

    selected_target = 'CHEMBL614780'  # CHEMBL614780 is related to type 1. Idk how this site is confusing
    activity = new_client.activity
    res = activity.filter(target_chembl_id=selected_target).filter(standard_type='IC50')

    data_df = pd.DataFrame.from_dict(res)

    # wat do?
    data_df.standard_type.unique()
    # print(data_df)

    data_df.to_csv(path_or_buf=r"C:\Users\Crow\Documents\Python\CHEMBLCSV.csv", index=False)


if __name__ == '__main__':
    main()

import os

from dask.distributed import Client

if __name__ == '__main__':
    client = Client("ec2-18-193-108-185.eu-central-1.compute.amazonaws.com:8786")
    print(client)

    import dask.dataframe as dd

    file_url = os.environ["DATASET_LOCATION"]

    df = dd.read_csv(file_path, header=None)
    # count words
    new_df = (
        df[0]
        .str
        .split()
        .explode()
        .value_counts()
        .reset_index()
    )
    new_df.columns = ['Word', 'Frequency']
    # new_df = new_df.sort_values(['Frequency', 'Word'], ascending=False)

    new_df.compute()
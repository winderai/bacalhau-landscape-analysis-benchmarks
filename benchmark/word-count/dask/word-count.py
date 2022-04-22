import os

from dask.distributed import Client

if __name__ == '__main__':
    try:
        client = Client("hadoop-master:8786")
        print("Connecting to hadoop-master...")
    except:
        client = Client()
        print("Connecting to localhost...")
    print(client)

    import dask.dataframe as dd

    file_url = os.environ["DATASET_LOCATION"]

    df = dd.read_csv(file_url, header=None)
    # count words
    new_df = (
        df[0]
        .str
        .split()
        .explode()
        .value_counts()
        .reset_index()
    )
    # new_df.columns = ['Word', 'Frequency']
    # new_df = new_df.sort_values(['Frequency', 'Word'], ascending=False)

    print(new_df.compute().head())
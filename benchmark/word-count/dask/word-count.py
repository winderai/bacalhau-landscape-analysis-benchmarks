from dask.distributed import Client

if __name__ == '__main__':
    client = Client()
    print(client)

    import dask.dataframe as dd

    file_path = "https://raw.githubusercontent.com/enricorotundo/hadoop-examples-mapreduce/main/src/test/resources/data/wordcount.txt"

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
    new_df = new_df.sort_values(['Frequency', 'Word'], ascending=False)

    print(new_df.compute())
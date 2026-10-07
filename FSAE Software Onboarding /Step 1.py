import polars as pl
path = "~/Desktop/software-data.parquet"
dfa = pl.read_parquet(path)
dfa = dfa.select(pl.all().fill_null(strategy = "forward"))
print(dfa)
df = dfa["Time", "SME_TRQSPD_Speed"]
print(df)
matched_df = df.filter(pl.col("Time")==10.00000)
print (matched_df)
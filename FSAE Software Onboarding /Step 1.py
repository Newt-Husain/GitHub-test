import polars as pl
path = "~/Desktop/software-data.parquet"
dfa = pl.read_parquet(path)
dfa = dfa.select(pl.all().fill_null(strategy = "forward"))
print(dfa)



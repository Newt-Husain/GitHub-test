import polars as pl
import matplotlib.pyplot as plt
path = "~/Desktop/software-data.parquet"
dfa = pl.read_parquet(path)
dfa = dfa.select(pl.all().fill_null(strategy = "forward"))
df = dfa["Time", "SME_TRQSPD_Speed"]
print(df)
total_len = len(df)
for i in range(total_len):
    if i == 10.0:
        matched_df = df.filter(pl.col("Time")==10.0)
        print (matched_df)
plt.plot(dfa["Time"], dfa ['SME_TRQSPD_Speed'])
plt.xlabel("Time")
plt.ylabel("Car Speed")
plt.show()

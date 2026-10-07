import polars as pl
import numpy as np
import matplotlib as plt
path = "~/Desktop/software-data.parquet"
dfa = pl.read_parquet(path)
dfa = dfa.select(pl.all().fill_null(strategy = "forward"))

df = pl.read_parquet("data.parquet", columns=["Time", "Car Speed"])
x = df["Time"].to_numpy()
y = df["Car Speed"].to_numpy()
target_x = 10
mask = np.isclose(x, target_x)

if np.any(mask):
    target_y = y[mask][0]
    plt.plot(x, y, label="Polars Data Stream", color="blue")
    plt.plot(target_x, target_y, "ro", markersize=10,label=f"Point at x={target_x}")
    plt.xlabel("Time")
    plt.ylabel("Car Speed")
    plt.title("Polars + NumPy Parquet Plot")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print(f"Value x = {target_x} was not found in the dataset.")
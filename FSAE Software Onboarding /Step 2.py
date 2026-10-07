import polars as pl
import matplotlib.pyplot as plt
import numpy as np
path = "~/Desktop/software-data.parquet"
dfa = pl.read_parquet(path)
dfa = dfa.select(pl.all().fill_null(strategy = "forward"))
df = dfa["SME_TRQSPD_Speed"]
wRPM = df * (12/41)
w = wRPM * ((2*np.pi)/60)
v_final = df * (12/41) * ((2*np.pi)/60) * 0.2
df = v_final
print(df)
df2 = dfa["Time"]
print(df2)
time = np.array([df2])
car_speed = np.array([df])
plt.plot(time, car_speed, marker='o', color='r', linestyle='-')
plt.title('Speed of Car vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Car Speed (mph)')
plt.figure(figsize=(10,5), dpi=300)
plt.style.use('seaborn-v0_8-whitegrid')
plt.show()
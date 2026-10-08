import polars as pl
import matplotlib.pyplot as plt
import numpy as np

# Reads the parquet file
path = "~/Desktop/software-data.parquet"
dfa = pl.read_parquet(path)
dfa = dfa.select(pl.all().fill_null(strategy = "forward"))

# This gets the speed data from the parquet file into it's own
# seperate data frame so I can manipulate it
df = dfa["SME_TRQSPD_Speed"]

# This converts the data from RPM to MPH
# side note: I thought I had to do a loop for this part to 
# perform the function for every value in the data table; turns out I don't
wRPM = df * (12/41)
w = wRPM * ((2*np.pi)/60)
v_final = df * (12/41) * ((2*np.pi)/60) * 0.2
df = v_final
print(df)

# Create a seperate data frame for time to isolate from main data frame
df2 = dfa["Time"]
print(df2)

# Sends both data frames to numpy; ready to graph :D
time = df2.to_numpy()
car_speed = df.to_numpy()
plt.plot(time, car_speed)
plt.title('Speed of Car vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Car Speed (mph)')
plt.grid(True)

# This part is to plot a point at 10 seconds, and it should 
# display the coordinates and hopefully print out the coordinates
target_time = 10.0
idx = np.argmin(np.abs(time - target_time))
t_val = time[idx]
s_val = car_speed[idx]
print(f"At time {t_val:.2f} s, car speed is {s_val:.2f} mph")
plt.scatter(t_val, s_val, color = "red", zorder = 5)

# And finally this shows a completed graph :]
plt.show()
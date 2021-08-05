import src.data_generate_yehoon as yh
import src.data_generate_jungmin as jm

data = []

data.extend(yh.gen_data())
data.extend(jm.gen_data())

print(len(data))
print(data[:5])
print(data[-3:])

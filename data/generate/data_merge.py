import src.data_generate_yehoon as yh
import src.data_generate_jungmin as jm
import src.data_generate_jongrin as jr
import src.data_generate_taehyung as th

data = []

data.extend(yh.gen_data())
data.extend(jm.gen_data())
data.extend(jr.gen_data())
data.extend(th.gen_data())

print(len(data))
print(data[:5])
print(data[-3:])

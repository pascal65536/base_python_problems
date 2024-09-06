import math

filename = "sinusoid.csv"
x = -10
amplitude = 10
phase = 0.2

with open(filename, "w") as f:
    while x < 10:
        x += 0.01
        y1 = math.sin(x)
        y2 = math.sin(x + phase) * amplitude

        x_str = str(x).replace(".", ",")
        y1_str = str(y1).replace(".", ",")
        y2_str = str(y2).replace(".", ",")

        f.write(f'"{x_str}";"{y1_str}";"{y2_str}"\n')

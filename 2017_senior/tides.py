N = int(input())
measurements = str(input())

data = [N]
measurement_list = measurements.split(" ")

for i in range(N):
    lowest = 1000001
    index = 0
    for k in range(len(measurement_list)):
        if int(measurement_list[k]) < lowest:
            lowest = int(measurement_list[k])
            index = k
    measurement_list.pop(index)
    data.append(lowest)
data.pop(0)

low_tide = True
high_tide = False
high_count = 1
low_count = 0
arranged_data = [N]

if N%2 == 0:
    index = int(N/2) - 1
else:
    index = int(N/2) 

for i in range(len(data)):
    if i%2 == 0:
        arranged_data.append(data[index - low_count])
        low_count += 1
    else:
        arranged_data.append(data[index + high_count])
        high_count += 1

for i in range(len(arranged_data) - 1):
    print(str(arranged_data[i + 1]) + " ", end='')
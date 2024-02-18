def read_data(file_path):
    data = {'t': [],'x': [],'y': [],'θr': [], 'θv': [], 'θa': []}
    with open(file_path, 'r') as file:
        next(file)  
        next(file)  # Skip the header
        for line in file:
            values = line.strip().split()
            data['t'].append(float(values[0]))
            data['x'].append(float(values[1]))
            data['y'].append(float(values[2]))
            data['θr'].append(float(values[3]))
            data['θv'].append(float(values[4]))
            data['θa'].append(float(values[5]))
    return data
# Read data from files
data_A = read_data('masse_A.txt')
data_B = read_data('masse_B.txt')

def write_to_file(file_path, datA, datB):
    with open(file_path, 'w') as file:
        file.write(f't {file_path.split("_")[1]}A {file_path.split("_")[1]}B\n')
        for t, val_A, val_B in zip(data_A['t'], datA, datB):
            file.write(f'{t} {val_A} {val_B-val_A}\n')



# Write to separate files
write_to_file('theta_r.txt', data_A['θr'], data_B['θr'])
write_to_file('theta_v.txt', data_A['θv'], data_B['θv'])
write_to_file('theta_a.txt', data_A['θa'], data_B['θa'])

import matplotlib.pyplot as plt
import numpy as np

def smooth_data(data, window_size=5):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

def plot_data(file_path, save_path=None, smooth=False, window_size=5):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    headers = lines[0].split()
    data = {header: [] for header in headers}

    for line in lines[1:]:
        values = line.split()
        for header, value in zip(headers, values):
            data[header].append(float(value))

    plt.figure(figsize=(8, 6))

    if smooth:
        for header in headers[1:]:
            smoothed_data = smooth_data(data[header], window_size)
            plt.plot(data['t'][:len(smoothed_data)], smoothed_data, label=f'Smoothed {header}')
    else:
        for header in headers[1:]:
            plt.plot(data['t'], data[header], label=header)

    plt.xlabel('Time (t)')
    plt.ylabel('Values')
    plt.title(f'Plot of {file_path} {"with Smoothing" if smooth else ""}')
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, format='png')
        print(f"Plot saved as {save_path}")
    else:
        plt.show()

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    save_path = input("Enter the save path (press Enter to skip): ").strip()
    smooth = input("Apply smoothing? (yes/no): ").lower() == 'yes'
    
    if smooth:
        window_size = int(input("Enter the smoothing window size (integer): "))
    else:
        window_size = 5  # Default window size
    
    plot_data(file_path, save_path, smooth, window_size)

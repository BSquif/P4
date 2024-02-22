import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def smooth_curve_savgol(y, window_size, order):
    return savgol_filter(y, window_size, order)

def save_smoothed_data(file_path, t, theta_A_smooth, theta_B_smooth):
    # Create a new file with "_smoothed" appended to the original file name
    output_file_path = file_path.replace('.txt', '_smoothed.txt')
    # Save the smoothed data to the new file
    np.savetxt(output_file_path, np.column_stack((t, theta_A_smooth, theta_B_smooth)), 
               header='t (s)  theta_A (rad)  theta_B (rad)', comments='', fmt='%.6f')

def process_files_in_folder(folder_path, window_size, order, save_smoothed=False):
    plt.figure(figsize=(16, 8))  # Adjust the figure size
    legend= ["Angle (rad)", "Angle speed [rad/s]", "Angle acceleration [rad/s^2]"]
    Atitles = ["θA", "ωA", "αA"]
    Btitles = ["θB", "ωB", "αB"]
    print(os.listdir(folder_path))
    for i, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing file: {file_path}")
            print(i)
            
            data = np.loadtxt(file_path, skiprows=1, unpack=True)
            t, theta_A, theta_B = data

            # Smooth curves using Savitzky-Golay filter
            theta_A_smooth = smooth_curve_savgol(theta_A, window_size, order)
            theta_B_smooth = smooth_curve_savgol(theta_B, window_size, order)

            # Plot original and smoothed curves
            plt.subplot(3, 2, (i)*2 + 1)
            plt.plot(t, theta_A, label=f'Original {Atitles[i]}', marker='o', linestyle='-', color='blue')
            plt.plot(t, theta_A_smooth, label=f'Smoothed {Atitles[i]}', linestyle='-', color='r')
            plt.title(Atitles[i] + f' - {os.path.basename(file_path)}')
            plt.xlabel('Time (s)')
            plt.ylabel(legend[i])
            plt.legend()
            plt.grid(True)

            plt.subplot(3, 2, (i)*2 + 2)
            plt.plot(t, theta_B, label=f'Original {Btitles[i]}', marker='o', linestyle='-', color='green')
            plt.plot(t, theta_B_smooth, label=f'Smoothed {Btitles[i]}', linestyle='-', color='orangered')
            plt.title(Btitles[i] + f' - {os.path.basename(file_path)}')
            plt.xlabel('Time (s)')
            #plt.ylabel(legend[i])
            plt.legend()
            plt.grid(True)

            if save_smoothed:
                save_smoothed_data(file_path, t, theta_A_smooth, theta_B_smooth)
                print(f"Smoothed data saved to {file_path.replace('.txt', '_smoothed.txt')}")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    folder_path = "data"
    window_size = 12
    order = 5

    #save_option = input("Do you want to save the smoothed data for each file? (y/n): ").lower()
    save_smoothed =  True

    process_files_in_folder(folder_path, window_size, order, save_smoothed)

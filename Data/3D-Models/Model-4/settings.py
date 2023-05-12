import os

# specify the path to the folder containing the files
folder_path = r"C:\Users\r04ra18\Desktop\Data-Model-4\Data-Model-4-222-2nd"

query = 'interpretations.csv'
y_dist = 50
uncertainty_distance = 50

# create an empty dictionary to store the file names and paths
file_dict = {}

# loop through all the files in the folder
for file_name in os.listdir(folder_path):

    # construct the full path to the file
    file_path = os.path.join(folder_path, file_name)
    
    if file_name.endswith('.csv') and file_name != "interpretations.csv":
        # add the file name and path to the dictionary
        file_dict[file_name] = uncertainty_distance
    else:
        pass

targets = file_dict.copy()


# targets = {
#     "fold-model-6-outcrop.csv":uncertainty_distance,
#     "Tunnel_Well.csv":uncertainty_distance,
#     "Tunnel_Well_113.csv":uncertainty_distance,
#     "Tunnel_Well_114.csv":uncertainty_distance,
#     "Tunnel_Well_115.csv":uncertainty_distance,
#     "Tunnel_Well_116.csv":uncertainty_distance,
#     "Tunnel_Well_117.csv":uncertainty_distance,
#     "Tunnel_Well_118.csv":uncertainty_distance,
#     "Tunnel_Well_119.csv":uncertainty_distance,
# }
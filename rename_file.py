import os
user = os.environ['USER']

def rename(directory):
    filename = os.listdir(directory)
    for files in filename:
        if files.endswith(".txt"):
            new_name = files.replace("_", "-")
            os.rename(os.path.join(directory, files), os.path.join(directory, new_name)) 
        else:
            pass
    
rename("/USER/Documents/")
from os import walk #lets us walk through different folders!

def import_folder(path):
    surface_list = []
    
    for folder in walk(path):
        print(folder)
    
    
    return surface_list
    

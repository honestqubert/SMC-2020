
def data_dir():
    
    from pathlib import Path
    
    path = Path.cwd()
    while not any(i.name == 'data' for i in path.iterdir()):
        path = path.parent   
        
    return path / 'data'
    

def find_data(folder):
    
    """
    Find a path to a specific folder in the data folder.
    """
    
    paths = list(data_dir().rglob(folder))
    if len(paths) == 1:
        return paths[0]
    else:
        print('Error: more than one path for folder name')
        for i in paths:
            print('{}'.format(i))
            
def get_file(filespec):
    
    file_dict = {'weather':'epvars90m_ChiLoopOnly_2015.Loop.csv',
                 'buildings':'chi0_90m_coord2bldg_smc.csv'}
        

    if filespec in file_dict:
        fname = file_dict[filespec]
        path = data_dir() / filespec / fname
        file_class = File(path)
    else:
        print('File not found')

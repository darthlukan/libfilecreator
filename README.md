# File Creator

> Author: Brian Tomlinson <brian@smartm.no>


## Description

> Creates a file populated with data based on the desired file type and passed in file content values.

> By default, the resulting file is saved in $HOME/$FILE.$EXT ($USER $HOME directory).  If the filename value
> that you pass in contains "/" then the library assumes that you want to write elsewhere, just make sure you 
> have write access to the desired location!


## Usage Example1 (CSV)

    
    from libfilecreator import detect_and_write
    
    filename = "test.csv"
    headers = ["Name", "Country"]
    rows = [
        {"Name": "Odd", "Country": "Norway"},
        {"Name": "Asbjørn", "Country": "Norway"},
        {"Name": "Mikael", "Country": "Norway"},
        {"Name": "Brian", "Country": "USA"}
    ]
    
    # >>> file
    # $HOME/test.csv
    file = detect_and_write(filename, headers, rows)
    


## Usage Example2 (CSV)

    
    from libfilecreator import create_csv
    
    filename = "test.csv"
    headers = ["Name", "Country"]
    rows = [
        {"Name": "Odd", "Country": "Norway"},
        {"Name": "Asbjørn", "Country": "Norway"},
        {"Name": "Mikael", "Country": "Norway"},
        {"Name": "Brian", "Country": "USA"}
    ]
    
    # >>> file
    # $HOME/test.csv
    file = create_csv(filename, headers, rows)
    

# File Creator

> Author: Brian Tomlinson <brian@smartm.no>


## Description

> Creates a file populated with data based on the desired file type and passed in file content values.
> By default, the resulting file is saved in $LIBFILECREATORPATH/files/$FILE.$EXT.  Make sure you have write-access
> to this directory!


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
    # $LIBFILECREATORPATH/files/test.csv
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
    # $LIBFILECREATORPATH/files/test.csv
    file = create_csv(filename, headers, rows)
    

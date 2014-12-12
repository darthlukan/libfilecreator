# ~*~ coding: utf-8 ~*~
import os
import csv


KNOWN_EXTENSIONS = ["csv"]


def create_csv(filename, headers, rows):
    new_filename = "%s/%s" % (os.path.expanduser('~'), filename) if "/" not in filename else filename
    try:
        with open(new_filename, 'wt') as new_csv:
            writer = csv.DictWriter(new_csv, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
    except Exception, e:
        print e.message

    return new_filename


def detect_and_write(filename, headers, rows):
    extension = filename[filename.find(".")+1:]

    if extension.lower() in KNOWN_EXTENSIONS:
        if extension.lower() == 'csv':
            return create_csv(filename, headers, rows)
        else:
            return "Filetype '%s' not yet implemented." % extension
    else:
        raise Exception("Unknown filetype, must be one of: %s" % ",".join(KNOWN_EXTENSIONS))


# Here as a usage example only!
def main():
    filename = "test.csv"
    headers = ["Name", "Country"]
    rows = [
        {"Name": "Odd", "Country": "Norway"},
        {"Name": "Asbjørn", "Country": "Norway"},
        {"Name": "Mikael", "Country": "Norway"},
        {"Name": "Brian", "Country": "USA"}
    ]
    for row in rows:
        row = {unicode(key, "utf-8"): unicode(value, "utf-8") for key, value in row.items()}
        print "row: ", row
    return detect_and_write(filename, headers, rows)


if __name__ == '__main__':
    main()

import csv

# todo keine modifizierung der Zeilen möglich - , oder Nullen dranhängen um ins format von protel zu kommen
with open("testdaten/testdatensatz.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("testdaten/testdatenexport.csv", "w") as export_file:
        csv_writer = csv.writer(export_file, delimiter=",")

        for line in csv_reader:
            writer = csv.writer

            line_protelparameters=["uhu", "aha", "oho"]

            line_new = line + line_protelparameters
            csv_writer.writerow(line_new)




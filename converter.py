import csv

with open("testdaten/testdatensatz.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("testdaten/testdatenexport.csv", "w") as export_file:
        csv_writer = csv.writer(export_file)

        for line in csv_reader:
            writer = csv.writer
            csv_writer.writerow(line)




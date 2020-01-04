import csv


with open("testdaten/testdatensatz.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("testdaten/testdatenexport.csv", "w") as export_file:
        csv_writer = csv.writer(export_file, delimiter=",")
        i=0
        for line in csv_reader:
            writer = csv.writer
            line_protelparameters=["uhu", "aha", "oho"]
# todo iterieren der Kunden
            i = i+1
            anzahl=i
            Line_iteration_kundennummer=[anzahl]

            line_new = Line_iteration_kundennummer + line + line_protelparameters
            csv_writer.writerow(line_new)


            print(line_new)
            #print(Line_iteration_kundennummer)

import csv
#todo Umplaute mit cp1005 formatieren oder wie der schit bei protel simpa import heißt
#todo einzelne Daten aus csv extrahieren ( Name usw, um sie korrekt in der ausgabecsv wiederzugeben

with open("testdaten/testdatensatz.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("testdaten/testdatenexport.csv", "w") as export_file:
        csv_writer = csv.writer(export_file, delimiter=",")

        i=0
        for line in csv_reader:
            writer = csv.writer
            line_protelparameters=["uhu", "aha", "oho"]

            i=i+1
            anzahl=i
            Line_iteration_kundennummer=[anzahl]
            Line_iteration_zero=["0"]
            Line_iteration_mpe = ["1"]
            Line_iteration_emptyvalue= [""]
            Line_iteration_emptydate= ["1900 - 01 - 01"]

            #list_name = [csv_reader[0]]

            line_new = Line_iteration_kundennummer + Line_iteration_zero +Line_iteration_mpe+Line_iteration_zero + line + Line_iteration_emptyvalue + line_protelparameters
            csv_writer.writerow(line_new)


            #print(csv_reader[0])
            print(list_name)
            #print(Line_iteration_kundennummer)

import csv
#todo Umplaute mit cp-1252 formatieren oder wie der schit bei protel simpa import heißt
#todo einzelne Daten aus csv extrahieren ( Name usw, um sie korrekt in der ausgabecsv wiederzugeben

with open("testdaten/testdatensatz.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)


    with open("testdaten/testdatenexport.txt", "w", encoding='cp1252') as export_file:
        #header schreiben
        text = "create table kunden (\"kdnr\" int not null default 0 ,\"cloudref\" int not null default 0 ,\"mpehotel\" int not null default 0 ,\"hotelkdnr\" int not null default 0 ,\"extref\" varchar(15) not null default '' ,\"member\" varchar(50) not null default '' ,\"outlsync\" int not null default 0 ,\"outldate\" datetime not null default '1900-01-01' ,\"passwd\" varchar(15) not null default '' ,\"typ\" int not null default 0 ,\"name1\" varchar(80) not null default '' ,\"name2\" varchar(80) not null default '' ,\"vorname\" varchar(50) not null default '' ,\"ehepartner\" varchar(80) not null default '' ,\"ehegeb\" datetime not null default '1900-01-01' ,\"strasse\" varchar(80) not null default '' ,\"strasse2\" varchar(80) not null default '' ,\"strasse3\" varchar(80) not null default '' ,\"plz\" varchar(17) not null default '' ,\"pfplz\" varchar(17) not null default '' ,\"postfach\" varchar(17) not null default '' ,\"ort\" varchar(50) not null default '' ,\"land\" varchar(80) not null default '' ,\"landkz\" int not null default 0 ,\"regionkz\" int not null default 0 ,\"gender\" int not null default 0 ,\"abteil\" varchar(80) not null default '' ,\"region\" varchar(80) not null default '' ,\"nat\" int not null default 0 ,\"marketing\" int not null default 0 ,\"sprache\" int not null default 0 ,\"vip\" int not null default 0 ,\"gebdat\" datetime not null default '1900-01-01' ,\"anrede\" varchar(40) not null default '' ,\"begr\" varchar(70) not null default '' ,\"telefonnr\" varchar(50) not null default '' ,\"funktel\" varchar(50) not null default '' ,\"email\" varchar(75) not null default '' ,\"twitter\" varchar(80) not null default '' ,\"homepage\" varchar(80) not null default '' ,\"cctypn\" int not null default 0 ,\"ccexp\" varchar(10) not null default '' ,\"cc\" varchar(35) not null default '' ,\"kfz\" varchar(30) not null default '' ,\"faxnr\" varchar(50) not null default '' ,\"telex\" varchar(50) not null default '' ,\"gdsident\" varchar(64) not null default '' ,\"resname\" varchar(80) not null default '' ,\"iata\" varchar(9) not null default '' ,\"contract\" varchar(20) not null default '' ,\"resvorn\" varchar(50) not null default '' ,\"resanr\" varchar(40) not null default '' ,\"restel\" varchar(100) not null default '' ,\"respanr\" varchar(70) not null default '' ,\"rechname\" varchar(80) not null default '' ,\"rechvorn\" varchar(50) not null default '' ,\"rechanr\" varchar(40) not null default '' ,\"rechtel\" varchar(100) not null default '' ,\"rechpanr\" varchar(70) not null default '' ,\"titel\" varchar(20) not null default '' ,\"firmenname\" varchar(50) not null default '' ,\"firmennam2\" varchar(50) not null default '' ,\"beruf\" varchar(50) not null default '' ,\"prof\" int not null default 0 ,\"wunschzi\" int not null default 0 ,\"zimmerattr\" varchar(50) not null default '' ,\"gfeat\" varchar(50) not null default '' ,\"preiscode\" int not null default 0 ,\"comcode\" int not null default 0 ,\"comtax1\" int not null default 0 ,\"comtax2\" int not null default 0 ,\"deleted\" int not null default 0 ,\"kredit\" int not null default 0 ,\"kreditbet\" decimal(19,2) not null default 0 ,\"intcredit\" int not null default 0 ,\"intcredita\" decimal(19,2) not null default 0 ,\"statement\" int not null default 0 ,\"sonderp\" int not null default 0 ,\"sonderp1\" decimal(7,2) not null default 0 ,\"sonderp2\" decimal(7,2) not null default 0 ,\"sonderp3\" decimal(7,2) not null default 0 ,\"sonderp4\" decimal(7,2) not null default 0 ,\"bemerkung\" varchar(250) not null default '' ,\"bemrest\" varchar(250) not null default '' ,\"aufenth\" int not null default 0 ,\"naechte\" int not null default 0 ,\"noshows\" int not null default 0 ,\"stornos\" int not null default 0 ,\"aufenth_vj\" int not null default 0 ,\"naechte_vj\" int not null default 0 ,\"noshows_vj\" int not null default 0 ,\"stornos_vj\" int not null default 0 ,\"letzterauf\" datetime not null default '1900-01-01' ,\"firststay\" datetime not null default '1900-01-01' ,\"erfasst\" datetime not null default '1900-01-01' ,\"erfassttim\" varchar(10) not null default '' ,\"erfasstusr\" varchar(50) not null default '' ,\"letzterpr\" decimal(19,2) not null default 0 ,\"letzteszi\" varchar(10) not null default '' ,\"fibudeb\" varchar(20) not null default '' ,\"logis\" decimal(19,2) not null default 0 ,\"fb\" decimal(19,2) not null default 0 ,\"extras\" decimal(19,2) not null default 0 ,\"logis_vj\" decimal(19,2) not null default 0 ,\"fb_vj\" decimal(19,2) not null default 0 ,\"extras_vj\" decimal(19,2) not null default 0 ,\"transfer\" int not null default 0 ,\"mailing\" int not null default 0 ,\"protected\" int not null default 0 ,\"changed\" datetime not null default '1900-01-01' ,\"changedby\" varchar(50) not null default '' ,\"changetime\" varchar(10) not null default '' ,\"merged\" datetime not null default '1900-01-01' ,\"mergetime\" varchar(10) not null default '' ,\"tosales\" int not null default 0 ,\"passnr\" varchar(30) not null default '' ,\"issued\" varchar(50) not null default '' ,\"issuedate\" datetime not null default '1900-01-01' ,\"discount\" int not null default 0 ,\"doctype\" int not null default 0 ,\"docvalid\" datetime not null default '1900-01-01' ,\"vatno\" varchar(30) not null default '' ,\"flags\" varchar(20) not null default '' ,\"afmno\" varchar(30) not null default '' ,\"gebort\" varchar(50) not null default '' ,\"gebland\" int not null default 0 ,\"mstatus\" int not null default 0 ,\"mahncode\" int not null default 0 ,\"masteracc\" int not null default 0 ,\"masterdeb\" int not null default 0 ,\"ismstdeb\" int not null default 0 ,\"extend\" int not null default 0 ,\"spfrom1\" datetime not null default '1900-01-01' ,\"spfrom2\" datetime not null default '1900-01-01' ,\"spfrom3\" datetime not null default '1900-01-01' ,\"spfrom4\" datetime not null default '1900-01-01' ,\"spto1\" datetime not null default '1900-01-01' ,\"spto2\" datetime not null default '1900-01-01' ,\"spto3\" datetime not null default '1900-01-01' ,\"spto4\" datetime not null default '1900-01-01' ,\"sp1p1\" decimal(7,2) not null default 0 ,\"sp2p1\" decimal(7,2) not null default 0 ,\"sp3p1\" decimal(7,2) not null default 0 ,\"sp4p1\" decimal(7,2) not null default 0 ,\"sp1p2\" decimal(7,2) not null default 0 ,\"sp2p2\" decimal(7,2) not null default 0 ,\"sp3p2\" decimal(7,2) not null default 0 ,\"sp4p2\" decimal(7,2) not null default 0 ,\"sp1p3\" decimal(7,2) not null default 0 ,\"sp2p3\" decimal(7,2) not null default 0 ,\"sp3p3\" decimal(7,2) not null default 0 ,\"sp4p3\" decimal(7,2) not null default 0 ,\"sp1p4\" decimal(7,2) not null default 0 ,\"sp2p4\" decimal(7,2) not null default 0 ,\"sp3p4\" decimal(7,2) not null default 0 ,\"sp4p4\" decimal(7,2) not null default 0 ,\"user00\" varchar(20) not null default '' ,\"user01\" varchar(20) not null default '' ,\"user02\" int not null default 0 ,\"user03\" int not null default 0 ,\"taxexemp\" int not null default 0 ,\"voidfee\" int not null default 0 ,\"depcode\" int not null default 0 ,\"laundry\" int not null default 0 ,\"posrcd\" int not null default 0 ,\"emptybfee\" int not null default 0 ,\"shortname\" varchar(80) not null default '' ,\"mastername\" varchar(80) not null default '' ,\"accountname\" varchar(80) not null default '' ,\"otapara\" varchar(51) not null default '' ,\"numcontacts\" int not null default 0 ,\"numaccounts\" int not null default 0 ,\"addcleansed\" int not null default 0 ,\"cpssrc\" varchar(30) not null default '' ,\"cpsid\" varchar(30) not null default '' ,\"_del\" int not null default 0 )\n"
        export_file.write(text)

        #inhalt schreiben
        csv_writer = csv.writer(export_file, delimiter=",")
        i=0
        for line in csv_reader:
            writer = csv.writer
            #line_protelparameters=["uhu", "aha", "oho"]

            i=i+1
            anzahl=i
            Line_iteration_kundennummer=[anzahl]
            #Line_zero=["0"]
            Line_mpe = ["1"]
            Line_emptyvalue= [""]
            #Line_emptydate= ["1900 - 01 - 01"]
            Line_Karteityp = ["0"]
            Line_Nachname = [line[0]]
            Line_Vorname = [line[1]]
            Line_Strasse = [line[2]]
            Line_plz = [line[3]]
            Line_Stadt = [line[4]]
            Line_Land = [""] #todo land noch anpassen wegen weiterer Tabelle
            Line_landkz = [""]
            Line_nat = [""]
            Line_sprache = [""]
            Line_Anrede = [""]
            Line_Begruessung = [""]
            Line_Tel = [line[5]]
            Line_Mail = [line[6]]


            line_new = Line_iteration_kundennummer + Line_emptyvalue +Line_mpe+ \
                       6 * Line_emptyvalue + Line_Karteityp + Line_Nachname + Line_emptyvalue + Line_Vorname+2 * Line_emptyvalue + \
                       Line_Strasse + 2 * Line_emptyvalue + Line_plz + 2 * Line_emptyvalue + Line_Stadt + Line_Land +Line_landkz + \
                       4 * Line_emptyvalue + Line_nat + Line_emptyvalue + Line_sprache + 2 * Line_emptyvalue + Line_Anrede + Line_Begruessung + \
                       Line_Tel + Line_emptyvalue + Line_Mail + 136 * Line_emptyvalue



            csv_writer.writerow(line_new)


            print(line_new)
            #print(Line_iteration_kundennummer)

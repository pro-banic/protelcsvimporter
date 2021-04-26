import csv

#import csvconverterlayout_support

# todo appendix anhängen wegen weiterer tabellen import - natcode usw
# todo https://wiki.protel.net/index.php?title=Datenkonvertierung#.C3.9Cbernahme_aus_protel_f.C3.BCr_pAIR bis Level 3 Datenübernehmen > testen
# todo UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 440: character maps to <undefined> abfangen wenn nicht lesbare zeichen > durch irgendwas ersetzen - Chinesiche / Russiche Schriftzeichen usw


def createdefaulttabels():

    with open("defaultdatatables.csv", "r", encoding='cp1252') as csv_file:
        csv_reader = csv.reader(csv_file)

    with open("testdaten/testdatenexport-createdefaulttables.txt", "w", encoding='cp1252') as export_file:

        # inhalt schreiben
        csv_writer = csv.writer(export_file, delimiter=",")
        print("exportfile: ", export_file)

    # sollte eigentlich laufen - line_new lässt sich mit oss nicht definieren
    #    for line in csv_reader:
    #        csv_writer.writerow(line_new)
    #       print(line_new)

# createdefaulttabels()


def convertlvl1pairtospe():
    print("start convert lvl1pairtospe")

    with open("testdaten/testdatensatzpair_originalbarnim.csv", "r", encoding='utf8', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)

        with open("testdaten/testdatenexport-lvl1pairtospe.txt", "w", encoding='cp1252', newline="", errors='replace') as export_file:
            # with open("testdaten/testdatenexport-lvl1pairtospe.txt", "wb") as export_file:
            # header schreiben
            text = "create table kunden (\"kdnr\" int not null default 0 ,\"cloudref\" bigint not null default 0 ,\"mpehotel\" int not null default 0 ,\"hotelkdnr\" int not null default 0 ,\"extref\" varchar(15) not null default '' ,\"member\" varchar(50) not null default '' ,\"outlsync\" int not null default 0 ,\"outldate\" datetime not null default '1900-01-01' ,\"passwd\" varchar(15) not null default '' ,\"typ\" int not null default 0 ,\"name1\" varchar(80) not null default '' ,\"name2\" varchar(80) not null default '' ,\"vorname\" varchar(50) not null default '' ,\"ehepartner\" varchar(80) not null default '' ,\"ehegeb\" datetime not null default '1900-01-01' ,\"strasse\" varchar(80) not null default '' ,\"strasse2\" varchar(80) not null default '' ,\"strasse3\" varchar(80) not null default '' ,\"plz\" varchar(17) not null default '' ,\"pfplz\" varchar(17) not null default '' ,\"postfach\" varchar(17) not null default '' ,\"ort\" varchar(50) not null default '' ,\"land\" varchar(80) not null default '' ,\"landkz\" int not null default 0 ,\"regionkz\" int not null default 0 ,\"gender\" int not null default 0 ,\"abteil\" varchar(80) not null default '' ,\"region\" varchar(80) not null default '' ,\"nat\" int not null default 0 ,\"marketing\" int not null default 0 ,\"sprache\" int not null default 0 ,\"vip\" int not null default 0 ,\"gebdat\" datetime not null default '1900-01-01' ,\"anrede\" varchar(40) not null default '' ,\"begr\" varchar(70) not null default '' ,\"telefonnr\" varchar(50) not null default '' ,\"funktel\" varchar(50) not null default '' ,\"email\" varchar(75) not null default '', \"twitter\" varchar(80) not null default '' ,\"homepage\" varchar(80) not null default '' ,\"cctypn\" int not null default 0 ,\"ccexp\" varchar(10) not null default '' ,\"cc\" varchar(35) not null default '' ,\"kfz\" varchar(30) not null default '' ,\"faxnr\" varchar(50) not null default '' ,\"telex\" varchar(50) not null default '' ,\"gdsident\" varchar(64) not null default '' ,\"resname\" varchar(80) not null default '' ,\"iata\" varchar(9) not null default '' ,\"contract\" varchar(20) not null default '' ,\"resvorn\" varchar(50) not null default '' ,\"resanr\" varchar(40) not null default '' ,\"restel\" varchar(100) not null default '' ,\"respanr\" varchar(70) not null default '' ,\"rechname\" varchar(80) not null default '' ,\"rechvorn\" varchar(50) not null default '' ,\"rechanr\" varchar(40) not null default '' ,\"rechtel\" varchar(100) not null default '' ,\"rechpanr\" varchar(70) not null default '' ,\"titel\" varchar(20) not null default '' ,\"firmenname\" varchar(50) not null default '' ,\"firmennam2\" varchar(50) not null default '' ,\"beruf\" varchar(50) not null default '' ,\"prof\" int not null default 0 ,\"wunschzi\" int not null default 0 ,\"zimmerattr\" varchar(50) not null default '' ,\"gfeat\" varchar(50) not null default '' ,\"preiscode\" int not null default 0 ,\"comcode\" int not null default 0 ,\"comtax1\" int not null default 0 ,\"comtax2\" int not null default 0 ,\"deleted\" int not null default 0 ,\"kredit\" int not null default 0 ,\"kreditbet\" decimal(19,2) not null default 0 ,\"intcredit\" int not null default 0 ,\"intcredita\" decimal(19,2) not null default 0 ,\"statement\" int not null default 0 ,\"sonderp\" int not null default 0 ,\"sonderp1\" decimal(7,2) not null default 0 ,\"sonderp2\" decimal(7,2) not null default 0 ,\"sonderp3\" decimal(7,2) not null default 0 ,\"sonderp4\" decimal(7,2) not null default 0 ,\"bemerkung\" varchar(250) not null default '' ,\"bemrest\" varchar(250) not null default '' ,\"aufenth\" int not null default 0 ,\"naechte\" int not null default 0 ,\"noshows\" int not null default 0 ,\"stornos\" int not null default 0 ,\"aufenth_vj\" int not null default 0 ,\"naechte_vj\" int not null default 0 ,\"noshows_vj\" int not null default 0 ,\"stornos_vj\" int not null default 0 ,\"letzterauf\" datetime not null default '1900-01-01' ,\"firststay\" datetime not null default '1900-01-01' ,\"erfasst\" datetime not null default '1900-01-01' ,\"erfassttim\" varchar(10) not null default '' ,\"erfasstusr\" varchar(50) not null default '' ,\"letzterpr\" decimal(19,2) not null default 0 ,\"letzteszi\" varchar(10) not null default '' ,\"fibudeb\" varchar(20) not null default '' ,\"logis\" decimal(19,2) not null default 0 ,\"fb\" decimal(19,2) not null default 0 ,\"extras\" decimal(19,2) not null default 0 ,\"logis_vj\" decimal(19,2) not null default 0 ,\"fb_vj\" decimal(19,2) not null default 0 ,\"extras_vj\" decimal(19,2) not null default 0 ,\"transfer\" int not null default 0 ,\"mailing\" int not null default 0 ,\"protected\" int not null default 0 ,\"changed\" datetime not null default '1900-01-01' ,\"changedby\" varchar(50) not null default '' ,\"changetime\" varchar(10) not null default '' ,\"merged\" datetime not null default '1900-01-01' ,\"mergetime\" varchar(10) not null default '' ,\"tosales\" int not null default 0 ,\"passnr\" varchar(30) not null default '' ,\"issued\" varchar(50) not null default '' ,\"issuedate\" datetime not null default '1900-01-01' ,\"discount\" int not null default 0 ,\"doctype\" int not null default 0 ,\"docvalid\" datetime not null default '1900-01-01' ,\"vatno\" varchar(30) not null default '' ,\"flags\" varchar(20) not null default '' ,\"afmno\" varchar(30) not null default '' ,\"gebort\" varchar(50) not null default '' ,\"gebland\" int not null default 0 ,\"mstatus\" int not null default 0 ,\"mahncode\" int not null default 0 ,\"masteracc\" int not null default 0 ,\"masterdeb\" int not null default 0 ,\"ismstdeb\" int not null default 0 ,\"extend\" int not null default 0 ,\"spfrom1\" datetime not null default '1900-01-01' ,\"spfrom2\" datetime not null default '1900-01-01' ,\"spfrom3\" datetime not null default '1900-01-01' ,\"spfrom4\" datetime not null default '1900-01-01' ,\"spto1\" datetime not null default '1900-01-01' ,\"spto2\" datetime not null default '1900-01-01' ,\"spto3\" datetime not null default '1900-01-01' ,\"spto4\" datetime not null default '1900-01-01' ,\"sp1p1\" decimal(7,2) not null default 0 ,\"sp2p1\" decimal(7,2) not null default 0 ,\"sp3p1\" decimal(7,2) not null default 0 ,\"sp4p1\" decimal(7,2) not null default 0 ,\"sp1p2\" decimal(7,2) not null default 0 ,\"sp2p2\" decimal(7,2) not null default 0 ,\"sp3p2\" decimal(7,2) not null default 0 ,\"sp4p2\" decimal(7,2) not null default 0 ,\"sp1p3\" decimal(7,2) not null default 0 ,\"sp2p3\" decimal(7,2) not null default 0 ,\"sp3p3\" decimal(7,2) not null default 0 ,\"sp4p3\" decimal(7,2) not null default 0 ,\"sp1p4\" decimal(7,2) not null default 0 ,\"sp2p4\" decimal(7,2) not null default 0 ,\"sp3p4\" decimal(7,2) not null default 0 ,\"sp4p4\" decimal(7,2) not null default 0 ,\"user00\" varchar(20) not null default '' ,\"user01\" varchar(20) not null default '' ,\"user02\" int not null default 0 ,\"user03\" int not null default 0 ,\"taxexemp\" int not null default 0 ,\"voidfee\" int not null default 0 ,\"depcode\" int not null default 0 ,\"laundry\" int not null default 0 ,\"posrcd\" int not null default 0 ,\"emptybfee\" int not null default 0 ,\"shortname\" varchar(80) not null default '' ,\"mastername\" varchar(80) not null default '' ,\"accountname\" varchar(80) not null default '' ,\"otapara\" varchar(51) not null default '' ,\"numcontacts\" int not null default 0 ,\"numaccounts\" int not null default 0 ,\"addcleansed\" int not null default 0 ,\"cpssrc\" varchar(30) not null default '' ,\"cpsid\" varchar(30) not null default '' ,\"_del\" int not null default 0 )\n"
            export_file.write(text)

            print("headertext: ", text)
            try:
                # inhalt schreiben
                csv_writer = csv.writer(export_file, delimiter=",")
                print("exportfile: ", export_file)
                i = 2000
                for line in csv_reader:
                    #writer = csv.writer
                    # line_protelparameters=["uhu", "aha", "oho"]

                    i = i + 1
                    anzahl = i
                    Line_iteration_kundennummer = [anzahl]
                    # Line_zero=["0"]
                    Line_mpe = ["1"]
                    Line_punktnull = [".00"]
                    Line_emptyvalue = ["''"]
                    # Line_emptydate= ["1900 - 01 - 01"]
                    if line[2] == "Firma":
                        # todo 0 ist privat / 1 ist Firma > wenn Feld 3 (saltut) == Firma > dann mach hier eine 1 rein
                        Line_Karteityp = ["1"]
                    else:
                        Line_Karteityp = ["0"]

                    if line[5] == "":
                        Line_Nachname = ["'"+line[8]+"'"]
                    else:
                        Line_Nachname = ["'" + line[5] + "'"]
                    Line_Vorname = ["'"+line[4]+"'"]
                    Line_Strasse = ["'"+line[13]+"'"]

                    if line[16] == "":
                        Line_plz = ["''"]
                    else:
                        Line_plz = ["'"+line[16]+"'"]
                    Line_Stadt = ["'"+line[17]+"'"]

                    if line[10] == "DE":
                        # todo land noch anpassen wegen weiterer Tabelle
                        Line_Land = ["'"+"Deutschland"+"'"]
                    else:
                        Line_Land = ["''"]

                    if line[10] == "DE":
                        Line_landkz = ["4"]  # natcode.natcodenr
                    else:
                        Line_landkz = ["''"]
                    if line[7] == "de_DE":
                        Line_nat = [4]  # todo noch checken
                    elif line[7] == "nl_NL":
                        Line_nat = [18]
                    elif line[7] == "en_US":
                        Line_nat = [1]
                    else:
                        Line_nat = ["''"]

                    if line[10] == "DE":
                        Line_sprache = ["4"]  # todo noch checken
                    else:
                        Line_sprache = ["''"]

                    Line_Anrede = ["'"+line[2]+"'"]
                    if line[2] == "Herr":
                        # todo sehr geehrter Herr / Frau + Line_Anrede = [line[2]] + Line_Nachname = [line[5]] // bei Firma > sehr geehrte Damen und Herren
                        Line_Begruessung = ["'"+"Sehr geehrter Herr"+"'"]
                    elif line[2] == "Frau":
                        Line_Begruessung = ["'"+"Sehr geehrte Frau"+"'"]
                    elif line[2] == "Firma":
                        Line_Begruessung = [
                            "'"+"Sehr geehrte Damen und Herren"+"'"]
                    elif line[2] == "Familie":
                        Line_Begruessung = ["'"+"Sehr geehrte Familie"+"'"]
                    else:
                        Line_Begruessung = ["''"]
                    Line_Tel = ["'"+line[19]+"'"]
                    Line_Mail = ["'"+line[21]+"'"]

                    # Line_finaltextamanfangeinezuviel = [",\'\',\'\',0,\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'Dr.\',\'BHW Lebensversicherung AG \',\'\',\'\',0,0,\'\',\'\',0,0,0,0,0,0,.00,0,.00,0,0,.00,.00,.00,.00,\'Stammgastkarte #1445, 29.09. HZ-Tag\',\'\',0,0,0,0,1,2,0,0,\'1900-01-01 00:00:00.000\',\'2007-02-23 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'\',\'\',.00,\'\',\'0\',.00,.00,.00,.00,.00,.00,0,0,0,\'1900-01-01 00:00:00.000\',\'\',\'\',\'1900-01-01 00:00:00.000\',\'\',0,\'\',\'\',\'1900-01-01 00:00:00.000\',0,0,\'1900-01-01 00:00:00.000\',\'\',\'\',\'\',\'\',0,0,0,0,0,0,0,\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,\'DE\',\'\',0,10,0,0,0,0,0,0,\'\',\'\',\'\',\'\',0,0,0,\'\',\'\',0\n"]
                    # Line_finaltext = [\'\',\'\',0,\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'\',\'Dr.\',\'BHW Lebensversicherung AG \',\'\',\'\',0,0,\'\',\'\',0,0,0,0,0,0,.00,0,.00,0,0,.00,.00,.00,.00,\'Stammgastkarte #1445, 29.09. HZ-Tag\',\'\',0,0,0,0,1,2,0,0,\'1900-01-01 00:00:00.000\',\'2007-02-23 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'\',\'\',.00,\'\',\'0\',.00,.00,.00,.00,.00,.00,0,0,0,\'1900-01-01 00:00:00.000\',\'\',\'\',\'1900-01-01 00:00:00.000\',\'\',0,\'\',\'\',\'1900-01-01 00:00:00.000\',0,0,\'1900-01-01 00:00:00.000\',\'\',\'\',\'\',\'\',0,0,0,0,0,0,0,\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',\'1900-01-01 00:00:00.000\',.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,.00,\'DE\',\'\',0,10,0,0,0,0,0,0,\'\',\'\',\'\',\'\',0,0,0,\'\',\'\',0]

                    line_new = Line_iteration_kundennummer + Line_emptyvalue + Line_mpe + \
                        6 * Line_emptyvalue + Line_Karteityp + Line_Nachname + Line_emptyvalue + Line_Vorname + 2 * Line_emptyvalue + \
                        Line_Strasse + 2 * Line_emptyvalue + Line_plz + 2 * Line_emptyvalue + Line_Stadt + Line_Land + Line_landkz + \
                        4 * Line_emptyvalue + Line_nat + Line_emptyvalue + Line_sprache + 2 * Line_emptyvalue + Line_Anrede + Line_Begruessung + \
                        Line_Tel + Line_emptyvalue + Line_Mail + 35 * Line_emptyvalue + Line_punktnull + Line_emptyvalue + Line_punktnull + 2 * Line_emptyvalue + \
                        4 * Line_punktnull + 15 * Line_emptyvalue + Line_punktnull + 2 * Line_emptyvalue + 6 * Line_punktnull + 34 * Line_emptyvalue + \
                        16 * Line_punktnull + 20 * Line_emptyvalue

                    #138 * Line_emptyvalue

                    csv_writer.writerow(line_new)

                    print(line_new)
            except UnicodeDecodeError as err:
                print("UnicodeDecodeError {0}".format(err))
                print("UnicodeEncodeError {0}".format(err))
# convertlvl1pairtospe()


def csvtolvl1():
    # TODO Fax Nummer noch hinterlegen und importierbar machen

    with open("testdaten/LVL1-Import-Gästedaten.csv", "r", encoding='utf8', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        # Test wie importdatei eingelesen wird:
        # for line in csv_reader:
        #   print("Importdatei inhalt: ", line)
        # utf 8 wäre eine Alternative: with open("testdaten/testdatensatz.csv", "r", encoding='utf8', errors='ignore') as csv_file:

        # csv.reader(csvfile, dialect='excel', **fmtparams)¶
        # excel dateien direkt einlesen?

        with open("testdaten/testdatenexport-lvl1.txt", "w", encoding='cp1252') as export_file:
            # header schreiben
            header = "create table kunden (\"kdnr\" int not null default 0 ,\"cloudref\" bigint not null default 0 ,\"mpehotel\" int not null default 0 ,\"hotelkdnr\" int not null default 0 ,\"extref\" varchar(15) not null default '' ,\"member\" varchar(50) not null default '' ,\"outlsync\" int not null default 0 ,\"outldate\" datetime not null default '1900-01-01' ,\"passwd\" varchar(15) not null default '' ,\"typ\" int not null default 0 ,\"name1\" varchar(80) not null default '' ,\"name2\" varchar(80) not null default '' ,\"vorname\" varchar(50) not null default '' ,\"ehepartner\" varchar(80) not null default '' ,\"ehegeb\" datetime not null default '1900-01-01' ,\"strasse\" varchar(80) not null default '' ,\"strasse2\" varchar(80) not null default '' ,\"strasse3\" varchar(80) not null default '' ,\"plz\" varchar(17) not null default '' ,\"pfplz\" varchar(17) not null default '' ,\"postfach\" varchar(17) not null default '' ,\"ort\" varchar(50) not null default '' ,\"land\" varchar(80) not null default '' ,\"landkz\" int not null default 0 ,\"regionkz\" int not null default 0 ,\"gender\" int not null default 0 ,\"abteil\" varchar(80) not null default '' ,\"region\" varchar(80) not null default '' ,\"nat\" int not null default 0 ,\"marketing\" int not null default 0 ,\"sprache\" int not null default 0 ,\"vip\" int not null default 0 ,\"gebdat\" datetime not null default '1900-01-01' ,\"anrede\" varchar(40) not null default '' ,\"begr\" varchar(70) not null default '' ,\"telefonnr\" varchar(50) not null default '' ,\"funktel\" varchar(50) not null default '' ,\"email\" varchar(75) not null default '' ,\"twitter\" varchar(80) not null default '' ,\"homepage\" varchar(80) not null default '' ,\"cctypn\" int not null default 0 ,\"ccexp\" varchar(10) not null default '' ,\"cc\" varchar(35) not null default '' ,\"kfz\" varchar(30) not null default '' ,\"faxnr\" varchar(50) not null default '' ,\"telex\" varchar(50) not null default '' ,\"gdsident\" varchar(64) not null default '' ,\"resname\" varchar(80) not null default '' ,\"iata\" varchar(9) not null default '' ,\"contract\" varchar(20) not null default '' ,\"resvorn\" varchar(50) not null default '' ,\"resanr\" varchar(40) not null default '' ,\"restel\" varchar(100) not null default '' ,\"respanr\" varchar(70) not null default '' ,\"rechname\" varchar(80) not null default '' ,\"rechvorn\" varchar(50) not null default '' ,\"rechanr\" varchar(40) not null default '' ,\"rechtel\" varchar(100) not null default '' ,\"rechpanr\" varchar(70) not null default '' ,\"titel\" varchar(20) not null default '' ,\"firmenname\" varchar(50) not null default '' ,\"firmennam2\" varchar(50) not null default '' ,\"beruf\" varchar(50) not null default '' ,\"prof\" int not null default 0 ,\"wunschzi\" int not null default 0 ,\"zimmerattr\" varchar(50) not null default '' ,\"gfeat\" varchar(50) not null default '' ,\"preiscode\" int not null default 0 ,\"comcode\" int not null default 0 ,\"comtax1\" int not null default 0 ,\"comtax2\" int not null default 0 ,\"deleted\" int not null default 0 ,\"kredit\" int not null default 0 ,\"kreditbet\" decimal(19,2) not null default 0 ,\"intcredit\" int not null default 0 ,\"intcredita\" decimal(19,2) not null default 0 ,\"statement\" int not null default 0 ,\"sonderp\" int not null default 0 ,\"sonderp1\" decimal(7,2) not null default 0 ,\"sonderp2\" decimal(7,2) not null default 0 ,\"sonderp3\" decimal(7,2) not null default 0 ,\"sonderp4\" decimal(7,2) not null default 0 ,\"bemerkung\" varchar(250) not null default '' ,\"bemrest\" varchar(250) not null default '' ,\"aufenth\" int not null default 0 ,\"naechte\" int not null default 0 ,\"noshows\" int not null default 0 ,\"stornos\" int not null default 0 ,\"aufenth_vj\" int not null default 0 ,\"naechte_vj\" int not null default 0 ,\"noshows_vj\" int not null default 0 ,\"stornos_vj\" int not null default 0 ,\"letzterauf\" datetime not null default '1900-01-01' ,\"firststay\" datetime not null default '1900-01-01' ,\"erfasst\" datetime not null default '1900-01-01' ,\"erfassttim\" varchar(10) not null default '' ,\"erfasstusr\" varchar(50) not null default '' ,\"letzterpr\" decimal(19,2) not null default 0 ,\"letzteszi\" varchar(10) not null default '' ,\"fibudeb\" varchar(20) not null default '' ,\"logis\" decimal(19,2) not null default 0 ,\"fb\" decimal(19,2) not null default 0 ,\"extras\" decimal(19,2) not null default 0 ,\"logis_vj\" decimal(19,2) not null default 0 ,\"fb_vj\" decimal(19,2) not null default 0 ,\"extras_vj\" decimal(19,2) not null default 0 ,\"transfer\" int not null default 0 ,\"mailing\" int not null default 0 ,\"protected\" int not null default 0 ,\"changed\" datetime not null default '1900-01-01' ,\"changedby\" varchar(50) not null default '' ,\"changetime\" varchar(10) not null default '' ,\"merged\" datetime not null default '1900-01-01' ,\"mergetime\" varchar(10) not null default '' ,\"tosales\" int not null default 0 ,\"passnr\" varchar(30) not null default '' ,\"issued\" varchar(50) not null default '' ,\"issuedate\" datetime not null default '1900-01-01' ,\"discount\" int not null default 0 ,\"doctype\" int not null default 0 ,\"docvalid\" datetime not null default '1900-01-01' ,\"vatno\" varchar(30) not null default '' ,\"flags\" varchar(20) not null default '' ,\"afmno\" varchar(30) not null default '' ,\"gebort\" varchar(50) not null default '' ,\"gebland\" int not null default 0 ,\"mstatus\" int not null default 0 ,\"mahncode\" int not null default 0 ,\"masteracc\" int not null default 0 ,\"masterdeb\" int not null default 0 ,\"ismstdeb\" int not null default 0 ,\"extend\" int not null default 0 ,\"spfrom1\" datetime not null default '1900-01-01' ,\"spfrom2\" datetime not null default '1900-01-01' ,\"spfrom3\" datetime not null default '1900-01-01' ,\"spfrom4\" datetime not null default '1900-01-01' ,\"spto1\" datetime not null default '1900-01-01' ,\"spto2\" datetime not null default '1900-01-01' ,\"spto3\" datetime not null default '1900-01-01' ,\"spto4\" datetime not null default '1900-01-01' ,\"sp1p1\" decimal(7,2) not null default 0 ,\"sp2p1\" decimal(7,2) not null default 0 ,\"sp3p1\" decimal(7,2) not null default 0 ,\"sp4p1\" decimal(7,2) not null default 0 ,\"sp1p2\" decimal(7,2) not null default 0 ,\"sp2p2\" decimal(7,2) not null default 0 ,\"sp3p2\" decimal(7,2) not null default 0 ,\"sp4p2\" decimal(7,2) not null default 0 ,\"sp1p3\" decimal(7,2) not null default 0 ,\"sp2p3\" decimal(7,2) not null default 0 ,\"sp3p3\" decimal(7,2) not null default 0 ,\"sp4p3\" decimal(7,2) not null default 0 ,\"sp1p4\" decimal(7,2) not null default 0 ,\"sp2p4\" decimal(7,2) not null default 0 ,\"sp3p4\" decimal(7,2) not null default 0 ,\"sp4p4\" decimal(7,2) not null default 0 ,\"user00\" varchar(20) not null default '' ,\"user01\" varchar(20) not null default '' ,\"user02\" int not null default 0 ,\"user03\" int not null default 0 ,\"taxexemp\" int not null default 0 ,\"voidfee\" int not null default 0 ,\"depcode\" int not null default 0 ,\"laundry\" int not null default 0 ,\"posrcd\" int not null default 0 ,\"emptybfee\" int not null default 0 ,\"shortname\" varchar(80) not null default '' ,\"mastername\" varchar(80) not null default '' ,\"accountname\" varchar(80) not null default '' ,\"otapara\" varchar(51) not null default '' ,\"numcontacts\" int not null default 0 ,\"numaccounts\" int not null default 0 ,\"addcleansed\" int not null default 0 ,\"cpssrc\" varchar(30) not null default '' ,\"cpsid\" varchar(30) not null default '' ,\"_del\" int not null default 0 )\n"
            export_file.write(header)
            #print("headertext: ", text)

            # inhalt schreiben
            csv_writer = csv.writer(export_file, delimiter=",")
            print("exportfile: ", export_file)
            inhaltssammler = []
            j = 0  # index com Zähler
            i = 2000
            for line in csv_reader:
                writer = csv.writer
                i = i + 1
                anzahl = i
                Line_iteration_kundennummer = [anzahl]
                Line_mpe = ["1"]
                Line_emptyvalue = [""]
                Line_emptydate = ["1900 - 01 - 01"]
                Line_Karteityp = ["0"]
                Line_Nachname = [line[0]]
                Line_Vorname = [line[1]]
                Line_Strasse = [line[2]]
                Line_plz = [line[3]]
                Line_Stadt = [line[4]]
                # todo land noch anpassen wegen weiterer Tabelle
                Line_Land = [line[5]]  # Deutschland
                Line_landkz = [line[6]]  # DE
                Line_gender = [line[7]]  # 1 = männlich, 2 = weiblich
                # nat = 1 für Deutschland > siehe "codenr" bei header natcode
                Line_nat = [1]  # 1 für Deutschland!
                Line_sprache = [""]  # 4 für Deutschland?

                # Line_Anrede = [line[12]]  # Frau
                #Line_Anrede = [""]
                if [line[7]] == ["1"]:
                    Line_Anrede = ["Herr"]
                elif [line[7]] == ["2"]:
                    Line_Anrede = ["Frau"]
                elif [line[7]] != ["2"] or ["1"]:
                    Line_Anrede = ["Guten Tag"]

                Line_Begruessung = [line[10]]  # Sehr geehrte Frau XY
                Line_Tel = [line[9]]
                Line_Mail = [line[8]]

                line_new = Line_iteration_kundennummer + Line_emptyvalue + Line_mpe + \
                    6 * Line_emptyvalue + Line_Karteityp + Line_Nachname + Line_emptyvalue + Line_Vorname + 2 * Line_emptyvalue + \
                    Line_Strasse + 2 * Line_emptyvalue + Line_plz + 2 * Line_emptyvalue + Line_Stadt + Line_Land + Line_landkz + \
                    Line_emptyvalue + Line_gender + \
                    2 * Line_emptyvalue + Line_nat + Line_emptyvalue + Line_sprache + 2 * Line_emptyvalue + Line_Anrede + Line_Begruessung + \
                    Line_Tel + Line_emptyvalue + Line_Mail + 136 * Line_emptyvalue

                # debugtest # line_new = Line_iteration_kundennummer + Line_mpe + Line_Nachname + \
                Line_Vorname + Line_Strasse + Line_plz + Line_Stadt

                csv_writer.writerow(line_new)

                print(line_new)
                j += 1
                if Line_Mail != "":
                    #gcomline = [j, Line_iteration_kundennummer, 1, Line_Mail]
                    gcomline = j, Line_iteration_kundennummer, 1, Line_Mail
                    # 1,838,1,'test@test.de','',0,0
                    # i,Kundennummer,Kommunikationsart,Inhalt,'',0,0
                    inhaltssammler.append(gcomline)
            print("updated Inhaltssammler:", inhaltssammler)

            # header natcode schreiben
            header_natcode = "create table natcode (\"abkuerz\" varchar(20) not null default '' ,\"land\" varchar(80) not null default '' ,\"statnr\" int not null default 0 ,\"codenr\" int not null default 0 ,\"sort\" int not null default 0 ,\"gruppe\" int not null default 0 ,\"brkopftyp\" int not null default 0 ,\"sprache\" int not null default 0 ,\"isocode\" varchar(4) not null default '' ,\"state\" varchar(80) not null default '' ,\"showfo\" int not null default 0 ,\"inet\" int not null default 0 ,\"nation\" varchar(80) not null default '' ,\"addinfo\" varchar(50) not null default '' ,\"user01\" int not null default 0 ,\"anreisen1\" int not null default 0 ,\"anzueber1\" int not null default 0 ,\"anreisen2\" int not null default 0 ,\"anzueber2\" int not null default 0 ,\"anreisen3\" int not null default 0 ,\"anzueber3\" int not null default 0 ,\"anreisen4\" int not null default 0 ,\"anzueber4\" int not null default 0 ,\"anreisen5\" int not null default 0 ,\"anzueber5\" int not null default 0 ,\"anreisen6\" int not null default 0 ,\"anzueber6\" int not null default 0 ,\"anreisen7\" int not null default 0 ,\"anzueber7\" int not null default 0 ,\"anreisen8\" int not null default 0 ,\"anzueber8\" int not null default 0 ,\"anreisen9\" int not null default 0 ,\"anzueber9\" int not null default 0 ,\"anreisen10\" int not null default 0 ,\"anzueber10\" int not null default 0 ,\"anreisen11\" int not null default 0 ,\"anzueber11\" int not null default 0 ,\"anreisen12\" int not null default 0 ,\"anzueber12\" int not null default 0 )\n"
            export_file.write(header_natcode)

            content_table_natcode = "'D','Deutschland',13,1,0,0,0,4,'DE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n'A','Österreich',33,15,0,0,2,-1,'AT','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n'DK','Dänemark',22,4,0,0,2,-1,'DK','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            export_file.write(content_table_natcode)

            # header natcode > 1 = Deutschland
            # create table natcode ("abkuerz" varchar(20) not null default '' ,"land" varchar(80) not null default '' ,"statnr" int not null default 0 ,"codenr" int not null default 0 ,"sort" int not null default 0 ,"gruppe" int not null default 0 ,"brkopftyp" int not null default 0 ,"sprache" int not null default 0 ,"isocode" varchar(4) not null default '' ,"state" varchar(80) not null default '' ,"showfo" int not null default 0 ,"inet" int not null default 0 ,"nation" varchar(80) not null default '' ,"addinfo" varchar(50) not null default '' ,"user01" int not null default 0 ,"anreisen1" int not null default 0 ,"anzueber1" int not null default 0 ,"anreisen2" int not null default 0 ,"anzueber2" int not null default 0 ,"anreisen3" int not null default 0 ,"anzueber3" int not null default 0 ,"anreisen4" int not null default 0 ,"anzueber4" int not null default 0 ,"anreisen5" int not null default 0 ,"anzueber5" int not null default 0 ,"anreisen6" int not null default 0 ,"anzueber6" int not null default 0 ,"anreisen7" int not null default 0 ,"anzueber7" int not null default 0 ,"anreisen8" int not null default 0 ,"anzueber8" int not null default 0 ,"anreisen9" int not null default 0 ,"anzueber9" int not null default 0 ,"anreisen10" int not null default 0 ,"anzueber10" int not null default 0 ,"anreisen11" int not null default 0 ,"anzueber11" int not null default 0 ,"anreisen12" int not null default 0 ,"anzueber12" int not null default 0 )
            #'BS','Baltische Staaten',20,2,0,0,0,0,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            #'EU','Sonstiges Europa',43,25,0,0,0,0,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            #'RS','Republik Südafrika',50,26,0,0,0,0,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            #'GOL','Arabische Golfstaaten',60,28,0,0,0,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            #'CHI','China & Honkong',61,29,0,0,0,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'IL','Israel',62,30,0,0,0,-1,'IL','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'J','Japan',63,31,0,0,0,0,'JP','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'SKO','Südkorea',64,32,0,0,0,-1,'KP','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'TWA','Taiwan',65,33,0,0,0,0,'TW','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            #'ASI','Sonstiges Asien',66,34,0,0,0,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'AMS','Mittelamerika',72,37,0,0,0,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'SAM','Südamerika',74,39,0,0,0,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            #'OA','Ohne Angaben',90,41,0,0,0,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'D','Deutschland',13,1,0,0,0,4,'DE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'A','Österreich',33,15,0,0,2,-1,'AT','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            #'AFR','Sonstige Afrikanische',55,27,0,0,2,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'B','Belgien',21,3,0,0,2,-1,'BE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'BRA','Brasilien',73,38,0,0,2,-1,'BR','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'CAN','Kanada',70,35,0,0,2,-1,'CA','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'CH','Schweiz',38,20,0,0,2,-1,'CH','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'DK','Dänemark',22,4,0,0,2,-1,'DK','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'S','Schweden',37,19,0,0,2,-1,'SE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            #'CZ','Tschische Republik',40,22,0,0,2,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'E','Spanien',39,21,0,0,2,-1,'ES','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'F','Frankreich',24,6,0,0,2,-1,'FR','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'FI','Finnland',23,5,0,0,2,-1,'FI','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'GB','Großbritanien',26,8,0,0,1,-1,'en','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'GR','Griechenland',25,7,0,0,2,-1,'GR','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'H','Ungarn',42,24,0,0,2,-1,'HU','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'I','Italien',29,11,0,0,2,-1,'IT','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'IRL','Irland',27,9,0,0,2,-1,'IE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'ISL','Island',28,10,0,0,2,-1,'IS','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'L','Luxembourg',30,12,0,0,2,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'N','Norwegen',32,14,0,0,2,-1,'NO','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'P','Portugal',35,17,0,0,2,-1,'PT','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'PL','Polen',34,16,0,0,2,-1,'PL','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'GUS','Rußland',36,18,0,0,2,-1,'RU','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'TK','Türkei',41,23,0,0,2,-1,'TR','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'USA','USA',71,36,0,0,2,-1,'US','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'NL','Niederlande',31,13,0,0,2,-1,'NL','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            # 'AUS','Australien',75,40,0,0,0,-1,'AU','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0


csvtolvl1()


def addgcomtolvl1():
    '''zu Level 1 müssen noch die Mailadressen und Telefonnummer usw als GCom Tabelle hinzugefügt werden'''

    # vorab erstellten lvl 1 Datensatz wieder einlesen:
    with open("testdaten/testdatenexport-lvl1.txt", "r", encoding='utf8', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print("Importdatei inhalt: ", line)

        with open("testdaten/testdatenexport-lvl2.txt", "w", encoding='cp1252') as export_file:
            # table gcom schreiben > Kommunikationsmöglichkeiten pro Gast
            table_gcom = "create table gcom (\"ref\" int not null default 0 ,\"kdnr\" int not null default 0 ,\"type\" int not null default 0 ,\"entry\" varchar(250) not null default '' ,\"info\" varchar(250) not null default '' ,\"prim\" int not null default 0 ,\"_del\" int not null default 0 )\n"
            export_file.write(table_gcom)

            '''
            # Inhalt table gcom schreiben 
            i=1
            i+=i
            #1,838,1,'test@test.de','',0,0
            i,Kundennummer,Kommunikationsart,Inhalt,'',0,0
            content_table_gcom = "'D','Deutschland',13,1,0,0,0,4,'DE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n'A','Österreich',33,15,0,0,2,-1,'AT','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n'DK','Dänemark',22,4,0,0,2,-1,'DK','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n"
            export_file.write(content_table_natcode)
            '''

# addgcomtolvl1()


def convertlvl1():
    print("start convert")
    #old and not working
    #csvconverterlayout_support = "testdaten/testdatensatz.csv"
    #csv_reader = csv.reader(csvconverterlayout_support)
    #print("Importdatei inhalt: ", csv_reader)

    with open("testdaten/testdatensatz.csv", "r", encoding='utf8', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)
        print("Importdatei inhalt: ", csv_reader)

    with open("testdaten/testdatenexport-lvl1.txt", "w", encoding='cp1252') as export_file:
        # header schreiben
        text = "create table kunden (\"kdnr\" int not null default 0 ,\"cloudref\" bigint not null default 0 ,\"mpehotel\" int not null default 0 ,\"hotelkdnr\" int not null default 0 ,\"extref\" varchar(15) not null default '' ,\"member\" varchar(50) not null default '' ,\"outlsync\" int not null default 0 ,\"outldate\" datetime not null default '1900-01-01' ,\"passwd\" varchar(15) not null default '' ,\"typ\" int not null default 0 ,\"name1\" varchar(80) not null default '' ,\"name2\" varchar(80) not null default '' ,\"vorname\" varchar(50) not null default '' ,\"ehepartner\" varchar(80) not null default '' ,\"ehegeb\" datetime not null default '1900-01-01' ,\"strasse\" varchar(80) not null default '' ,\"strasse2\" varchar(80) not null default '' ,\"strasse3\" varchar(80) not null default '' ,\"plz\" varchar(17) not null default '' ,\"pfplz\" varchar(17) not null default '' ,\"postfach\" varchar(17) not null default '' ,\"ort\" varchar(50) not null default '' ,\"land\" varchar(80) not null default '' ,\"landkz\" int not null default 0 ,\"regionkz\" int not null default 0 ,\"gender\" int not null default 0 ,\"abteil\" varchar(80) not null default '' ,\"region\" varchar(80) not null default '' ,\"nat\" int not null default 0 ,\"marketing\" int not null default 0 ,\"sprache\" int not null default 0 ,\"vip\" int not null default 0 ,\"gebdat\" datetime not null default '1900-01-01' ,\"anrede\" varchar(40) not null default '' ,\"begr\" varchar(70) not null default '' ,\"telefonnr\" varchar(50) not null default '' ,\"funktel\" varchar(50) not null default '' ,\"email\" varchar(75) not null default '' ,\"twitter\" varchar(80) not null default '' ,\"homepage\" varchar(80) not null default '' ,\"cctypn\" int not null default 0 ,\"ccexp\" varchar(10) not null default '' ,\"cc\" varchar(35) not null default '' ,\"kfz\" varchar(30) not null default '' ,\"faxnr\" varchar(50) not null default '' ,\"telex\" varchar(50) not null default '' ,\"gdsident\" varchar(64) not null default '' ,\"resname\" varchar(80) not null default '' ,\"iata\" varchar(9) not null default '' ,\"contract\" varchar(20) not null default '' ,\"resvorn\" varchar(50) not null default '' ,\"resanr\" varchar(40) not null default '' ,\"restel\" varchar(100) not null default '' ,\"respanr\" varchar(70) not null default '' ,\"rechname\" varchar(80) not null default '' ,\"rechvorn\" varchar(50) not null default '' ,\"rechanr\" varchar(40) not null default '' ,\"rechtel\" varchar(100) not null default '' ,\"rechpanr\" varchar(70) not null default '' ,\"titel\" varchar(20) not null default '' ,\"firmenname\" varchar(50) not null default '' ,\"firmennam2\" varchar(50) not null default '' ,\"beruf\" varchar(50) not null default '' ,\"prof\" int not null default 0 ,\"wunschzi\" int not null default 0 ,\"zimmerattr\" varchar(50) not null default '' ,\"gfeat\" varchar(50) not null default '' ,\"preiscode\" int not null default 0 ,\"comcode\" int not null default 0 ,\"comtax1\" int not null default 0 ,\"comtax2\" int not null default 0 ,\"deleted\" int not null default 0 ,\"kredit\" int not null default 0 ,\"kreditbet\" decimal(19,2) not null default 0 ,\"intcredit\" int not null default 0 ,\"intcredita\" decimal(19,2) not null default 0 ,\"statement\" int not null default 0 ,\"sonderp\" int not null default 0 ,\"sonderp1\" decimal(7,2) not null default 0 ,\"sonderp2\" decimal(7,2) not null default 0 ,\"sonderp3\" decimal(7,2) not null default 0 ,\"sonderp4\" decimal(7,2) not null default 0 ,\"bemerkung\" varchar(250) not null default '' ,\"bemrest\" varchar(250) not null default '' ,\"aufenth\" int not null default 0 ,\"naechte\" int not null default 0 ,\"noshows\" int not null default 0 ,\"stornos\" int not null default 0 ,\"aufenth_vj\" int not null default 0 ,\"naechte_vj\" int not null default 0 ,\"noshows_vj\" int not null default 0 ,\"stornos_vj\" int not null default 0 ,\"letzterauf\" datetime not null default '1900-01-01' ,\"firststay\" datetime not null default '1900-01-01' ,\"erfasst\" datetime not null default '1900-01-01' ,\"erfassttim\" varchar(10) not null default '' ,\"erfasstusr\" varchar(50) not null default '' ,\"letzterpr\" decimal(19,2) not null default 0 ,\"letzteszi\" varchar(10) not null default '' ,\"fibudeb\" varchar(20) not null default '' ,\"logis\" decimal(19,2) not null default 0 ,\"fb\" decimal(19,2) not null default 0 ,\"extras\" decimal(19,2) not null default 0 ,\"logis_vj\" decimal(19,2) not null default 0 ,\"fb_vj\" decimal(19,2) not null default 0 ,\"extras_vj\" decimal(19,2) not null default 0 ,\"transfer\" int not null default 0 ,\"mailing\" int not null default 0 ,\"protected\" int not null default 0 ,\"changed\" datetime not null default '1900-01-01' ,\"changedby\" varchar(50) not null default '' ,\"changetime\" varchar(10) not null default '' ,\"merged\" datetime not null default '1900-01-01' ,\"mergetime\" varchar(10) not null default '' ,\"tosales\" int not null default 0 ,\"passnr\" varchar(30) not null default '' ,\"issued\" varchar(50) not null default '' ,\"issuedate\" datetime not null default '1900-01-01' ,\"discount\" int not null default 0 ,\"doctype\" int not null default 0 ,\"docvalid\" datetime not null default '1900-01-01' ,\"vatno\" varchar(30) not null default '' ,\"flags\" varchar(20) not null default '' ,\"afmno\" varchar(30) not null default '' ,\"gebort\" varchar(50) not null default '' ,\"gebland\" int not null default 0 ,\"mstatus\" int not null default 0 ,\"mahncode\" int not null default 0 ,\"masteracc\" int not null default 0 ,\"masterdeb\" int not null default 0 ,\"ismstdeb\" int not null default 0 ,\"extend\" int not null default 0 ,\"spfrom1\" datetime not null default '1900-01-01' ,\"spfrom2\" datetime not null default '1900-01-01' ,\"spfrom3\" datetime not null default '1900-01-01' ,\"spfrom4\" datetime not null default '1900-01-01' ,\"spto1\" datetime not null default '1900-01-01' ,\"spto2\" datetime not null default '1900-01-01' ,\"spto3\" datetime not null default '1900-01-01' ,\"spto4\" datetime not null default '1900-01-01' ,\"sp1p1\" decimal(7,2) not null default 0 ,\"sp2p1\" decimal(7,2) not null default 0 ,\"sp3p1\" decimal(7,2) not null default 0 ,\"sp4p1\" decimal(7,2) not null default 0 ,\"sp1p2\" decimal(7,2) not null default 0 ,\"sp2p2\" decimal(7,2) not null default 0 ,\"sp3p2\" decimal(7,2) not null default 0 ,\"sp4p2\" decimal(7,2) not null default 0 ,\"sp1p3\" decimal(7,2) not null default 0 ,\"sp2p3\" decimal(7,2) not null default 0 ,\"sp3p3\" decimal(7,2) not null default 0 ,\"sp4p3\" decimal(7,2) not null default 0 ,\"sp1p4\" decimal(7,2) not null default 0 ,\"sp2p4\" decimal(7,2) not null default 0 ,\"sp3p4\" decimal(7,2) not null default 0 ,\"sp4p4\" decimal(7,2) not null default 0 ,\"user00\" varchar(20) not null default '' ,\"user01\" varchar(20) not null default '' ,\"user02\" int not null default 0 ,\"user03\" int not null default 0 ,\"taxexemp\" int not null default 0 ,\"voidfee\" int not null default 0 ,\"depcode\" int not null default 0 ,\"laundry\" int not null default 0 ,\"posrcd\" int not null default 0 ,\"emptybfee\" int not null default 0 ,\"shortname\" varchar(80) not null default '' ,\"mastername\" varchar(80) not null default '' ,\"accountname\" varchar(80) not null default '' ,\"otapara\" varchar(51) not null default '' ,\"numcontacts\" int not null default 0 ,\"numaccounts\" int not null default 0 ,\"addcleansed\" int not null default 0 ,\"cpssrc\" varchar(30) not null default '' ,\"cpsid\" varchar(30) not null default '' ,\"_del\" int not null default 0 )\n"
        export_file.write(text)
        #print("headertext: ", text)

        # inhalt schreiben
        csv_writer = csv.writer(export_file, delimiter=",")
        print("exportfile: ", export_file)
        i = 0
        for line in csv_reader:
            writer = csv.writer
            # line_protelparameters=["uhu", "aha", "oho"]

            i = i + 1
            anzahl = i
            Line_iteration_kundennummer = [anzahl]
            print("Line_iteration_kundennummer",
                  Line_iteration_kundennummer)
            # Line_zero=["0"]
            Line_mpe = ["1"]
            Line_emptyvalue = [""]
            # Line_emptydate= ["1900 - 01 - 01"]
            Line_Karteityp = ["0"]
            Line_Nachname = [line[0]]
            Line_Vorname = [line[1]]
            Line_Strasse = [line[2]]
            Line_plz = [line[3]]
            Line_Stadt = [line[4]]
            # todo land noch anpassen wegen weiterer Tabelle
            Line_Land = [""]
            Line_landkz = [""]
            Line_nat = [""]
            Line_sprache = [""]
            Line_Anrede = [""]
            Line_Begruessung = [""]
            Line_Tel = [line[5]]
            Line_Mail = [line[6]]

            line_new = Line_iteration_kundennummer + Line_emptyvalue + Line_mpe + \
                6 * Line_emptyvalue + Line_Karteityp + Line_Nachname + Line_emptyvalue + Line_Vorname + 2 * Line_emptyvalue + \
                Line_Strasse + 2 * Line_emptyvalue + Line_plz + 2 * Line_emptyvalue + Line_Stadt + Line_Land + Line_landkz + \
                4 * Line_emptyvalue + Line_nat + Line_emptyvalue + Line_sprache + 2 * Line_emptyvalue + Line_Anrede + Line_Begruessung + \
                Line_Tel + Line_emptyvalue + Line_Mail + 136 * Line_emptyvalue

            csv_writer.writerow(line_new)

            print(line_new)


# convertlvl1()


def convertoldschollway():
    with open("testdaten/testdatensatz.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        with open("testdaten/testdatenexportoldschollway.txt", "w", encoding='cp1252') as export_file:
            # header schreiben
            text = "create table kunden (\"kdnr\" int not null default 0 ,\"cloudref\" bigint not null default 0 ,\"mpehotel\" int not null default 0 ,\"hotelkdnr\" int not null default 0 ,\"extref\" varchar(15) not null default '' ,\"member\" varchar(50) not null default '' ,\"outlsync\" int not null default 0 ,\"outldate\" datetime not null default '1900-01-01' ,\"passwd\" varchar(15) not null default '' ,\"typ\" int not null default 0 ,\"name1\" varchar(80) not null default '' ,\"name2\" varchar(80) not null default '' ,\"vorname\" varchar(50) not null default '' ,\"ehepartner\" varchar(80) not null default '' ,\"ehegeb\" datetime not null default '1900-01-01' ,\"strasse\" varchar(80) not null default '' ,\"strasse2\" varchar(80) not null default '' ,\"strasse3\" varchar(80) not null default '' ,\"plz\" varchar(17) not null default '' ,\"pfplz\" varchar(17) not null default '' ,\"postfach\" varchar(17) not null default '' ,\"ort\" varchar(50) not null default '' ,\"land\" varchar(80) not null default '' ,\"landkz\" int not null default 0 ,\"regionkz\" int not null default 0 ,\"gender\" int not null default 0 ,\"abteil\" varchar(80) not null default '' ,\"region\" varchar(80) not null default '' ,\"nat\" int not null default 0 ,\"marketing\" int not null default 0 ,\"sprache\" int not null default 0 ,\"vip\" int not null default 0 ,\"gebdat\" datetime not null default '1900-01-01' ,\"anrede\" varchar(40) not null default '' ,\"begr\" varchar(70) not null default '' ,\"telefonnr\" varchar(50) not null default '' ,\"funktel\" varchar(50) not null default '' ,\"email\" varchar(75) not null default '' ,\"twitter\" varchar(80) not null default '' ,\"homepage\" varchar(80) not null default '' ,\"cctypn\" int not null default 0 ,\"ccexp\" varchar(10) not null default '' ,\"cc\" varchar(35) not null default '' ,\"kfz\" varchar(30) not null default '' ,\"faxnr\" varchar(50) not null default '' ,\"telex\" varchar(50) not null default '' ,\"gdsident\" varchar(64) not null default '' ,\"resname\" varchar(80) not null default '' ,\"iata\" varchar(9) not null default '' ,\"contract\" varchar(20) not null default '' ,\"resvorn\" varchar(50) not null default '' ,\"resanr\" varchar(40) not null default '' ,\"restel\" varchar(100) not null default '' ,\"respanr\" varchar(70) not null default '' ,\"rechname\" varchar(80) not null default '' ,\"rechvorn\" varchar(50) not null default '' ,\"rechanr\" varchar(40) not null default '' ,\"rechtel\" varchar(100) not null default '' ,\"rechpanr\" varchar(70) not null default '' ,\"titel\" varchar(20) not null default '' ,\"firmenname\" varchar(50) not null default '' ,\"firmennam2\" varchar(50) not null default '' ,\"beruf\" varchar(50) not null default '' ,\"prof\" int not null default 0 ,\"wunschzi\" int not null default 0 ,\"zimmerattr\" varchar(50) not null default '' ,\"gfeat\" varchar(50) not null default '' ,\"preiscode\" int not null default 0 ,\"comcode\" int not null default 0 ,\"comtax1\" int not null default 0 ,\"comtax2\" int not null default 0 ,\"deleted\" int not null default 0 ,\"kredit\" int not null default 0 ,\"kreditbet\" decimal(19,2) not null default 0 ,\"intcredit\" int not null default 0 ,\"intcredita\" decimal(19,2) not null default 0 ,\"statement\" int not null default 0 ,\"sonderp\" int not null default 0 ,\"sonderp1\" decimal(7,2) not null default 0 ,\"sonderp2\" decimal(7,2) not null default 0 ,\"sonderp3\" decimal(7,2) not null default 0 ,\"sonderp4\" decimal(7,2) not null default 0 ,\"bemerkung\" varchar(250) not null default '' ,\"bemrest\" varchar(250) not null default '' ,\"aufenth\" int not null default 0 ,\"naechte\" int not null default 0 ,\"noshows\" int not null default 0 ,\"stornos\" int not null default 0 ,\"aufenth_vj\" int not null default 0 ,\"naechte_vj\" int not null default 0 ,\"noshows_vj\" int not null default 0 ,\"stornos_vj\" int not null default 0 ,\"letzterauf\" datetime not null default '1900-01-01' ,\"firststay\" datetime not null default '1900-01-01' ,\"erfasst\" datetime not null default '1900-01-01' ,\"erfassttim\" varchar(10) not null default '' ,\"erfasstusr\" varchar(50) not null default '' ,\"letzterpr\" decimal(19,2) not null default 0 ,\"letzteszi\" varchar(10) not null default '' ,\"fibudeb\" varchar(20) not null default '' ,\"logis\" decimal(19,2) not null default 0 ,\"fb\" decimal(19,2) not null default 0 ,\"extras\" decimal(19,2) not null default 0 ,\"logis_vj\" decimal(19,2) not null default 0 ,\"fb_vj\" decimal(19,2) not null default 0 ,\"extras_vj\" decimal(19,2) not null default 0 ,\"transfer\" int not null default 0 ,\"mailing\" int not null default 0 ,\"protected\" int not null default 0 ,\"changed\" datetime not null default '1900-01-01' ,\"changedby\" varchar(50) not null default '' ,\"changetime\" varchar(10) not null default '' ,\"merged\" datetime not null default '1900-01-01' ,\"mergetime\" varchar(10) not null default '' ,\"tosales\" int not null default 0 ,\"passnr\" varchar(30) not null default '' ,\"issued\" varchar(50) not null default '' ,\"issuedate\" datetime not null default '1900-01-01' ,\"discount\" int not null default 0 ,\"doctype\" int not null default 0 ,\"docvalid\" datetime not null default '1900-01-01' ,\"vatno\" varchar(30) not null default '' ,\"flags\" varchar(20) not null default '' ,\"afmno\" varchar(30) not null default '' ,\"gebort\" varchar(50) not null default '' ,\"gebland\" int not null default 0 ,\"mstatus\" int not null default 0 ,\"mahncode\" int not null default 0 ,\"masteracc\" int not null default 0 ,\"masterdeb\" int not null default 0 ,\"ismstdeb\" int not null default 0 ,\"extend\" int not null default 0 ,\"spfrom1\" datetime not null default '1900-01-01' ,\"spfrom2\" datetime not null default '1900-01-01' ,\"spfrom3\" datetime not null default '1900-01-01' ,\"spfrom4\" datetime not null default '1900-01-01' ,\"spto1\" datetime not null default '1900-01-01' ,\"spto2\" datetime not null default '1900-01-01' ,\"spto3\" datetime not null default '1900-01-01' ,\"spto4\" datetime not null default '1900-01-01' ,\"sp1p1\" decimal(7,2) not null default 0 ,\"sp2p1\" decimal(7,2) not null default 0 ,\"sp3p1\" decimal(7,2) not null default 0 ,\"sp4p1\" decimal(7,2) not null default 0 ,\"sp1p2\" decimal(7,2) not null default 0 ,\"sp2p2\" decimal(7,2) not null default 0 ,\"sp3p2\" decimal(7,2) not null default 0 ,\"sp4p2\" decimal(7,2) not null default 0 ,\"sp1p3\" decimal(7,2) not null default 0 ,\"sp2p3\" decimal(7,2) not null default 0 ,\"sp3p3\" decimal(7,2) not null default 0 ,\"sp4p3\" decimal(7,2) not null default 0 ,\"sp1p4\" decimal(7,2) not null default 0 ,\"sp2p4\" decimal(7,2) not null default 0 ,\"sp3p4\" decimal(7,2) not null default 0 ,\"sp4p4\" decimal(7,2) not null default 0 ,\"user00\" varchar(20) not null default '' ,\"user01\" varchar(20) not null default '' ,\"user02\" int not null default 0 ,\"user03\" int not null default 0 ,\"taxexemp\" int not null default 0 ,\"voidfee\" int not null default 0 ,\"depcode\" int not null default 0 ,\"laundry\" int not null default 0 ,\"posrcd\" int not null default 0 ,\"emptybfee\" int not null default 0 ,\"shortname\" varchar(80) not null default '' ,\"mastername\" varchar(80) not null default '' ,\"accountname\" varchar(80) not null default '' ,\"otapara\" varchar(51) not null default '' ,\"numcontacts\" int not null default 0 ,\"numaccounts\" int not null default 0 ,\"addcleansed\" int not null default 0 ,\"cpssrc\" varchar(30) not null default '' ,\"cpsid\" varchar(30) not null default '' ,\"_del\" int not null default 0 )\n"
            export_file.write(text)

            # inhalt schreiben
            csv_writer = csv.writer(export_file, delimiter=",")
            i = 0
            for line in csv_reader:
                writer = csv.writer
                #line_protelparameters=["uhu", "aha", "oho"]

                i = i+1
                anzahl = i
                Line_iteration_kundennummer = [anzahl]
                # Line_zero=["0"]
                Line_mpe = ["1"]
                Line_emptyvalue = [""]
                #Line_emptydate= ["1900 - 01 - 01"]
                Line_Karteityp = ["0"]
                Line_Nachname = [line[0]]
                Line_Vorname = [line[1]]
                Line_Strasse = [line[2]]
                Line_plz = [line[3]]
                Line_Stadt = [line[4]]
                # todo land noch anpassen wegen weiterer Tabelle
                Line_Land = [""]
                Line_landkz = [""]
                Line_nat = [""]
                Line_sprache = [""]
                Line_Anrede = [""]
                Line_Begruessung = [""]
                Line_Tel = [line[5]]
                Line_Mail = [line[6]]

                line_new = Line_iteration_kundennummer + Line_emptyvalue + Line_mpe + \
                    6 * Line_emptyvalue + Line_Karteityp + Line_Nachname + Line_emptyvalue + Line_Vorname+2 * Line_emptyvalue + \
                    Line_Strasse + 2 * Line_emptyvalue + Line_plz + 2 * Line_emptyvalue + Line_Stadt + Line_Land + Line_landkz + \
                    4 * Line_emptyvalue + Line_nat + Line_emptyvalue + Line_sprache + 2 * Line_emptyvalue + Line_Anrede + Line_Begruessung + \
                    Line_Tel + Line_emptyvalue + Line_Mail + 136 * Line_emptyvalue

                csv_writer.writerow(line_new)

                print(line_new)

                # print(Line_iteration_kundennummer)
# convertlvl1pairtospe()
# convertoldschollway()
# if __name__ == '__main__':
#     convert()

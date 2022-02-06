import csv


def csvtolvl1():
    '''Konvertiert csv zu protel lesbarer Form mit SQL Header Tablellen'''


# input
# Nachname;Vorname;Straße;PLZ;Ort;Land;Sprache;Geschlecht(m=1,w=2,d=3);EMail;Tel;Briefanrede;Karteityp(Gast=0,Firma=1);VIPcode;Marketingcode
# Berge;Sebastian;Musterstraße 44;04275;Leipzig;Deutschland;DE;1;berge@prohotel-edv.de;03519988776655;Sehr geehrter Herr Berge;0;Stammgast;Sportler
# Musterfrau;Juliane;Musterstraße 1;01299;Dresden;Deutschland;DE;2;muster@prohotel-edv.de;03519111111;Sehr geehrte Frau Musterfrau;0;;;
# Tesla;;Teslastraße 1;11299;Berlin;Deutschland;DE;;tesla@prohotel-edv.de;03019111111;;1;;

# TODO VIP Codes testen > geht das bei Firmen? > int nummern exportieren, nicht den namen
# TODO Marketcodes mit verarbeiten > geht das bei Firmen?
# TODO Firmenansprechpartner (Elon Musk) wird nicht mit eingespielt > noch mit testen oder in wiki ändern dass das nicht geht > geht nicht
# TODO Gästedaten und Firmendaten grundsätzlich getrennt von Kundenabfordern und Vorlage erstellen die Sie uns zuarbeiten müssen?
# TODO error abfangen wenn delimiter ; statt , in csv damit nicht lange gesucht werden muss
# TODO Länder noch weiter hinterlegen (Frankreich, England, Polen usw) > erledigt > noch testen
# TODO Formel in xls wegen Firma in Anrede gleich mit in python einbinden (sucht "Firma" in der Anrede und ergänzt das Flag 1): =WENN(ISTFEHLER(FINDEN("Firma";K1;1));"0";"1")
# TODO Konvertierung bricht bei sonderzeichen (kyrillisch uws ab > Konvertierung der Sonderzeichen in utf8 vorher einbauen in python)
# TODO xls wegen Anrede vorab =WENN(A2="Herr"; "Sehr geehrter Herr "&E2;WENN(A2="Frau"; "Sehr geehrte Frau "&E2; "Sehr geehrte Damen und Herren") )

#global variables

## input variables
input_encoding = str("cp1252") ## encoding möglich mit utf8 und cp1252
input_file="testdaten/testdatensatz-mitfirma-flag.csv"

## output variables
output_encoding = str("cp1252") # encoding sollte immer cp1252 sein, da der Import von protel so ausgelegt ist
output_file="testdaten/test-datenexport-mitfirma-vip-marketing.txt"

# input Verarbeitung
with open(input_file, "r", encoding=input_encoding, errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    # output Verarbeitung
    with open(output_file, "w", encoding=output_encoding) as export_file:
        # prelude schreiben
        prelude = "-- 'Verbesserung und Kritik an berge@prohotel-edv.de', 'falls dieser Service Ihnen hilft, teilen Sie Ihr Wissen mit einer positiven Bewertung auf https://www.google.com/search?q=google+bewertung+pro+hotel&oq=google+bewertung+pro+hotel&aqs=chrome..69i57j69i64l3.6383j0j9&sourceid=chrome&ie=UTF-8#lrd=0x47a6f938c6a32803:0x3312b6678c6d9ef8,1'\n"
        export_file.write(prelude)

        # header schreiben
        header = "create table kunden (\"kdnr\" int not null default 0 ,\"cloudref\" bigint not null default 0 ,\"mpehotel\" int not null default 0 ,\"hotelkdnr\" int not null default 0 ,\"extref\" varchar(15) not null default '' ,\"member\" varchar(50) not null default '' ,\"outlsync\" int not null default 0 ,\"outldate\" datetime not null default '1900-01-01' ,\"passwd\" varchar(15) not null default '' ,\"typ\" int not null default 0 ,\"name1\" varchar(80) not null default '' ,\"name2\" varchar(80) not null default '' ,\"vorname\" varchar(50) not null default '' ,\"ehepartner\" varchar(80) not null default '' ,\"ehegeb\" datetime not null default '1900-01-01' ,\"strasse\" varchar(80) not null default '' ,\"strasse2\" varchar(80) not null default '' ,\"strasse3\" varchar(80) not null default '' ,\"plz\" varchar(17) not null default '' ,\"pfplz\" varchar(17) not null default '' ,\"postfach\" varchar(17) not null default '' ,\"ort\" varchar(50) not null default '' ,\"land\" varchar(80) not null default '' ,\"landkz\" int not null default 0 ,\"regionkz\" int not null default 0 ,\"gender\" int not null default 0 ,\"abteil\" varchar(80) not null default '' ,\"region\" varchar(80) not null default '' ,\"nat\" int not null default 0 ,\"marketing\" int not null default 0 ,\"sprache\" int not null default 0 ,\"vip\" int not null default 0 ,\"gebdat\" datetime not null default '1900-01-01' ,\"anrede\" varchar(40) not null default '' ,\"begr\" varchar(70) not null default '' ,\"telefonnr\" varchar(50) not null default '' ,\"funktel\" varchar(50) not null default '' ,\"email\" varchar(75) not null default '' ,\"twitter\" varchar(80) not null default '' ,\"homepage\" varchar(80) not null default '' ,\"cctypn\" int not null default 0 ,\"ccexp\" varchar(10) not null default '' ,\"cc\" varchar(35) not null default '' ,\"kfz\" varchar(30) not null default '' ,\"faxnr\" varchar(50) not null default '' ,\"telex\" varchar(50) not null default '' ,\"gdsident\" varchar(64) not null default '' ,\"resname\" varchar(80) not null default '' ,\"iata\" varchar(9) not null default '' ,\"contract\" varchar(20) not null default '' ,\"resvorn\" varchar(50) not null default '' ,\"resanr\" varchar(40) not null default '' ,\"restel\" varchar(100) not null default '' ,\"respanr\" varchar(70) not null default '' ,\"rechname\" varchar(80) not null default '' ,\"rechvorn\" varchar(50) not null default '' ,\"rechanr\" varchar(40) not null default '' ,\"rechtel\" varchar(100) not null default '' ,\"rechpanr\" varchar(70) not null default '' ,\"titel\" varchar(20) not null default '' ,\"firmenname\" varchar(50) not null default '' ,\"firmennam2\" varchar(50) not null default '' ,\"beruf\" varchar(50) not null default '' ,\"prof\" int not null default 0 ,\"wunschzi\" int not null default 0 ,\"zimmerattr\" varchar(50) not null default '' ,\"gfeat\" varchar(50) not null default '' ,\"preiscode\" int not null default 0 ,\"comcode\" int not null default 0 ,\"comtax1\" int not null default 0 ,\"comtax2\" int not null default 0 ,\"deleted\" int not null default 0 ,\"kredit\" int not null default 0 ,\"kreditbet\" decimal(19,2) not null default 0 ,\"intcredit\" int not null default 0 ,\"intcredita\" decimal(19,2) not null default 0 ,\"statement\" int not null default 0 ,\"sonderp\" int not null default 0 ,\"sonderp1\" decimal(7,2) not null default 0 ,\"sonderp2\" decimal(7,2) not null default 0 ,\"sonderp3\" decimal(7,2) not null default 0 ,\"sonderp4\" decimal(7,2) not null default 0 ,\"bemerkung\" varchar(250) not null default '' ,\"bemrest\" varchar(250) not null default '' ,\"aufenth\" int not null default 0 ,\"naechte\" int not null default 0 ,\"noshows\" int not null default 0 ,\"stornos\" int not null default 0 ,\"aufenth_vj\" int not null default 0 ,\"naechte_vj\" int not null default 0 ,\"noshows_vj\" int not null default 0 ,\"stornos_vj\" int not null default 0 ,\"letzterauf\" datetime not null default '1900-01-01' ,\"firststay\" datetime not null default '1900-01-01' ,\"erfasst\" datetime not null default '1900-01-01' ,\"erfassttim\" varchar(10) not null default '' ,\"erfasstusr\" varchar(50) not null default '' ,\"letzterpr\" decimal(19,2) not null default 0 ,\"letzteszi\" varchar(10) not null default '' ,\"fibudeb\" varchar(20) not null default '' ,\"logis\" decimal(19,2) not null default 0 ,\"fb\" decimal(19,2) not null default 0 ,\"extras\" decimal(19,2) not null default 0 ,\"logis_vj\" decimal(19,2) not null default 0 ,\"fb_vj\" decimal(19,2) not null default 0 ,\"extras_vj\" decimal(19,2) not null default 0 ,\"transfer\" int not null default 0 ,\"mailing\" int not null default 0 ,\"protected\" int not null default 0 ,\"changed\" datetime not null default '1900-01-01' ,\"changedby\" varchar(50) not null default '' ,\"changetime\" varchar(10) not null default '' ,\"merged\" datetime not null default '1900-01-01' ,\"mergetime\" varchar(10) not null default '' ,\"tosales\" int not null default 0 ,\"passnr\" varchar(30) not null default '' ,\"issued\" varchar(50) not null default '' ,\"issuedate\" datetime not null default '1900-01-01' ,\"discount\" int not null default 0 ,\"doctype\" int not null default 0 ,\"docvalid\" datetime not null default '1900-01-01' ,\"vatno\" varchar(30) not null default '' ,\"flags\" varchar(20) not null default '' ,\"afmno\" varchar(30) not null default '' ,\"gebort\" varchar(50) not null default '' ,\"gebland\" int not null default 0 ,\"mstatus\" int not null default 0 ,\"mahncode\" int not null default 0 ,\"masteracc\" int not null default 0 ,\"masterdeb\" int not null default 0 ,\"ismstdeb\" int not null default 0 ,\"extend\" int not null default 0 ,\"spfrom1\" datetime not null default '1900-01-01' ,\"spfrom2\" datetime not null default '1900-01-01' ,\"spfrom3\" datetime not null default '1900-01-01' ,\"spfrom4\" datetime not null default '1900-01-01' ,\"spto1\" datetime not null default '1900-01-01' ,\"spto2\" datetime not null default '1900-01-01' ,\"spto3\" datetime not null default '1900-01-01' ,\"spto4\" datetime not null default '1900-01-01' ,\"sp1p1\" decimal(7,2) not null default 0 ,\"sp2p1\" decimal(7,2) not null default 0 ,\"sp3p1\" decimal(7,2) not null default 0 ,\"sp4p1\" decimal(7,2) not null default 0 ,\"sp1p2\" decimal(7,2) not null default 0 ,\"sp2p2\" decimal(7,2) not null default 0 ,\"sp3p2\" decimal(7,2) not null default 0 ,\"sp4p2\" decimal(7,2) not null default 0 ,\"sp1p3\" decimal(7,2) not null default 0 ,\"sp2p3\" decimal(7,2) not null default 0 ,\"sp3p3\" decimal(7,2) not null default 0 ,\"sp4p3\" decimal(7,2) not null default 0 ,\"sp1p4\" decimal(7,2) not null default 0 ,\"sp2p4\" decimal(7,2) not null default 0 ,\"sp3p4\" decimal(7,2) not null default 0 ,\"sp4p4\" decimal(7,2) not null default 0 ,\"user00\" varchar(20) not null default '' ,\"user01\" varchar(20) not null default '' ,\"user02\" int not null default 0 ,\"user03\" int not null default 0 ,\"taxexemp\" int not null default 0 ,\"voidfee\" int not null default 0 ,\"depcode\" int not null default 0 ,\"laundry\" int not null default 0 ,\"posrcd\" int not null default 0 ,\"emptybfee\" int not null default 0 ,\"shortname\" varchar(80) not null default '' ,\"mastername\" varchar(80) not null default '' ,\"accountname\" varchar(80) not null default '' ,\"otapara\" varchar(51) not null default '' ,\"numcontacts\" int not null default 0 ,\"numaccounts\" int not null default 0 ,\"addcleansed\" int not null default 0 ,\"cpssrc\" varchar(30) not null default '' ,\"cpsid\" varchar(30) not null default '' ,\"_del\" int not null default 0 )\n"
        export_file.write(header)
        # print("headertext: ", text)

        # inhalt schreiben
        csv_writer = csv.writer(export_file, delimiter=",")
        print("exportfile: ", export_file)
        inhaltssammler_gcom = []
        inhaltssammler_vipcode = []
        inhaltssammler_Marketcode = []
        export_Line_VIP = []
        export_Line_VIP_dic = {}
        export_Line_Marketing = []
        j = 0  # index gcom Zähler
        vipcounter = 0 
        Marketcounter = 0 
        i = 2000
        Line_Karteityp = ["not defined"]
        for line in csv_reader:
            writer = csv.writer
            i = i + 1
            anzahl = i
            Line_iteration_kundennummer = [anzahl]
            Line_mpe = ["1"]
            Line_emptyvalue = [""]
            Line_emptydate = ["1900 - 01 - 01"]
            # Line_Karteityp > 0 = privat | 1 = Firma mit abfragen in Importtabelle bei Karteityp
            if [line[11]] == ["1"]:
                Line_Karteityp = ["1"]
            elif [line[11]] == ["0"]:
                Line_Karteityp = ["0"]
            Line_Nachname = [line[0]]
            Line_Vorname = [line[1]]
            Line_Strasse = [line[2]]
            Line_plz = [line[3]]
            Line_Stadt = [line[4]]
            Line_Land = [line[5]]  # Deutschland
            Line_landkz = [line[6]]  # DE
            Line_gender = [line[7]]  # 1 = männlich, 2 = weiblich
            # nat = 1 für Deutschland > siehe "codenr" bei header natcode
            Line_nat = [1]  # 1 für Deutschland!
            Line_sprache = [""]  # 4 für Deutschland?

            # Line_Anrede = [line[12]]  # Frau
            # Line_Anrede = [""]
            if [line[7]] == ["1"]:
                Line_Anrede = ["Herr"]
            elif [line[7]] == ["2"]:
                Line_Anrede = ["Frau"]
            elif [line[7]] != ["2"] or ["1"]:
                Line_Anrede = ["Guten Tag"]

            Line_Begruessung = [line[10]]  # Sehr geehrte Frau XY
            Line_Tel = [line[9]]
            Line_Mail = [line[8]]
            Line_VIP = [line[12]]
            Line_Marketing = [line[13]]

            line_new = Line_iteration_kundennummer + Line_emptyvalue + Line_mpe + \
                6 * Line_emptyvalue + Line_Karteityp + Line_Nachname + Line_emptyvalue + Line_Vorname + 2 * Line_emptyvalue + \
                Line_Strasse + 2 * Line_emptyvalue + Line_plz + 2 * Line_emptyvalue + Line_Stadt + Line_Land + Line_landkz + \
                Line_emptyvalue + Line_gender + \
                2 * Line_emptyvalue + Line_nat + export_Line_Marketing + Line_sprache + export_Line_VIP + Line_emptyvalue + Line_Anrede + Line_Begruessung + \
                Line_emptyvalue + Line_emptyvalue + Line_emptyvalue + 136 * Line_emptyvalue
            '''
            #Alternative SPE Import: Mail und Telefonnummer direkt in die tablelle kunden > geht nicht bei Air
            line_new = Line_iteration_kundennummer + Line_emptyvalue + Line_mpe + \
                6 * Line_emptyvalue + Line_Karteityp + Line_Nachname + Line_emptyvalue + Line_Vorname + 2 * Line_emptyvalue + \
                Line_Strasse + 2 * Line_emptyvalue + Line_plz + 2 * Line_emptyvalue + Line_Stadt + Line_Land + Line_landkz + \
                Line_emptyvalue + Line_gender + \
                2 * Line_emptyvalue + Line_nat + Line_emptyvalue + Line_sprache + 2 * Line_emptyvalue + Line_Anrede + Line_Begruessung + \
                Line_Tel + Line_emptyvalue + Line_Mail + 136 * Line_emptyvalue
            '''

            csv_writer.writerow(line_new)

            # sammeln der Inhalte innerhalb der Schleife für die spätere Ausgabe beim korrekten Header weiter unten im Quelltext
            ## inhaltssammler EMail
            if line[8] != '':
                # gcomline = [j, Line_iteration_kundennummer, 1, Line_Mail]
                # 1,838,1,'test@test.de','',0,0
                j += 1
                #print ("mail", j) 
                gcomline_mail = str(j) + "," + str(anzahl) + "," + \
                    "1" + ","+"'"+str(line[8])+"'" + ","+'"",0,0'
                inhaltssammler_gcom.append(gcomline_mail)

            ## inhaltssammler Telefonnummer
            if line[9] != '':
                j += 1
                #print ("tele", j) 
                gcomline_telefonnummer = str(j) + "," + str(anzahl) + "," + \
                    "2" + ","+"'"+str(line[9])+"'" + ","+'"",0,0'
                inhaltssammler_gcom.append(gcomline_telefonnummer)

            ## inhaltssammler VIPCodes

            #Output Bsp:
            #'VIP1','VIP1',1,0,1,'Begrüßungsgetränk und Wellness- GS',0,''
            #'VIP2','VIP2',2,0,1,'Begrüßungsgetränk, Wellness- GS, Obst, Sekt',0,''

            # TODO noch für export programmieren: es muss eine Liste mit den aktuellen VIPCodes angelegt werden. > erledigt / prüfen
            # Wenn neue VIPCodes dazukommen muss append gemacht werden. 
            # bei inptput muss der Sting "VIPXX" gegen die Liste geprüft werden und die Übersetzung der int Zahl zurückgegeben werden. Quasi eine Übersetzungstabelle
            # Übersetzungstabelle: also keine Liste sondern ein dictionary { } 
            # https://www.guru99.com/python-dictionary-append.html und https://www.w3schools.com/python/python_dictionaries.asp
                 
            # Dict Vipcodes
            # bei inptput muss der Sting "VIPXX" gegen die Liste geprüft werden und die Übersetzung der int Zahl zurückgegeben werden. Quasi eine Übersetzungstabelle
            # TODO vipcounter ersetzen mit zähler der keys damit korrekt mit tabelle der vips im Gästeoutput abgeglichen werden kann
            if str(line[12]) not in export_Line_VIP_dic.values() and str(line[12]) != "":
                #print(str(line[12]), " hinzufügen")
                vipcounter += 1  
                export_Line_VIP_dic[vipcounter]=str(line[12])
                #print("export_Line_VIP_dic", export_Line_VIP_dic)
      
                #print ("vipcounter", vipcounter)     
                content_vipcode = "'" + str(line[12]) + "'" + "," + "'" + str(line[12]) + "'" + "," + str(vipcounter) + ","+ "0" + ","+ "1" + "," + "'" + "'" +  "," + "0" +  ","+ "'" + "'" 
                inhaltssammler_vipcode.append(content_vipcode)

            if str(line[12]) in export_Line_VIP_dic.values():
                #print("gib mir den key zurück der dann in die Gästekartei geschreiben werden muss", (list(export_Line_VIP_dic.keys())[list(export_Line_VIP_dic.values()).index(str(line[12]))]))
                export_Line_VIP = [list(export_Line_VIP_dic.keys())[list(export_Line_VIP_dic.values()).index(str(line[12]))]]
                #print(export_Line_VIP)

            ## inhaltssammler Marketcodes
            if line[13] != '':
                Marketcounter += 1      
                #print ("Market", Marketcounter)   
                content_Marketcode = str(Marketcounter) + "," + "1" + "," + "0" + "," +  "'" + str(Marketcounter) + "'" + "," + "'" + str(line[13]) + "'" + "," +  "'" + "'" + "," + "'" + str(line[13]) + "'" +"'" + "," + "'" + "'" +  "," + "'" + "'" +  "," + "0" + ","+ "0" 
                inhaltssammler_Marketcode.append(content_Marketcode)

            # Output Bsp:
            #"create table mktcodes (\"ref\" int not null default 0 ,\"mpehotel\" int not null default 0 ,\"hidden\" int not null default 0 ,\"no\" varchar(10) not null default '' ,\"text\" varchar(40) not null default '' ,\"xgroup\" varchar(50) not null default '' ,\"short\" varchar(50) not null default '' ,\"user1\" varchar(250) not null default '' ,\"user2\" varchar(250) not null default '' ,\"sort\" int not null default 0 ,\"inet\" int not null default 0 )\n"
            #1 , 1 , 0 , ' 1 ' , ' Stammgast ' , ' ' , ' Stamm ' , '','', 0,0
            #2,1,0,'2','Anwohner','','Anwohner','','',0,0
            #3,1,0,'3','Golfer','','Golfer','','',0,0
            #4,1,0,'4','Feiertagsgast','','Feiertag','','',0,0
            #5,1,0,'5','Christus Wallfahrt'     ,'' ,'Chr.Wallf.'   ,'','',0,0
            #3,1,0,'3','EAuto',             ''      ,EAuto',        '','',0,0

            # TODO Market ähnlich wie vip noch für export programmieren
            #export_Line_Marketing = 1


        # header natcode schreiben
        header_natcode = "create table natcode (\"abkuerz\" varchar(20) not null default '' ,\"land\" varchar(80) not null default '' ,\"statnr\" int not null default 0 ,\"codenr\" int not null default 0 ,\"sort\" int not null default 0 ,\"gruppe\" int not null default 0 ,\"brkopftyp\" int not null default 0 ,\"sprache\" int not null default 0 ,\"isocode\" varchar(4) not null default '' ,\"state\" varchar(80) not null default '' ,\"showfo\" int not null default 0 ,\"inet\" int not null default 0 ,\"nation\" varchar(80) not null default '' ,\"addinfo\" varchar(50) not null default '' ,\"user01\" int not null default 0 ,\"anreisen1\" int not null default 0 ,\"anzueber1\" int not null default 0 ,\"anreisen2\" int not null default 0 ,\"anzueber2\" int not null default 0 ,\"anreisen3\" int not null default 0 ,\"anzueber3\" int not null default 0 ,\"anreisen4\" int not null default 0 ,\"anzueber4\" int not null default 0 ,\"anreisen5\" int not null default 0 ,\"anzueber5\" int not null default 0 ,\"anreisen6\" int not null default 0 ,\"anzueber6\" int not null default 0 ,\"anreisen7\" int not null default 0 ,\"anzueber7\" int not null default 0 ,\"anreisen8\" int not null default 0 ,\"anzueber8\" int not null default 0 ,\"anreisen9\" int not null default 0 ,\"anzueber9\" int not null default 0 ,\"anreisen10\" int not null default 0 ,\"anzueber10\" int not null default 0 ,\"anreisen11\" int not null default 0 ,\"anzueber11\" int not null default 0 ,\"anreisen12\" int not null default 0 ,\"anzueber12\" int not null default 0 )\n"
        export_file.write(header_natcode)

        content_table_natcode = "\
'D','Deutschland',13,1,0,0,0,4,'DE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'A','Österreich',33,15,0,0,2,-1,'AT','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'DK','Dänemark',22,4,0,0,2,-1,'DK','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'CZ','Tschechische Republik',40,22,0,0,2,-1,'CZ','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'J','Japan',63,31,0,0,0,0,'JP','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'B','Belgien',21,3,0,0,2,-1,'BE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'BRA','Brasilien',73,38,0,0,2,-1,'BR','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'CAN','Kanada',70,35,0,0,2,-1,'CA','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'CH','Schweiz',38,20,0,0,2,-1,'CH','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'DK','Dänemark',22,4,0,0,2,-1,'DK','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'S','Schweden',37,19,0,0,2,-1,'SE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'E','Spanien',39,21,0,0,2,-1,'ES','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'F','Frankreich',24,6,0,0,2,-1,'FR','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'FI','Finnland',23,5,0,0,2,-1,'FI','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'GB','Großbritanien',26,8,0,0,1,-1,'en','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'GR','Griechenland',25,7,0,0,2,-1,'GR','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'H','Ungarn',42,24,0,0,2,-1,'HU','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'I','Italien',29,11,0,0,2,-1,'IT','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'IRL','Irland',27,9,0,0,2,-1,'IE','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'ISL','Island',28,10,0,0,2,-1,'IS','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'L','Luxembourg',30,12,0,0,2,-1,'','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'N','Norwegen',32,14,0,0,2,-1,'NO','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'P','Portugal',35,17,0,0,2,-1,'PT','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'PL','Polen',34,16,0,0,2,-1,'PL','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'GUS','Rußland',36,18,0,0,2,-1,'RU','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'TK','Türkei',41,23,0,0,2,-1,'TR','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'USA','USA',71,36,0,0,2,-1,'US','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'NL','Niederlande',31,13,0,0,2,-1,'NL','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
'AUS','Australien',75,40,0,0,0,-1,'AU','',0,1,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n\
"
        export_file.write(content_table_natcode)

        # header gcom table schreiben
        header_gcom = "create table gcom (\"ref\" int not null default 0 ,\"kdnr\" int not null default 0 ,\"type\" int not null default 0 ,\"entry\" varchar(250) not null default '' ,\"info\" varchar(250) not null default '' ,\"prim\" int not null default 0 ,\"_del\" int not null default 0 )\n"
        export_file.write(header_gcom)

        # Gastkommunikationsarten - gcom table - content deploy
        # print("updated Inhaltssammler:", inhaltssammler_gcom)
        for line in inhaltssammler_gcom:
            # print(line)
            export_file.write(str(line)+'\n')

        # header gcomref table schreiben
        header_gcomref = "create table gcomref (\"mpehotel\" int not null default 0, \"kdnr\" int not null default 0)\n"
        export_file.write(header_gcomref)

        # Gastkommunikationsarten - gcomref table - content deploy
        gcomref_mpehotel = 1
        gcomref_end = i  # letzte Kundennummer
        gcomref_content = str(gcomref_mpehotel) + "," + str(gcomref_end)
        export_file.write(gcomref_content+'\n')

        # header gcomtref table schreiben - types of communication
        header_gcomtref = "create table gcomtref (\"mpehotel\" int not null default 0, \"kdnr\" int not null default 0)\n"
        export_file.write(header_gcomtref)

        # Gastkommunikationsarten - gcomtref table - content deploy - types of communication - Anzahl der Kommunikationsarten
        gcomtref_mpehotel = 1
        gcomtref_end = 4  # Anzahl der Kommunikationsarten, Bsp: Mail + Tele + Mobil +Fax = 4
        gcomtref_content = str(gcomtref_mpehotel) + \
            "," + str(gcomtref_end)
        export_file.write(gcomtref_content+'\n')

        # header gcomtype table schreiben - types of communication
        header_gcomtype = "create table gcomtype (\"ref\" int not null default 0 ,\"class\" int not null default 0 ,\"text\" varchar(250) not null default '' ,\"short\" varchar(50) not null default '' ,\"para\" varchar(100) not null default '' ,\"para2\" varchar(100) not null default '' ,\"para3\" int not null default 0 ,\"para4\" int not null default 0 ,\"para5\" int not null default 0 ,\"para6\" int not null default 0 ,\"para7\" int not null default 0 ,\"para8\" varchar(250) not null default '' ,\"xgroup\" varchar(50) not null default '' ,\"sort\" int not null default 0 ,\"icon\" int not null default 0 ,\"_del\" int not null default 0 ,\"dontshow\" int not null default 0 ,\"hidefo\" int not null default 0 ,\"lockdel\" int not null default 0 ,\"inet\" int not null default 0 )\n"
        export_file.write(header_gcomtype)

        # Gastkommunikationsarten - gcomtype table - content deploy - types of communication - Anzahl der Kommunikationsarten
        content_gcomtype = "1,0,'E-Mail','E-Mail','','',18,-1,-1,-1,-1,'','',0,0,0,0,0,0,0\n2,0,'Telefon','Telefon','','',18,-1,-1,-1,-1,'','',0,0,0,0,0,0,0\n3,0,'Mobil','Mobil','','',18,-1,-1,-1,-1,'','',0,0,0,0,0,0,0\n4,0,'Fax','Fax','','',18,-1,-1,-1,-1,'','',0,0,0,0,0,0,0\n"
        export_file.write(content_gcomtype)

        # header VIPcode table schreiben - VIP Codes
        header_vipcode = "create table vipcode (\"nr\" varchar(20) not null default '' ,\"bezeich\" varchar(40) not null default '' ,\"codenr\" int not null default 0 ,\"resblock\" int not null default 0 ,\"resremind\" int not null default 0 ,\"remindtx\" varchar(120) not null default '' ,\"showfo\" int not null default 0 ,\"sort\" varchar(10) not null default '' )\n"
        export_file.write(header_vipcode)

        # VIP Content - vipcode table content deploy
        # TODO VIPinhalte mit dem Gast verknüpfen: es muss die int Nummer aus dem vipzähler rein  in die Gästekartei, nicht der Text als Variable
        #print("updated Inhaltssammler:", inhaltssammler_vipcode)
        for line in inhaltssammler_vipcode:
            export_file.write(str(line)+'\n')

        # Zählertabelle mit vip
        ## header Zählertabelle mit vip
        header_vipnr = "create table vipnr (\"mpehotel\" int not null default 0 ,\"kdnr\" int not null default 0 )\n"
        export_file.write(header_vipnr)

        ## Content Zählertabelle mit vip
        vipnr_mpehotel = 1
        vipnr_end = i  # letzte Kundennummer
        vipnr_content = str(vipnr_mpehotel) + "," + str(vipnr_end)
        export_file.write(vipnr_content+'\n')
        # Bsp
        # create table vipnr ("mpehotel" int not null default 0 ,"kdnr" int not null default 0 )
        # 1,5

        # header Marketcode table schreiben - Marketcode
        header_Marketcode = "create table mktcodes (\"ref\" int not null default 0 ,\"mpehotel\" int not null default 0 ,\"hidden\" int not null default 0 ,\"no\" varchar(10) not null default '' ,\"text\" varchar(40) not null default '' ,\"xgroup\" varchar(50) not null default '' ,\"short\" varchar(50) not null default '' ,\"user1\" varchar(250) not null default '' ,\"user2\" varchar(250) not null default '' ,\"sort\" int not null default 0 ,\"inet\" int not null default 0 )\n"
        export_file.write(header_Marketcode)

        # Market Content - Marketcode table content deploy
        #print("updated Inhaltssammler:", inhaltssammler_Marketcode)
        for line in inhaltssammler_Marketcode:
            # print(line)
            export_file.write(str(line)+'\n')

        # Zählertabelle mit market 
        ## header Zählertabelle mit market
        header_marketnr = "create table mktcodnr (\"mpehotel\" int not null default 0 ,\"kdnr\" int not null default 0 )\n"
        export_file.write(header_marketnr)

        ## Content Zählertabelle mit market
        # TODO marketinhalte mit dem Gast verknüpfen: es muss die int Nummer aus dem marketzähler in die Gästekartei rein, nicht der Text als Variable
        marketnr_mpehotel = 1
        marketnr_end = i  # letzte Kundennummer
        marketnr_content = str(marketnr_mpehotel) + "," + str(marketnr_end)
        export_file.write(marketnr_content+'\n')
        # Bsp
        #create table mktcodnr ("mpehotel" int not null default 0 ,"kdnr" int not null default 0 )
        #1,5

        print("all done: ", i-2000, " Gäste")
csvtolvl1()
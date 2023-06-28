import pandas

with open('obciety_do_naprawy.txt', mode= 'r', encoding='latin-1', newline='\r\n', closefd=True) as fread:
    with open('naprawion_misja.txt', 'w') as fwrite:
        lines = fread.readlines()
        try:
            for line in lines:
                usd_count =0
                splitted = line.split('$',9)
                
                revised = splitted[9]
                
                splitted[2]="ADC"

                
                
                
                wsu, rest = revised.split('RAD')
                try:
                    if((wsu[0]!='W')&(wsu[1]!='S')&(wsu[3]!='U')):
                        wsu = "WSU$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$"
                except Exception as ee2:
                    print(ee2)
                    wsu = "WSU$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$"
                for n in range(len(wsu)):
                    if(wsu[n]=='$'):
                        usd_count +=1
                if(usd_count!=12):
                    wsu = "WSU$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$0.00$"
                fixed_line = str(splitted[0])+'$'+str(splitted[1])+'$'+str(splitted[2])+'$'+str(splitted[3])+'$'+str(splitted[4])+'$'+str(splitted[5])+'$'+str(splitted[6])+'$'+str(splitted[7])+'$'+str(splitted[8])+'$'+str(wsu)+"RAD"+str(rest)
                fwrite.write(fixed_line)


        except Exception as ee:
                print(ee)
                print(line)    

        fread.close()
        fwrite.close()
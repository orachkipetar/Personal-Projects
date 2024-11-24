import time
produkti = []
produktik = []
sifri = []
produkti_brojac = 0
produkti_cena = {}
main_loop = True
while main_loop:
    opcii = input("Vnesi opcija (p, k, menu, torbicka) ili 0 za kraj: ")
    first = True
    if opcii == "p":
        while first:
            kod = int(input("Vnesi lozinka ili (0 za izlez): "))
            if kod == 1234:
                print("Vleze vo sistemo")
                while first:
                    if produkti_brojac < 30:
                        produkt = input("Vnesi ime na produkt ili 0 za izlez: ")
                        if produkt == str(0):
                            first = False
                            break
                        elif produkt not in produkti:
                            produkti.append(produkt)
                            produkti_brojac += 1
                            while first:
                                sifra = input("Vnesi SIFRA na produkt 0 za izlez: ")
                                if sifra == str(0):
                                    #print("Uspesno Izleze")
                                    first = False
                                    break
                                elif sifra.isdigit() and len(sifra) == 4:
                                    if sifra not in sifri:
                                        sifri.append(sifra)
                                        produkt == int(sifra)
                                        print(f"Uspesno dodade {produkt} so sifra {sifra}")
                                        cena = float(input(f"Vnesi cena za {produkt} so sifra {sifra}: "))
                                        produkti_cena[produkt] = cena
                                        print(f"Vnese cena za produktot {produkt} cena:{cena} lv")
                                        break
                                    else:
                                        print(f"Sifrata {sifra} vekje postoi")
                                else:
                                    print("Mora da bide so tocno 4 brojki")
                        else:
                            print(f"{produkt} e vekje dodaden")
                    else:
                        print("Nemozete da dodavate povekje od 30 produkti")
                        print(f"Momentalnata niza na marketot e:\n{produkti}")
                        break
                
            else:
                if kod == 0:
                     #print("USpesno izleze")
                     first = False
                     break
                #print("Nevaliden kod")
                obidi = 0
                obidi += 1
                print(f"Nevaliden kod, imas {obidi}/3")
                if obidi == 3:
                    first = False
                    break
    elif opcii == "k":
        while first:
            ime = str(input("Vnesi go svoeto ime (0 za kraj): "))
            if ime == str(0):
                first = False
                break
            elif ime != "":
                budzet = float(input(f"{ime} vnesi si go budzetot (0 za kraj): "))
                while first:
                    
                    if budzet == 0:
                        first = False
                        break
                    elif budzet >= 1:
                        vid = input("Vnesi vid torbicka (mala/golema) ili 0 za kraj: ")
                        if vid == str(0):
                            break
                        elif vid == "mala":
                            while first:
                                m_korpa = int(input(f"{ime} vnesi go kapaciteto na torbickata (0 za kraj): "))
                                if m_korpa == 0:
                                    #print("Izleze")
                                    first = False
                                    break
                                elif m_korpa > 0 and m_korpa <= 10:
                                    while first:
                                        produkt = input("Vnesi ime na produkt ili 0 za izlez: ")
                                        if produkt == str(0):
                                            first = False
                                            break
                                        elif produkt in produkti:
                                            if produkt not in str(m_korpa):
                                                while True:
                                                    kolicina = float(input(f"Vnesi kolicina {produkt}: "))
                                                    if m_korpa > 0 and kolicina <= m_korpa:
                                                        if budzet >= kolicina*produkti_cena[produkt]:
                                                            m_korpa -= kolicina
                                                            print("Vo torbickata imas uste ",round(m_korpa,2)," slobodno mesto")
                                                            #print(f"Tvojo budzet e presmetano od {produkt} i cena:{produkti_cena[produkt]} so kolicina:{kolicina}")
                                                            budzet -= kolicina*produkti_cena[produkt]
                                                            print(f"Budzet: {budzet:.2f}lv")
                                                            #print(f"Vo korpata uspesno dodadovte {produkt}")
                                                            produktik.append(produkt)
                                                            #print(f"Nizata so produkti ti izgleda {produktik}")
                                                            break
                                                        else:
                                                            print("Nemas dovolno pari")
                                                    else:
                                                        print("Nemas mesto vo torbickata")
                                            else:
                                                print("Kupenjo vekej")
                                        else:
                                            print("Ne postoi")
                                else:
                                    print("Kapacitetot mora da bide povekje od 0 ili pomalku od 10")
                        elif vid == "golema":
                            while first:
                                d_korpa = int(input(f"{ime} vnesi go kapaciteto na torbickata (0 za kraj): "))
                                if d_korpa == 0:
                                    #print("Izleze")
                                    first = False
                                    break
                                elif d_korpa > 0 and d_korpa <= 35:
                                    while first:
                                        produkt = input("Vnesi ime na produkt ili 0 za izlez: ")
                                        if produkt == str(0):
                                            first = False
                                            break
                                        elif produkt in produkti:
                                            if produkt not in str(d_korpa):
                                                while True:
                                                    kolicina = float(input(f"Vnesi kolicina {produkt}: "))
                                                    if d_korpa > 0 and kolicina <= d_korpa:
                                                        if budzet >= kolicina*produkti_cena[produkt]:
                                                            d_korpa -= kolicina
                                                            print("Vo torbickata imas uste ",round(d_korpa,2)," slobodno mesto")
                                                            #print(f"Tvojo budzet e presmetano od {produkt} i cena:{produkti_cena[produkt]} so kolicina:{kolicina}")
                                                            budzet -= kolicina*produkti_cena[produkt]
                                                            print(f"Budzet: {budzet:.2f}lv")
                                                            #print(f"Vo korpata uspesno dodadovte {produkt}")
                                                            produktik.append(produkt)
                                                            #print(f"Nizata so produkti ti izgleda {produktik}")
                                                            break
                                                        else:
                                                            print("Nemas dovolno pari")
                                                    else:
                                                        print("Nemas mesto vo torbickata")
                                            else:
                                                print("Kupenjo vekej")
                                        else:
                                            print("Ne postoi")
                                else:
                                    print("Kapacitetot mora da bide povekje od 0 ili pomalku od 35")
                            else:
                                print("Nevaliden vid torbicka")
                    else:
                        print("Budzeto mora da bide povekje od 1")
            else:
                print("Vnesi ime!")
                #break
    elif opcii == "menu":
        if len(produkti) != 0:
            for produkt in produkti:
                if produkt in produkti_cena:
                    print(f"{produkt} / sifra: {sifri[produkti.index(produkt)]} : cena {produkti_cena[produkt]}")
                else:
                    print(f"{produkt} / sifra: {sifri[produkti.index(produkt)]} : cena N/A")
        else:
            print("Nemate dodadeno produkti vo marketo")
    elif opcii == "torbicka":
        if len(produktik) != 0:
            for produkt in produktik:
                print(f"Momentalnata sostojba vo torbickata izglda: \n{produktik}")
        else:
            print("Nemas nisto vo torbickata")
        
    elif opcii == str(0):
        print("Kraj na programata")
        time.sleep(3)
        break
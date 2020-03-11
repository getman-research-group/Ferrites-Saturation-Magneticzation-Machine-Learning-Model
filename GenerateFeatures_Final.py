import math
import os


with open('PWD10') as sp:
    for line in sp:
        line  = line.replace('\n', '')
        os.chdir(line)
        #os.chdir("..")
        test = []
        with open('POSCAR') as fp:
            for line in fp:
                test.append(line)
            #lines = fp.readlines()
            elem = test[5]
            Elem = elem.split()
            numb = test[6]
            Numb = numb.split()
            preass_x =[0.125, 0.875, 0.625, 0.375, 0.125, 0.875, 0.625, 0.375, 0.5, 0.25, 0.75, 0.75, 0.25, 1.0, 0.0, 0.5, 0.25,
                       0.75, 0.75, 0.25, 0.0, 0.5, 0.5, 0.0]
            preass_y =[0.125, 0.875, 0.125, 0.875, 0.625, 0.375, 0.625, 0.375, 0.5, 0.75, 0.25, 1.0, 0.0, 0.25, 0.75, 1.0, 0.25,
                       0.75, 0.5, 0.5, 0.5, 0.25, 0.75, 1.0]
            preass_z =[0.125, 0.875, 0.625, 0.375, 0.625, 0.375, 0.125, 0.875, 0.5, 0.0, 1.0, 0.25, 0.75, 0.75, 0.25, 0.0, 0.5,
                       0.5, 0.75, 0.25, 0.0, 0.25, 0.75, 0.5]
            l = len(Elem)
            print(l)
            extra = int(Numb[0]) - 16
            metals = ['Fe', 'Co', 'Ni', 'Zn', 'Cu', 'Mn']
	    redox = [0.44, 0.28, 0.25, 0.76, -0.34, 1.18]# Me - 2e = Me2+ http://accounts.smccd.edu/batesa/chem220/reference/Reduction-Potential.PDF
            elenega = [1.83, 1.88, 1.91, 1.65, 1.90, 1.55]
            eleaff = [16.7, 64.7, 113, 1, 119.4, 1]
            valence = [3, 4, 2, 2, 2, 4]
            ioni1 = [762.5, 760.4, 737.1, 906.4, 745.5, 717.3]
            ioni2 = [1561.876, 1648.356, 1753.027, 1733.3, 1957.919, 717.3]
	    ioni3 = [2957, 3232, 3395, 3833, 3555, 3248]
	    ioni4 = [5290, 4950, 5300, 5731, 5536, 4940]
	    ioni5 = [7240, 7670, 7339, 7970, 7700, 6990]
            radius = [156, 152, 149, 142, 145, 161]
            EC = [100, 170, 140, 170, 590, 6.2]#electronic conductivity
            NC = [2.56, 37.2, 4.5, 1.1, 3.78, 13.3] #Neutron Cross Section
            NM = [0.0015, 0.0021, 0.0026, 0.00055, 0.0021, 0.0083] #	Neutron Mass Absorption	
            LCx =[286.65, 250.71, 352.4, 266.49, 361.49, 891.25] #lattice constants_x
            LCz =[286.65, 406.95, 352.4, 494.68, 361.49, 891.25] #lattice constants_z
            SH = [449.0, 421.0, 445.0, 388.0, 384.4, 479.0] #specific HEAT
	    iradius = [75, 79, 83, 88, 87, 81] #ionic radius https://www.webelements.com
	    hyden = [-1840, -1915, -1980, -1915, -2010, -1760]#hydrogenation energy https://pubs.rsc.org/en/content/articlepdf/1991/ft/ft9918702995
	    oxir = [-648, -513, -360, -694, -368, -772 ]# Me + 0.5O2 = MeO 
	    TC = [79, 100, 91, 120, 400,7.7] #THERMAL Conductivity
	    HF = [13.8, 16.2, 17.2, 7.35, 13.1, 13.2] #heat of fusion
	    resis = [9.7,6,7,5.9,1.7, 160] #resistivity
            list_metals = [0, 0, 0, 0, 0, 0, 0, 0]
            v = 0
            b = extra
            if b > 0:
                for p in range(b):
                    list_metals[p] = 'Fe'
                for q in range(1, l-1):
                    #for p in range(4);
                    #if Elem[q] == metals[p]:
                       #v = p
                    b = b + v
                    v = int(Numb[q])
                    for p in range(b, b+v):
                        list_metals[p] = Elem[q]
            else:
                for q in range(1, l - 1):
                    # for p in range(4);
                    # if Elem[q] == metals[p]:
                    # v = p
                    b = b + v
                    v = int(Numb[q])
                    for p in range(b, b + v):
                        list_metals[p] = Elem[q]
            print(list_metals)
            elenega_m = [0, 0, 0, 0, 0, 0, 0, 0]#preassign the 8 sites interested
            eleaff_m =[0, 0, 0, 0, 0, 0, 0, 0]
            valence_m =[0, 0, 0, 0, 0, 0, 0, 0]
            ioni1_m =[0, 0, 0, 0, 0, 0, 0, 0]
            ioni2_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    ioni3_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    ioni4_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    ioni5_m = [0, 0, 0, 0, 0, 0, 0, 0]
            EC_m = [0, 0, 0, 0, 0, 0, 0, 0]
            NC_m = [0, 0, 0, 0, 0, 0, 0, 0]
            NM_m = [0, 0, 0, 0, 0, 0, 0, 0]
            LCx_m = [0, 0, 0, 0, 0, 0, 0, 0]
            LCz_m = [0, 0, 0, 0, 0, 0, 0, 0]
            SH_m = [0, 0, 0, 0, 0, 0, 0, 0]
            radius_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    iradius_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    oxir_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    hyden_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    TC_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    HF_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    resis_m = [0, 0, 0, 0, 0, 0, 0, 0]
	    redox_m = [0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(8):
                for n in range(6):
                    if list_metals[i] == metals[n]:
                        nn = n
                        break
                    else:
                        continue
                elenega_m[i] = elenega[nn] # assign the value corresponding the metal atoms
                eleaff_m[i] = eleaff[nn]
                valence_m[i] = valence[nn]
                ioni1_m[i] = ioni1[nn]
                ioni2_m[i] = ioni2[nn]
		ioni3_m[i] = ioni3[nn]
		ioni4_m[i] = ioni4[nn]
		ioni5_m[i] = ioni5[nn]
                EC_m[i] = EC[nn]
                NC_m[i] = NC[nn]
                NM_m[i] = NM[nn]
                LCx_m[i] = LCx[nn]
                LCz_m[i] = LCz[nn]
                SH_m[i] = SH[nn]
                radius_m[i] = radius[nn]
		iradius_m[i] = iradius[nn]
	        oxir_m[i] = oxir[nn]
		hyden_m[i] = hyden[nn]
		TC_m[i] = TC[nn]
		HF_m[i] = HF[nn]
		resis_m[i] = resis[nn]
		redox_m[i] = redox[nn]
            elenega_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]#preassign the 16 iron 3+
            eleaff_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            valence_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ioni1_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ioni2_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    ioni3_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    ioni4_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    ioni5_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            EC_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
            NC_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
            NM_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
            SH_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            LCx_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            LCz_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            radius_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    HF_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    TC_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    iradius_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    oxir_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    hyden_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            resis_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	    redox_m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(16):
                elenega_m1[i] = elenega[0]
                eleaff_m1[i] = eleaff[0]
                valence_m1[i] = valence[0]
                ioni1_m1[i] = ioni1[0]
                ioni2_m1[i] = ioni2[0]
		ioni3_m1[i] = ioni3[0]
		ioni4_m1[i] = ioni4[0]
		ioni5_m1[i] = ioni5[0]
                EC_m1[i] = EC[0]
                NC_m1[i] = NC[0]
                NM_m1[i] = NM[0]
                SH_m1[i] = SH[0]
                LCx_m1[i] = LCx[0]
                LCz_m1[i] = LCz[0]
                radius_m1[i] = radius[0]
		iradius_m1[i] = 69
		oxir_m1[i] = -1820
		hyden_m1[i] = -4265
		TC_m1[i] = TC[0]
		HF_m1[i] = HF[0]
		resis_m1[i] = resis[0]
		redox_m1[i] = redox[0]
            elenega_mt = elenega_m1 + elenega_m
            eleaff_mt = eleaff_m1 + eleaff_m
            valence_mt = valence_m1 + valence_m
            ioni1_mt = ioni1_m1 + ioni1_m
            ioni2_mt = ioni2_m1 + ioni2_m
	    ioni3_mt = ioni3_m1 + ioni3_m
	    ioni4_mt = ioni4_m1 + ioni4_m
	    ioni5_mt = ioni5_m1 + ioni5_m
            EC_mt = EC_m1 + EC_m
            NC_mt = NC_m1 + NC_m
            NM_mt = NM_m1 + NM_m
            SH_mt = SH_m1 + SH_m
            LCx_mt = LCx_m1 + LCx_m
            LCz_mt = LCz_m1 + LCz_m
            radius_mt = radius_m1 + radius_m
	    TC_mt = TC_m1 + TC_m
	    iradius_mt = iradius_m1 + iradius_m
	    oxir_mt = oxir_m1 + oxir_m
	    hyden_mt = hyden_m1 + hyden_m
	    HF_mt = HF_m1 + HF_m
	    resis_mt = resis_m1 + resis_m
	    redox_mt = redox_m1 + redox_m
            elenegaf = [0, 0, 0, 0, 0, 0, 0, 0]
            eleafff = [0, 0, 0, 0, 0, 0, 0, 0]
            valencef = [0, 0, 0, 0, 0, 0, 0, 0]
            ioni1f = [0, 0, 0, 0, 0, 0, 0, 0]
            ioni2f = [0, 0, 0, 0, 0, 0, 0, 0]
	    ioni3f = [0, 0, 0, 0, 0, 0, 0, 0]
	    ioni4f = [0, 0, 0, 0, 0, 0, 0, 0]
	    ioni5f = [0, 0, 0, 0, 0, 0, 0, 0]
            ECf = [0, 0, 0, 0, 0, 0, 0, 0]  
            NCf = [0, 0, 0, 0, 0, 0, 0, 0]  
            NMf = [0, 0, 0, 0, 0, 0, 0, 0]  
            SHf = [0, 0, 0, 0, 0, 0, 0, 0]  
            LCxf = [0, 0, 0, 0, 0, 0, 0, 0]  
            LCzf = [0, 0, 0, 0, 0, 0, 0, 0]  
            radiusf = [0, 0, 0, 0, 0, 0, 0, 0]
	    TCf = [0, 0, 0, 0, 0, 0, 0, 0]
	    HFf = [0, 0, 0, 0, 0, 0, 0, 0]
	    resisf = [0, 0, 0, 0, 0, 0, 0, 0]
	    redoxf = [0, 0, 0, 0, 0, 0, 0, 0]
	    iradiusf = [0, 0, 0, 0, 0, 0, 0, 0]
	    oxirf = [0, 0, 0, 0, 0, 0, 0, 0]
	    hydenf = [0, 0, 0, 0, 0, 0, 0, 0]
            for p in range(8):
                elenega_ac = 0
                eleaff_ac = 0
                valence_ac = 0
                ioni1_ac = 0
                ioni2_ac = 0
		ioni3_ac = 0
		ioni4_ac = 0
		ioni5_ac = 0
                EC_ac = 0
                NC_ac = 0
                NM_ac = 0
                SH_ac = 0
                LCx_ac = 0
                LCz_ac = 0
                radius_ac = 0
	        TC_ac = 0
		HF_ac = 0
		iradius_ac = 0
		oxir_ac = 0
		hyden_ac = 0
		resis_ac = 0
		redox_ac = 0
                for q in range(24):
                    ss = 16 + int(p)
                    elenega_ac = elenega_ac + elenega_m[p]*elenega_mt[q] / math.sqrt(1 + abs(preass_x[ss]**2 - preass_x[q]**2) +abs(preass_y[ss]**2 - preass_y[q]**2) + abs(preass_z[ss]**2 - preass_z[q]**2))
                    eleaff_ac = eleaff_ac + eleaff_m[p] * eleaff_mt[q] / math.sqrt(1 +
                                abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    valence_ac = valence_ac + valence_m[p] * valence_mt[q] / math.sqrt(1+
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    ioni1_ac = ioni1_ac + ioni1_m[p] * ioni1_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 -preass_z[q] ** 2))
                    ioni2_ac = ioni2_ac + ioni2_m[p] * ioni2_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    ioni3_ac = ioni3_ac + ioni3_m[p] * ioni3_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    ioni4_ac = ioni4_ac + ioni4_m[p] * ioni4_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    ioni5_ac = ioni5_ac + ioni5_m[p] * ioni5_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    EC_ac = EC_ac + EC_m[p] * EC_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    NC_ac = NC_ac + NC_m[p] * NC_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    NM_ac = NM_ac + NM_m[p] * NM_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    SH_ac = SH_ac + SH_m[p] * SH_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    LCx_ac = LCx_ac + LCx_m[p] * LCx_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    LCz_ac = LCz_ac + LCz_m[p] * LCz_mt[q] / math.sqrt(1 +
                            abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                    radius_ac = radius_ac + radius_m[p] * radius_mt[q] / math.sqrt(1 + 
                        abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    TC_ac = TC_ac + TC_m[p] * TC_mt[q] / math.sqrt(1 + 
                        abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    HF_ac = HF_ac + HF_m[p] * HF_mt[q] / math.sqrt(1 + 
                        abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    resis_ac = resis_ac + resis_m[p] * resis_mt[q] / math.sqrt(1 + 
                        abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    redox_ac = redox_ac + redox_m[p] * redox_mt[q] / math.sqrt(1 + 
                        abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    iradius_ac = iradius_ac + iradius_m[p] * iradius_mt[q] / math.sqrt(1 + 
                        abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    oxir_ac = oxir_ac + oxir_m[p] * oxir_mt[q] / math.sqrt(1 + 
                        abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
		    hyden_ac = hyden_ac + hyden_m[p] * hyden_mt[q] / math.sqrt(1 + 
                        abs(preass_x[ss] ** 2 - preass_x[q] ** 2) + abs(preass_y[ss] ** 2 - preass_y[q] ** 2) + abs(preass_z[ss] ** 2 - preass_z[q] ** 2))
                elenega_av = elenega_ac / 23
                eleaff_av = eleaff_ac / 23
                valence_av = valence_ac / 23
                ioni1_av = ioni1_ac / 23
                ioni2_av = ioni2_ac / 23
		ioni3_av = ioni3_ac / 23
		ioni4_av = ioni4_ac / 23
		ioni5_av = ioni5_ac / 23
                EC_av = EC_ac/23 
                NC_av = NC_ac/23 
                NM_av = NM_ac/23 
                SH_av = SH_ac/23 
                LCx_av = LCx_ac/23
                LCz_av = LCz_ac/23
                radius_av = radius_ac / 23
		TC_av = TC_ac / 23
		iradius_av = iradius_ac / 23
		oxir_av = oxir_ac / 23
		hyden_av = hyden_ac / 23
		HF_av = HF_ac / 23
		resis_av = resis_ac / 23
		redox_av = redox_ac / 23
                elenegaf[p] = elenega_av
                eleafff[p] = eleaff_av
                valencef[p] = valence_av
                ioni1f[p] = ioni1_av
                ioni2f[p] = ioni2_av
		ioni3f[p] = ioni3_av
		ioni4f[p] = ioni4_av
		ioni5f[p] = ioni5_av
                ECf[p] = EC_av 
                NCf[p] = NC_av
                NMf[p] = NM_av
                SHf[p] = SH_av
                LCxf[p] = LCx_av
                LCzf[p] = LCz_av
                radiusf[p] = radius_av
		TCf[p] = TC_av
		iradiusf[p] = iradius_av
		oxirf[p] = oxir_av
		hydenf[p] = hyden_av
                HFf[p] = HF_av
		resisf[p] = resis_av
		redoxf[p] = redox_av
            feature = elenegaf + eleafff + valencef + ioni1f + ioni2f + radiusf + redoxf + TCf + HFf + resisf + iradiusf + oxirf + hydenf + ioni3f + ioni4f + ioni5f + ECf + NCf + NMf + SHf + LCxf + LCzf
            os.chdir('/curium/jiazhoz/material_project/Material_project/')
            with open("features1.txt", 'a') as file:
                for item in feature:
                   file.write("%s " % item) 
                file.write('\n')

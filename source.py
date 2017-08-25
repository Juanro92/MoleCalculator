import re

#some element data

elements ={}
elements["H"] = 1.0078
elements["C"] = 12.0107
elements["O"] = 15.9994
elements["Cl"] = 35.453
elements["He"] = 4.0026
elements["Li"] = 6.941
elements["Be"] = 9.0122
elements["B"] = 10.811
elements["N"] = 14.0067
elements["F"] = 18.9984
elements["Ne"] = 20.1797
elements["Na"] = 22.9897
elements["Mg"] = 24.305
elements["Al"] = 26.9815
elements["Si"] = 28.0855
elements["P"] = 30.9738
elements["S"] = 32.065
elements["Cl"] = 35.453
elements["Ar"] = 39.948
elements["K"] = 39.0983
elements["Ca"] = 40.078
elements["Sc"] = 44.9559
elements["Ti"] = 47.867
elements["V"] = 50.9415
elements["Cr"] = 51.9961
elements["Mn"] = 54.938
elements["Fe"] = 55.845
elements["Co"] = 58.9332
elements["Ni"] = 58.6934
elements["Cu"] = 63.546
elements["Zn"] = 65.39
elements["Ga"] = 69.723
elements["Ge"] = 72.64
elements["As"] = 74.9216
elements["Se"] = 78.96
elements["Br"] = 79.904
elements["Kr"] = 83.8
elements["Rb"] = 85.4678
elements["Sr"] = 87.62
elements["Y"] = 88.9059
elements["Zr"] = 91.224
elements["Nb"] = 92.9064
elements["Mo"] = 95.94
elements["Tc"] = 98
elements["Ru"] = 101.07
elements["Rh"] = 102.9055
elements["Pd"] = 106.42
elements["Ag"] = 107.8682
elements["Cd"] = 112.411
elements["In"] = 114.818
elements["Sn"] = 118.71
elements["Sb"] = 121.76
elements["Te"] = 127.6
elements["I"] = 126.9045
elements["Xe"] = 131.293
elements["Cs"] = 132.9055
elements["Ba"] = 137.327
elements["La"] = 138.9055
elements["Ce"] = 140.116
elements["Pr"] = 140.9077
elements["Nd"] = 144.24
elements["Pm"] = 145
elements["Sm"] = 150.36
elements["Eu"] = 151.964
elements["Gd"] = 157.25
elements["Tb"] = 158.9253
elements["Dy"] = 162.5
elements["Ho"] = 164.9303
elements["Er"] = 167.259
elements["Tm"] = 168.9342
elements["Yb"] = 173.04
elements["Lu"] = 174.967
elements["Hf"] = 178.49
elements["Ta"] = 180.9479
elements["W"] = 183.84
elements["Re"] = 186.207
elements["Os"] = 190.23
elements["Ir"] = 192.217
elements["Pt"] = 195.078
elements["Au"] = 196.9665
elements["Hg"] = 200.59
elements["Tl"] = 204.3833
elements["Pb"] = 207.2
elements["Bi"] = 208.9804
elements["Po"] = 209
elements["At"] = 210
elements["Rn"] = 222
elements["Fr"] = 223
elements["Ra"] = 226
elements["Ac"] = 227
elements["Th"] = 232.0381
elements["Pa"] = 231.0359
elements["U"] = 238.0289
elements["Np"] = 237
elements["Pu"] = 244
elements["Am"] = 243
elements["Cm"] = 247
elements["Bk"] = 247
elements["Cf"] = 251
elements["Es"] = 252
elements["Fm"] = 257
elements["Md"] = 258
elements["No"] = 259
elements["Lr"] = 262
elements["Rf"] = 261
elements["Db"] = 262
elements["Sg"] = 266
elements["Bh"] = 264
elements["Hs"] = 277
elements["Mt"] = 268




#Search data inside ()
def getWeight(formula):
    myRegEx = re.compile(r"(\()(\w*)(\))(\d*)",re.I)

    myMatches = myRegEx.findall(formula)

    while myMatches:
        myMatches = myRegEx.findall(formula)
        for match in myMatches:
            print (match[1], match[3])
            count = match[3]
            text =""
            if (count == ""):
                count = 1
            else:
                count = int(match[3])
            while (count >= 1):
                text = text + match[1]
                count -= 1
                print(text)
            formula = formula.replace('(' + match[1] + ')' + match[3], text)
            print("Replaced formula: ",formula)

    myRegEx = re.compile("(C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|U|V|W|Xe|Yb?|Z[nr])(\d*)")

    myMatches = myRegEx.findall(formula)

    molecularFormula =""
    MW = 0
    text =""

    for match in myMatches:
        #Search symbol
        symbol = match[0]
        #Search numbers
        number = match[1]
        print(symbol,number)
        if (number == ""):
            number = 1
        else:
            number = int(match[1])
        MW = MW + float(elements[symbol])*number
        while (number >=1):
            molecularFormula = molecularFormula + symbol
            number -= 1 
    print(molecularFormula)
    print("formula: " + formula + " MW = " + str(MW))


# formula = "(ClC6H4)2CH(CCl3))"
formula = "KMnO4"


print("Original Formula: ", formula)
getWeight(formula)

formula = "C6H12O6"


print("Original Formula: ", formula)
getWeight(formula)

formula = "H2O2"


print("Original Formula: ", formula)
getWeight(formula)
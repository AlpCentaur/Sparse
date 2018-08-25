
#Serie01 Luca Wulf
import csv
from numpy import *
import numpy as np
from decimal import *
import re



class Sparse(object):
        """Klasse der Sparsevektoren"""
        typ = 0
        null = 0
        
        
        
        def __init__(self, vektor, leng):     
                """Konstruktur der Sparseklasse
                
                :param:   vektor, datentyp list mit eintraegen aus einem allgemeinen koerper oder im Falle Sparse liste aus tupeln und laenge des Vektors, datentyp int 
                :returns: via str wird ausschliesslich der Sparsevektor im stringformat ausgegeben"""
                
                
                
                vectry = len(np.array(vektor).shape)
                #print vectry
                if vectry == 1:
                    
                    
                        
                    
                    for n in range(len(vektor)-1):
                            if type(vektor[n]) != type(vektor[n+1]):
                                raise TypeError('Alle Eintraege des Vektors sollten den gleichen Typ haben')                  
                    try:
                        for n in range(len(vektor)):
                            
                            a = vektor[n] - vektor[n]
                            if vektor[n] != a:
                                
                                b = vektor[n] + vektor[n]
                                c = vektor[n] / vektor[n]
                                d = vektor[n] * vektor[n]
                                e = vektor[n] <= vektor[n]
                    except ValueError:
                        print("In der InputDatei befindet sich etwas, was kein koerper zu sein scheint.")
                    
                    except TypeError:
                        print("In der InputDatei befindet sich etwas, was kein koerper zu sein scheint.")
                    
                    
                    v =0
                    for i in vektor:
                            v = v+1
                    
                    if np.array(vektor).shape[0] == 0:
                        N = 0
                        self.N = N
                        nachSparse = [(0,self.N)]
                        Sparse.typ = 'Donna know till know..'
                    else:
                        
                        N = vektor[0] - vektor[0]
                        self.N = N
                        Sparse.typ = type(vektor[0])
                    
                    te = []
                    for i in range(v):
                            if vektor[i] != vektor[i] + vektor[i]:
                                    te.append(1)
                            else:
                                    continue
                    if not te:	      
                            
                            preSparse = [(0,N)]
                            anzahl = 1
                    
                    else:	
                            
                            preSparse = np.array(empty((v,2))).tolist()
                            
                            anzahl = 0
                            for stelle in range(v):
                                    if vektor[stelle] == N:
                                            continue 
                                    else: 
                                            preSparse[anzahl][0] = stelle +1
                                            preSparse[anzahl][1] = vektor[stelle]
                                            anzahl = anzahl + 1
                    l = 0
                    for i in preSparse[0:anzahl][:]:
                            l = l+1
                                    
                                    
                    #self.Sparse = preSparse[0:anzahl][:]
                    
                    vorSparse = preSparse[0:anzahl][:]
                    nachSparse = []
                    for n in range(len(vorSparse)):
                        nachSparse.append((vorSparse[n][0],vorSparse[n][1]))
                    
                    self.Sparse = nachSparse
                    self.length = leng	
                    self.slength = l
                    
                    type(self).null = N
                    
                if vectry == 2:
                    if leng < 0:
                        raise IndexError('Die von Ihnen angegebene Laenge ist negativ.')
                    for n in range(np.array(vektor).shape[0]-1):
                        if type(vektor[n][1]) != type(vektor[n+1][1]):
                            raise TypeError('Alle Eintraege des Vektors sollten den gleichen Typ haben')   
                    
                    #print np.array(vektor).shape[0]
                    for n in range(np.array(vektor).shape[0]):
                        if vektor[n][0] > leng:
                            raise IndexError('Die Indizees haben groessere Eintraege als die angegebene Laenge.')
                        if vektor[n][0] < 0:
                            raise IndexError('bitte keine negativen Indizees, starten Sie das Programm erneut.')
                        for m in range(np.array(vektor).shape[0]):
                            
                            if m != n:
                                if vektor[m][0] == vektor[n][0]:
                                    raise IndexError('es existieren mehrere Werte fuer einen Index')
                    
                    try:
                        for n in range(len(vektor)):
                            a = vektor[n][1] - vektor[n][1]
                            b = vektor[n][1] + vektor[n][1]
                            
                            d = vektor[n][1] * vektor[n][1]
                            e = vektor[n][1] <= vektor[n][1]
                    except ValueError:
                        print("In der InputDatei befindet sich etwas, was kein koerper zu sein scheint.")
                    
                    
                    self.N = vektor[0][1] - vektor[0][1]
                    count = 0
                    vektorr = []
                    for n in range(len(vektor)):
                        if vektor[n][1] == self.N:
                            continue
                        else:
                            vektorr.append((vektor[n][0],vektor[n][1]))
                            count =+ 1
                    if count == 0:
                        vektorr = [(0,self.N)]
                    
                    
                    
                    self.Sparse = vektorr
                    self.length = leng
                    self.slength = np.array(vektorr).shape[0]
                    
                    
                    type(self).typ = type(vektor[0][1])
                    type(self).null = vektor[0][1] - vektor[0][1]
                
                    if np.array(vektor).shape[1] > 2:
                        raise Exception('Fuer den Input als Sparse sollte es sich um eine Liste aus Tupeln handeln')
                
        def __eq__(self, other):
            """In diesem Programm wird mit Hilfe von magic methods, also aufrufbar mit == ueberprueft, ob die beiden Sparsevektoren gleich sind
            
            :param: self, other bezeichnen Vektoren der Sparse Klasse.
            :returns: True fuer gleich und False fuer unterschiedlich"""
            if self.length != other.length:
                return bool(None)
            
            if self.Sparse == [(0,self.N)] and other.Sparse == [(0,other.N)]:
                return not bool(None)
            
            else:
                                
                                                                
                Val = all([self.Sparse[m][1] == other.Sparse[m][1] for m in range(self.slength)])
                
                
                
                return Val 
            
            
        
        
        def __str__(self):
                """in diesem Programm wird ein Element der Sparse Klasse zu einem string Objekt ueberfuehrt
                
                :param: self bezeichnet einen Vektor der Sparse Klasse.
                :returns: einen vektor im stringformat"""

                return str((self.Sparse,self.length)).strip('[]') 

        #def __mul__(self,L):
                #"""in diesem Programm wird ein Sparsevektor mit einem Skalar multipliziert
                
                #:param: L bezeichnet den Skalar aus dem Koerper. Der zweite Parameter ist mit self ein Vektor der Sparse Klasse.
                #:returns: einen Vektor der Sparse Klasse"""
                
                
                #out = []
                #for stelle in range(0, self.slength):
                        #out.append([self.N,self.N])
                
                
                
                #if L!=self.N:
                        
                        #for stelle in range(0, self.slength):
                                #out[stelle][0]= self.Sparse[stelle][0]
                                #out[stelle][1]= self.Sparse[stelle][1]*L      
                
                #else:
                        #out = [[self.N,self.N]]
                
                
                #return Sparse(out,self.length)
        #def __mul__(L,self):
                #"""in diesem Programm wird ein Sparsevektor mit einem Skalar multipliziert
                
                #:param: L bezeichnet den Skalar aus dem Koerper. Der zweite Parameter ist mit self ein Vektor der Sparse Klasse.
                #:returns: einen Vektor der Sparse Klasse"""
                
                
                #out = []
                #for stelle in range(0, self.slength):
                        #out.append([self.N,self.N])
                
                
                
                #if L!=self.N:
                        
                        #for stelle in range(0, self.slength):
                                #out[stelle][0]= self.Sparse[stelle][0]
                                #out[stelle][1]= self.Sparse[stelle][1]*L      
                
                #else:
                        #out = [[self.N,self.N]]
                
                
                #return Sparse(out,self.length)

        
        
        def __add__(self,other):              #benutzen von magic methods
                """in diesem Programm werden zwei Sparsevektoren addiert
                
                :param: self und other bezeichnen zwei Vektoren der Sparse Klasse.
                :returns: einen Vektor der Klasse Sparse"""

                
                
                
                if self.length == other.length:
                        if self.Sparse == [(0,self.N)]:
                            return Sparse(other.Sparse, self.length)
                        
                        
                        if other.Sparse == [(0,other.N)]:
                            return Sparse(self.Sparse, self.length)
                        out = []
                            
                            
                        
                        #print self.length
                        #print other.length
                        
                        
                        
                        equalsel = []
                        equaloth = []
                        for i in range(self.slength):
                            for j in range(other.slength):
                                if self.Sparse[i][0] == other.Sparse[j][0]:            
                                    out.append((self.Sparse[i][0],other.Sparse[j][1]+self.Sparse[i][1]))
                                    equalsel.append(i)
                                    equaloth.append(j)
                        Rangesel = [x for x in range(self.slength) if not x in equalsel]
                        Rangeoth = [x for x in range(other.slength) if not x in equaloth]
                        
                        #print Rangesel
                        #print Rangeoth
                        
                        for i in Rangesel:
                            out.append((self.Sparse[i][0],self.Sparse[i][1]))
                        for i in Rangeoth:
                            out.append((other.Sparse[i][0],other.Sparse[i][1]))    
                                            
                        
                        #print out
                        
                        Sum = Sparse(out,self.length)
                        
                        return Sum
                else:
                        raise IndexError("Vektorenlaenge ungleich!")
    
        """Die Differenz eines Sparsevektors wird berechnet als Kombination aus Summe und Skalarmultiplikation """

        def __sub__(self,other):              #benutzen von magic methods
                """in diesem Programm werden zwei Sparsevektoren subtrahiert
                
                :param: self und other bezeichnen zwei Vektoren der Sparse Klasse.
                :returns: einen Vektor der Klasse Sparse"""
                
                if self.length == other.length:
                        
                        if self.Sparse == [(0,self.N)]:
                            return Sparse([(x,-y) for x, y in other.Sparse], self.length)
                        
                        
                        if other.Sparse == [(0,other.N)]:
                            return Sparse(self.Sparse, self.length)
                        
                        out = []
                            
                        
                        
                        equalsel = []
                        equaloth = []
                        for i in range(self.slength):
                            for j in range(other.slength):
                                if self.Sparse[i][0] == other.Sparse[j][0]:            
                                    out.append((self.Sparse[i][0],other.Sparse[j][1]-self.Sparse[i][1]))
                                    equalsel.append(i)
                                    equaloth.append(j)
                        Rangesel = [x for x in range(self.slength) if not x in equalsel]
                        Rangeoth = [x for x in range(other.slength) if not x in equaloth]
                        
                        #print Rangesel
                        #print Rangeoth
                        
                        for i in Rangesel:
                            out.append((self.Sparse[i][0],self.Sparse[i][1]))
                        for i in Rangeoth:
                            out.append((other.Sparse[i][0],-other.Sparse[i][1]))    
                                            
                        
                        
                        Dif = Sparse(out,self.length)
                        
                        return Dif
                else:
                        raise IndexError("Vektorenlaenge ungleich!")
                

        
        def __mul__(self,other):
                """in diesem Programm werden zwei Sparsevektoren skalarmultipliziert oder ein Skalar an einen Sparsevektor multipliziert
                
                :param: self und other bezeichnen zwei Vektoren der Sparse Klasse oder self ist Sparse, other ist Skalar.
                :returns: c, Datentyp integer or Sparse(out) Datentyp Sparse"""
                
                #print 'B', proof
                #print 'A', proof.dtype
                if isinstance(self, Sparse) and isinstance(other, Sparse):
                        if self.length == other.length:
                                
                                if self.Sparse == [(0,self.N)]:
                                    return Sparse(self.Sparse, self.length)
                                c=self.N
                                for stelleA in range(self.slength):
                                        for stelleB in range(other.slength):
                                                if self.Sparse[stelleA][0]==other.Sparse[stelleB][0]:
                                                        c= c+ self.Sparse[stelleA][1]*other.Sparse[stelleB][1]
                                return c
                        else:
                                raise IndexError("Vektorenlaenge ungleich!")
                if isinstance(self, Sparse) and not isinstance(other, Sparse):
                        if self.Sparse == [(0,self.N)]:
                                    return Sparse(self.Sparse, self.length)
                        
                                            
                        out = []
                        for stelle in range(0, self.slength):
                                out.append([self.N,self.N])
                        
                        
                        
                        if other!=self.N:
                                
                                for stelle in range(0, self.slength):
                                        out[stelle][0]= self.Sparse[stelle][0]
                                        out[stelle][1]= self.Sparse[stelle][1]*other      
                        
                        else:
                                out = [[self.N,self.N]]
                        
                        
                        return Sparse(out,self.length)
        @staticmethod
        def full2sparse(vektor):
            """in diesem Programm wird aus einem numpy array ein Objekt der Sparse Klasse gemacht
            
            :param: ein numpy.array
            :returns: ein Vektor der Sparse Klasse"""
            leng = len(vektor)
            out = Sparse(vektor,leng)
            return out
        
        def __rmul__(self,other):
                """in diesem Programm werden zwei Sparsevektoren skalarmultipliziert oder ein Skalar von rechts an einen Sparsevektor multipliziert
                
                :param: self und other bezeichnen zwei Vektoren der Sparse Klasse oder self ist Sparse, other ist Skalar.
                :returns: c, Datentyp integer or Sparse(out) Datentyp Sparse"""
                
                if isinstance(self, Sparse) and isinstance(other, Sparse):
                        
                        if self.length == other.length:
                                if self.Sparse == [(0,self.N)]:
                                    return Sparse(self.Sparse, self.length)
                                
                                c=self.N
                                for stelleA in range(self.slength):
                                        for stelleB in range(other.slength):
                                                if self.Sparse[stelleA][0]==other.Sparse[stelleB][0]:
                                                        c= c+ self.Sparse[stelleA][1]*other.Sparse[stelleB][1]
                                return c
                        else:
                                raise IndexError("Vektorenlaenge ungleich!")
                if isinstance(self, Sparse) and not isinstance(other, Sparse):
                        out = []
                        for stelle in range(0, self.slength):
                                out.append([self.N,self.N])
                        if self.Sparse == [(0,self.N)]:
                                    return Sparse(self.Sparse, self.length)
                        
                        
                        if other!=self.N:
                                
                                for stelle in range(0, self.slength):
                                        out[stelle][0]= self.Sparse[stelle][0]
                                        out[stelle][1]= self.Sparse[stelle][1]*other      
                        
                        else:
                                out = [[self.N,self.N]]
                        
                        
                        return Sparse(out,self.length)
            
                
        """Das Produkt mit einem Skalar eines Sparsevektors wird berechnet, indem jeder Eintrag in der zweiten Spalte des Sparsevektors, (also die Vektorwerte ungleich 0) mit dem Skalar multipliziert wird. Die erste Spalte bleibt erhalten """

        

        
                        
        @staticmethod
        def readVector(datei, typ):
            """in diesem Programm werden wird ein Vektor aus einer Csv Datei eingelesen. Das Programm erkennt
            in welchen Format die Daten vorliegen und waehlt das passende Programm aus. Vorgabe: sparse: dann der vektor, full: dann der vektor.
            
            :param: CSV Datei im Sparseformat oder Listenformat, gewuenschtes Format float oder Decimal, Datentyp string
            :returns: Vektor der Klasse Sparse, Datentyp der Eintraege je nach Eingabe float oder Decimal, Datentyp Object"""
            
            
            csvdoc= open(datei)
            liste = []
            indliste = []
            #print csvdoc
            for line in csvdoc:
                #print '1'
                #print line
                indliste.append(line)
                liste.append([x for x in re.findall(r'\b\d+\b', line)])
            v=[]
            eintraege=[]
            alle=[]
            i=0
            
            liste = liste[0]
            
            #print '2'
            #print liste			
            #print '22'
            #print indliste
            #print indliste[0][0:6]
            if len(liste) == 0:
                raise BaseException ("Die Datei enthaelt eine leere Zeile")
            
                    
            
            i=0
            if typ == float:
                try:
                    a=[float(k) for k in liste]
                except ValueError:
                    print("In der InputDatei befindet sich etwas, das nicht zu float umgewandelt werden kann.")
                
                test = []
                with open(datei) as f:
                    #print '3'
                    #print f
                    for line in f:
                        
                        test.append([ float(n) for n in re.findall(r'\b\d+\b', line)])
                
                
                
            if typ == Decimal:
                try:
                    a=[Decimal(k) for k in liste]
                except ValueError:
                    print("In der InputDatei befindet sich etwas, das nicht zu Decimal umgewandelt werden kann.")
            
                test = []
                with open(datei) as f:
                    #print '3'
                    #print f
                    for line in f:
                        
                        test.append([ Decimal(n) for n in re.findall(r'\b\d+\b', line)])
                        
                
            #print '4'
            #print test
                
            if indliste[0][0:6] == 'sparse':
                    
                for n in range(len(test)-1):
                    if len(test[n]) !=2:
                        raise BaseException('Your Input has to be 2 dim * n dim of numbers if you want to read sparse, with the dim of the vector as last entry')
                
                n = len(test)-1
                lang = test.pop()
                test = test[0:n]
                #print '5'
                #print test
                lang = int(lang[0])    
                if len(test) == 0:
                    test = [(Decimal(0),Decimal(0))]
        
            if indliste[0][0:4] == 'full':
                lang = len(test[0])
                test = test[0]
                #print lang
                    
            
            
            
            
            return Sparse(test,lang)

        def maxabs(self):
                """in diesem Programm wird der groesste Eintrag eines Sparsevektors normiert ausgegeben
                
                :param: self ein Vektor der Sparse Klasse.
                :returns: c, Datentyp integer"""
                
                out = []
                for stelle in range(0, self.length+1):
                        out.append(self.N)
                
                
                for i in range(self.slength):
                        
                        if self.Sparse[i][1] < self.N:
                                out[i] = -self.Sparse[i][1]
                        if self.Sparse[i][1] >= self.N:
                                out[i] = self.Sparse[i][1]
                
                
                c=self.N
                for stelle in range(self.slength):
                        c=max(c,out[stelle])
                return c



        def printFull(self):       #Ausgabe des vollen Vektors
                """in diesem Programm wird ein Sparsevektor in Stringformat ueberfuehrt.
                
                :param: self ein Vektor der Sparse Klasse.
                :returns: out, Datentyp string"""
                out = []
                for stelle in range(1, self.length+1):
                        out.append(self.N)
                
                for stelle in range(1,self.length+1):
                        for i in range(self.slength):
                                if stelle == self.Sparse[i][0]:
                                        out[stelle-1] = self.Sparse[i][1]
                                else:
                                        continue
                return ','.join(str(x) for x in out)





def csvReaderlist(datei):	
        """in diesem Programm wird aus einer comma separated values Datei im Listenformat ein Vektor ausgelesen, .
        
        :param: CSV Datei im Listenformat.
        :returns: resultli, Datentyp Liste"""
        
        csvdoc=csv.reader(open(datei))
        v=[]
        eintraege=[]
        alle=[]
        i=0
                                
        for line in csvdoc:
                if not line:
                        raise BaseException ("Die Datei enthaelt eine leere Zeile")
                else:
                        v+=[line]
        if len(v)==0: 
                raise BaseException("Die CSV-Datei ist leer")
                
        while i < len(v)-1:
                alle+=[v[i][0]]
                alle+=[v[i][1]]
                i+=1
        alle+=v[len(v)-1]
                
        i=0
        try:
                a=[float(k) for k in alle]
        except ValueError:
                print("In der Datei finden sich Characters oder Strings.")
        
        
        with open(datei) as csvfile:
                Vektor = csv.reader(csvfile, delimiter=',', quotechar='|')
                resultli = []
                for row in Vektor:
                        for i in row:
                                i = float(i)
                                resultli.append(i)
                        
                        
        
        return resultli

def csvReaderSparse(datei):
        """in diesem Programm wird aus einer comma separated values Datei mit Eintraegen im Sparseformat,
        der letzte Eintrag bezeichnet die Dimension, ein Vektor ausgelesen, .
        
        :param: CSV Datei im Sparseformat.
        :returns: out, Datentyp Liste"""
        
        csvdoc=csv.reader(open(datei))
        v=[]
        eintraege=[]
        alle=[]
        i=0
                                
        for line in csvdoc:
                if not line:
                        raise BaseException ("Die Datei enthaelt eine leere Zeile")
                else:
                        v+=[line]
        if len(v)==0: 
                raise BaseException("Die CSV-Datei ist leer")
                
        while i < len(v)-1:
                alle+=[v[i][0]]
                alle+=[v[i][1]]
                i+=1
        alle+=v[len(v)-1]
                
        i=0
        try:
                a=[float(k) for k in alle]
        except ValueError:
                print("In der Datei finden sich Characters oder Strings.")
        
        
        
        
        mynumbers = []
        with open(datei) as f:
                for line in f:
                        mynumbers.append([int(n) for n in line.strip().split(',')])
        
        

        dim = mynumbers.pop()
        dim = map(int, dim)
        d = dim[0]

        

        sd = 0
        for i in mynumbers:
                sd = sd+1
        

        out = zeros(d)
        a = 0
        for stelle in range(0,d):
                for i in range(0,sd):
                        if stelle == mynumbers[i][0]:
                                out[stelle-1] = mynumbers[i][1]
                        else:
                                continue
        return out		      

def csvReadercombined(datei, typ):
        """in diesem Programm werden die beiden Programme csvReaderlist und csvReaderSparse kombiniert. Das Programm erkennt
        in welchen Format die Daten vorliegen und waehlt das passende Programm aus. Nur im uneindeutigen Fall von einem Eintrag, wird der Benutzer gefragt, ob er Sparse oder List moechte.
        
        :param: CSV Datei im Sparseformat oder Listenformat, Typ Auswahl 'float' oder 'Decimal' im Stringformat.
        :returns: Vektor der Sparse Klasse"""
        
        
        csvdoc=csv.reader(open(datei))
        v=[]
        eintraege=[]
        alle=[]
        i=0
                                
        for line in csvdoc:
                if not line:
                        raise BaseException ("Die Datei enthaelt eine leere Zeile")
                else:
                        v+=[line]
        if len(v)==0: 
                raise BaseException("Die CSV-Datei ist leer")
                
        while i < len(v)-1:
                alle+=[v[i][0]]
                alle+=[v[i][1]]
                i+=1
        alle+=v[len(v)-1]
                
        i=0
        if typ == 'float':
            try:
                a=[float(k) for k in alle]
            except ValueError:
                print("In der InputDatei befindet sich etwas, das nicht zu float umgewandelt werden kann.")
        
            test = []
            with open(datei) as f:
                for line in f:
                    test.append([ float(n) for n in line.strip().split(',')])
        if typ == 'Decimal':
            try:
                a=[Decimal(k) for k in alle]
            except ValueError:
                print("In der InputDatei befindet sich etwas, das nicht zu Decimal umgewandelt werden kann.")
        
            test = []
            with open(datei) as f:
                for line in f:
                    test.append([ Decimal(n) for n in line.strip().split(',')])
                    
        
        tele = test[0]
        if len(tele) == 1:
                datin = str(raw_input("Geben Sie bitte ein s ein, falls Sie einen Sparsevektoren einlesen moechten. Fuer jede andere Eingabe wird davon ausgegangen, dass Sie eine Liste einlesen moechten:"))
        
                if datin == 's':
                        vekt = []
                        N = tele[0]-tele[0]
                        lang = tele
                        if tele[0] == N:
                                vekt = [N]
                        else:
                                for i in range(int(tele[0])):
                                        vekt.append(N)
                else:
                        vekt = csvReaderlist(datei)
                        lang = len(tele)
        else:
                testd = test.pop()
                if len(testd) == 1:
                        vekt = csvReaderSparse(datei)
                        lang = len(vekt)
                else:
                        vekt = csvReaderlist(datei)
                        lang = len(vekt)
        return Sparse(vekt,lang)




if __name__ == '__main__':
    """ name == main funktioniert folgendermassen: Wenn das Programm Sparse.py gestartet wird, ist name = main, wenn die Klasse Sparse importiert wird, dann ist name = Sparse, also wird der folgende Code nicht ausgefuehrt.
    
    :param: automatische Variable beim Starten des Programms.
    :returns: Ausfuehren des Testing Codes im Falle True"""
    
    z = [1,2,4,3,0,3]
    q = [-1,-2,-4,-3,0,-3]
    zb = [0,0,0,0,0,0]
    
    zb = Sparse(zb,6)
    
    
    print( 'blub')
    print( zb)
    z = Sparse(z,6)
    print(zb + z)
    print(z)
    print(z.Sparse)
    print(z.length)
    print(z + z)
    print('Ab hier die Beispiele aus der Mail im Koerper Z3:')
    
    import finite as fin

    Z3 = fin.Z(3)
    elem3 = Z3(3)
    elem11 = Z3(11)
    elem10 = Z3(10)
    vec1 = Sparse([(2,elem3),(4,elem11)],7)
    print(vec1)
    
    vec2 = vec1-vec1
    print(vec2)
    vec3 = vec2-vec1
    vec4 = vec1-vec2
    print(Sparse(vec1.Sparse,7))
    print(vec2)
    print(vec3)
    print(vec4)
    print(vec4.N)
    print(vec1==vec2)
    print('Skalarmultiplikation von rechts:', vec4*elem3)
    print(vec4*vec4)
    print('Skalarmultiplikation von links:', elem3*vec4)
    print('Und der Typ:')
    print(vec4.typ)
    vec5 = Sparse([(2,elem3),(4,elem11),(5,elem10)],7)
    print('Die MaxNorm angewendet auf den Vektor der darueber steht:')
    print(vec5)
    m5 = vec5.maxabs()
    print(m5)
    print('Und die print Full Methode noch angewendet:')
    print(vec5.printFull())
    
    
    Z13 = fin.Z(13)
    one = Z13(1)
    zero = Z13(0)

    vec1 = Sparse([(i,one) for i in range(1,1000)], 1000)
    vec2 = vec1*zero
    vec3 = Sparse([],1000) # added by franz for test reasons 13.1
    
    print(vec2.Sparse)
    print( vec3.Sparse)
    print( vec2 == vec3)
    print( vec2 + vec3)
    print('blub')
    print( zero*vec3)
    
    if ( (not(vec2 == vec3))  or (not(vec3 == vec2)) ):
        raise AssertionError("vec*Sparse.null != nullVec ")
    
    
    
    
    
    
    y = [(3,-4),(1,-3),(4,-5),(5,-6),(6,-3)]
    
    print( 'Hier wird nochmal der folgende vektor y..')
    print( y)
    x = [(2,4),(5,3),(6,5)]
    
    
    #xf = np.array(x).astype('float16')
    #yf = np.array(y).astype('float16')
    
    xs = Sparse(x,6)
    ys = Sparse(y,6)
    print( '... in sparse umgewandelt und dann der typ ausgelesen:')
    print( ys.typ)
    
    #getcontext().prec = 8
    #for n in range(len(y)):
    #y[n][1] = Decimal(y[n][1])
    #for m in range(len(x)):
    #x[m] = Decimal(x[m])
        
    
    #xs = Sparse(x,6)
    #ys = Sparse(y,6)
    
    print()
    print( 'Neue Operation mit folgenden Vektoren:') 
    print( )
    print( xs)
    print( ys)
    print( 'Jetzt werden die beiden Vektoren addiert')
    print()
    print( xs + ys)
    
    print()
    print()
    print()
    print( 'die eq function und wieder typen wird hier angezeigt:')
    
    print( xs==ys)
    print( xs.typ)
    print( ys.typ)
    print( 'Jetzt werden die beiden Vektoren subtrahiert')
    print( xs - ys)
    
    z = Sparse.readVector('Argumente.csv',float)
    zd = Sparse.readVector('Argumente.csv',Decimal)
    
    print( 'Das hier ist Ergebnis einer staticmethod:')
    print( z)
    print( zd)
    print( 'Hier wird dieses Ergebnis mit sich selbst skalarmultipliziert und anschliessend die 4 von rechts sowie von links heranmultipliziert:')
    print()
    print( z*z)
    print( )
    print( z*4)
    print()
    print( 4*z)
    
    print()
    print( 'Die zweite staticmethod full2sparse:')
    print()
    print( Sparse.full2sparse(np.array([1,1,2])))
    #x = ['Auto',0,4,5,6,3]
    #print Sparse(x,6)





            

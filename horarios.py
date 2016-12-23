class Hora:
    #Hora: str -> Hora
    def __init__(self,time):
        if type(time) != str: raise TypeError
        if ":" not in time: raise ValueError("Colon not in argument")
        indexColon = time.index(":")
        if indexColon == 0 or indexColon == len(time) - 1:
            raise ValueError("Colon must be between hours and minutes")
        self.hora = int(time[:indexColon])
        self.min = int(time[indexColon+1:])

    #getHoraFloat: None -> float
    #retorna hora con decimal (10:30 es 10.5; 18:45 es 18,75)
    def getHoraFloat(self):
        return self.hora + self.min/60.0

    #getHora: None -> float
    def getHora(self):
        return self.getHoraFloat()

    #getMinutos: None -> int
    #retorna cuantos minutos han pasado desde las 8:30
    def getMinutos(self):
        minutos = int(self.getHora()*60)
        ocho30 = 510 #minutos desde medianoche
        return minutos-ocho30

assert Hora("09:30").getMinutos() == 60
        
class Bloque:
    #Bloque: str str (str or int) Hora Hora -> Bloque
    def __init__(self,tipo,dia,ti,tf):
        if tipo not in ["cat","aux","lab","con","otro"]:
            raise ValueError("tipo must be 'cat', 'aux', 'lab', 'con' or 'otro'")
        self.tipo = tipo
        diaNum = [1,2,3,4,5,6]
        diaNom = ["lu","ma","mi","ju","vi","sa"]
        if type(dia) == int:
            self.dia = diaNom[diaNum.index(dia)]
        else:
            self.dia = dia.lower()[:2]
        self.ti = ti
        self.tf = tf

    def getBloque(self):
        return [tipo, dia, ti.getHora(), tf.getHora()]

    #__eq__: Bloque -> bool
    #True si 2 bloques empiezan y terminan a la misma hora el mismo dia
    def __eq__(self,x):
        return self.dia == x.dia and self.ti == x.ti and self.tf == x.tf

    #chocaCon: Bloque int -> bool
    #True si 2 bloques se solapan. Si el parametro "margen" se pasa, considera
    #ese tiempo (en minutos) como tolerancia maxima
    def chocaCon(self,x,margen=0):
        inicioA = self.ti.getHora()
        inicioB = x.ti.getHora()
        finA = self.tf.getHora()
        finB = x.tf.getHora()
        
        puntoA = max(inicioA, inicioB)
        puntoB = min(finA,finB)

        if puntoB*60.0 - puntoA*60.0 > margen and self.dia == x.dia:
            return True
        return False

class Seccion:
    #Seccion: int str *vargs(Bloque) -> Seccion
    def __init__(self, num, profesor, *clases):
        if len(clases) == 0: #raise SyntaxError("Pass at least one class")
            pass
        self.numero = num
        self.profe = profesor
        self.numbloques = len(clases)
        self.bloques = list(clases)

    #getClases: None -> list
    def getClases(self):
        L = []
        for clase in self.clases:
            L.append(clase.getBloque())
        return L

    #addBloque: Bloque -> None
    def addBloque(self,x):
        self.bloques.append(x)

class Ramo:
    #Ramo: str *vargs(Ramo) -> Ramo
    def __init__(self, nombre, *secciones):
        self.nombre = nombre
        self.secciones = list(secciones)

    #getRamo: None -> list(str)
    def getProfesSec(self):
        nombres = []
        for seccion in secciones:
            nombres.append(seccion.profe)
        return nombres
        

#####################################
#####################################

### CVV ###
bloque01 = Bloque("cat", "lu", Hora("10:15"), Hora("11:45"))
bloque02 = Bloque("cat", "vi", Hora("10:15"), Hora("11:45"))
bloque03 = Bloque("aux", "ma", Hora("16:00"), Hora("18:00"))

bloque04 = Bloque("cat", "ma", Hora("16:15"), Hora("17:45"))
bloque05 = Bloque("aux", "vi", Hora("10:00"), Hora("12:00"))

bloque06 = Bloque("cat", "lu", Hora("12:00"), Hora("13:30"))
bloque07 = Bloque("cat", "vi", Hora("12:00"), Hora("13:30"))

bloque08 = Bloque("cat", "ma", Hora("12:00"), Hora("13:30"))
bloque09 = Bloque("cat", "ju", Hora("12:00"), Hora("13:30"))

s1_cvv = Seccion(1,"Rafael Correa", bloque01, bloque02, bloque03)
s2_cvv = Seccion(2,"Manuel del Pino", bloque01, bloque04, bloque05)
s3_cvv = Seccion(3,"Juan Davila", bloque06, bloque07, bloque03)
s4_cvv = Seccion(4,"Aris Daniilidis", bloque06, bloque07, bloque03)
s5_cvv = Seccion(5,"Marcelo Leseigneur", bloque08, bloque09, bloque03)
s6_cvv = Seccion(6, "Alexander Frank", bloque08, bloque09, bloque03)

cvv = Ramo("CVV", s1_cvv, s2_cvv, s3_cvv, s4_cvv, s5_cvv, s6_cvv)

### CDI ###
bloque10 = Bloque("aux", "mi", Hora("14:00"), Hora("16:00"))

s1_cdi = Seccion(1,"Natacha Astromujoff", bloque01, bloque02, bloque10)
s2_cdi = Seccion(2,"Raul Uribe", bloque01, bloque02, bloque10)
s3_cdi = Seccion(3,"Jaime Ortega", bloque01, bloque02, bloque10)

cdi = Ramo("CDI", s1_cdi, s2_cdi, s3_cdi)

### EDO ###
bloque11 = Bloque("cat", "ma", Hora("10:15"), Hora("11:45"))
bloque12 = Bloque("cat", "ju", Hora("10:15"), Hora("11:45"))
bloque13 = Bloque("aux", "vi", Hora("16:00"), Hora("18:00"))

bloque14 = Bloque("cat", "vi", Hora("16:15"), Hora("17:45"))

s1_edo = Seccion(1,"Salome Martinez", bloque06, bloque07, bloque13)
s2_edo = Seccion(2,"Raul Manasevich", bloque06, bloque07, bloque13)
s3_edo = Seccion(3,"Cristobal Bertoglio", bloque11, bloque12, bloque13)
s4_edo = Seccion(4,"Gino Montecinos", bloque11, bloque12, bloque13)
s5_edo = Seccion(5,"Hector Olivero", bloque01, bloque14, bloque05)
s6_edo = Seccion(6,"Cristobal Quin!inao", bloque01, bloque02, bloque13)

edo = Ramo("EDO", s1_edo, s2_edo, s3_edo, s4_edo, s5_edo, s6_edo)

### Lineal ###
bloque15 = Bloque("aux", "mi", Hora("16:00"), Hora("18:00"))
bloque16 = Bloque("aux", "mi", Hora("10:00"), Hora("12:00"))

s1_lineal = Seccion(1,"Alejandro Maass", bloque06, bloque07, bloque15)
s2_lineal = Seccion(2,"Natacha Astromujoff", bloque06, bloque07, bloque16)
s3_lineal = Seccion(3,"Mauricio Telias", bloque06, bloque07, bloque15)

lineal = Ramo("Lineal", s1_lineal, s2_lineal, s3_lineal)

### Mecanica ###
bloque17 = Bloque("aux", "lu", Hora("16:00"), Hora("18:00"))
bloque18 = Bloque("aux", "vi", Hora("14:00"), Hora("16:00"))

s1_mec = Seccion(1,"Francisco Brieva", bloque11, bloque12, bloque17, bloque18)
s2_mec = Seccion(2,"Nestor Sepulveda", bloque11, bloque12, bloque17, bloque18)
s3_mec = Seccion(3,"Hugo Arellano", bloque01, bloque02, bloque17, bloque18)
s4_mec = Seccion(4,"Ricardo Mun!oz", bloque01, bloque02, bloque17, bloque18)
s5_mec = Seccion(5,"Aliro Cordero", bloque08, bloque09, bloque17, bloque18)
s6_mec = Seccion(6,"Claudio Romero", bloque08, bloque09, bloque17, bloque18)

mecanica = Ramo("Mecanica", s1_mec, s2_mec, s3_mec, s4_mec, s5_mec, s6_mec)

### Sistemas ###
bloque19 = Bloque("cat", "lu", Hora("16:15"), Hora("19:30"))
bloque20 = Bloque("lab", "ma", Hora("10:15"), Hora("13:30"))
bloque21 = Bloque("lab", "ju", Hora("10:15"), Hora("13:30"))
bloque22 = Bloque("lab", "ju", Hora("14:30"), Hora("17:45"))

s1_sis = Seccion(1,"Maria Cordero", bloque19, bloque20)
s2_sis = Seccion(2,"Mario Riquelme", bloque19, bloque21)
s3_sis = Seccion(3,"Victor Fuenzalida", bloque19, bloque22)

sistemas = Ramo("Sistemas", s1_sis, s2_sis, s3_sis)

### Economia ###
bloque23 = Bloque("cat", "ma", Hora("08:30"), Hora("10:00"))
bloque24 = Bloque("cat", "ju", Hora("08:30"), Hora("10:00"))
bloque25 = Bloque("aux", "lu", Hora("14:30"), Hora("16:00"))
bloque26 = Bloque("cat", "mi", Hora("08:30"), Hora("10:00"))
bloque27 = Bloque("cat", "vi", Hora("08:30"), Hora("10:00"))
bloque28 = Bloque("aux", "ma", Hora("14:30"), Hora("16:00"))

s1_econo = Seccion(1,"NN", bloque23, bloque24, bloque25)
s2_econo = Seccion(2,"Alexandre Janiak", bloque23, bloque24, bloque25)
s3_econo = Seccion(3,"Raphael Bergoeing", bloque23, bloque24, bloque25)
s4_econo = Seccion(4,"A.Mizala/ A.Canales", bloque23, bloque24, bloque25)
s5_econo = Seccion(5,"Leonardo Basso", bloque23, bloque24, bloque25)
s6_econo = Seccion(6,"NN", bloque26, bloque27, bloque28)

economia = Ramo("Economia", s1_econo, s2_econo, s3_econo, s4_econo, s5_econo, s6_econo)

### Progra(?) ###
bloque29 = Bloque("cat", "lu", Hora("08:30"), Hora("10:00"))
bloque30 = Bloque("cat", "vi", Hora("08:30"), Hora("10:00"))
bloque31 = Bloque("aux", "ju", Hora("18:00"), Hora("20:00"))

s1_progra = Seccion(1,"Juan Alvarez", bloque29, bloque30, bloque31)

progra = Ramo("Programacion", s1_progra)

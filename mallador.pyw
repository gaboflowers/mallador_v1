from horarios import *
from random import randint
from Tkinter import *
from os import name as os_name

def update(*args):
    cal = varCalculo.get()
    dim = varDim.get()
    if cal == "cdi" or dim == "lineal":
        rMec.pack_forget()
        rSis.select()
    else: rMec.pack(anchor=W)
    if mosPressed: dibujarMalla()

def upDis(*args):
    vdim = vDims.get()
    vfis = vFis.get()
    if vdim:
        rCVV.config(state=NORMAL)
        rCDI.config(state=NORMAL)
        rEDO.config(state=NORMAL)
        rLin.config(state=NORMAL)
        varCalculo.set("cvv")
        varDim.set("edo")
    else:
        rCVV.config(state=DISABLED)
        rCDI.config(state=DISABLED)
        rEDO.config(state=DISABLED)
        rLin.config(state=DISABLED)
        varCalculo.set("none")
        varDim.set("none")
    if vfis:
        rMec.config(state=NORMAL)
        rSis.config(state=NORMAL)
        varFis.set("mec")
    else:
        rMec.config(state=DISABLED)
        rSis.config(state=DISABLED)
        varFis.set("none")
        
def tipoRamo(nombre):
    if nombre in ["CVV","CDI"]: return "cal"
    elif nombre in ["EDO","Lineal"]: return "dim"
    elif nombre in ["Mecanica","Sistemas"]: return "fis"
    elif nombre == "Economia": return "eco"
    elif nombre == "Programacion": return "pro"
    else: return "none"
    
def colorBloque(tipo,nombre):
    ramo = tipoRamo(nombre)
    if ramo == "cal":
        if tipo == "cat": return "#DC0000"
        if tipo == "aux": return "#FF0000"
        return "#FF9090"
    elif ramo == "dim":
        if tipo == "cat": return "#0000DC"
        elif tipo == "aux": return "#0000FF"
        return "#9090FF"
    elif ramo == "fis":
        if tipo == "cat": return "#DCDC00"
        if tipo == "aux": return "#FFFF00"
        return "#FFFF90"
    elif ramo == "eco":
        if tipo == "cat": return "#E8A400"
        if tipo == "aux": return "#FFB400"
        return "#FFD775"
    elif ramo == "pro":
        if tipo == "cat": return "#00DCDC"
        if tipo == "aux": return "#00FFFF"
        return "#D3F5F5"
    else:
        mapa = map(lambda x: x.nombre, ramosExtra)
        if nombre in mapa:
            r = mapa.index(nombre) % 5
        else:
            r = randint(0,4)
        if r == 0:
            if tipo == "cat": return "#00DC00"
            if tipo == "aux": return "#00FF00"
            return "#F590F5"
        if r == 1:
            if tipo == "cat": return "#B39B00"
            if tipo == "aux": return "#FFDD00"
            return "#FFED7A"
        if r == 2:
            if tipo == "cat": return "#A88FBF"
            if tipo == "aux": return "#C997F7"
            return "#DFC3FA"
        if r == 3:
            if tipo == "cat": return "#79B500"
            if tipo == "aux": return "#AAFF00"
            return "#DAFF8F"
        if tipo == "cat": return "#DC00DC"
        if tipo == "aux": return "#FF00FF"
        return "#FF8FFF"   
        
    
#dibujarBloque: Canvas Bloque str -> none
def dibujarBloque(canvas,bloque,nombre):
    color = colorBloque(bloque.tipo, nombre)
    dias = ["lu","ma","mi","ju","vi","sa"]
    w = 600
    offset = 0
    t = tipoRamo(nombre)
    if t == "cal": offset = 20
    elif t == "edo": offset = 10
    elif t == "fis": offset = 7
    equis1 = dias.index(bloque.dia)*w/5+offset
    equis2 = equis1+w/5-30
    ygriega1 = minsToCoord(bloque.ti.getMinutos())
    ygriega2 = minsToCoord(bloque.tf.getMinutos())
    dashTuple = None
    if bloque.tipo == "aux":
        dashTuple = (2,2)
    elif bloque.tipo == "lab":
        dashTuple = (3,2,1)
    canvas.create_rectangle(equis1,ygriega1,equis2,ygriega2,dash=dashTuple,fill=color)
    texto = nombre+"\n("+bloque.tipo+")"
    canvas.create_text(equis1+w/10-offset, (ygriega1+ygriega2)/2 ,text = texto)
    
def dibujarRamosPersonales():
    global ramosExtra, can
    if len(ramosExtra) != 0:
        for i in range(len(ramosExtra)):
            seccion = ramosExtra[i].secciones[0]
            for bloque in seccion.bloques:
                dibujarBloque(can,bloque,ramosExtra[i].nombre)

#dibujarMalla: None -> None
def dibujarMalla(*args):
    global ramos, varsRamos, can
    can.delete("all")
    h,w=304,600
    
    for i in range(w/5,w+10,w/5):
        can.create_line(i,0,i,h)
    dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
    for i in range(5):
        can.create_text(w/10+i*w/5,10,text=dias[i])
    can.create_line(0,20,664,20)

    can.create_line(0,minsToCoord(90),664,minsToCoord(90), fill="blue") #8:30 + 90mins (10:00)
    can.create_line(0,minsToCoord(210),664,minsToCoord(210),fill="blue") #12:00
    can.create_line(0,minsToCoord(300),664,minsToCoord(300), fill="red") #13:30 (almuerzo)
    can.create_line(0,minsToCoord(360),664,minsToCoord(360), fill="red") #14:30
    can.create_line(0,minsToCoord(450),664,minsToCoord(450), fill="blue") #16:00
    can.create_line(0,minsToCoord(570),664,minsToCoord(570), fill="blue") #18:00
    can.create_line(0,minsToCoord(690),664,minsToCoord(690), fill="blue") #20:00

    can.create_text(615,13,text="8:30")
    can.create_text(615,minsToCoord(70),text="10:00")
    can.create_text(615,minsToCoord(190),text="12:00")
    can.create_text(615,minsToCoord(280),text="13:30")
    can.create_text(615,minsToCoord(343),text="14:30")
    can.create_text(615,minsToCoord(430),text="16:00")
    can.create_text(615,minsToCoord(550),text="18:00")
    can.create_text(615,minsToCoord(670),text="20:00")             

    dibujarRamosPersonales()
    
    for i in range(len(ramos)):
        seccion = ramos[i].secciones[ varsRamos[i].get() - 1]
        for bloque in seccion.bloques:
            dibujarBloque(can, bloque, ramos[i].nombre)

def seccionesSelect(show):
    global frameSec, framesRamos, varsRamos, ramos
    if show:
        frameSec = Frame(frameCanOut)
        frameSec.pack(anchor=W)
        cal = varCalculo.get()
        dim = varDim.get()
        fis = varFis.get()
        eco = varEco.get()
        pro = varPro.get()
        if cal == "cvv": cal = cvv
        elif cal == "cdi": cal = cdi
        else: cal = None
        
        if dim == "edo": dim = edo
        elif dim == "lineal": dim = lineal
        else: dim = None
        
        if fis == "mec": fis = mecanica
        elif fis == "sis": fis = sistemas
        else: fis = None
        ramos = [cal, dim, fis]
        if eco: ramos.append(economia)
        if pro: ramos.append(progra)
        framesRamos = []
        varsRamos = []
        x = []
        for ramo in ramos:
            if ramo != None: x.append(ramo)
        ramos = x
        for ramo in ramos:
            varAux = IntVar()
            frameAux = Frame(frameSec)
            frameAux.pack(anchor=W)
            framesRamos.append(frameAux)
            varsRamos.append(varAux)
            Label(frameAux, text=ramo.nombre).pack(anchor=W)
            radios = []
            for seccion in ramo.secciones:
                texto = str(seccion.numero)+" - "+seccion.profe
                r=Radiobutton(frameAux, text=texto, variable=varAux, value=seccion.numero, compound=BOTTOM)
                r.pack(side=LEFT)
                radios.append(r)
            radios[0].select()
        dibujarMalla()
        for var in varsRamos:
            var.trace("w",dibujarMalla)            
    else:
        frameSec.destroy()
        framesRamos = []
        varsRamos = []
        
            
    
def mostrar(*args):
    global mosPressed, can, frameCanIn
    if not mosPressed:
        #frameCanOut.pack(side=RIGHT)
        frameCanIn.pack()
        can = Canvas(frameCanIn, width=660, height=300, bg="white")
        can.pack()
        mosPressed = True
        mos.config(text="Ocultar")
        seccionesSelect(True)
        labelMos.pack()
        ins.pack()
    else:
        can.destroy()
        frameCanIn.pack_forget()
        mosPressed = False
        mos.config(text="Mostrar")
        seccionesSelect(False)

def minsToCoord(mins):
    return mins*28/75+20

#########################################

def nuevaVentana(v2):
    global varMenuBloques, menuBloques, frames, frame2
    frame1 = Frame(v2)
    frame1.pack(anchor=W)

    Label(frame1,text="\nSeleccione numero de bloques\n(Clases de catedra+auxiliares+labs)",justify=LEFT).pack(side=LEFT)
    varMenuBloques = StringVar()
    varMenuBloques.set("")
    varMenuBloques.trace("w",selectedMenu)
    menuBloques = OptionMenu(frame1, varMenuBloques,"1","2","3","4","5","6")
    menuBloques.pack(side=LEFT)

    frame2 = Frame(v2)
    frame2.pack(anchor=W)
    
def insertar(*args):
    global insPressed, v2
    if not insPressed:
        ins.config(text="Cancelar insercion")
        v2 = Toplevel()
        v2.wm_title("Ramo personalizado")
        nuevaVentana(v2)
        insPressed = True
    else:
        ins.config(text="Insertar ramo?")
        v2.destroy()
        insPressed = False
    

def crearRamo(*args):
    global ramosExtra, v2
    
    todoEnOrden = True
    for i in range(len(menuVars)):
        if menuVars[i].get() == "":
            horas[i][0].delete(0,END)
            horas[i][0].insert(0,"<------")
            horas[i][1].delete(0,END)
            horas[i][1].insert(0,"Seleccione")
            todoEnOrden = False
    for varDia in diasVars:
        if varDia.get() == "":
            entryNombre.delete(0,END)
            entryNombre.insert(0,"SELECCIONE DIAS")
            todoEnOrden = False
    for i in range(len(horas)):
        tupla = horas[i]
        a,b = tupla
        a = a.get()
        b = b.get()
        if len(a) != 5 or len(b) != 5 or ":" not in a or ":" not in b:
            entryNombre.delete(0,END)
            entryNombre.insert(0,"Hora ej: 08:45")
            todoEnOrden = False

    if todoEnOrden:
        seccionNva = Seccion(0,"NN")
        print "largo de menuVars:",len(menuVars)
        for i in range(len(menuVars)):
            tipo = menuVars[i].get()
            tipo = tipo[:3].lower()

            dia = diasVars[i].get()
            dia = dia[:2].lower()

            horaInicio,horaFin = horas[i]
            horaInicio = horaInicio.get()
            horaFin = horaFin.get()
            horaInicio = Hora(horaInicio)
            horaFin = Hora(horaFin)
            bloque = Bloque(tipo, dia, horaInicio, horaFin)
            seccionNva.addBloque(bloque)
            
        ramoNvo = Ramo(entryNombre.get(),seccionNva)
        ramosExtra.append(ramoNvo)
        dibujarMalla()

        insPressed=False
        ins.config(text="Insertar ramo?")
        v2.destroy()
        
        

    
    
def selectedMenu(*args):
    opcion = varMenuBloques.get()
    global frames,agregar,diasVars,entryNombre,frame2,menuVars,horas
    if opcion == "":
        pass
    else:
        #limpiando utlima instancia de la ventana
        frame2.destroy()
        frame2 = Frame(v2)
        frame2.pack(anchor=W)
        for frame in frames:
            frame.destroy()
        frames = []
        menuVars = []
        diasVars = []
        horas = []

        #creando nueva cantidad de entradas
        entryNombre = Entry(frame2)
        entryNombre.pack()
        entryNombre.insert(0,"Nombre ramo")
        opcion = int(opcion)
        for i in range(opcion):
            frameAux = Frame(frame2)
            varTipo = StringVar()
            varTipo.set("")
            menuAux = OptionMenu(frameAux, varTipo, "Catedra", "Auxiliar", "Laboratorio", "Control")
            menuAux.pack(side=LEFT)

            varDias = StringVar()
            varDias.set("")
            
            menuDia = OptionMenu(frameAux, varDias, "lunes", "martes", "miercoles", "jueves", "viernes")
            menuDia.pack(side=LEFT)
            Label(frameAux, text="de").pack(side=LEFT)
            horaIn = Entry(frameAux,width=8)
            horaIn.pack(side=LEFT)
            horaIn.insert(0,"HH:MM")
            Label(frameAux, text="hasta").pack(side=LEFT)
            horaFin = Entry(frameAux,width=10)
            horaFin.pack(side=LEFT)
            horaFin.insert(0,"HH:MM")
                                 
            frames.append(frameAux)
            menuVars.append(varTipo)
            diasVars.append(varDias)
            horas.append((horaIn,horaFin))
        for frame in frames:
            frame.pack()

        agregar = Button(frame2, text="Agregar Ramo", command=crearRamo)
        agregar.pack()

__author__ = "Gabriel Flores"
__license__ = "creativecommons.org/licenses/by-nc/2.5/deed.es_ES"
__version__ = "1.0"

#############################          
            

ventana = Tk()
ventana.wm_title("Mallador")
if os_name == 'nt':
	ventana.iconbitmap(default='favicon2.ico')

varCalculo = StringVar()

varFis = StringVar()
frameFis = Frame(ventana)

varDim = StringVar()

varEco = BooleanVar()
varEco.set(False)

varPro = BooleanVar()
varPro.set(False)

#NVO
vDims = BooleanVar()
vDims.set(False)
vFis = BooleanVar()
vFis.set(False)

#Label(text="DIMs :").pack(anchor=W)
cDim = Checkbutton(ventana, text="DIMs:", variable=vDims, onvalue=True, offvalue=False)
cDim.pack(anchor=W)
cDim.select()


frameCanOut = Frame(ventana)
frameCanOut.pack(side=RIGHT,expand=YES,fill=BOTH)
frameCanIn = Frame(frameCanOut)

rCVV=Radiobutton(ventana, text="Calculo en Varias Variables", variable=varCalculo, value="cvv")
rCVV.pack(anchor=W)
rCVV.select()
rCDI=Radiobutton(ventana, text="Calculo Diferencial e Integral", variable=varCalculo, value="cdi")
rCDI.pack(anchor=W)
rEDO=Radiobutton(ventana, text="Ecuaciones Diferenciales Ordinarias", variable=varDim, value="edo")
rEDO.pack(anchor=W)
rEDO.select()
rLin=Radiobutton(ventana, text="Algebra Lineal",variable=varDim, value="lineal")
rLin.pack(anchor=W)

#Label(text="Fisica:").pack(anchor=W)
cFis = Checkbutton(ventana,text="Fisica:", variable = vFis, onvalue=True, offvalue=False)
cFis.pack(anchor=W)
cFis.select()
vDims.trace("w",upDis)
vFis.trace("w",upDis)

frameFis.pack(anchor=W)
rSis=Radiobutton(frameFis, text="Sistemas Newtonianos", variable=varFis, value="sis")
rSis.pack(anchor=W)
rMec=Radiobutton(frameFis, text="Mecanica", variable=varFis, value="mec")
rMec.pack(anchor=W)
rMec.select()

Label(text="Otros:").pack(anchor=W)
cEco = Checkbutton(ventana, text="Economia", variable=varEco, onvalue=True, offvalue=False)
cEco.pack(anchor=W)
cEco.select()
Checkbutton(ventana, text="Programacion", variable=varPro, onvalue=True, offvalue=False).pack(anchor=W)

Label(text="No estoy tan loco como para poner\ntodos los horarios de Taller de Proyecto\n").pack()

varCalculo.trace("w",update)
varDim.trace("w",update)
varFis.trace("w",update)

mosPressed = False
mos = Button(ventana, text="Mostrar", command=mostrar)
labelMos = Label(ventana,text="Ocultar y volver a mostrar para\nrefrescar la ventana al cambiar ramos")
mos.pack()

insPressed = False
ins = Button(text="Insertar ramo personalizado?", command=insertar)


frames = []
menuVars = []
menus = []
horas = []
diasVars = []

ramosExtra = []



ventana.mainloop()



# mallador_v1
Genera visualizaciones horarios posibles semestre 2016-1 fcfm

Instrucciones:

El programa principal es "Mallador.pyw"; si tiene Python (2.x) instalado, al hacer doble clic en el archivo, debería
crearse la ventana de Tkinter.
En "horarios.py" se encuentra la información de las secciones de cada ramo, según aparece en U-campus.

-Seleccionar los cursos Primavera 2016 en la ventana inicial
(Mecánica desaparece si no se puede tomar)

-Si desmarca un casillero, los ramos que le pertenecen no se graficarán

-Clic en "Mostrar", ahí se puede probar cómo se ven las distintas secciones.

-Si desea cambiar un ramo del menú, haga el cambio, y haga clic en "Ocultar" y de nuevo en "Mostrar".

-Para agregar un ramo que no está en el menú, haga clic en "Insertar ramo?"

-En la ventana de Ramo personalizado, puede agregar una cantidad indefinida de ramos personalizados a su horario.
Para esto, ingrese la cantidad de bloques que tiene el ramo (entre cátedras, laboratorios y auxiliares).

Una vez seleccionada una cantidad N de bloques (N=1..6), se crearan N filas de entrada, donde deberá ingresar Tipo de
bloque (Cátedra, Auxiliar...), Día de la semana del bloque, Hora de inicio del bloque (HH:MM, siempre con 2
digitos para la hora y 2 para los minutos, separados con ":"). Al hacer clic en "Agregar ramo", éste aparecerá
en el recuadro de la derecha, independiente de las secciones predefinidas que usted seleccione.

Por el momento, no existe opción para eliminar ramos personalizados, por lo que deberá cerrar y abrir el programa
para eliminar bloques insertados del horario.

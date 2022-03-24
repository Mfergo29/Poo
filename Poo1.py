Ficcion={'Frank Herbert':['Dune', 'El Mesías de Dune', 'Hijos de Dune'],
 'Arthur Clarke': ['2001: Una odisea espacial', '2010: Odisea dos','2061: Odisea tres'],
  'Frederik Pohl': ['Pórtico','Tras el incierto horizonte','El encuentro']}

Romance={'Juliana Gray':['Una dama nunca miente','Un caballero siempre es discreto','Un duque nunca se rinde'],
'Jamie Mcguire':['Maravilloso desastre','Inevitable desastre','Un desastre es para siempre'],
'Sylvia Day':['No te escondo nada','Reflejada en ti','Atada a ti']}

Aventura={'JR. Tolkien':['El señor de los anillos 1','El señor de los anillos 2','El señor de los anillos 3'],
'JK Rowling':['Harry Potter 1','Harry Potter 2','Harry Potter 3'],
'Robert Jordan':['La rueda del tiempo 1','La rueda del tiempo 2','La rueda del tiempo 3']}

biblioteca=[Ficcion,Romance,Aventura]

arrendado=[]
devueltos=[]
nombres=[]
fechas=[]
fechasd=[]
atraso=[]
print('Bienvenido a la interfaz de la Biblioteca P.O.O. Debido a convenios con ciertas editoriales nuestra biblioteca trabaja solo con los autores del catalogo. \n Recuerde tambien que el uso de mayusculas para modos de trabajo es obligatorio \n Muchas Gracias')  

while True:
  print()
  main=int(input('Que desea hacer: \n 1. Ver inventario \n 2. Manejar Arriendos \n 3. Categorizar Inventario \n 4. Modificar Catalogo \n 5. Terminar sesion \n'))

  if main==1:
    print(Ficcion, Romance, Aventura)
    print()
    print('Actualmente no se encuentran disponibles:', arrendado) 
    print()

  if main==2:
    print()
    main2=int(input(' 1. Arrendar Libro: \n 2. Ver Disponibilidad \n 3. Manejar Arriendos \n'))

    if main2==1:
      print()
      nombre=input('Escriba su nombre: ')
      nombres.append(nombre)
      libro=input('Escriba el nombre del libro que desea arrendar: ')
      a=0
      for i in biblioteca:
        for j in i:
          for k in range(len(i)):
            if libro==i[j][k]:
              a=1
              arrendado.append(libro)
            else:
              continue
      if a==0:
        print('El libro no existe en nuestra base de datos')       
        break 
      fi=int(input('Ingrese fecha de hoy (solo numero de dia): '))
      fechas.append(fi)
      print('Tienes 7 dias para devolverlo')

    elif main2==2:
      print()
      dl=input('Escriba el nombre del libro que desea checkear: ')
      if dl in arrendado:
        print('No esta disponible')
      else:
        print('Esta disponible')

    elif main2==3:
      main2_3=int(input(' 1. Devolver libro  \n 2. Informacion de arriendos \n'))

      if main2_3==1:
        dlibro=input('Ingrese nombre del libro que desea devolver: ')
        if dlibro in arrendado:
          fdev=int(input('Ingrese la fecha de devolucion: '))
          for l in range(len(arrendado)):
            if dlibro==arrendado[l]:
              dias=fechas[l]-fdev
              if abs(dias)<=7:
                print('Entregado a tiempo, Muchas gracias')
                atraso.append('a tiempo')
              else:
                print('Entregado fuera de plazo')
                atraso.append('atrasado')
          fechas.pop(l)
          arrendado.pop(l)
          nombres.pop(l)
          devueltos.append(dlibro)
          fechasd.append(fdev)
        else:
          print('El libro', dlibro , 'No se encuentra arrendado')
      
      elif main2_3==2:
        ilibro=input('Ingrese el nombre del libro arrendado: ')
        if ilibro in arrendado:
          for i in range(len(arrendado)):
            if ilibro==arrendado[i]:
              if fechas[i]+7>=31:
                fdevolver=fechas[i]+7-31
              else:
                fdevolver=fechas[i]+7
              print('El libro ', arrendado[i], 'fue arrendado por ', nombres[i], 'y debe devolverlo el dia ', fdevolver)
        elif ilibro in devueltos:
          for i in range(len(devueltos)):
            if ilibro==devueltos[i]:
              print('El libro ',ilibro, 'fue devuelto el dia ', fechasd[i], atraso[i])

  if main==3:
    print()
    main3=int(input('Como desea buscar: \n 1. Por Generos \n 2. Por Autor \n'))
    if main3==1:
      gen=input('Ingrese el genero que desea buscar: ')
      if gen=='Ficcion':
        print(Ficcion.values())
      elif gen=='Romance':
        print(Romance.values())
      elif gen=='Aventura':
        print(Aventura.values())
      else:
        print('Esta categoria no esta disponible')
  
    if main3==2:
      aut=input('Ingrese el nombre del autor que desea buscar: ')
      for a in biblioteca:
        for j in a:
          if aut in j:
            if j==aut:
              for k in range(len(a)):
                print(a[j][k])   ####FALTA QUE NO SE ENCUENTRE####
  
  if main==4:
    main4=int(input('Que deseas hacer: \n 1. Añadir Libro \n 2. Quitar Libro \n'))

    if main4==1:
        aut=input('Ingrese nombre del autor: ')
        libro=input('Ingrese nombre del libro: ')
        gen=input('Ingrese el genero del libro (Ficcion, Romance, Aventura): ')
        if gen !='Ficcion' and gen!='Romance' and gen!= 'Aventura':
            print('El genero que ha elegido no se encuentra entre las opciones')
        else:
            
            if gen=='Ficcion':
                for i in biblioteca[0]:
                    if i==aut:
                        biblioteca[0][aut].append(libro)
                    
            elif gen=='Romance':
                for i in biblioteca[1]:
                    if i==aut:
                        biblioteca[1][aut].append(libro)
                    
            elif gen=='Aventura':
                for i in biblioteca[2]:
                    if i==aut:
                        biblioteca[2][aut].append(libro)
            else:
                print('El autor que ha ingresado no pertenece al genero elegido')
        '''
        for i in biblioteca:
            for j in i:
                if aut i:
                    i[aut].append(libro)
                else:
                    gen=input('Ingrese genero del libro: ')
                    for i in biblioteca:
                        if i==gen:
                            dic={aut: libro}
                            print(dic)
                            i.update(dic)
        '''


    if main4==2:
      libro=input('Escriba el nombre del libro que deseas quitar del catalogo: ')
      for i in biblioteca:
        for j in i:
          if libro in i[j]:
              i[j].pop(i[j].index(libro))
              


  if main==5:
    break







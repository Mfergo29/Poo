ficcion={'Frank Herbert':['Dune', 'El Mesías de Dune', 'Hijos de Dune'],
 'Arthur Clarke': ['2001: Una odisea espacial', '2010: Odisea dos','2061: Odisea tres'],
  'Frederik Pohl': ['Pórtico','Tras el incierto horizonte','El encuentro']}

romance={'Juliana Gray':['Una dama nunca miente','Un caballerosiempre es discreto','Un duque nunca se rinde'],
'Jamie Mcguire':['Maravilloso desastre','Inevitable desastre','Un desastre es para siempre'],
'Sylvia Day':['No te escondo nada','Reflejada en ti','Atada a ti']}

aventura={'JR. Tolkien':['El señor de los anillos 1','El señor de los anillos 2','El señor de los anillos 3'],
'JK Rowling':['Harry Potter 1','Harry Potter 2','Harry Potter 3'],
'Robert Jordan':['La rueda del tiempo 1','La rueda del tiempo 2','La rueda del tiempo 3']}

arrendado=[]
devueltos=[]
nombres=[]
fechas=[]
fechasd=[]

while True:
  print()
  main=int(input('Que desea hacer: \n 1. Ver inventario \n 2. Manejar Arriendos \n 3. Categorizar Inventario \n 4. Modificar Catalogo \n 5. Terminar sesion \n'))

  if main==1:
    print(ficcion, romance, aventura)
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
      gen=input('Escriba el genero de libro que desea arrendar: ')
      aut=input('Escriba el autor de libro que desea arrendar: ')
      libro=input('Escriba el nombre del libro que desea arrendar: ')
      if libro in gen[aut]:
        print('Aqui tiene su libro muchas gracias')
        arrendado.append(libro)
      else:
        print('El libro no se encuentra en nuestra base de datos')
        break
      fi=int(input('Ingrese fecha de hoy (solo numero de dia): '))
      fechas.append(fi)
      fechasd.append(fi+7)
      print('Tienes 7 dias para devolverlo')

    elif main2==2:
      print()
      dl=input('Escriba el nombre del libro que desea checkear: ')
      if dl in arrendado:
        print('No esta disponible')
      else:
        print('Esta disponible')

    elif main2==3:
      main2_3=int(input(' 1. Devolver libro \n 2. Informacion de arriendos'))

      if main2_3==1:
        dlibro=input('Ingrese nombre del libro que desea devolver: ')
        if dlibro in arrendado:
          fdev=input('Ingrese la fecha de devolucion: ')
          for l in range(len(arrendado)):
            if dlibro == arrendado[l]:
              dias=fechasd[l]-fdev
              if abs(dias)<=7:
                print('Entregado a tiempo, Muchas gracias')
              else:
                print('Entregado fuera de plazo')
        else:
          print('El libro', dlibro , 'No se encuentra arrendado')





  if main==5:
    break

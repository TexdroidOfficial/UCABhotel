import pickle
import os

if os.path.exists("hotelData.bin"):
    if os.path.getsize("hotelData.bin") > 0:
        with open("hotelData.bin", 'rb') as file:
            matriz_habitaciones = pickle.load(file)
    else:
        print("El archivo binario esta vacio. Por favor, ejecute matriz.py nuevamente para generar el archivo binario")
        exit()
else:
    print("El archivo binario no ha sido encontrado. Por favor, asegurese de que el archivo binario este en el directorio")
    exit()
    
print('Este programa fue elaborado por: Stephanie "Texdroid" Vielma, Luis Mora, Diego "Darv" Rivas y Luciano Di Battista')
print('\nLider del proyecto: Stephanie "Texdroid" Vielma\n')
    
def statusOrder(status):
    if status == "free":
        return 0
    if status == "saved":
        return 1
    elif status == "locked":
        return 2
    else:
        return -1
    
def roomOrder(category):
    if category == "mono":
        return 0
    if category == "duo":
        return 1
    if category == "deluxe":
        return 2
    if category == "royal":
        return 3
    else:
        return -1
    
def reformatDate(date):
    if date and date != "":
        return f"{date[6:8]}/{date[4:6]}/{date[:4]}"
    return date

def mergesortCategory(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        
        mergesortCategory(left_half)
        mergesortCategory(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            
            left_room_prio = roomOrder(left_half[i][1])
            right_room_prio = roomOrder(right_half[j][1])
            
            if left_room_prio < right_room_prio:
                array[k] = left_half[i]
                i += 1
            elif left_room_prio > right_room_prio:
                array[k] = right_half[j]
                j += 1
            else:
                left_status_prio = statusOrder(left_half[i][2])
                right_status_prio = statusOrder(right_half[j][2])
                
                if left_status_prio < right_status_prio:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
            k += 1
                
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

def mergesortNum(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        
        mergesortNum(left_half)
        mergesortNum(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            
            if left_half[i][0] < right_half[j][0]:
                    array[k] = left_half[i]
                    i += 1
            elif left_half[i][0] > right_half[j][0]:
                array[k] = right_half[j]
                j += 1
            else:    
                left_status_prio = statusOrder(left_half[i][0])
                right_status_prio = statusOrder(right_half[j][0])
                
                if left_status_prio < right_status_prio:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                
            k += 1
                
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

def revisar_disponibilidad(habitaciones):
    
    selection = str(input("\n¿Desea organizar el listado de habitaciones por Numero (N) o por Categoria (C)? ")).upper()
    match selection:
        case "N":
            mergesortNum(matriz_habitaciones)
    
            print("--- Listado de habitaciones ---")
            
            for room in habitaciones:
                room_number = room[0]
                room_category_code = room[1]
                room_status = room[2]
                
                display_category = ""
                if room_category_code == "mono":
                    display_category = "Sencilla"
                elif room_category_code == "duo":
                    display_category = "Doble"
                elif room_category_code == "deluxe":
                    display_category = "Suite"
                elif room_category_code == "royal":
                    display_category = "Presidencial"
                
                display_status = ""    
                if room_status == "free":
                    display_status = "Disponible"
                elif room_status == "saved":
                    display_status = "Reservado"
                elif room_status == "locked":
                    display_status = "Ocupado"
                    
                entry_date_display = reformatDate(room[3]) if len(room) > 3 else ""
                exit_date_display = reformatDate(room[4]) if len(room) > 4 else ""
                
                room_id_display = room[5] if len(room) > 5 else ""
                room_name_display = room[6] if len(room) > 6 else ""
                    
                room_info = f"Numero de la habitacion: {room_number} | Categoria: {display_category} | Estado: {display_status}"
                
                if room_id_display:
                    room_info += f" | Cedula: {room_id_display}"
                if room_name_display:
                    room_info += f" | Nombre: {room_name_display}"
                
                if room_status in ["locked", "saved"] and entry_date_display and exit_date_display:
                    room_info += f" | Fecha de entrada: {entry_date_display} | Fecha de salida:{exit_date_display}"
                
                print(f"{room_info}")
                
        case "C":
            mergesortCategory(matriz_habitaciones)
            
            print("--- Listado de habitaciones ---")

            for room in habitaciones:
                room_number = room[0]
                room_category_code = room[1]
                room_status = room[2]
                
                display_category = ""
                if room_category_code == "mono":
                    display_category = "Sencilla"
                elif room_category_code == "duo":
                    display_category = "Doble"
                elif room_category_code == "deluxe":
                    display_category = "Suite"
                elif room_category_code == "royal":
                    display_category = "Presidencial"
                
                display_status = ""    
                if room_status == "free":
                    display_status = "Disponible"
                elif room_status == "saved":
                    display_status = "Reservado"
                elif room_status == "locked":
                    display_status = "Ocupado"
                    
                entry_date_display = reformatDate(room[3]) if len(room) > 3 else ""
                exit_date_display = reformatDate(room[4]) if len(room) > 4 else ""
                
                room_id_display = room[5] if len(room) > 5 else ""
                room_name_display = room[6] if len(room) > 6 else ""
                    
                room_info = f"Numero de la habitacion: {room_number} | Categoria: {display_category} | Estado: {display_status}"
                
                if room_id_display:
                    room_info += f" | Cedula: {room_id_display}"
                if room_name_display:
                    room_info += f" | Nombre: {room_name_display}"
                
                if room_status in ["locked", "saved"] and entry_date_display and exit_date_display:
                    room_info += f" | Fecha de entrada: {entry_date_display} | Fecha de salida:{exit_date_display}"
                
                print(f"{room_info}")
                
        case _:
            print(f"\nError: {selection} no es una opcion valida, intente nuevamente.")
            
def buscar_habitacion(habitaciones):
    criterio = str(input("Escriba 1 para buscar por tipo de habitación y 2 para buscar por número: "))
    
    if criterio == "1":
        encontrada = False
        
        valor = input("Ingrese el tipo de habitación que busca: Sencilla, Doble, Suite o Presidencial: ").capitalize()
        print("\n")
        match valor:
            case "Sencilla":
                true_valor = "mono"
            case "Doble":
                true_valor = "duo"
            case "Suite":
                true_valor = "deluxe"
            case "Presidencial":
                true_valor = "royal"
            case _:
                print(f"\n Error: {valor} no es un tipo de habitación valido, intente nuevamente.")
                return
            
        rooms_found = []
        for i in range(len(habitaciones)):
            if habitaciones[i][1].lower() == true_valor:
                room_status = habitaciones[i][2]
                
                display_status = ""    
                if room_status == "free":
                    display_status = "Disponible"
                elif room_status == "saved":
                    display_status = "Reservado"
                elif room_status == "locked":
                    display_status = "Ocupado"
                    
                entry_date_display = reformatDate(habitaciones[i][3]) if len(habitaciones[i]) > 3 else ""
                exit_date_display = reformatDate(habitaciones[i][4]) if len(habitaciones[i]) > 4 else ""
                
                room_id_display = habitaciones[i][5] if len(habitaciones[i]) > 5 else ""
                room_name_display = habitaciones[i][6] if len(habitaciones[i]) > 6 else ""
                
                encontrada = True
                room_list = f"Habitación encontrada! Numero de la habitacion: {habitaciones[i][0]} | Categoria: {valor} | Estado: {display_status}"
                
                if room_id_display:
                    room_list += f" | Cedula: {room_id_display}"
                if room_name_display:
                    room_list += f" | Nombre: {room_name_display}"
                
                if room_status in ["locked", "saved"] and entry_date_display and exit_date_display:
                    room_list += f" | Fecha de entrada: {entry_date_display} | Fecha de salida:{exit_date_display}"
                
                rooms_found.append(room_list)
        
        if rooms_found:
            print("\n".join(rooms_found))
    
    elif criterio == "2":
        encontrada = False
        
        selected_room_input = input("\nIngrese el número de habitación que busca: ")
        if selected_room_input.isdigit():
            valor = int(selected_room_input)
            
            for habitacion in habitaciones:
                if habitacion[0] == valor:
                    encontrada = True
                    room_status = habitacion[2]
                    room_category_code = habitacion[1]
                
                    display_category = ""
                    if room_category_code == "mono":
                        display_category = "Sencilla"
                    elif room_category_code == "duo":
                        display_category = "Doble"
                    elif room_category_code == "deluxe":
                        display_category = "Suite"
                    elif room_category_code == "royal":
                        display_category = "Presidencial"
                    
                    display_status = ""    
                    if room_status == "free":
                        display_status = "Disponible"
                    elif room_status == "saved":
                        display_status = "Reservado"
                    elif room_status == "locked":
                        display_status = "Ocupado"
                    
                    entry_date_display = reformatDate(habitacion[3]) if len(habitacion) > 3 else ""
                    exit_date_display = reformatDate(habitacion[4]) if len(habitacion) > 4 else ""
                    
                    room_id_display = habitacion[5] if len(habitacion) > 5 else ""
                    room_name_display = habitacion[6] if len(habitacion) > 6 else ""
                    
                    room_list = f"Habitación encontrada! Numero de la habitacion: {valor} | Categoria: {display_category} | Estado: {display_status}"
                    
                    if room_id_display:
                        room_list += f" | Cedula: {room_id_display}"
                    if room_name_display:
                        room_list += f" | Nombre: {room_name_display}"
                    
                    if room_status in ["locked", "saved"] and entry_date_display and exit_date_display:
                        room_list += f" | Fecha de entrada: {entry_date_display} | Fecha de salida:{exit_date_display}"
                    
                    print(f"{room_list}")
                    
        
            if not encontrada:
                print(f"\nLa habitacion {valor} no existe.")
                
        else:
            print("\nERROR: El número de habitación no es válido. Por favor, introduzca una habitación válida.")
            
    
    else:
        print(f"\n{criterio} no es una opcion valida. Intente nuevamente.")
            
def checkin(array):
    while True:
        print("\n--- Fecha de entrada ---")
        entry_day = str(input("Introduzca el dia usando 2 digitos: "))
        entry_month = str(input("Introduzca el mes usando 2 digitos: "))
        entry_year = str(input("Introduzca el año (4 digitos): "))
        if (len(entry_day) == 2 and entry_day.isdigit() and 1 <= int(entry_day) <= 31 and
            len(entry_month) == 2 and entry_month.isdigit() and 1 <= int(entry_month) <= 12 and
            len(entry_year) == 4 and entry_year.isdigit()):
            entry_date = entry_year + entry_month + entry_day
            break
        else:
            print("\nERROR: Ha ingresado una fecha invalida. Intente nuevamente.")
    while True:
        print("\n --- Fecha de salida ---")
        exit_day = str(input("Introduzca el dia usando 2 digitos: "))
        exit_month = str(input("Introduzca el mes usando 2 digitos: "))
        exit_year = str(input("Introduzca el año (4 digitos): "))
        if (len(exit_day) == 2 and exit_day.isdigit() and 1 <= int(exit_day) <= 31 and
            len(exit_month) == 2 and exit_month.isdigit() and 1 <= int(exit_month) <= 12 and
            len(exit_year) == 4 and exit_year.isdigit()):
            exit_date = exit_year + exit_month + exit_day
            break
        else:
            print("\nERROR: Ha ingresado una fecha invalida. Intente nuevamente.")
    if entry_date == exit_date:
        print("\nERROR: La fecha de entrada y la fecha de salida son iguales. Intente nuevamente.")
        return
    elif entry_date > exit_date:
        print("\nERROR: La fecha de entrada es posterior a la fecha de salida. Intente nuevamente.")
        return
    
    print("\n --- Datos para el Check-In ---")
    user_first_name = input(str("Introduzca el nombre: "))
    user_last_name = input(str("Introduzca el apellido: "))
    
    valid_letters = ['V', 'E', 'P', 'S', 'J', 'G']
    while True:
        user_ID = input(str("Introduzca su cedula. Ejemplo: V-XXXXXXXXXX: ")).upper()
        if (len(user_ID) > 2 and user_ID[0] in valid_letters and user_ID[1] == '-' and user_ID[2:].isdigit()):
            break
        else:
            print("\nERROR: Ha introducido una cedula invalida. Intente nuevamente.")
    
    found = False
    
    for room in array:
        room_number = room[0]
        room_status = room[2]
        room_category_code = room[1]
        
        display_category = ""
        if room_category_code == "mono":
            display_category = "Sencilla"
        elif room_category_code == "duo":
            display_category = "Doble"
        elif room_category_code == "deluxe":
            display_category = "Suite"
        elif room_category_code == "royal":
            display_category = "Presidencial"
        
        if room_status == "free":
            print(f"Habitación {room_number} - {display_category}")
    
    while True:
        selected_room_input = input("\nSeleccione el número de habitación que desea reservar: ")
        if selected_room_input.isdigit():
            selected_room = int(selected_room_input)
            break
        else:
            print("\nERROR: El número de habitación no es válido. Por favor, introduzca una habitacion valida.")
    
    for room in array:
        if room[0] == selected_room:
            found = True
            if room[2] == "free":
                room[2] = "locked"
                room[3] = entry_date
                room[4] = exit_date
                room[5] = user_ID
                room[6] = f"{user_first_name} {user_last_name}"
                
                with open("hotelData.bin", "wb") as file:
                    pickle.dump(array, file)
                    
                print(f"La habitacion {selected_room} ha sido registrada con éxito.")
                print(f"Los datos del registro son:\n"
                      f"Nombre: {user_first_name}\n"
                      f"Apellido: {user_last_name}\n"
                      f"Cedula: {user_ID}\n"
                      f"Fecha de entrada: {entry_day}/{entry_month}/{entry_year}\n"
                      f"Fecha de salida: {exit_day}/{exit_month}/{exit_year}")
            else:
                print("\nERROR: La habitación seleccionada ya está ocupada o reservada.")
            break
                    
    if not found:
        print(f"La Habitación {selected_room} no existe, intentelo nuevamente.")
        
def checkout_room(array):
    found = False
    
    operacion = str(input("\n¿Desea buscar por Cedula (C) o Habitacion (H)? ")).upper()
    match operacion:
    
        case "H":
            user_number = input("\nIngrese el número de habitación a liberar: ")
            if user_number.isdigit():
                room_number = int(user_number)
            else:
                print(f"\nERROR: {user_number} no es una habitacion valida. Intente nuevamente.")
                return
            for room in array:
                if room[0] == room_number:
                    found = True
                    print("Desea confirmar el Check-Out?")
                    confirm = str(input("y/n: ")).lower()
                    if confirm == "y":
                        if room[2] == "locked":
                            room[2] = "free"
                            room[3] = ""
                            room[4] = ""
                            room[5] = ""
                            room[6] = ""
                            with open("hotelData.bin", "wb") as file:
                                pickle.dump(array, file)
                            print(f"Habitación {room_number} liberada con éxito!")
                        else:
                            print(f"\nError: La habitación {room_number} no está ocupada")
                    elif confirm == "n":
                        print("El Check-Out ha sido abortado.")
                    else:
                        print(f"\nError: {confirm} no es una opcion valida, intente nuevamente.")

            if not found:
                print(f"\nError: Habitación {room_number} no encontrada, intente nuevamente.")
                
        case "C":
            valid_letters = ['V', 'E', 'P', 'S', 'J', 'G']
            while True:
                user_ID = input(str("Introduzca su cedula. Ejemplo: V-XXXXXXXXXX: ")).upper()
                if (len(user_ID) > 2 and user_ID[0] in valid_letters and user_ID[1] == '-' and user_ID[2:].isdigit()):
                    break
                else:
                    print("\nERROR: Ha introducido una cedula invalida. Intente nuevamente.")
            
            for i in array:
                user_ID_comparison = i[5]
                
                if user_ID_comparison == user_ID:
                    found = True
                    
                    room_number = i[0]
                    room_name_display = i[6] if len(i) > 6 else ""
                    entry_date_display = reformatDate(i[3]) if len(i) > 3 else ""
                    exit_date_display = reformatDate(i[4]) if len(i) > 4 else ""
                    
                    print("Usuario encontrado!\n")
                    print(f"Nombre y Apellido: {room_name_display}\n"
                          f"Cedula: {user_ID}\n"
                          f"Habitacion: {room_number}\n"
                          f"Fecha de entrada: {entry_date_display}\n"
                          f"Fecha de salida: {exit_date_display}\n")
                    
                    print("Desea confirmar el Check-Out?")
                    confirm = str(input("y/n: ")).lower()
                    if confirm == "y":
                        if i[2] == "locked":
                            i[2] = "free"
                            i[3] = ""
                            i[4] = ""
                            i[5] = ""
                            i[6] = ""
                            with open("hotelData.bin", "wb") as file:
                                pickle.dump(array, file)
                            print(f"La habitación {room_number} liberada con éxito!")
                            
                        else:
                            print(f"\nError: La habitación {room_number} no está ocupada")
                    elif confirm == "n":
                        print("El Check-Out ha sido abortado.")
                    else:
                        print(f"\nError: {confirm} no es una opcion valida, intente nuevamente.")

            if not found:
                print("\nError: Habitación no encontrada, intente nuevamente.")
                return
                
        case _:
            print(f"\nError: {operacion} no es una opcion valida, intente nuevamente.")
            
def booking(array):
    while True:
        print("\n--- Fecha de entrada ---")
        entry_day = str(input("Introduzca el dia usando 2 digitos: "))
        entry_month = str(input("Introduzca el mes usando 2 digitos: "))
        entry_year = str(input("Introduzca el año (4 digitos): "))
        if (len(entry_day) == 2 and entry_day.isdigit() and 1 <= int(entry_day) <= 31 and
            len(entry_month) == 2 and entry_month.isdigit() and 1 <= int(entry_month) <= 12 and
            len(entry_year) == 4 and entry_year.isdigit()):
            entry_date = entry_year + entry_month + entry_day
            break
        else:
            print("\nERROR: Ha ingresado una fecha invalida. Intente nuevamente.")
    while True:
        print("\n --- Posible fecha de salida ---")
        exit_day = str(input("Introduzca el dia usando 2 digitos: "))
        exit_month = str(input("Introduzca el mes usando 2 digitos: "))
        exit_year = str(input("Introduzca el año (4 digitos): "))
        if (len(exit_day) == 2 and exit_day.isdigit() and 1 <= int(exit_day) <= 31 and
            len(exit_month) == 2 and exit_month.isdigit() and 1 <= int(exit_month) <= 12 and
            len(exit_year) == 4 and exit_year.isdigit()):
            exit_date = exit_year + exit_month + exit_day
            break
        else:
            print("\nERROR: Ha ingresado una fecha invalida. Intente nuevamente.")
    if entry_date == exit_date:
        print("\nERROR: La fecha de entrada y la fecha de salida son iguales. Intente nuevamente.")
        return
    elif entry_date > exit_date:
        print("\nERROR: La fecha de entrada es posterior a la fecha de salida. Intente nuevamente.")
        return
    
    print("\n --- Datos para la reserva ---")
    user_first_name = input(str("Introduzca el nombre: "))
    user_last_name = input(str("Introduzca el apellido: "))
    
    valid_letters = ['V', 'E', 'P', 'S', 'J', 'G']
    while True:
        user_ID = input(str("Introduzca su cedula. Ejemplo: V-XXXXXXXXXX: ")).upper()
        if (len(user_ID) > 2 and user_ID[0] in valid_letters and user_ID[1] == '-' and user_ID[2:].isdigit()):
            break
        else:
            print("\nERROR: Ha introducido una cedula invalida. Intente nuevamente.")
    
    found = False
    
    for room in array:
        room_number = room[0]
        room_status = room[2]
        room_category_code = room[1]
        
        display_category = ""
        if room_category_code == "mono":
            display_category = "Sencilla"
        elif room_category_code == "duo":
            display_category = "Doble"
        elif room_category_code == "deluxe":
            display_category = "Suite"
        elif room_category_code == "royal":
            display_category = "Presidencial"
        
        if room_status == "free":
            print(f"Habitación {room_number} - {display_category}")
    
    while True:
        selected_room_input = input("\nSeleccione el número de habitación que desea reservar: ")
        if selected_room_input.isdigit():
            selected_room = int(selected_room_input)
            break
        else:
            print("\nERROR: El número de habitación no es válido. Por favor, introduzca una habitacion valida.")
    
    for room in array:
        if room[0] == selected_room:
            found = True
            if room[2] == "free":
                room[2] = "saved"
                room[3] = entry_date
                room[4] = exit_date
                room[5] = user_ID
                room[6] = f"{user_first_name} {user_last_name}"
                
                with open("hotelData.bin", "wb") as file:
                    pickle.dump(array, file)
                    
                print(f"La habitacion {selected_room} ha sido reservada con éxito.")
                print(f"Los datos de la reservacion son:\n"
                      f"Nombre: {user_first_name}\n"
                      f"Apellido: {user_last_name}\n"
                      f"Cedula: {user_ID}\n"
                      f"Fecha de entrada: {entry_day}/{entry_month}/{entry_year}\n"
                      f"Posible fecha de salida: {exit_day}/{exit_month}/{exit_year}")
            else:
                print("\nERROR: La habitación seleccionada ya está ocupada o reservada.")
    
    if not found:
        print(f"La Habitación {selected_room} no existe, intentelo nuevamente.")
        
def cancelBooking(array):
    valid_letters = ['V', 'E', 'P', 'S', 'J', 'G']
    while True:
        user_ID = input(str("Introduzca su cedula. Ejemplo: V-XXXXXXXXXX: ")).upper()
        if (len(user_ID) > 2 and user_ID[0] in valid_letters and user_ID[1] == '-' and user_ID[2:].isdigit()):
            break
        else:
            print("\nERROR: Ha introducido una cedula invalida. Intente nuevamente.")
    
    found = False
    
    for i in array:
        user_ID_comparison = i[5]
        
        if user_ID_comparison == user_ID:
            found = True
            print("Deseas cancelar la reserva de la habitación?")
            confirm = str(input("y/n: ")).lower()
            if confirm == "y":
                if i[2] == "saved":
                    i[2] = "free"
                    i[3] = ""
                    i[4] = ""
                    i[5] = ""
                    i[6] = ""
                    with open("hotelData.bin", "wb") as file:
                        pickle.dump(array, file)
                    print("La reserva ha sido cancelada con exito.")
                else:
                    print("La habitación no tiene reserva.")
                    break
            elif confirm == "n":
                print("La cancelacion de la reserva ha sido abortada.")
            else:
                print(f"\nError: {confirm} no es una opcion valida, intente nuevamente.")
    
    if not found:
        print("La reserva no existe, intente de nuevo.")

while True:
    print("\n --- MENU ---\n")
    print("0 = Ordenar y revisar la disponibilidad de las habitaciones")
    print("1 = Buscar un habitacion")
    print("2 = Ingresar usuario al hotel (hacer un Check-In)")
    print("3 = Egresar usuario del hotel(hacer un Check-Out)")
    print("4 = Reservar una habitacion")
    print("5 = Cancelar una reservacion")
    print("x = SALIR")
    
    selection = str(input("Por favor elige una opcion: ")).lower()
    match selection:
        case "0":
            revisar_disponibilidad(matriz_habitaciones)
        case "1":
            buscar_habitacion(matriz_habitaciones)
        case "2":
            checkin(matriz_habitaciones)
        case "3":
            checkout_room(matriz_habitaciones)
        case "4":
            booking(matriz_habitaciones)
        case "5":
            cancelBooking(matriz_habitaciones)
        case "x":
            print("Has seleccionado salir. Hasta luego!")
            break
        case _:
            print(f"\n{selection} es una opcion invalida. Por favor, intente de nuevo")
            

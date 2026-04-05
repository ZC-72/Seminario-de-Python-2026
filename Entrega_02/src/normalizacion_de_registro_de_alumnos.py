def normalizacion_de_registro_de_alumnos():
   students = [
        {"name": " Ana García ", "grade": "8", "status":"aprobado"},
        {"name": "pedro lópez", "grade": "4", "status":"DESAPROBADO"},
        {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":"Aprobado"},
        {"name": "ana garcía", "grade": "9", "status":"aprobado"},
        {"name": None, "grade": "7", "status": "aprobado"},
        {"name": "Luis Martínez ", "grade": None, "status":"aprobado"},
        {"name": " carlos RUIZ", "grade": "6", "status":"aprobado"},
        {"name": "PEDRO LÓPEZ ", "grade": "3", "status":"desaprobado"},
        {"name": " ", "grade": "5", "status": "aprobado"},
        {"name": "María Fernández", "grade": "7", "status":"APROBADO"},
        {"name": "Sofía Torres", "grade": "9", "status":"Aprobado"},
        {"name": " sofía torres ", "grade": "8", "status":"aprobado"},
        {"name": "Carlos Ruiz", "grade": "6", "status":"APROBADO"},
        {"name": "Roberto Díaz", "grade": "absent", "status":"ausente"},
        {"name": "roberto díaz", "grade": "", "status":"Ausente"},
        {"name": None, "grade": None, "status": None},
        {"name": "Laura Méndez", "grade": "7", "status":"aprobado"},
        {"name": " laura méndez", "grade": "8", "status":"Aprobado"},
        {"name": "GABRIELA RÍOS", "grade": "5", "status":"aprobado"},
        {"name": "gabriela ríos ", "grade": "4", "status":"Desaprobado"},
    ]
   students_normalizados = {}

   # Recorre los estudiantes
   for student in students:
      name = student.get("name")
      grade = student.get("grade")
      status = student.get("status")

      # Valida que no sean nulos o espacios.
      if not name or not name.strip():
         continue
      
      # Valida que no sea nulo y sea un número.
      if not grade or not grade.isdigit():
         continue
      
      # Valida que no sea nulo o espacios.
      if not status or not status.strip():
         continue
      
      # Formatea los valores.
      name = name.strip().title()
      grade = int(grade)
      status = status.strip().title()

      # Agrega los alumnos al diccionario o los actualiza.
      if name not in students_normalizados or grade > students_normalizados[name]["grade"]:
         students_normalizados[name] = {
            "grade": grade,
            "status": status
         }
   # Ordena el diccionario por orden alfabético.
   sorted_normalized_students = sorted(students_normalizados.items())

   # Muestra los datos en pantalla.
   print('Registros limpios de alumnos: ')

   print(f'{"Nombre":<20} {"Nota":<5} {"Estado"}')
   print('-'*40)

   for name, data in sorted_normalized_students:
      print(f'{name:<20} {data["grade"]:<5} {data["status"]}')
    
   print(f"\nTotal de alumnos válidos: {len(sorted_normalized_students)}")
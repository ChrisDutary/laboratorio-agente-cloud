from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
agregar_tarea(tareas, "Preparar laboratorio", "Trabajo")
agregar_tarea(tareas, "Repasar pruebas unitarias", "estudio")
completar_tarea(tareas, 1)

print("Pendientes:")
for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')

print("Pendientes de la categoría 'ESTUDIO':")
for tarea in pendientes(tareas, "ESTUDIO"):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')

eliminada = eliminar_tarea(tareas, 2)
print(f'Tarea eliminada: {eliminada["id"]}: {eliminada["titulo"]}')

print("Pendientes tras eliminar:")
for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')

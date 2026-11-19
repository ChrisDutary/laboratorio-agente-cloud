import unittest
from tasks import agregar_tarea, completar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_agregar_tarea_con_categoria_valida(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "  Estudio  ")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertEqual(tareas, [tarea])

    def test_agregar_tarea_sin_categoria_usa_general(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["categoria"], "general")

    def test_agregar_tarea_con_categoria_vacia(self):
        tareas = []
        for categoria in ("", "   ", None):
            with self.subTest(categoria=categoria):
                with self.assertRaises(ValueError):
                    agregar_tarea(tareas, "Leer documentación", categoria)
        self.assertEqual(tareas, [])

    def test_pendientes_filtra_por_categoria_sin_distinguir_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes", "Estudio")
        agregar_tarea(tareas, "Preparar informe", "Trabajo")
        agregar_tarea(tareas, "Repasar pruebas", "estudio")
        agregar_tarea(tareas, "Leer paper", "ESTUDIO")
        completar_tarea(tareas, 4)

        resultado = pendientes(tareas, "eStUdIo")
        self.assertEqual([t["id"] for t in resultado], [1, 3])

    def test_pendientes_sin_categoria_devuelve_todas(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes", "Estudio")
        agregar_tarea(tareas, "Preparar informe", "Trabajo")
        self.assertEqual([t["id"] for t in pendientes(tareas)], [1, 2])

    def test_pendientes_categoria_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Estudiar agentes", "Estudio")
        self.assertEqual(pendientes(tareas, "Hogar"), [])


if __name__ == "__main__":
    unittest.main()

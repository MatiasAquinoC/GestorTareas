import unittest
from src.vista.gestortareas import Gestortareas
class Test_gestor_tareas(unittest.TestCase):
    def setUp(self):
        self.gestor = Gestortareas()

    def test_agregar_tarea_conCampos_agrega(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 1")
        self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea 1")

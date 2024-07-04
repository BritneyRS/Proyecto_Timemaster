import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import  QTime
import sys


from src.modelo.RelojF import Reloj


class TestReloj(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.window = Reloj()

    def test_initialization(self):
        self.assertEqual(self.window.windowTitle(), "Reloj")
        self.assertEqual(self.window.font().family(), "Palatino Linotype")
        self.assertEqual(self.window.pantalla.count(), 6)  # Verificar que haya 6 pestañas

    def test_start_pomodoro(self):
        self.window.startPomodoro()
        self.assertTrue(self.window.timer.isActive())
        self.assertEqual(self.window.remaining_time, self.window.pomodoro_duration)

    def test_start_break(self):
        self.window.startBreak()
        self.assertTrue(self.window.timer.isActive())
        self.assertEqual(self.window.remaining_time, 5 * 60)

    def test_cancel_pomodoro(self):
        self.window.startPomodoro()
        self.window.cancelPomodoro()
        self.assertFalse(self.window.timer.isActive())
        self.assertEqual(self.window.lcdNumber.value(), 25 * 60)

    def test_update_lcd(self):
        self.window.startPomodoro()
        initial_time = self.window.remaining_time
        self.window.updateLCD()
        self.assertEqual(self.window.remaining_time, initial_time - 1)

    def test_save_config_changes(self):
        self.window.timeEdit_pomodoro.setTime(QTime(0, 30))
        self.window.timeEdit_break.setTime(QTime(0, 5))
        self.window.saveConfigChanges()
        self.assertEqual(self.window.pomodoro_duration, 30 * 60)
        self.assertEqual(self.window.break_duration, 5 * 60)

    def test_add_task(self):
        self.window.addTask()
        # Aquí podrías agregar más comprobaciones específicas de la lógica de agregar tareas

    @classmethod
    def tearDownClass(cls):
        cls.app.exit()


if __name__ == '__main__':
    unittest.main()

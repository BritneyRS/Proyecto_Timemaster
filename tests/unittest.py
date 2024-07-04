import unittest
from PyQt5.QtCore import QTime
from Proyecto_Timemaster.src.modelo.RelojF import Reloj


class TestReloj(unittest.TestCase):
    def setUp(self):
        self.reloj = Reloj()

    def test_initial_pomodoro_duration(self):
        self.assertEqual(self.reloj.pomodoro_duration, 25 * 60)

    def test_save_config_changes(self):
        self.reloj.timeEdit_pomodoro.setTime(QTime(0, 30))
        self.reloj.timeEdit_break.setTime(QTime(0, 5))
        self.reloj.saveConfigChanges()
        self.assertEqual(self.reloj.pomodoro_duration, 30 * 60)
        self.assertEqual(self.reloj.break_duration, 5 * 60)

    def test_update_lcd(self):
        self.reloj.pomodoro_duration = 120  # 2 minutes
        self.reloj.remaining_time = 120
        self.reloj.updateLCD()
        self.assertEqual(self.reloj.remaining_time, 119)


if _name_ == '_main_':
    unittest.main()
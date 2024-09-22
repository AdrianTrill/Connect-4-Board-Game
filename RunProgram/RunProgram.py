from tests.tests import TestBoard
from UI.UI import UI, GUI

tests = TestBoard()
tests.testAll()

ui = UI()
gui = GUI()

#ui.run()
gui.run()

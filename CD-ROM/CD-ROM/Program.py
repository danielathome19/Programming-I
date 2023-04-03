import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import Application
import MainForm

try:
	Application.EnableVisualStyles()
	form = MainForm.MainForm()
	Application.Run(form)
except Exception as e:
	print("Error:", e)
	input("Press enter to continue...")	

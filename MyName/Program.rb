require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
require "MainForm"

Application = System::Windows::Forms::Application

Application.EnableVisualStyles()
form = MainForm.new()
Application.Run(form)

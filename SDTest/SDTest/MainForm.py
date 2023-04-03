import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._btn1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textlen = System.Windows.Forms.TextBox()
		self._textwid = System.Windows.Forms.TextBox()
		self._lblarea = System.Windows.Forms.Label()
		self._lblperim = System.Windows.Forms.Label()
		self._btnreset = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# btn1
		# 
		self._btn1.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btn1.Location = System.Drawing.Point(34, 244)
		self._btn1.Name = "btn1"
		self._btn1.Size = System.Drawing.Size(322, 103)
		self._btn1.TabIndex = 0
		self._btn1.Text = "Calculate"
		self._btn1.UseVisualStyleBackColor = True
		self._btn1.Click += self.Btn1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(34, 53)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(192, 88)
		self._label1.TabIndex = 1
		self._label1.Text = "Length"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(381, 53)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(182, 88)
		self._label2.TabIndex = 2
		self._label2.Text = "Width"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textlen
		# 
		self._textlen.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textlen.Location = System.Drawing.Point(34, 156)
		self._textlen.Name = "textlen"
		self._textlen.Size = System.Drawing.Size(192, 57)
		self._textlen.TabIndex = 3
		# 
		# textwid
		# 
		self._textwid.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textwid.Location = System.Drawing.Point(381, 156)
		self._textwid.Name = "textwid"
		self._textwid.Size = System.Drawing.Size(182, 57)
		self._textwid.TabIndex = 4
		# 
		# lblarea
		# 
		self._lblarea.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._lblarea.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lblarea.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblarea.Location = System.Drawing.Point(34, 370)
		self._lblarea.Name = "lblarea"
		self._lblarea.Size = System.Drawing.Size(529, 79)
		self._lblarea.TabIndex = 5
		self._lblarea.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblperim
		# 
		self._lblperim.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._lblperim.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lblperim.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblperim.Location = System.Drawing.Point(34, 472)
		self._lblperim.Name = "lblperim"
		self._lblperim.Size = System.Drawing.Size(529, 79)
		self._lblperim.TabIndex = 6
		self._lblperim.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# btnreset
		# 
		self._btnreset.Font = System.Drawing.Font("Microsoft Sans Serif", 22, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnreset.Location = System.Drawing.Point(381, 244)
		self._btnreset.Name = "btnreset"
		self._btnreset.Size = System.Drawing.Size(182, 103)
		self._btnreset.TabIndex = 7
		self._btnreset.Text = "Reset"
		self._btnreset.UseVisualStyleBackColor = True
		self._btnreset.Click += self.BtnresetClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.Highlight
		self.ClientSize = System.Drawing.Size(607, 578)
		self.Controls.Add(self._btnreset)
		self.Controls.Add(self._lblperim)
		self.Controls.Add(self._lblarea)
		self.Controls.Add(self._textwid)
		self.Controls.Add(self._textlen)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._btn1)
		self.Name = "MainForm"
		self.Text = "Area and Perim Calc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Btn1Click(self, sender, e):
		length = int(self._textlen.Text)
		width = int(self._textwid.Text)
		area = length * width
		perim = 2 * length + 2 * width
		self._lblarea.Text = str(area)
		self._lblperim.Text = str(perim)

	def BtnresetClick(self, sender, e):
		self._lblarea.Text = ""
		self._lblperim.Text = ""
		self._textlen.Text = ""
		self._textwid.Text = ""
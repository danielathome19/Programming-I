import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._button10 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._button6)
		self._groupBox1.Controls.Add(self._button7)
		self._groupBox1.Controls.Add(self._button8)
		self._groupBox1.Controls.Add(self._button9)
		self._groupBox1.Controls.Add(self._button10)
		self._groupBox1.Controls.Add(self._button5)
		self._groupBox1.Controls.Add(self._button4)
		self._groupBox1.Controls.Add(self._button3)
		self._groupBox1.Controls.Add(self._button2)
		self._groupBox1.Controls.Add(self._button1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 190)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(870, 403)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Select a Format"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(24, 56)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(403, 48)
		self._button1.TabIndex = 0
		self._button1.Text = "Number format (n)"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(24, 121)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(403, 48)
		self._button2.TabIndex = 1
		self._button2.Text = "Fixed-point format (f)"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(24, 189)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(403, 48)
		self._button3.TabIndex = 2
		self._button3.Text = "Exponential format (e)"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(24, 258)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(403, 48)
		self._button4.TabIndex = 3
		self._button4.Text = "Currency format (c)"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(24, 327)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(403, 48)
		self._button5.TabIndex = 4
		self._button5.Text = "Percent format (c)"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(443, 327)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(403, 48)
		self._button6.TabIndex = 9
		self._button6.Text = "Full date/time (F)"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(443, 258)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(403, 48)
		self._button7.TabIndex = 8
		self._button7.Text = "Long time (T)"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(443, 189)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(403, 48)
		self._button8.TabIndex = 7
		self._button8.Text = "Short time (t)"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(443, 121)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(403, 48)
		self._button9.TabIndex = 6
		self._button9.Text = "Long date (D)"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# button10
		# 
		self._button10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button10.Location = System.Drawing.Point(443, 56)
		self._button10.Name = "button10"
		self._button10.Size = System.Drawing.Size(403, 48)
		self._button10.TabIndex = 5
		self._button10.Text = "Short date (d)"
		self._button10.UseVisualStyleBackColor = True
		self._button10.Click += self.Button10Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(398, 48)
		self._label1.TabIndex = 1
		self._label1.Text = "Enter a number or date:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 112)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(398, 53)
		self._label2.TabIndex = 2
		self._label2.Text = "Formatted:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(416, 29)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(466, 48)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Enabled = False
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(416, 112)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(466, 48)
		self._textBox2.TabIndex = 4
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(894, 605)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg147Format"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	# Number formats -- 67895.34926	
	def Button1Click(self, sender, e):
		# Number format (n)
		num = float(self._textBox1.Text)
		self._textBox2.Text = '{:,.2f}'.format(num)

	def Button2Click(self, sender, e):
		# Fixed-point format (f)
		num = float(self._textBox1.Text)
		self._textBox2.Text = '{:.2f}'.format(num)

	def Button3Click(self, sender, e):
		# Exponential format (e)
		num = float(self._textBox1.Text)
		self._textBox2.Text = '{:e}'.format(num)

	def Button4Click(self, sender, e):
		# Currency format (c)
		num = float(self._textBox1.Text)
		self._textBox2.Text = '${:,.2f}'.format(num)

	def Button5Click(self, sender, e):
		# Percent format (p)
		num = float(self._textBox1.Text)
		self._textBox2.Text = '{:,.2%}'.format(num)
	
	
	# Date formats -- May 5, 2009 6:35 PM
	def Button10Click(self, sender, e):
		# Short date (d)
		from datetime import *
		dtstr = self._textBox1.Text
		dt = datetime.strptime(dtstr, "%b %d %Y %I:%M %p")
		self._textBox2.Text = date.strftime(dt, "%m/%d/%y")

	def Button9Click(self, sender, e):
		# Long date (D)
		from datetime import *
		dtstr = self._textBox1.Text
		dt = datetime.strptime(dtstr, "%b %d %Y %I:%M %p")
		self._textBox2.Text = date.strftime(dt, "%A, %d %B, %Y")

	def Button8Click(self, sender, e):
		# Short time (t)
		from datetime import *
		dtstr = self._textBox1.Text
		dt = datetime.strptime(dtstr, "%b %d %Y %I:%M %p")
		self._textBox2.Text = date.strftime(dt, "%H:%M:%S")

	def Button7Click(self, sender, e):
		# Long time (T)
		from datetime import *
		dtstr = self._textBox1.Text
		dt = datetime.strptime(dtstr, "%b %d %Y %I:%M %p")
		self._textBox2.Text = date.strftime(dt, "%I:%M:%S %p")

	def Button6Click(self, sender, e):
		# Full date/time (F)
		from datetime import *
		dtstr = self._textBox1.Text
		dt = datetime.strptime(dtstr, "%b %d %Y %I:%M %p")
		self._textBox2.Text = date.strftime(dt, "%A, %d %B, %Y %I:%M:%S %p")
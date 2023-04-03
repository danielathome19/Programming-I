import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(29, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(144, 43)
		self._label1.TabIndex = 0
		self._label1.Text = "Num1:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(29, 103)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(144, 43)
		self._label2.TabIndex = 1
		self._label2.Text = "Num2:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(179, 19)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(235, 48)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(179, 100)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(235, 48)
		self._textBox2.TabIndex = 3
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(463, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(200, 67)
		self._button1.TabIndex = 4
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(463, 93)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(200, 67)
		self._button2.TabIndex = 5
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(29, 179)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(634, 76)
		self._button3.TabIndex = 6
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(29, 267)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(258, 43)
		self._label3.TabIndex = 7
		self._label3.Text = "Sum:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(29, 323)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(258, 43)
		self._label4.TabIndex = 8
		self._label4.Text = "Difference:"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(29, 381)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(258, 43)
		self._label5.TabIndex = 9
		self._label5.Text = "Product:"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(29, 435)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(258, 43)
		self._label6.TabIndex = 10
		self._label6.Text = "Average:"
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(29, 489)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(258, 43)
		self._label7.TabIndex = 11
		self._label7.Text = "Absolute Val:"
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(29, 546)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(258, 43)
		self._label8.TabIndex = 12
		self._label8.Text = "Max:"
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(29, 600)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(258, 43)
		self._label9.TabIndex = 13
		self._label9.Text = "Min:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(314, 600)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(349, 43)
		self._label10.TabIndex = 20
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(314, 546)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(349, 43)
		self._label11.TabIndex = 19
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(314, 489)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(349, 43)
		self._label12.TabIndex = 18
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(314, 435)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(349, 43)
		self._label13.TabIndex = 17
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label14.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(314, 381)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(349, 43)
		self._label14.TabIndex = 16
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label15.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(314, 323)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(349, 43)
		self._label15.TabIndex = 15
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._label16.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(314, 267)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(349, 43)
		self._label16.TabIndex = 14
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(705, 677)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		diff = num1 - num2
		
		
		
		
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:
			Max = num2
		
		if num1 < num2:
			Min = num1
		else:
			Min = num2
		
		self._label11.Text = str(Max)
		self._label10.Text = str(Min)
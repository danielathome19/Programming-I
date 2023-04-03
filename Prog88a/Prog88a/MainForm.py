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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(70, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(177, 63)
		self._label1.TabIndex = 0
		self._label1.Text = "Num1:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(70, 69)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(177, 63)
		self._label2.TabIndex = 1
		self._label2.Text = "Num2:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(278, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(211, 53)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(278, 66)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(211, 53)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(46, 146)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(177, 63)
		self._label3.TabIndex = 4
		self._label3.Text = "Sum:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(278, 135)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(209, 63)
		self._label4.TabIndex = 5
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(278, 198)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(209, 63)
		self._label5.TabIndex = 7
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(36, 198)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(226, 63)
		self._label6.TabIndex = 6
		self._label6.Text = "Difference:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(278, 258)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(209, 63)
		self._label7.TabIndex = 9
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(46, 250)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(177, 63)
		self._label8.TabIndex = 8
		self._label8.Text = "Product:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(278, 316)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(209, 63)
		self._label9.TabIndex = 11
		# 
		# label10
		# 
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(46, 305)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(177, 63)
		self._label10.TabIndex = 10
		self._label10.Text = "Average:"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(278, 363)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(209, 63)
		self._label11.TabIndex = 13
		# 
		# label12
		# 
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(36, 363)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(211, 63)
		self._label12.TabIndex = 12
		self._label12.Text = "Abs Diff:"
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(278, 426)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(209, 63)
		self._label13.TabIndex = 15
		# 
		# label14
		# 
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(39, 426)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(208, 63)
		self._label14.TabIndex = 14
		self._label14.Text = "Maximum:"
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label15.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(278, 477)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(209, 63)
		self._label15.TabIndex = 17
		# 
		# label16
		# 
		self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(36, 477)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(199, 63)
		self._label16.TabIndex = 16
		self._label16.Text = "Minimum:"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 561)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(223, 63)
		self._button1.TabIndex = 18
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(291, 561)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(152, 63)
		self._button2.TabIndex = 19
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(494, 561)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(152, 63)
		self._button3.TabIndex = 20
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(658, 628)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Diff = num1 - num2
		
		
		# Hint: use the abs() function to get the absolute diff
		
		
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:  # Otherwise...
			Max = num2
			
		if Max == num1:
			Min = num2
		else:
			Min = num1
		
		
		self._label13.Text = str(Max)
		self._label15.Text = str(Min)
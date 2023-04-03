import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("Flags.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._radioButton13 = System.Windows.Forms.RadioButton()
		self._radioButton14 = System.Windows.Forms.RadioButton()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton15 = System.Windows.Forms.RadioButton()
		self._radioButton16 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._lblname = System.Windows.Forms.Label()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._groupBox4.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self._pictureBox3.BeginInit()
		self._pictureBox2.BeginInit()
		self._pictureBox1.BeginInit()
		self._groupBox3.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._pictureBox4.BeginInit()
		self.SuspendLayout()
		# 
		# radioButton13
		# 
		self._radioButton13.Location = System.Drawing.Point(6, 270)
		self._radioButton13.Name = "radioButton13"
		self._radioButton13.Size = System.Drawing.Size(312, 53)
		self._radioButton13.TabIndex = 3
		self._radioButton13.TabStop = True
		self._radioButton13.Text = "Strikeout"
		self._radioButton13.UseVisualStyleBackColor = True
		# 
		# radioButton14
		# 
		self._radioButton14.Location = System.Drawing.Point(6, 201)
		self._radioButton14.Name = "radioButton14"
		self._radioButton14.Size = System.Drawing.Size(312, 53)
		self._radioButton14.TabIndex = 2
		self._radioButton14.TabStop = True
		self._radioButton14.Text = "Underline"
		self._radioButton14.UseVisualStyleBackColor = True
		# 
		# groupBox4
		# 
		self._groupBox4.Controls.Add(self._radioButton13)
		self._groupBox4.Controls.Add(self._radioButton14)
		self._groupBox4.Controls.Add(self._radioButton15)
		self._groupBox4.Controls.Add(self._radioButton16)
		self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox4.Location = System.Drawing.Point(752, 364)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(324, 346)
		self._groupBox4.TabIndex = 13
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Font Style"
		# 
		# radioButton15
		# 
		self._radioButton15.Location = System.Drawing.Point(6, 132)
		self._radioButton15.Name = "radioButton15"
		self._radioButton15.Size = System.Drawing.Size(312, 53)
		self._radioButton15.TabIndex = 1
		self._radioButton15.TabStop = True
		self._radioButton15.Text = "Italic"
		self._radioButton15.UseVisualStyleBackColor = True
		# 
		# radioButton16
		# 
		self._radioButton16.Location = System.Drawing.Point(6, 63)
		self._radioButton16.Name = "radioButton16"
		self._radioButton16.Size = System.Drawing.Size(312, 53)
		self._radioButton16.TabIndex = 0
		self._radioButton16.TabStop = True
		self._radioButton16.Text = "Bold"
		self._radioButton16.UseVisualStyleBackColor = True
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(6, 201)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(312, 53)
		self._radioButton10.TabIndex = 2
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "Black"
		self._radioButton10.UseVisualStyleBackColor = True
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(324, 346)
		self._groupBox1.TabIndex = 11
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Flags"
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(6, 270)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(312, 53)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Mouse"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(6, 201)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(312, 53)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Keyboard"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(6, 132)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(312, 53)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Computer"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 63)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(312, 53)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Bus"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# pictureBox3
		# 
		self._pictureBox3.BackColor = System.Drawing.Color.White
		self._pictureBox3.Image = resources.GetObject("pictureBox3.Image")
		self._pictureBox3.Location = System.Drawing.Point(720, 34)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(175, 175)
		self._pictureBox3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox3.TabIndex = 18
		self._pictureBox3.TabStop = False
		self._pictureBox3.Visible = False
		# 
		# pictureBox2
		# 
		self._pictureBox2.BackColor = System.Drawing.Color.White
		self._pictureBox2.Image = resources.GetObject("pictureBox2.Image")
		self._pictureBox2.Location = System.Drawing.Point(539, 34)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(175, 175)
		self._pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox2.TabIndex = 17
		self._pictureBox2.TabStop = False
		self._pictureBox2.Visible = False
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.Color.White
		self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
		self._pictureBox1.Location = System.Drawing.Point(358, 34)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(175, 175)
		self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox1.TabIndex = 16
		self._pictureBox1.TabStop = False
		self._pictureBox1.Visible = False
		# 
		# lblname
		# 
		self._lblname.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._lblname.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lblname.Location = System.Drawing.Point(358, 223)
		self._lblname.Name = "lblname"
		self._lblname.Size = System.Drawing.Size(718, 114)
		self._lblname.TabIndex = 15
		self._lblname.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(6, 270)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(312, 53)
		self._radioButton9.TabIndex = 3
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "White"
		self._radioButton9.UseVisualStyleBackColor = True
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._radioButton9)
		self._groupBox3.Controls.Add(self._radioButton10)
		self._groupBox3.Controls.Add(self._radioButton11)
		self._groupBox3.Controls.Add(self._radioButton12)
		self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(358, 364)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(324, 346)
		self._groupBox3.TabIndex = 14
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Font Color"
		# 
		# radioButton11
		# 
		self._radioButton11.Location = System.Drawing.Point(6, 132)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(312, 53)
		self._radioButton11.TabIndex = 1
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "Blue"
		self._radioButton11.UseVisualStyleBackColor = True
		# 
		# radioButton12
		# 
		self._radioButton12.Location = System.Drawing.Point(6, 63)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(312, 53)
		self._radioButton12.TabIndex = 0
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "Red"
		self._radioButton12.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radioButton5)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Controls.Add(self._radioButton7)
		self._groupBox2.Controls.Add(self._radioButton8)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(12, 364)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(324, 346)
		self._groupBox2.TabIndex = 12
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Font Size"
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(6, 270)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(312, 53)
		self._radioButton5.TabIndex = 3
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "36"
		self._radioButton5.UseVisualStyleBackColor = True
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(6, 201)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(312, 53)
		self._radioButton6.TabIndex = 2
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "18"
		self._radioButton6.UseVisualStyleBackColor = True
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(6, 132)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(312, 53)
		self._radioButton7.TabIndex = 1
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "10"
		self._radioButton7.UseVisualStyleBackColor = True
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(6, 63)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(312, 53)
		self._radioButton8.TabIndex = 0
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "6"
		self._radioButton8.UseVisualStyleBackColor = True
		# 
		# pictureBox4
		# 
		self._pictureBox4.BackColor = System.Drawing.Color.White
		self._pictureBox4.Image = resources.GetObject("pictureBox4.Image")
		self._pictureBox4.Location = System.Drawing.Point(901, 34)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(175, 175)
		self._pictureBox4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox4.TabIndex = 19
		self._pictureBox4.TabStop = False
		self._pictureBox4.Visible = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(1105, 732)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._lblname)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._pictureBox4)
		self.Name = "MainForm"
		self.Text = "Flags"
		self._groupBox4.ResumeLayout(False)
		self._groupBox1.ResumeLayout(False)
		self._pictureBox3.EndInit()
		self._pictureBox2.EndInit()
		self._pictureBox1.EndInit()
		self._groupBox3.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._pictureBox4.EndInit()
		self.ResumeLayout(False)


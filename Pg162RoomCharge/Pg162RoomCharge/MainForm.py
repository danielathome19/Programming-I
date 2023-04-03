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
		self._label3 = System.Windows.Forms.Label()
		self._lblDateToday = System.Windows.Forms.Label()
		self._lblTimeToday = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(139, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(352, 56)
		self._label1.TabIndex = 0
		self._label1.Text = "Highlander Hotel"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(139, 88)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(235, 68)
		self._label2.TabIndex = 1
		self._label2.Text = "Today's Date:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(139, 156)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(235, 68)
		self._label3.TabIndex = 2
		self._label3.Text = "Time:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# lblDateToday
		# 
		self._lblDateToday.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._lblDateToday.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblDateToday.Location = System.Drawing.Point(400, 84)
		self._lblDateToday.Name = "lblDateToday"
		self._lblDateToday.Size = System.Drawing.Size(299, 68)
		self._lblDateToday.TabIndex = 3
		self._lblDateToday.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblTimeToday
		# 
		self._lblTimeToday.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._lblTimeToday.Font = System.Drawing.Font("Microsoft Sans Serif", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTimeToday.Location = System.Drawing.Point(400, 156)
		self._lblTimeToday.Name = "lblTimeToday"
		self._lblTimeToday.Size = System.Drawing.Size(299, 68)
		self._lblTimeToday.TabIndex = 4
		self._lblTimeToday.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# groupBox1
		# 
		self._groupBox1.Location = System.Drawing.Point(68, 269)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(200, 100)
		self._groupBox1.TabIndex = 5
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# groupBox2
		# 
		self._groupBox2.Location = System.Drawing.Point(400, 285)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(200, 100)
		self._groupBox2.TabIndex = 6
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "groupBox2"
		# 
		# groupBox3
		# 
		self._groupBox3.Location = System.Drawing.Point(94, 406)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(200, 100)
		self._groupBox3.TabIndex = 7
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "groupBox3"
		# 
		# btnCalculate
		# 
		self._btnCalculate.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnCalculate.Location = System.Drawing.Point(45, 543)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(329, 88)
		self._btnCalculate.TabIndex = 8
		self._btnCalculate.Text = "Calculate Charges"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClear
		# 
		self._btnClear.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnClear.Location = System.Drawing.Point(389, 543)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(174, 88)
		self._btnClear.TabIndex = 9
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = True
		# 
		# btnExit
		# 
		self._btnExit.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnExit.Location = System.Drawing.Point(578, 543)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(174, 88)
		self._btnExit.TabIndex = 10
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(773, 709)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._lblTimeToday)
		self.Controls.Add(self._lblDateToday)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg162RoomCharge"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		# Get today's date from the system and display it
		from datetime import date
		self._lblDateToday.Text = date.today().strftime("%A, %B %d, %Y")
		# Get the current time from the system and display it
		import time
		self._lblTimeToday.Text = time.strftime("%I:%M:%S %p")

	def BtnCalculateClick(self, sender, e):
		
		# Declare variables for the calculations
		decRoomCharges = 0.0  # Room charges total
		decAddCharges = 0.0   # Additional charges
		decSubtotal = 0.0     # Subtotal
		decTax = 0.0          # Tax
		decTotal = 0.0        # Total of all charges
		decTAX_RATE = 0.08    # Tax rate
		
		try:
			# Calculate and display the room charges.
			# Handle error if the fields are blank.
			decAddCharges = float(self._txtRoomService.Text) + \
			  float(self._txtTelephone.Text) + \
			  float(self._txtMisc.Text)
			self._lblAddCharges.Text = str(round(decAddCharges, 2))
		except:
			MessageBox.Show("Room service, Telephone, and Misc. must be numbers", "Error")
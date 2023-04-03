import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._lbl1 = System.Windows.Forms.Label()
		self._btnShow = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# lbl1
		# 
		self._lbl1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lbl1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._lbl1.Font = System.Drawing.Font("Microsoft Sans Serif", 26, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lbl1.Location = System.Drawing.Point(37, 45)
		self._lbl1.Name = "lbl1"
		self._lbl1.Size = System.Drawing.Size(685, 136)
		self._lbl1.TabIndex = 0
		self._lbl1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# btnShow
		# 
		self._btnShow.BackColor = System.Drawing.Color.SteelBlue
		self._btnShow.Font = System.Drawing.Font("Microsoft Sans Serif", 26, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnShow.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._btnShow.Location = System.Drawing.Point(37, 262)
		self._btnShow.Name = "btnShow"
		self._btnShow.Size = System.Drawing.Size(317, 112)
		self._btnShow.TabIndex = 1
		self._btnShow.Text = "Show"
		self._btnShow.UseVisualStyleBackColor = False
		self._btnShow.Click += self.BtnShowClick
		# 
		# btnClear
		# 
		self._btnClear.BackColor = System.Drawing.Color.SteelBlue
		self._btnClear.Font = System.Drawing.Font("Microsoft Sans Serif", 26, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnClear.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._btnClear.Location = System.Drawing.Point(405, 262)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(317, 112)
		self._btnClear.TabIndex = 2
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = False
		self._btnClear.Click += self.BtnClearClick
		# 
		# btnExit
		# 
		self._btnExit.BackColor = System.Drawing.Color.SteelBlue
		self._btnExit.Font = System.Drawing.Font("Microsoft Sans Serif", 26, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnExit.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._btnExit.Location = System.Drawing.Point(37, 438)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(685, 112)
		self._btnExit.TabIndex = 3
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = False
		self._btnExit.Click += self.BtnExitClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(804, 647)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnShow)
		self.Controls.Add(self._lbl1)
		self.Name = "MainForm"
		self.Text = "HelloWorld"
		self.ResumeLayout(False)


	def BtnShowClick(self, sender, e):
		self._lbl1.Text = "Hello, World!"

	def BtnClearClick(self, sender, e):
		self._lbl1.Text = ""

	def BtnExitClick(self, sender, e):
		Application.Exit()
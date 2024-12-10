import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.R = System.Random()
        self.ballup = 0
        self.balld = 0
        self.flagleft = False
        self.flagright = False
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        self._lbltitle = System.Windows.Forms.Label()
        self._leftscore = System.Windows.Forms.Label()
        self._rightscore = System.Windows.Forms.Label()
        self._lblball = System.Windows.Forms.Label()
        self._lblleft = System.Windows.Forms.Label()
        self._lblright = System.Windows.Forms.Label()
        self._timerdummy = System.Windows.Forms.Timer(self._components)
        self._timerboolean = System.Windows.Forms.Timer(self._components)
        self._timerright = System.Windows.Forms.Timer(self._components)
        self._timerleft = System.Windows.Forms.Timer(self._components)
        self._timerball = System.Windows.Forms.Timer(self._components)
        self._timermulti = System.Windows.Forms.Timer(self._components)
        self.SuspendLayout()
        # 
        # lbltitle
        # 
        self._lbltitle.BackColor = System.Drawing.Color.Transparent
        self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._lbltitle.ForeColor = System.Drawing.Color.White
        self._lbltitle.Location = System.Drawing.Point(12, 25)
        self._lbltitle.Name = "lbltitle"
        self._lbltitle.Size = System.Drawing.Size(958, 52)
        self._lbltitle.TabIndex = 0
        self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
        self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # leftscore
        # 
        self._leftscore.BackColor = System.Drawing.Color.Transparent
        self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._leftscore.ForeColor = System.Drawing.Color.White
        self._leftscore.Location = System.Drawing.Point(78, 96)
        self._leftscore.Name = "leftscore"
        self._leftscore.Size = System.Drawing.Size(166, 109)
        self._leftscore.TabIndex = 1
        self._leftscore.Text = "0"
        self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # rightscore
        # 
        self._rightscore.BackColor = System.Drawing.Color.Transparent
        self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._rightscore.ForeColor = System.Drawing.Color.White
        self._rightscore.Location = System.Drawing.Point(734, 96)
        self._rightscore.Name = "rightscore"
        self._rightscore.Size = System.Drawing.Size(166, 109)
        self._rightscore.TabIndex = 2
        self._rightscore.Text = "0"
        self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # lblball
        # 
        self._lblball.BackColor = System.Drawing.Color.White
        self._lblball.Location = System.Drawing.Point(479, 304)
        self._lblball.Name = "lblball"
        self._lblball.Size = System.Drawing.Size(20, 20)
        self._lblball.TabIndex = 3
        self._lblball.Click += self.LblballClick
        # 
        # lblleft
        # 
        self._lblleft.BackColor = System.Drawing.Color.White
        self._lblleft.Location = System.Drawing.Point(12, 246)
        self._lblleft.Name = "lblleft"
        self._lblleft.Size = System.Drawing.Size(20, 100)
        self._lblleft.TabIndex = 4
        # 
        # lblright
        # 
        self._lblright.BackColor = System.Drawing.Color.White
        self._lblright.Location = System.Drawing.Point(950, 246)
        self._lblright.Name = "lblright"
        self._lblright.Size = System.Drawing.Size(20, 100)
        self._lblright.TabIndex = 5
        # 
        # timerright
        # 
        self._timerright.Interval = 20
        self._timerright.Tick += self.TimerrightTick
        # 
        # timerleft
        # 
        self._timerleft.Interval = 20
        self._timerleft.Tick += self.TimerleftTick
        # 
        # timerball
        # 
        self._timerball.Interval = 20
        self._timerball.Tick += self.TimerballTick
        # 
        # timermulti
        # 
        self._timermulti.Interval = 20
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(982, 590)
        self.Controls.Add(self._lblright)
        self.Controls.Add(self._lblleft)
        self.Controls.Add(self._lblball)
        self.Controls.Add(self._rightscore)
        self.Controls.Add(self._leftscore)
        self.Controls.Add(self._lbltitle)
        self.Name = "MainForm"
        self.Text = "Pong"
        self.Load += self.MainFormLoad
        self.SizeChanged += self.MainFormSizeChanged
        self.KeyDown += self.MainFormKeyDown
        self.ResumeLayout(False)


    def TimerballTick(self, sender, e):
        pass

    def MainFormKeyDown(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        """ TODO: ADD 3 UNIQUE SECRETS/CHEATS/EASTER EGGS
        IN TOTAL & FINISH MULTIPLAYER & SCOREBOARD & DUMMY AI """
        self.balld = 1
        self.ballup = self.R.Next(-4, 5)
    
    def pdlTick(self, pdl, flagd, tmr):
        if flagd == True:
            pdl.Top += 5
        else:
            pdl.Top -= 5
        if pdl.Top <= 10 or pdl.Bottom >= self.Height - 50:
            tmr.Enabled = False

    def TimerleftTick(self, sender, e):
        self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

    def TimerrightTick(self, sender, e):
        self.pdlTick(self._lblright, self.flagright, self._timerright)

    def LblballClick(self, sender, e):
        self._lblball.BackColor = Color.Red
        self.BackColor = Color.Green  # Form BG Color
        """ TODO: PUT MORE EASTER EGGS LATER """

    def MainFormSizeChanged(self, sender, e):
        self._lblright.Left = self.Width - 25 - self._lblright.Width
        self._rightscore.Left = self.Width - 75 - self._rightscore.Width
        self._lbltitle.Width = self.Width - 25
        self._lblball.Left = self.Width // 2
        self._lblball.Top = self.Height // 2
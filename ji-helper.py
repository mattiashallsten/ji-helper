from math import gcd
import sys

# main class
class Ratio:
  def __init__(self, num, den):
    self.num = int(num)
    self.den = int(den)

  def printratio(self):
    print("The ratio is: " + str(self.num) + "/" + str(self.den))

  def minfrac(self):
    divisor = gcd(self.num, self.den)
    self.num = int(self.num / divisor)
    self.den = int(self.den / divisor)

  def forceoct(self):
    if self.num / self.den >= 2:
      self.den = int(self.den * 2)
      return self.forceoct()

    elif self.num / self.den < 1:
      self.num = int(self.num * 2)
      return self.forceoct()

    else:
      return self.minfrac()

  def multiply(self, ratio2):
    self.num = self.num * ratio2.num
    self.den = self.den * ratio2.den

    return self.forceoct()

  def divide(self, ratio2):
    self.num = self.num * ratio2.den
    self.den = self.den * ratio2.num

    return self.forceoct()

  
# reading creation arguments
  
if sys.argv[1] == 'min':
  argstr = sys.argv[2].split('/')
  ratio = Ratio(argstr[0], argstr[1])

  ratio.minfrac()

  ratio.printratio()
  
elif sys.argv[1] == 'force':
  argstr = sys.argv[2].split('/')
  ratio = Ratio(argstr[0], argstr[1])

  ratio.forceoct()

  ratio.printratio()

elif sys.argv[1] == 'mult':
  argstr1 = sys.argv[2].split('/')
  argstr2 = sys.argv[3].split('/')

  ratio = Ratio(argstr1[0], argstr1[1])
  ratio2 = Ratio(argstr2[0], argstr2[1])

  ratio.multiply(ratio2)

  ratio.printratio()

elif sys.argv[1] == 'div':
  argstr1 = sys.argv[2].split('/')
  ratio = Ratio(argstr1[0], argstr1[1])

  argstr2 = sys.argv[3].split('/')
  ratio2 = Ratio(argstr2[0], argstr2[1])

  ratio.divide(ratio2)

  ratio.printratio()

elif sys.argv[1] == 'help':
  with open("ji-helper-help.txt") as f:
    print(f.read())

class Shape:
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self.area = 0
    self.perim = 0

  def calc(self):
    self.area = self.length * self.width
    self.perim = 2 * self.length + 2 * self.width

  def getArea(self):
    return self.area

  def getPerim(self):
    return self.perim


def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width: "))
  rectangle = Shape(len, wid)
  rectangle.calc()
  area = rectangle.getArea()
  perim = rectangle.getPerim()
  print("Area:", area)
  print("Perimeter:", perim)
  pass


if __name__ == "__main__":
  main()
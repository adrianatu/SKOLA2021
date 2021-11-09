
class Robots:
  """klase reprezentēta ar specifisku vārdu"""

  def __init__(self,vards):
    """datu inilizācija"""


   
    self.vards=vards


    print(f"incializējam{self.vards}")


  def sasveicinaties(self):
   print(f"Sveiks! Mani sauc{self.vards}")

rob1 = Robots("R1")

rob1.sasveicinaties()

rob2 = Robots("R2")
rob2.sasveicinaties()
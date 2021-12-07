#Izveido klasi Transportlīdeklis
class Transportlideklis:


  krasa = "Melna"
  #Pievieno īpašības
  def __init__ (self, nosaukums, max_atrums,nobraukums):
    self.nosaukums = nosaukums
    self.max_atrums = max_atrums
    self.nobraukums = nobraukums



  def sedvietu_skaits(self,skaits):
    self.skaits = skaits
    return f"Sēdvietu skaits {self.nosaukums} ir
    {self.skaits} vietas."

  def biletes(self):
    return self.skaits * 0.5



#modelisX = Transportlideklis("Mersedess",150,55)
#  print(modelisX.nosaukums,modelisX.max_atrums,modelisX.nobraukums)

class Buss(Transportlideklis):
 def sedvietu_skaits(self,skaits = 50):
    return super().sedvietu_skaits(skaits = 50)

#modelisY = Buss("Mersedess",150,55)
#print(modelisY.nosaukums,modelisY.max_atrums,modelisY.nobraukums)

Skolas_buss = Buss("Mersedess",140, 20)
print(Skolas_buss.sedvietu_skaits())
print(sedvietu_skaits.krasa, Skolas_buss.nosaukums,"Ātrums:", Skolas_buss.max_atrums, "Nobraukums:", Skolas_buss.nobraukums)

print(f'{"Sveiks/a!":^25s}')
print("Šī programma izdrukā vienkāršu rēkinu koka lādītēm ar gravējumu!\n\n\n")

kliens = input("Pasūtītāja vārds uzvārds:")
print("-"*50)
veltijums = input("Nepieciešamais veltījums:")
print("-"*50)
izmers = input("Lādites izmēri Garums,platums,augstums")
print("-"*50)
materials = input("Kokmateriāla cena EUR/2:")


class Rekins():

  def __init__ (self,kliens,veltijums,izmers, materials):

   self.kliens  = kliens 
   self.veltijums = veltijums
   self.izmers = izmers
   self.materials = int(materials)
   
   
   self.teksta_gar = len(self.veltijums)
 #print(Rekins)

   self.lad_iz = self.izmers.split(",")
   self.garums = int(self.lad_iz[0])
   self.platums = int(self.lad_iz[1])
   self.augstums = int(self.lad_iz[2])
   


  def izdruka(self):
 
   print(f'Klienta vrds:{self.kliens}')
   print(f'Klienta uzrakstItais veltIjums:{self.veltijums}')
   print(f'Klienta ievadītais izmers:{self.izmers}')
   print(f'Klienta ievadītais materiāls:{self.materials}')
   print("\n\n")
   print('\033[1m'+"Pasūtītāja dati:"+'\033[0m')
   print("-"*50)
   print(f"\x1B[3mPasūtītāja vārds un uzvārds:\x1B[0m \033[1;32mklients\033[1;0m")
   print(f"\x1B[3mVeltījuma teksts:\x1B[0m \033[1;32m{self.kliens}\033[1;0m")
   print(f"\x1B[3m Lādītes izmēri:\x1B[0m \033[1;32m{self.izmers}\033[1;0m")
   print(f"\x1B[3mGarums:\x1B[0m \033[1;32m{self.garums}\033[1;0m")
   print(f"\x1B[3mPlatums:\x1B[0m \033[1;32m{self.platums}\033[1;0m")
   print(f"\x1B[3mAugstums:\x1B[0m \033[1;32m{self.augstums}\033[1;0m")
   print(f"\x1B[3mMateriāla cena EUR/2:\x1B[0m \033[1;32m{self.materials}\033[1;0m")
   print(f"\x1B[3mIzmaksas:\x1B[0m \033[1;32m{self.aprekins()}\033[1;0m")


  


 
  def aprekins(self):
     darba_samaksa = 15
     PVN = 21
     produkta_cena = (self.teksta_gar)*1.2 +    (self.platums/100 * self.garums/100 * self.augstums/100)/ 3 *  self.materials
     PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
     rekina_summa = (produkta_cena + darba_samaksa) +  PVN_summa

     return rekina_summa


# kliens = input("Uzraksti savu vardu:")
# veltijums = input("Uzraksti veltjumu:")
# izmers = input("Ievadi ladites izmerus\n Garums,platums,augstums (raksti veselus skaits, atdalot tos ar komatiem\n")
# materials = input("materiala cena EUR/m2")

rekins = Rekins(kliens, veltijums,izmers,materials)
print(rekins.izdruka())
# print(rekins.kliens)
# print(rekins.veltijums)
# print(rekins.izmers)
# print(rekins.lad_iz)

# print(veltijums)
# print(type(veltijums))
# print(izmeri.split(","))
# sadal = izmeri.split(",")
# print(sadal[0])
# print(sadal[1])
# print(sadal[2])
# print(len(veltijums))



   

  

  


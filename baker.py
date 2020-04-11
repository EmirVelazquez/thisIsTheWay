from bakerClass import Baker
from masterBaker import MasterBaker

myBaker = Baker()

myBaker.make_pecan_pie()
myBaker.make_tres_leches_cake()
myBaker.make_special_treat()
print("````````````````````````````````````````````````````")
# Master baker inherits the functions from the Baker class
# Has access to Baker class functions as well
myMasterBaker = MasterBaker()
myMasterBaker.make_tiramisu()
myMasterBaker.make_special_treat()
myMasterBaker.make_pecan_pie()

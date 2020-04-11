# Using inheritance to import the same functions from the Baker class
from bakerClass import Baker


class MasterBaker(Baker):
    def make_special_treat(self):
        print("Baker makes his special cannoli")

    def make_tiramisu(self):
        print("Baker makes tiramisu")

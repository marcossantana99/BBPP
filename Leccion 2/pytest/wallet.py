class wallet():

    def __init__(self,cantidad = 0):
        self.saldo = cantidad
    
    def gastar_dinero(self,cantidad):
        if self.saldo < cantidad :
            raise Exception
        else:
            self.saldo -= cantidad
    
    def anadir_saldo(self,cantidad):
        self.saldo += cantidad
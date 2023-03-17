#====================== to calculate any calculations =============================
class calculate:
    #====================== to calculate percentage =============================
    def percent(gain,max):
        return(round((gain/max)*100,2))

    #====================== to calculate monthly fee =============================
    def feepayment(monthly,_from,_to):
        return(monthly*((_to - _from) +1)) 
    
    #====================== to calculate computer installment fee =============================
    def computer_installment(installment,number):
        return(installment*number)


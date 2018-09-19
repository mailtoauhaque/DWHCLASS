import VisaDS
import MedicalDS
import  Stockdata



class GenerateData():
    def __init__(self):
        self.name= 'Data Generator Class'


    def Generate(self, PiSeeds, Radn):

        Visa_data = VisaDS.VISA().VISA_GEN("3.145632156323698574521330214521025369878545214521022365221458896547854145210253698785452145210223652214588965452102536987854521452102236522145889654785414521025369878545214521022365221458896544521452102236522145889654785414521025369878545214521022365221458896545210253698785452145210223652214588965478541452102536987854521452102236522145889654")
        Medical_data = MedicalDS.MedicalTests().Data_Loader(Radn)
        Stock_data = Stockdata.DataFeed().Feed_Monthly()

        Master_Dict = {
            'Stock': Stock_data,
            'CreditCard': Visa_data,
            'Medical':Medical_data,
                }

        return Master_Dict



#Development Debbug

#print GenerateData().Generate(3, 5)
import random


class VISA():
    def __init__(self):
        self.name='VISA'


    education=['MS(CS)', 'BS(CS)', 'PhD', 'MS(SE)', 'MBA', 'BBA', 'MCS', 'BCS', 'EMBA', 'MSIF','MBBS', 'FCPS','Matric','F.Sc', 'B.Sc','Diploma'];
    worklocation=['Hongkon','Mumbai','Faisalabad','Multan','Peshawer','Naran','Sedny','Columbo','Karachi', 'Lahore', 'Islamabad', 'Quetta', 'Hyderabad', 'Dubai', 'Beijing', 'New York'];


    def Gen_CCN(self,data):
        B,A= data.split('.')
        CCN= '4' + A[95:99] + A[115:119] + A[180:183] + A[10:12] + A[49:51]
        return CCN

    def Gen_CCV(self,data):
        B, A = data.split('.')
        CCV = '7' + A[99] + A[119]
        return CCV

    def Gen_PIN(self,data):
        B, A = data.split('.')
        PIN = A[131] + A[99] + A[119] + A[181]
        return PIN

    def Gen_PAS(self,data):
        B, A = data.split('.')
        PAS = A[109:110] + A[61:63] + A[174:176] + A[181]
        return PAS

    def Gen_CEL(self,data):
        B, A = data.split('.')
        CEL = '00' + '923' + A[131] + A[99] + A[119] + A[181] + A[9] + A[41] + A[137:140]
        return CEL

    def Gen_SAL(self,data):
        B, A = data.split('.')
        SAL = A[131] + A[99] + A[119] + A[181] + A[9] + A[41]
        return SAL

    def Gen_EDU(self):
        EDU=self.education[random.randint(1,len(self.education)-1)]

        return EDU

    def Gen_LOC(self):
        LOC=self.worklocation[random.randint(1,len(self.worklocation)-1)]

        return LOC

    def VISA_GEN(self, pi_data):

        CCN=self.Gen_CCN(pi_data)
        CCV=self.Gen_CCV(pi_data)
        PIN=self.Gen_PIN(pi_data)
        PAS=self.Gen_PAS(pi_data)
        CEL=self.Gen_CEL(pi_data)
        SAL=self.Gen_SAL(pi_data)
        EDU=self.Gen_EDU()
        LOC=self.Gen_LOC()
        AGE=str(random.randint(18,75))
        Storable = {
            'CCN': CCN,
            'CCV': CCV,
            'PIN': PIN,
            'PAS': PAS,
            'CEL': CEL,
            'SAL': SAL,
            'LOC': LOC,
            'EDU': EDU,
            'AGE':AGE

        }
        return Storable


from logging import DEBUG, basicConfig, debug, info, warning, error, critical
basicConfig(level=DEBUG,
            filename='lesson8log.log',
            filemode='a',
            format="We have next loggin massage: %(asctime)s : %(levelname)s - %(message)s")
def IntSum(a, b):
    strDigit1 = str(a)
    strDigit2 = str(b)
    return int(a + b)
'''
if(IntSum(5, 7.2) == 12):
    print("True")
else:
    print("False")
'''
try:
    digit1 = input(Enter)
    assery IntSum(5.8, 7.25) == 12
except AssertionError as ae:
    error(ae)

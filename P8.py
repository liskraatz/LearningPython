# property tax program calculator 2
def getinput(msg):
    xin = float(input(msg))
    return xin

def main(a,e, b,c):
    print('\n'*a)
    AssessmentLevel = .10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45
    PropertyValue = float(input('Enter value of property: '))
    LocalTaxRate = float(input('Enter loacal tax rate: '))
# %%
    LocalTaxRate = LocalTaxRate/100

    StateEqualizer = float(input('Enter state equalizer: '))
    print('\n'*e)
    AssessedValue= PropertyValue * AssessmentLevel
    EqualizeValue = AssessedValue * StateEqualizer
    PropertyTaxBefore = EqualizeValue * LocalTaxRate
    TotalPropertyTax = PropertyTaxBefore - HomeOwnerEx - SeniorCEX
    print('\n'*b)
    print(' Property tax due: ',TotalPropertyTax)
    print('\n'*c)
    return
main(2, 2, 2, 3)

print("-------------------------Mather-------------------------")

for lists in ['1. Pythagorean Triplet', '2. Find Quadrilateral']:
    print(lists)

mainInput = input("Enter number or text to do math: ")
if mainInput == '1' or mainInput == 'Pythagorean Triplet' or mainInput == 'pythagorean triplet' or mainInput == 'Pythagorean triplet':
    for i in range(1, 100):
        def main(gettingNumberFromUser):
            # The main formula for getting the third formula {2m}
            formula_3 = gettingNumberFromUser // 2

            # This code will find the triplet
            underLineFormula_1 = formula_3 * 2
            underLineFormula_2 = formula_3 ** 2 - 1
            underLineFormula_3 = formula_3 ** 2 + 1
            print(underLineFormula_1, end=', ')
            print(underLineFormula_2, end=', ')
            print(underLineFormula_3)

            # this suite accesses the math steps
            showProcedure = input('Enter "show procedure" to show the steps: ')
            if showProcedure == 'show procedure':
                print(f'''
                 m2 - 1 = {gettingNumberFromUser}, m2 = {gettingNumberFromUser} + 1 => m2 = {gettingNumberFromUser + 1}                                             
                 m2 + 1 = {gettingNumberFromUser}, m2 = {gettingNumberFromUser} - 1 => m2 = {gettingNumberFromUser - 1}
                 2m = {gettingNumberFromUser}, m = {gettingNumberFromUser}/2 = {gettingNumberFromUser // 2} => m = {gettingNumberFromUser // 2} 

                 2m = 2*{formula_3} = {formula_3 * 2}
                 m2 - 1 => {formula_3}Sq - 1 =. {formula_3 ** 2} - 1 => {formula_3 ** 2 - 1}
                 m2 + 1 => {formula_3}Sq + 1 =. {formula_3 ** 2} + 1 => {formula_3 ** 2 + 1}
                \n Hence the Pythagorean Triplet of {gettingNumberFromUser} = {underLineFormula_1}, {underLineFormula_2}, {underLineFormula_3}''')


        # Getting user's input
        gettingNumberFromUser = int(input('Enter a number to find the Pythagorean Triplet: '))
        main(gettingNumberFromUser)
        print('----------------------------------------------------------')



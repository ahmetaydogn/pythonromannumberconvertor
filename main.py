def main():
    print("Roma Sayısını, Dijital Sayıya dönüştüren uygulamaya hoşgeldiniz!")

    # Variables
    romanNumbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    exceptionRomanNumbers = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
        'MV': 4000
    }
    digitalTotal = 0

    # Inputs
    romanNumber = input("Lütfen dönüştürmek istediğiniz roma sayısını giriniz. (1-4999 arasında): ")
    listOfNumber = list(romanNumber)
    for number in listOfNumber:
        if number in romanNumbers:
            continue
        else:
            print("Böyle bir Roma Sayısı yok.")
            return

    # Read Exception Roman Numbers
    for exceptionRomanNumber in exceptionRomanNumbers.keys():
        if exceptionRomanNumber in romanNumber:
            romanNumber = romanNumber.replace(exceptionRomanNumber, "")
            digitalTotal += exceptionRomanNumbers.get(exceptionRomanNumber)

    # Convert To List
    listOfNumber = list(romanNumber)

    for i in range(len(listOfNumber)):
        if i == len(listOfNumber) - 1:
            break
        if int(romanNumbers.get(listOfNumber[i])) < int(romanNumbers.get(listOfNumber[i + 1])):
            print("Böyle bir Roma Sayısı yok.")
            return

    # Read Other Numbers
    for number in listOfNumber:
        digitalTotal += romanNumbers.get(number)
    print(digitalTotal)


if __name__ == '__main__':
    main()

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    '''
    number = str(number)
    numdigits = (len(number))
    if numdigits == 1:
        return trans[number]
    if numdigits == 2 and int(number) < 20:
        return trans['10'] + " " + trans[number[1]]
    if numdigits == 2 and number[1] != '0':
        return trans[number[0]] + " " + trans['10'] + " " + trans[number[1]]
    if numdigits == 2:
        return trans[number[0]] + " " + trans['10']
    if numdigits == 3 and number[1] == '0' and number[2] == '0':
        return trans[number[0]] + " " + trans['100']
    if numdigits == 3 and number[1] == "0":
        return trans[number[0]] + " " + trans['100'] + " " + trans[number[1]] + " " + trans[number[2]]
    if numdigits == 3 and number[2] != "0":
        return trans[number[0]] + " " + trans['100'] + " " + trans[number[1]] + " " + trans["10"] + " " + trans[number[2]]
    if numdigits == 3:
        return trans[number[0]] + " " + trans['100'] + " " + trans[number[1]] + " " + trans["10"]
        
# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()

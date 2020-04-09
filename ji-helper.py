###############
# --- TODO ---#
###############

# [x] simplify/minimize a fraction, making it easier to read

# [x] force a ratio into an octave

# [x] multiply two or more ratios, make it easy to read

# [] divide two or more ratios, make it easy to read

# [x] give common names for the ratios

# [] supply a name, get suggestions for ratios in different limits

# [] power of an interval, i.e pow 3/2 4 equals 81/64

# [] generate a scale in some way

# [] implement a way to chose what processes to do, i.e -m -f is to
#    both minimize and force, -p -m is to both multiply and print

from math import gcd
import math
import sys
import argparse

intervalnames = [
    'prime',
    'three quarter-flat second',
    'minor second',
    'neutral second',
    'major second',
    'quarter-sharp second',
    'minor third',
    'neutral third',
    'major third',
    'quarter-sharp major third',
    'fourth',
    'quarter-sharp fourth',
    'tritone',
    'quarter-flat fifth',
    'perfect fifth',
    'quarter-sharp fifth',
    'minor sixth',
    'neutral sixth',
    'major sixth',
    'three-quarter flat seventh (almost septimal)',
    'minor seventh',
    'neutral seventh',
    'major seventh',
    'quarter-flat octave'
]

def ratiomidi(ratio):
    return round(24 * math.log2(ratio)) / 2

def ratio_to_list(ratiostring):
    return ratiostring.split('/')

# main class
class Ratio:
    def __init__(self, num, den):
        self.num = int(num)
        self.den = int(den)
        self.value = self.num / self.den
        return None

    def printratio(self):
        print_msg = str(self.num) + "/" + str(self.den)
        return print_msg

    def minfrac(self):
        divisor = gcd(self.num, self.den)
        self.num = int(self.num / divisor)
        self.den = int(self.den / divisor)

        return None
    
    def forceoct(self):

        
        if self.num / self.den >= 2:
            self.den = int(self.den * 2)
            return self.forceoct()
        
        elif self.num / self.den < 1:
            self.num = int(self.num * 2)
            return self.forceoct()
        
        else:

            return None

    def multiply(self, ratio2):
        self.num = self.num * ratio2.num
        self.den = self.den * ratio2.den
        
        return None
    
    def divide(self, ratio2):
        num1, den1, num2, den2 = self.num, self.den, ratio2.num, ratio2.den
        if self.value < ratio2.value:
            
            self.num = num2 * den1

            self.den = den2 * num1


        else:
            self.num = num1 * den2
            self.den = den1 * num2
            
        return None
    
    def approx(self):

        quarternote = int(ratiomidi(self.value) * 2) % 24

        print_msg = str(self.num) + '/' + str(self.den)
        print_msg += " is approximately a "
        print_msg += intervalnames[quarternote]
        print_msg += "."
        
        return print(print_msg)

class RatioCollection:
    def __init__(self, ratios, ratioinput):
        self.ratios = list(ratios)
        self.ratioinput = list(ratioinput)
        
    def minfrac(self):
        print_msg = '\n V V V V V \n \n'
        print_msg += '- M I N I M I Z E -\n \n'
        IN = []
        OUT = []
        for i in range(0, len(self.ratios)):
            IN.append(self.ratios[i].printratio())
            self.ratios[i].minfrac()
            OUT.append(self.ratios[i].printratio())

        for i in range(0, len(IN)):
            print_msg += IN[i] + ' turns into ' + OUT[i] + '\n'

        return print_msg

    def forceoct(self):
        print_msg = '\n V V V V V \n \n'
        print_msg += '- F O R C E  O C T A V E - \n \n'
        IN = []
        OUT = []
        for i in range(0, len(self.ratios)):
            IN.append(self.ratios[i].printratio())
            self.ratios[i].forceoct()
            OUT.append(self.ratios[i].printratio())

        for i in range(0, len(IN)):
            print_msg += IN[i] + ' turns into ' + OUT[i] + '\n'

        return print_msg

    def multiply(self):
        print('\n V V V V V \n')
        print('- M U L T I P L Y -')
        for i in reversed(range(0, len(self.ratios) - 1)):
            self.ratios[i].multiply(self.ratios[i + 1])


        for i in reversed(range(0, len(self.ratios))):
            if i != len(self.ratios) - 1:
                self.ratios.pop(i)

        return self.ratios

    def divide(self):
        if len(self.ratios) < 2:
            print('Not enough ratios!')
        else:
            print('\n V V V V V \n')
            print('- D I V I D E -')
            for i in range(0, len(self.ratios) - 1):
                self.ratios[i].divide(self.ratios[i + 1])

            self.ratios.pop(len(self.ratios)-1)

        return None

    def approx(self):
        for ratio in self.ratios:
            ratio.approx()

        
def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--function", "-f", help="decide what function to use")

    parser.add_argument(
        "--ratios", "-r", help="specify a number of ratios", nargs="+")

    args = parser.parse_args()
    
    if args.function:
        commands = list(args.function)
    
    if args.ratios:
        ratios = []
        for ratiostring in args.ratios:
            ratio_as_list = ratiostring.split('/')
            ratios.append(Ratio(ratio_as_list[0], ratio_as_list[1]))

    ratiocollection = RatioCollection(ratios, args.ratios)

    print('Your inputs:\n')
    print(ratiocollection.ratioinput)
    
    for command in commands:
        
        if command == 'm':
            print(ratiocollection.minfrac())

        elif command == 'f':
            print(ratiocollection.forceoct())

        elif command == 'M':
            ratiocollection.multiply()

            print(ratiocollection.ratios[0].printratio())
            print(len(ratiocollection.ratios))
            # print(ratiocollection.ratios[len(ratiocollection.ratios) - 1].printratio())

        elif command == 'D':
            ratiocollection.divide()

            for i in range(0, len(ratiocollection.ratioinput) - 1):
                print_msg = ratiocollection.ratioinput[i] + '---- \\ \n'
                print_msg += '\t' + ratiocollection.ratios[i].printratio() + '\n'
                print_msg += ratiocollection.ratioinput[i + 1] + '---- / \n'
                print_msg += '----------'

                print(print_msg)
            # for i in range(0, len(ratios) - 1):
            #     ratios[i].divide(ratios[i + 1])
            #     print(ratios[i].printratio())

        elif command == 'a':
            print('\n V V V V V \n')
            print('- A P P R O X I M A T E -\n')
            ratiocollection.approx()
            # print('----------')
            # for ratio in ratios:
            #     ratio.approx()
            #     print('----------')
            # for arg in arguments:
            #     argstr = arg.split('/')
            #     ratio = Ratio(argstr[0], argstr[1])
            #     ratio.approx()
            #     print('----------')
        else:
            print_str = 'Command not legible! \n \n'
            print_str += 'Accepted commands are: \n'
            print_str += '    m = Minimize the ratios \n'
            print_str += '    f = Force the ratios into an octave \n'
            print_str += '    M = Multiply the given ratios \n'
            print_str += '    D = Divide the given ratios (the ratios between the ratios) \n'
            print_str += '    a = Approximate the ratios'

            print(print_str)

    print('\n V V V V V \n')
    print('- R E S U L T -')
    
    
    print('Your inputs:')
    print(ratiocollection.ratioinput)
    print('\n')
    print('Your outputs:')
    ratio_output_list = []
    for i in range(0, len(ratiocollection.ratios)):
        ratio_output_list.append(ratiocollection.ratios[i].printratio())

    print(ratio_output_list)
    

    

if __name__ == "__main__":
    main()

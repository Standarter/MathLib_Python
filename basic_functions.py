import decimal
from decimal import Decimal
import settings
import re
import all_functions
class basic_functions:
    decimal_type = type(Decimal("0"))
    def __init__(self):
        all_functions.e = self.to_decimal_number("2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405462531520961836908887070167683964243781405927145635490613031072085103837505101157477041718986106873969655212671546889570350354")
        all_functions.pi = self.to_decimal_number("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989")
    def to_decimal_number(self, number, roundto=settings.default_function_round):
        number = str(number)
        number = str("{:." + str(roundto) + "f}").format(Decimal(number))
        if number.rfind(".") != -1:
            temp = number.split(".")
            temp[1] = temp[1] + "0"*(roundto-len(temp[1]))
            number = ".".join(temp)
        else:
            number += "." + "0"*roundto
        #print(number)
        return Decimal(number)
    def to_decimal_number_with_round(self, number, roundto=settings.default_function_round):
        number = str(number)
        number = str("{:." + str(roundto) + "f}").format(Decimal(number))
        if number.rfind(".") != -1:
            temp = number.split(".")
            temp[1] = temp[1] + "0"*(roundto-len(temp[1]))
            number = ".".join(temp)
        else:
            number += "." + "0"*roundto
        try:
            result = Decimal(number).quantize(Decimal("1." + "0"*roundto))
        except:
            #print(str(number))
            result = Decimal(number)
        #print(result)
        return result
    def to_split_array(self, formula, variables: dict):
        result = [""]
        result1 = []
        i = 0
        n = 0
        while i < len(formula):
            if formula[i] == "*":
                n += 2
                result.append("*")
                result.append("")
            elif formula[i] == "/":
                n += 2
                result.append("/")
                result.append("")
            elif formula[i] == "+":
                n += 2
                result.append("+")
                result.append("")
            elif formula[i] == "-":
                n += 2
                result.append("-")
                result.append("")
            elif formula[i] == "(":
                n += 2
                result.append("(")
                result.append("")
            elif formula[i] == ")":
                n += 2
                result.append(")")
                result.append("")
            elif formula[i] == "'":
                n += 2
                result.append("'")
                result.append("")
            elif formula[i] == '"':
                n += 2
                result.append('"')
                result.append("")
            elif formula[i] == ",":
                n += 2
                result.append(",")
                result.append("")
            else:
                result[n] += formula[i]
            i += 1
        for element in result:
            if element in variables.keys():
                result1.append(str(variables[element]))
            else:
                result1.append(element)
        result1 = self.delete_blank(result1)
        #print(result1)
        return result1
    def delete_blank(self, array):
        result = []
        for element in array:
            if element != "":
                result.append(element)
        return result
    def array_transform(self, array):
        result = []
        for element in array:
            if self.is_Number(element):
                element = "Decimal('{0}')".format(element)
                result.append(element)
            else:
                result.append(element)
        #print(result)
        return "".join(result)
    def is_Number(self, number):
        result = re.findall("[0-9]{1,}[.]{0,1}[0-9]{0,}", number)
        #print(result)
        result = self.delete_blank(result)
        #print(result)
        if len(result) >= 1:
            return True
        else:
            return False
    def default_function(self, formula, variables: dict, roundto=settings.default_function_round):
        #####################################
        sin = all_functions.sin
        cos = all_functions.cos
        factorial = all_functions.factorial
        #####################################
        formula = self.to_split_array(formula, variables=variables)
        formula = self.array_transform(formula)
        #print(formula)
        return self.to_decimal_number_with_round(eval(formula), roundto=roundto)
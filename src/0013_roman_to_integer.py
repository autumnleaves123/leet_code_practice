class Solution:
    def romanToInt(self, s: str) -> int:

        # Completed 3/21/2023

        roman = {} # create hashmap with roman number definitions
        roman["I"] = 1
        roman["IV"] = 4
        roman["V"] = 5
        roman["IX"] = 9
        roman["X"] = 10
        roman["XL"] = 40
        roman["L"] = 50
        roman["XC"] = 90
        roman["C"] = 100
        roman["CD"] = 400
        roman["D"] = 500
        roman["CM"] = 900
        roman["M"] = 1000

        val = 0
        parse = s
        while len(parse) > 0:
            last_letter = parse[-1]
            try:
                last_two_letters = parse[-2:]
                if last_two_letters in roman:
                    val += roman[last_two_letters]
                    parse = parse[0:-2]
                else:
                    val += roman[last_letter]
                    parse = parse[:-1]
            except:
                val += roman[last_letter]
                parse = parse[:-1]
        return val


            

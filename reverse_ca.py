import itertools

# Returns a single value based on the 3 bit lookup
def lookup_126(val:str) ->str:
    if len(val) != 3:
        print("You needed to have 3 values only for lookups")
        exit()
    
    lookup = {
        "111": "0",
        "110": "1",
        "101": "1",
        "100": "1",
        "011": "1",
        "010": "1",
        "001": "1",
        "000": "0"
    }
    return lookup[val]

# Finds the rule 126 response regardless of length 
def find_126(s:str) -> str:
    s_len = len(s)
    bin_len = s_len * 4
    bin_s = int(s,16)
    bin_s = format(bin_s, "0%db" % bin_len)
    bin_s = bin_s[-1] + bin_s + bin_s[1]
    counter = 0
    final = ''
    while counter <= bin_len-1:
        check = bin_s[counter] + bin_s[counter+1] + bin_s[counter+2]
        final += lookup_126(check)
        counter += 1

    return format(int(final,2),'0%dx' % s_len)

# Brute force possible values for the key. Iterates every combination for (255,255) and if the second half matches the check position, it's a possible option.
def compare_126(s:str) -> list:
    vari = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
    final = []
    for i in itertools.product(vari,vari):
        test = ''.join(i)
        check = find_126(test)
        if check[2:] == s:
            final.append(test[2:])
        
    return final
   
# First, find possible hex digits in key. Second, create string with those digits and output only those which rule_126(string) -> the goal.
def try_126(goal:str)-> list:
    ultimate = []
    result = ''
    
    # Finding possible options for the key
    for i in range(0,len(goal),2):
        each = compare_126(goal[i]+goal[i+1])
        ultimate.append(list(set(each)))    

    # Placing those options in a string and checking against the goal
    for i in itertools.product(*ultimate):
        test = ''.join(i)
        result = find_126(test)
        if result == goal:
            print(test)



def main():
    goal = "66de3c1bf87fdfcf"
    try_126(goal)




main()
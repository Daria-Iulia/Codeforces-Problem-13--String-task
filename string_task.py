inp = input().strip()
def vow(inp):
    vowels = "AaOoYyEeUuIi"
    result=""
    for i in inp:
        if i not in vowels:
            low= i.lower()
            result += "." + low
    return result


output= vow(inp)

print(output)




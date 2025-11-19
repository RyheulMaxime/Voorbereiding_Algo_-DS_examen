def isPalindroom(s):
    # Basisgevallen: lege string of lengte 1
    if len(s) <= 1:
        return True
    # Als eerste en laatste karakter niet gelijk zijn, is het geen palindroom
    if s[0] != s[-1]:
        return False
    # Recursief controleren van de substring zonder eerste en laatste karakter
    return isPalindroom(s[1:-1])
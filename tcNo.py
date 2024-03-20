def tcKimlikDogrulama(tc):
    if len(tc) != 11 or not tc.isdigit() or tc[0] == '0':
        return False
    
    odd_sum = sum(map(int, tc[0:9:2]))
    
    even_sum = sum(map(int, tc[1:9:2]))
    result = ((odd_sum * 7) - even_sum) % 10

    if result != int(tc[9]):
        return False
    
    total = sum(map(int, tc[:10]))
    if total % 10 != int(tc[10]):
        return False
    
    return True

while True:
    tc = input("Lütfen T.C. kimlik numaranızı giriniz: ")
    
    if tcKimlikDogrulama(tc):
        print("Girilen T.C. kimlik numarası doğru.")
        break
    else:
        print("Girilen T.C. kimlik numarası yanlış. Lütfen tekrar deneyin.")

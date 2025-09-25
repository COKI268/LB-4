
print("Введите три целых числа через пробел:")
a, b, c = map(int, input().split())

result_mult_ab = a * b  
result_mult_bc = b * c  
result_mult_ca = c * a  

result_pow_a = a ** 4    
result_mod_bc = b % c    
result_div_ca = c // a   

print("\n" + "="*60)
print("РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ЗАДАНИЯ")
print("="*60)

print("\nПункт 2: Результаты умножения")
print("a * b = ", result_mult_ab)
print("b * c = ", result_mult_bc)
print("c * a = ", result_mult_ca)

print("\nПункт 4: Дополнительные операции")
print("a ** 4 = ", result_pow_a)
print("b % c = ", result_mod_bc)
print("c // a = ", result_div_ca)

print("\nПункт 6: Сумма переменных из пункта 5")
sum_p5 = result_pow_a + result_mod_bc + result_div_ca
print("result_pow_a + result_mod_bc + result_div_ca = ", sum_p5)


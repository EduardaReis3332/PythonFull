# Receba uma temperatura em farenheit e exiba a conversão para celsius.

fh = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (fh - 32) * 5/9

print(f'A temperatura {fh}°F corresponde a {celsius:.2f}°C.')
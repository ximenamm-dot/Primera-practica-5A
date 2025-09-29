print("=== CALCULADORA DE SUEÑO Y ESTUDIO - 5TO GRADO ===")
print()

# Datos recomendados para 5to grado (10-11 años)
horas_sueno_recomendadas = 9.5
horas_estudio_recomendadas = 2

nombre = input("¿Cuál es tu nombre?")
print(f"\nHola {nombre}! Eres estudiante de 5to grado")

# Calcular sueño
hora_de despertar = int (input("¿A que hora te despiertas? (formato 24h, ej: 7 ): "))
hora_dormir = hora_despertar - horas_sueño_recomendadas

if hora_dormir < 0:
    hora_dormir+=24
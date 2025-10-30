def converter_idade_em_dias(dias_totais):

    DIAS_NO_ANO = 365 
    DIAS_NO_MES = 30

    anos = dias_totais // DIAS_NO_ANO
    dias_restantes_apos_anos = dias_totais % DIAS_NO_ANO
    meses = dias_restantes_apos_anos // DIAS_NO_MES
    dias_restantes_apos_meses = dias_restantes_apos_anos % DIAS_NO_MES
    dias_finais = dias_restantes_apos_meses
    return anos, meses, dias_finais
if __name__ == "__main__":
    print("--- Conversor de Idade (Dias para Anos, Meses, Dias) ---")
    while True:
        try:
            entrada = input("Digite a idade da pessoa expressa em dias: ")
            dias_totais = int(entrada)
            if dias_totais < 0:
                print("Por favor, digite um valor não negativo para os dias.")
                continue
            break
        except ValueError:
            print(" Entrada inválida. Por favor, digite um número inteiro.")
    anos, meses, dias_finais = converter_idade_em_dias(dias_totais)
    print(f"Idade total em dias: {dias_totais}")
    print("Resultado da Conversão:")
    print(f" {anos} anos, {meses} meses e {dias_finais} dias.")

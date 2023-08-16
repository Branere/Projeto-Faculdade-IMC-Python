# MENSAGEM INTRODUTÓRIA

#SOLICITAÇÃO DO NOME
def solicitar_nome():
    print("Olá, Eu sou o Guilherme e hoje verificaremos o seu IMC \nAntes de começarmos, como você se chama?")
    nome = input("Diga-me o seu Nome: ")
    print(f"Belo nome! Muito bem {nome}, agora vamos medir o seu IMC e ver como você está!")
    return nome

#COLETA E CONVERSÃO DE DADOS PARA O CALCULO
def calcular_imc():
    Altura_str = input("Sua altura em Metros: ")
    Altura = float(Altura_str.replace(',', '.'))   
    Peso_str = input("Seu Peso: ")
    Peso = float(Peso_str.replace(',', '.'))         
#CALCULO DO IMC
    imc = Peso / (Altura ** 2)
    imc_arrendondado = round(imc, 2)
    return imc_arrendondado

#VARIAÇÕES DE RESULTADOS
def determinar_variacao(imc, nome):
    
    if imc < 18.5:
        variacao = f" Poxa {nome}, Você está abaixo do peso ideal."
        recomendacao = "Segundo a tabela o seu Resultado foi MAGREZA, bora comer mais para melhorar esse IMC!"
    elif 18.5 <= imc < 24.9:
        variacao = f"Parabéns {nome}! Seu IMC está ideal!"
        recomendacao = "Segundo a tabela o seu Resultado foi PESO IDEAL. Continue assim e não se esqueça de sempre comer coisas saudáveis e praticar exercícios!"
    elif 25 <= imc < 29.9:
        variacao = f"Você está quase {nome}! Seu IMC está um pouco acima do Ideal, que seria 24,9!"
        recomendacao = "Segundo a tabela o seu Resultado foi SOBREPESO. Evite ficar sem comer por muito tempo, e procure sempre alimentos saudáveis e praticar alguns exercícios para melhor seu IMC!"
    elif 30 <= imc < 34.9:
        variacao = f"{nome} Seu IMC precisa de atenção, na Tabela o seu IMC ficou como OBESIDADE GRAU I."
        recomendacao = "Este é o momento ideal para você mudar esta situação, procure fazer refeições saudáveis e em menor quantidade a cada 3 horas, e fazer algumas caminhadas durante a semana para fazer esse IMC melhorar!"
    elif 35 <= imc < 39.9:
        variacao = f"{nome}, Você fez muito bem em medir seu IMC, atualmente você está com Obesidade Grau II e precisa de atenção."
        recomendacao = "Sua saúde pode estar em risco, Inicialmente recomendamos que você coma a cada 3 horas coisas saudáveis e diminua a quantidade de cada refeição, e pratique algumas caminhadas durante a semana, recomendamos também que procure um especialista para um acompanhamento da sua saúde."
    else:
        variacao = f"{nome} Você fez muito bem em medir seu IMC, isso significa que quer mudar de vida, atualmente o seu IMC é considerado Obesidade Grau III"
        recomendacao = "Isso significa que primeiramente você precisa procurar um médico para verificar sua saúde, em seguida um nutricionista para melhorar sua alimentação e seu dia a dia, para que na próxima vez, tenha um IMC melhor!"
    
    return variacao, recomendacao

# ORDEM DE CHAMADAS
def main():
    nome = solicitar_nome()
    imc_calculado = calcular_imc()
    variacao, recomendacao = determinar_variacao(imc_calculado, nome)
    
    print(f"Vamos lá {nome}! Seu IMC é:")
    print(imc_calculado)
    print(variacao)
    print(recomendacao)

# FUNÇÃO PRINCIPAL
main()
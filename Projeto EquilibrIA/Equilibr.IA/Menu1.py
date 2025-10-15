usuarios = {}

while True:
    print("BEM-VINDO AO Equilibr.IA")
    print("=========================")
    print("1. Cadastrar Novo Usuário")
    print("2. Acessar Dados e Recomendações")
    print("3. Excluir Usuário")
    print("0. Sair do Programa")
    
    escolha = input("Qual função deseja acessar? ")

    if escolha == '1':
        print(" CADASTRO ")
        
        while True:
            username = input("Crie um nome de usuário:").strip()
            if not username:
                print("O nome de usuário não pode ser vazio.")
            elif username in usuarios:
                print("Este nome de usuário já existe. Tente outro.")
            else:
                break
        
        password = input("Crie uma senha:").strip()
        nome_completo = input("Digite seu nome completo:").strip()
        
        while True:
            sexo = input("Sexo (M/F):").strip().upper()
            if sexo == 'M' or sexo == 'F':
                break
            else:
                print("Entrada inválida. Digite 'M' ou 'F'.")
        
        while True:
            idade_str = input("Idade (anos): ").strip()
            if idade_str.isdigit():
                idade = int(idade_str)
                if 10 < idade < 120:
                    break
                else:
                    print("Idade deve ser um número entre 10 e 120.")
            else:
                print("Por favor, digite um número para a idade.")

        while True:
            peso_str = input("Peso em kg (ex: 75.5): ").strip()
            try:
                peso = float(peso_str)
                if peso > 0:
                    break
                else:
                    print("O peso deve ser maior que zero.")
            except ValueError:
                print("Por favor, digite um número válido para o peso.")
        
        while True:
            altura_str = input("Altura em metros (ex: 1.75): ").strip()
            try:
                altura = float(altura_str)
                if 0.5 < altura < 3.0:
                    break
                else:
                    print("A altura deve estar entre 0.5 e 3.0 metros.")
            except ValueError:
                print("Por favor, digite um número válido para a altura.")
        
        usuarios[username] = {
            'senha': password,
            'nome': nome_completo,
            'sexo': sexo,
            'idade': idade,
            'peso': peso,
            'altura': altura
        }
        print(f"Usuário {username} cadastrado com sucesso!")

    elif escolha == '2':
        print(" ACESSAR CONTA ")
        username = input("Digite o nome de usuário: ").strip()
        password = input("Digite a senha: ").strip()

        if username in usuarios and usuarios[username]['senha'] == password:
            user_data = usuarios[username]
            print(f"Acesso liberado! Bem-vindo(a), {user_data['nome']}!")
            
            peso = user_data['peso']
            altura = user_data['altura']
            sexo = user_data['sexo']
            idade = user_data['idade']
            
            imc = peso / (altura * altura)
            
            altura_cm = altura * 100
            if sexo == 'M':
                tmb = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
            else: 
                tmb = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
            
            print(" SEUS RESULTADOS ")
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Sua Taxa Metabólica Basal (TMB) é: {tmb:.0f} kcal por dia.")

            print(" RECOMENDAÇÕES ")
            if imc >= 30.0:
                print(" Alerta: Seu IMC indica Obesidade. Busque ajuda profissional.")
            elif imc >= 25.0:
                print(" Aviso: Seu IMC indica Sobrepeso. Atenção ao estilo de vida.")
            elif imc < 18.5:
                print(" Aviso: Seu IMC indica Abaixo do Peso. Atenção à nutrição.")
            else:
                print(" Parabéns! Seu IMC está na faixa Normal (Bem-Estar).")

            print("Para uma recomendação de dieta e treino, escolha seu objetivo:")
            print("1. Ganhar massa")
            print("2. Secar (perder gordura)")
            objetivo = input("Escolha 1 ou 2: ")
            
            if objetivo == '1':
                print(" > Foco em dietas com mais calorias e treinos de força.")
            elif objetivo == '2':
                print(" > Foco em dietas com menos calorias e treinos com mais cardio.")
            else:
                print(" > Escolha um objetivo para receber uma dica.")

        else:
            print(" Usuário ou senha incorretos.")

    elif escolha == '3':
        print(" EXCLUIR PERFIL ")
        username = input("Digite o nome de usuário que deseja excluir: ").strip()
        
        if username in usuarios:
            password = input("Confirme a senha para excluir: ").strip()
            if usuarios[username]['senha'] == password:
                del usuarios[username]
                print(f" Perfil de {username} excluído com sucesso.")
            else:
                print(" Senha incorreta. Exclusão cancelada.")
        else:
            print(" Usuário não encontrado.")

    elif escolha == '0':
        print("Obrigado por usar o Equilibr.IA! Saindo...")
        break

    else:
        print(" Opção inválida. Por favor, tente novamente.")



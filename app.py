
import os

restaurantes = restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                            {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                            {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nm_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcao():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')
    
def voltar_ao_menu_princpal():
    exibir_subtitulo(input('\nDigite uma tecla para voltar ao menu principal '))
    
def opcao_invalida():
    print('opcao invalida!')
    voltar_ao_menu_princpal()
    
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nm_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nm_restaurante}:')
    dados_restaurante = {'nome': nm_restaurante,
                         'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante{nm_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_princpal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes: ')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        voltar_ao_menu_princpal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nm_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nm_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nm_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativo com sucesso'
        print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
        voltar_ao_menu_princpal() 
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Ecolha um opção:'))
        #   print(f'Você escolheu a opção{opcao_escolhida}') 
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
         opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nm_programa()
    exibir_opcao()
    escolher_opcao()
    
if __name__ == '__main__':
    main()


import os
import time

restaurantes = ['Xis Patrola', 'Xis do Gringo']

def exibir_nome_do_programa():
    nome_do_programa = '''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
'''
    print(nome_do_programa)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    time_to_finish = 5
    print(f'\nEncerrando o programa, aguarde {time_to_finish} segundos.')

    time.sleep(time_to_finish)
    os.system('cls')

def voltar_ao_menu_principal():
    input('\nPressione ENTER para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi adicionado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
import hashlib
import sys

def criar_hash():
	nome_arquivo = input("\nInforme o nome do arquivo: ")
	ler_arquivo = open(nome_arquivo, 'rb').read()
	hash_md5 = hashlib.md5(ler_arquivo)
	global hash_arquivo 
	hash_arquivo = hash_md5.hexdigest()
	print("\nHash do arquivo: ", hash_arquivo)
	return hash_arquivo

criar_hash()

def verificar_integridade(hash_arquivo):
	hash_antigo = hash_arquivo
	hash_atual = criar_hash()
	if(hash_antigo == hash_atual):
		print("\nO arquivo está íntegro.")
	else: print("\nO conteúdo do arquivo foi modificado!")

def menu():
	opcao = input(
    "\nEsoclha uma opção:\n\n1 - Verificar a integridade do arquivo\n2 - Sair\n\n")

	if(opcao == "1"):
		verificar_integridade(hash_arquivo)
		menu()

	if(opcao == "2" or opcao != "1"):
		sys.exit()

menu()

#!/usr/bin/python3
from sys import argv as args
import os.path as path_file

lines_of_markdown = []

def transformaMarkdown(linhas_markdown: list):
	saida = str()

	for linha in linhas_markdown:
		# Tratamento
		linha = linha.replace('\n', '')
		if "#" in linha:
			linha = linha.replace("#", '').strip()
			print("*" + linha+"*")
			
		else:
			print(linha)

	pass

def main(args: list):
	if len(args) >= 1:
		# Inicia o codigo de arquivo
		if path_file.exists(args[0]):
			with open(f'{args[0]}', 'r') as file_markdown:
				lines_of_markdown = file_markdown.readlines()

			transformaMarkdown(lines_of_markdown)

			# print(whatsapp_text)
		else:
			print("Me da um arquivo que existe vei >:(")

	else:
		print("Lhe falta argumentos!")

	pass


if __name__ == '__main__':
	args = args[1:]
	main(args)

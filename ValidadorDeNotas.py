#Validador de notas v1.1 (BETA)
#Dev -> nickSc01
#USE COM MODERAÇÃO ! 

import time

def Status(approved):
	print('<✔️>', approved)

def Status2(disapproved):
	print('<❌>', disapproved)
	


print('=-=-=-' * 10)

NomeAluno = (input('Digite o nome do aluno >> '))

Nota1 = float(input('Nota 1 >> '))
Nota2 = float(input('Nota 2 >> '))
Nota3 = float(input('Nota 3 >> '))
MediaAluno = ( Nota1 + Nota2 + Nota3 ) / 3

if MediaAluno == MediaAluno >= 6:
	print('[ + ] PREPARANDO')
	time.sleep (3)
	print('[ ✔️ ]NOTA GERADA ')
	print('O(a) aluno {} Tem a média de {}, ele(a) está aprovado(a)! < ✔️ >'.format(NomeAluno, MediaAluno))
else:
	print('')
	


if MediaAluno == MediaAluno < 6:
	print('[ + ] PREPARANDO')
	time.sleep (3)
	print('[ ✔️ ]NOTA GERADA ')
	print(Status2)
	print('O(a) aluno {} Tem a média de {}, ele(a) está reprovado(a)! < ❌ >'.format(NomeAluno, MediaAluno))
else:
	print('')

Name = NomeAluno.upper()

print('DADOS >>')
print('{} , {}'.format(Name, MediaAluno))
from googletrans import Translator
import argparse


parser = argparse.ArgumentParser(description='Lista de parametros a ser utilizado:')
parser.add_argument('--origin', metavar='N', type=str,
                    help='Linguagem atual do texto', default='pt')
parser.add_argument('--text-translate', help='Texto a ser passado para o ingles',required=True)
parser.add_argument('--amorEterno', help='Informa a quantidade de amor eterno que a Nah tem pelo Jaum', default='infinito')
#parser.print_help()

args = parser.parse_args()


translator = Translator()
result = translator.translate(args.text_translate, src=args.origin, dest='en')
print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation)


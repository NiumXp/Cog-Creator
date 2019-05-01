from os import system, name, rename
from time import sleep
from re import search

def snake_case(value):
    return str(value).strip(" ").replace(" ", "_").lower()

def camel_case(value):
    return "".join(str(value).title().strip(" ").split(" "))

def clear():
    return system("cls" if name == "nt" else "clear")

def pause():
    print("""
 O terminal foi pausado, aperte qualquer tecla para continuar.
""")
    return system("pause > null" if name == "nt" else "read dummy")

def create_text_file():
    with open("config.txt", "w") as file:
        file.write("""
    COLOQUE OS VALORES ENTRE AS CHAVES, NÃO PULE LINHAS!!
    NÃO MODIFIQUE O QUE ESTÁ FORA DAS CHAVES!

file_name: {};
 - Nome do arquivo.
  - Exemplo: (ping)
  (Será passado para Snake_Case evitando espaços " ")

cog_name: {};
 - Nome da Cog/Classe ou Objeto.
  - Exemplo: (personagem)
  (Será passado para CamelCase, não se preocupe)

command_name: {};
 - Nome do comando.
  - Exemplo: (send question to)
  (Será passado para Snake_Case, não se preocupe)

bot_instance: {client};
 - Variavel que será usada dentro da Cog para chamar a instância do bot.
  - Exemplo: (bot instance)
  (Será passado para Snake_Case, não se preocupe)

modules: {};
 - Módulos para importar. 
  - Exemplo: {os, sys, random, math}
""")
        file.close()

def open_config_text_file():
    command = "start ./config.txt" if name == "nt" else "nano ./config.txt"
    try:
        system(command)
    except Exception as error:
        raise error.__class__.__name__(error)

print("""
 Hmmmm, temos um preguiçoso aqui também!
 Este script foi desenvolvido por Nium!!

 Github: https://github.com/Niump
 Discord: Nium#6672

 Quais sejam as dúvidas sobre este script me chame!
""")

pause(); clear()

print("""
 Antes de começar você precisa me seder algumas informações.
 Irei criar um arquivo de texto e você irá editar conforme quiser!

 > Criando arquivo de texto.""")
sleep(1)
try:
    create_text_file()
except Exception as error:
    print(f"  > Não foi possivel criar o arquivo de texto.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print("   > Arquivo de texto criado.")

print("\n > Abrindo arquivo de texto.")
sleep(1)
try:
    open_config_text_file()
except Exception as error:
    print(f"  > Não foi possivel abrir o arquivo de texto.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print("   > Arquivo de texto aberto.")

print("\n Após modificar o arquivo, volte aqui.")
sleep(1)
pause(); clear()
print("""
 Espero que você tenha modificado os valores.
 Vamos começar! Vou me preparar aqui!

 > Lendo arquivo.""")
sleep(1)
try:
    with open("./config.txt") as file:
        texto = "".join(file.readlines())
except Exception as error:
    print(f"  > Não foi possivel abrir ler o arquivo de texto.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print("  > Arquivo lido com sucesso.")

print("\n > Pegando nome do arquivo.")
sleep(1)
try:
    file_name = snake_case(search(r"file_name:.*{(.*)};", texto).groups()[0])
except Exception as error:
    print(f"  > Não foi possivel pegar o nome do arquivo.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print(f"  - Nome do arquivo: {file_name}")

print("\n > Pegando nome da cog/classe/objeto.")
sleep(1)
try:
    cog_name = camel_case(search(r"cog_name:.*{(.*)};", texto).groups()[0])
except Exception as error:
    print(f"  > Não foi possivel pegar o nome da cog/classe/objeto.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print(f"  - Nome da cog/classe/objeto: {cog_name}")

print("\n > Pegando nome do comando.")
sleep(1)
try:
    command_name = snake_case(search(r"command_name:.*{(.*)};", texto).groups()[0])
except Exception as error:
    print(f"  > Não foi possivel pegar o nome do comando.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print(f"  - Nome do comando: {command_name}")

print("\n > Pegando nome da variável do bot.")
sleep(1)
try:
    bot_var = snake_case(search(r"bot_instance:.*{(.*)};", texto).groups()[0])
except Exception as error:
    print(f"  > Não foi possivel pegar o nome da variável.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print(f"  - Nome da variável: {bot_var}")

print("\n > Pegando módulos.")
sleep(1)
try:
    modules = search(r"modules:.*{(.*)};", texto).groups()[0].split(",")
    modules = [x.strip() for x in modules]
except Exception as error:
    print(f"  > Não foi possivel pegar os módulos.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print(f"  - Módulos: {modules}")

pause(); clear()

print("""
 Parece que eu tenho todas as informações que você escreveu no arquivo de texto.
 Vamos terminar isso logo! Espere um pouquinho que eu já vou terminar!

 > Gerando arquivo.""")

if len(modules) == 1 and modules[0] == "":
    imports = "from discord.ext.commands import command, Cog"
else:
    imports = "from discord.ext.commands import command, Cog\n" + "\n".join([f"import {module}" for module in modules])

try:
    with open(file_name + ".txt", "w") as file:
        file.write(f"""{imports}


class {cog_name}(Cog):
    def __init__(self, bot_instance):
        self.{bot_var} = bot_instance

    @command()
    async def {command_name}(self, ctx, *args):
        pass

def setup(bot_instance):
    bot_instance.add_cog({cog_name}(bot_instance))
""")
    rename(file_name+ ".txt", file_name + ".py")

except Exception as error:
    print(f"  > Não foi possivel gerar o arquivo.\n   - {error.__class__.__name__}: {error}")
    pause(); exit()
else:
    print("  - Arquivo gerado e pronto para editar!")
pause()

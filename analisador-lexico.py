"""
Analisador Léxico - Explicação Geral
Um analisador léxico, ou scanner, é um componente essencial de um compilador. Ele é responsável 
por converter o código-fonte escrito em linguagem humana (texto) em uma sequência de tokens, 
que são as menores unidades significativas do programa (como palavras reservadas, identificadores, 
números, símbolos, etc.). Esses tokens são posteriormente utilizados por outros estágios do compilador, 
como o analisador sintático e o analisador semântico.

Este analisador léxico utiliza expressões regulares para identificar e categorizar os tokens 
em diferentes tipos, como inteiros, números de ponto flutuante, identificadores, palavras-chave, 
strings e símbolos. Ele processa uma entrada de texto e retorna uma lista de tokens identificados 
e suas respectivas categorias.
"""

import re  # Importa o módulo de expressões regulares para identificar padrões nos tokens

def lexical_analyzer():
    """
    Função principal do analisador léxico.
    Define os padrões de tokens, lê o texto de entrada, identifica os tokens e retorna o resultado formatado.
    """

    # 1. Definir os padrões de tokens usando expressões regulares
    # Cada chave representa uma categoria, e o valor é o padrão regex correspondente.
    token_patterns = {
        'int': r'\b\d+\b',  # Números inteiros (ex: 123, 456)
        'float': r'\b\d+\.\d+\b',  # Números de ponto flutuante (ex: 123.45, 0.98)
        'identifier': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',  # Identificadores (ex: var1, nome_variavel)
        'keyword': r'\b(if|else|while|for|return|int|float|string|void)\b',  # Palavras-chave reservadas
        'string': r'"[^"]*"',  # Strings entre aspas (ex: "Olá mundo")
        'symbol': r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]',  # Símbolos especiais (ex: +, -, *, /, etc.)
    }

    # 2. Ler a entrada do usuário
    # Solicita ao usuário que insira o texto a ser analisado.
    input_text = input("Digite o texto a ser analisado (ou 'sair' para encerrar):\n")

    # Verifica se o usuário deseja sair
    if input_text.lower() == 'sair':
        return "Encerrando a análise léxica."

    # 3. Inicializar uma lista para armazenar os tokens identificados
    tokens = []

    # 4. Processar cada linha do texto de entrada
    # Divide o texto em linhas e analisa cada uma delas.
    for line in input_text.split('\n'):
        for token_type, pattern in token_patterns.items():
            # Encontra todas as correspondências para o padrão atual na linha
            matches = re.findall(pattern, line)
            for match in matches:
                # Adiciona cada correspondência como um token na lista
                tokens.append({
                    'Token': match,
                    'Categoria': token_type
                })

    # 5. Formatar a saída dos tokens encontrados
    # Cria uma string com os tokens formatados para exibição.
    output = ''
    for token in tokens:
        output += f"<Token: '{token['Token']}', Categoria: {token['Categoria']}>\n"

    # Retorna a lista de tokens encontrados
    return output

# Loop principal para executar o analisador léxico continuamente
# Permite que o usuário insira múltiplos textos para análise até decidir encerrar.
while True:
    result = lexical_analyzer()  # Chama o analisador léxico
    print(result)  # Exibe os tokens identificados
    if result.startswith("Encerrando"):  # Encerra o programa se o usuário desejar
        break
    print()

#Bruno Garcia de Oliveira Breda - 11212702
#Felipe Oliveira Carvalho - 14613879
#Gabriel Fernando Machado Fachini - 11953481
#Isabela Oliveira Costa - 10747972
#Vitor Antônio de Almeida Lacerda - 12544761
class Automato:
    def __init__(self, num_estados, simbolos, estados_aceitacao, transicoes):
        self.num_estados = num_estados
        self.simbolos = simbolos
        self.estados_aceitacao = estados_aceitacao
        self.transicoes = transicoes

    def aceita_cadeia(self, cadeia):
        estados_atuais = {0}
        for simbolo in cadeia:
            proximos_estados = set()
            for estado in estados_atuais:
                try:
                    proximos_estados.update(self.transicoes[estado][simbolo])
                except KeyError:
                    pass
            estados_atuais = proximos_estados
        return any(estado in self.estados_aceitacao for estado in estados_atuais)


def ler_automato(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        # Ler número de estados
        num_estados = int(arquivo.readline().strip())

        # Ler conjunto de símbolos terminais
        simbolos = arquivo.readline().strip().split()[1:]

        # Ler estados de aceitação
        estados_aceitacao = set(map(int, arquivo.readline().strip().split()[1:]))

        # Ler transições
        num_transicoes = int(arquivo.readline().strip())
        transicoes = [{} for _ in range(num_estados)]
        for _ in range(num_transicoes):
            origem, simbolo, destino = arquivo.readline().strip().split()
            origem, destino = int(origem), int(destino)
            if simbolo not in transicoes[origem]:
                transicoes[origem][simbolo] = set()
            transicoes[origem][simbolo].add(destino)

        # Ler número de cadeias de entrada
        num_cadeias = int(arquivo.readline().strip())
        cadeias = [arquivo.readline().strip() for _ in range(num_cadeias)]

    return Automato(num_estados, simbolos, estados_aceitacao, transicoes), cadeias


def main():
    nome_arquivo = input('Insira o nome do arquivo de entrada:')
    automato, cadeias = ler_automato(nome_arquivo)

    with open("saida.txt", 'w') as arquivo_saida:
        for cadeia in cadeias:
            resultado = "aceita" if automato.aceita_cadeia(cadeia) else "rejeita"
            arquivo_saida.write(f"{resultado}\n")


if __name__ == "__main__":
    main()

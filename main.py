import os
import re
import sys
import time

EXECUCOES = 30    # quantas execuções entram na estatística
AQUECIMENTO = 5   # execuções iniciais descartadas (aquecimento)


def ler_arquivo(caminho):
    """Lê todos os inteiros do arquivo e devolve uma lista (ou None se falhar)."""
    try:
        with open(caminho, "r", encoding="utf-8-sig") as f:
            texto = f.read()
    except OSError as e:
        print(f"Nao consegui abrir o arquivo: {e}", file=sys.stderr)
        return None

    # Pega qualquer inteiro no texto, independente do separador (espaço, vírgula, quebra de linha)
    return [int(x) for x in re.findall(r"-?\d+", texto)]


def busca_binaria(v, item, inicio, fim, crescente):
    """Encontra a posição onde 'item' deve ser inserido em v[inicio..fim]."""
    while inicio <= fim:
        meio = inicio + (fim - inicio) // 2

        # Em ordem crescente, itens maiores ou iguais vão para a direita;
        # em decrescente, a comparação é invertida.
        # O ">=" / "<=" (com igualdade) mantém a ordenação estável.
        va_para_direita = item >= v[meio] if crescente else item <= v[meio]

        if va_para_direita:
            inicio = meio + 1
        else:
            fim = meio - 1
    return inicio  # posição de inserção


def binary_insertion_sort(v, crescente):
    """Ordena a lista 'v' in-place usando Binary Insertion Sort."""
    for i in range(1, len(v)):
        chave = v[i]

        # A parte v[0..i-1] já está ordenada, então usamos busca binária
        # para achar onde a chave entra (O(log n) comparações)
        pos = busca_binaria(v, chave, 0, i - 1, crescente)

        # Equivalente ao memmove do C: desloca v[pos..i-1] uma posição para a direita
        # (o Python avalia o lado direito antes de atribuir, então não há problema de sobreposição)
        v[pos + 1:i + 1] = v[pos:i]

        v[pos] = chave


def esta_ordenado(v, crescente):
    """Confere se a lista está ordenada na direção pedida."""
    for i in range(len(v) - 1):
        if (v[i] > v[i + 1]) if crescente else (v[i] < v[i + 1]):
            return False
    return True


def medir(original, crescente):
    """Executa a ordenação várias vezes e imprime média, mínimo e máximo do tempo."""
    print(f"\n=== {'CRESCENTE' if crescente else 'DECRESCENTE'} ===")

    soma = 0.0
    minimo = 1e18
    maximo = 0.0
    vetor = []

    for k in range(AQUECIMENTO + EXECUCOES):
        # Sempre ordena uma cópia, para cada execução partir da lista original
        vetor = original.copy()

        # perf_counter é o relógio mais indicado para benchmarks em Python
        inicio = time.perf_counter()
        binary_insertion_sort(vetor, crescente)
        fim = time.perf_counter()

        tempo = (fim - inicio) * 1000.0  # converte para milissegundos

        # As execuções de aquecimento são ignoradas na estatística
        if k >= AQUECIMENTO:
            soma += tempo
            minimo = min(minimo, tempo)
            maximo = max(maximo, tempo)

    print(f"Primeiros 10: [{', '.join(map(str, vetor[:10]))}]")
    print(f"Ordenado corretamente: {'true' if esta_ordenado(vetor, crescente) else 'false'}")
    print(f"Tempo em {EXECUCOES} execucoes (ms) -> "
          f"media: {soma / EXECUCOES:.2f} | minimo: {minimo:.2f} | maximo: {maximo:.2f}")


def main():
    # Procura o arquivo na pasta do script (e não na pasta de onde o comando foi executado)
    pasta_do_script = os.path.dirname(os.path.abspath(__file__))
    caminho = sys.argv[1] if len(sys.argv) > 1 else os.path.join(pasta_do_script, "1000_numbers.txt")

    original = ler_arquivo(caminho)
    if not original:
        print(f"Erro ao ler o arquivo: {caminho}", file=sys.stderr)
        return 1
    print(f"Arquivo: {caminho} ({len(original)} numeros)")

    medir(original, True)   # ordem crescente
    medir(original, False)  # ordem decrescente
    return 0


if __name__ == "__main__":
    sys.exit(main())
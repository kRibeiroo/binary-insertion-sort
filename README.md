# Binary Insertion Sort

Implementação do **Binary Insertion Sort** com medição de tempo de execução, ordenando em ordem crescente e decrescente.

## Sobre o projeto

Projeto originalmente desenvolvido em **C** para a faculdade. Esta é a versão em **Python**, mantendo a mesma estrutura de funções e a mesma lógica do código original.

## Como funciona

- Lê uma lista de números inteiros de um arquivo de texto.
- Ordena a lista com Binary Insertion Sort (busca binária para achar a posição de inserção).
- Repete a ordenação várias vezes (`EXECUCOES = 30`, descartando `AQUECIMENTO = 5` execuções iniciais) e mostra o tempo **médio, mínimo e máximo** em milissegundos.
- Confere se o resultado ficou realmente ordenado.

## Como executar

Requer Python 3.

```bash
python main.py                    # lê 1000_numbers.txt (mesma pasta do script)
python main.py outro_arquivo.txt  # lê o arquivo informado
```

O arquivo deve conter números inteiros separados por espaço, vírgula ou quebra de linha.

## Exemplo de saída

```
Arquivo: 1000_numbers.txt (1000 numeros)

=== CRESCENTE ===
Primeiros 10: [...]
Ordenado corretamente: true
Tempo em 30 execucoes (ms) -> media: ... | minimo: ... | maximo: ...
```

## Observação

Os tempos em Python são bem maiores que os da versão em C, por causa do interpretador, então não são diretamente comparáveis.

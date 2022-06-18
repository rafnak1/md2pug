# Gobuster

## Descrição:

`gobuster` é um enumerador que utiliza ataques de dicionário e força bruta em URIs, subdomínios DNS e nomes de hosts virtuais em servidor web.

## Uso:

```gobuster [opções globais] <modo> [opções de modo]```

### Opções:

O `gobuster` tem três modos: `dns`, `dir` e `vhost`.

#### Globais:

- -t <threads>:
	define o número de threads usadas para rodar o programa
- -w/--wordlist <arquivo>:
	define qual wordlist usar

#### dir

- -u/--url <url>:
	define qual o alvo do ataque

#### Exemplos:

Escanear por um subdiretório em https://intheshell.page/ usando a wordlist `./wordlist.txt`

```gobuster dir -u https://intheshell.page/ --wordlist ./wordlist.txt```


# Aula 4: Introdução a Classes em Python

### Por que Classes

- Embora bibliotecas como Pandas (próxima aula) abstraiam muita complexidade, entender classes é fundamental para:

    - Organizar código de análise de dados de forma estruturada

    - Criar processamentos personalizados 

    - **Chave**  
        Entender como bibliotecas como Pandas e ML funcionam internamente

### Conceitos Básicos de Classes

- método `__init__` é o construtor. Roda ao criar um objeto
- `self.` referencia o próprio objeto. Padrão em toda classe. Acessa métodos internos
- **instância**, instanciar: objeto, criar objeto do tipo Classe


```python
class AnalisaDataset:
    """Classe básica para análise de datasets"""
    
    def __init__(self, nome_dataset):
        # Método construtor - inicializa o objeto
        self.nome = nome_dataset
        self.dados = None
        self.metricas = {}
    
    def carregar_dados(self, dados):
        """Carrega dados para análise"""
        self.dados = dados
        print(f"Dados carregados para {self.nome}")
    
    def calcular_media(self, coluna):
        """Calcula média de uma coluna"""
        if self.dados is not None:
            return sum(self.dados[coluna]) / len(self.dados[coluna])
        return None

# Uso prático
# 1. Cria uma instância. Um objeto do tipo AnalisaDataset
analisador = AnalisaDataset("Vendas 2024")
# 2. Usa o método carregar_dados que está embutido no objeto analisador que é uma instância da classe AnalisaDataset
analisador.carregar_dados({"produtos": [100, 150, 200], "precos": [29.90, 49.90, 79.90]})
# 3. Usa outro método
media_precos = analisador.calcular_media("precos")
```

## Exemplos práticos


1. `my_zero_class.py`
2. `my_first_class.py`
3. `class_template.py`
4. inheritance: `my_second_class.py`
5. Exemplo fun: `batalha.py`

**Exercício**
    
 - Como você faria uma classe que recebesse como inputs horas, minutos e segundos e tivesse a capacidade de somar e imprimir objetos no mesmo formato?
 - Quais dados seriam necessários?
 - Qual método central?
 - Qual a dificuldade central de somar horas, minutos e segundos?
 - Como resolver essa dificuldade?
 - Qual outro método seria necessário? (dica: output?)
 - Exemplo: use o `debug` para ver que minute = 61. Logo, ajustes são necessários

**Extra**
- Acrescente dias e anos no exemplo!

# Persistência

### O que é? Como faz? De onde vem, para onde vai?

🔥 1. Para quê?
**Seus dados sobrevivem mesmo depois do programa fechar!**

2. Parãmetros de abertura
- **'w'** - WRITE: Muita calma, nessa hora! Se o arquivo já existir, apaga tudo e começa do zero. *overwrite*
- **'a'** - APPEND: Seguro! Adiciona no final sem perder o que já existe
- **'r'** - READ: Apenas leitura, não modifica o arquivo

💾 3. Fluxo padrão: SALVAR → LER → REUTILIZAR
```python
# 1º Salve dados complexos
# 2º Leia de volta  
# 3º Recupere a estrutura original
# 4º Use os dados como se nunca tivessem saído da memória!

# `my_first_file.py`
# Criação 
first()

#Acúmulo 
(second(), numbers())

# Leitura 
reading()

# Processamento 
recover_list()

# Utilização sum_list()
```

4. Detalhe:
- o `with open()` garante que o arquivo é fechado depois que utilizado
- o primeiro parâmetro é o caminho do arquivo, o segundo é o modo como será aberto: `with open('dados.txt', 'a')` 
- o `as f` oferece o **handle**, a maçaneta que você utiliza para operar o arquivo: `f.read()` `f.write()`


```python
with open('dados.txt', 'a') as f:  # f é a "maçaneta"
    f.write('Novo dado')           # Usando a maçaneta para escrever
# Arquivo fecha sozinho 
```
5. Arquivo. `my_first_file.py` 
5. **Cuidados**:
- **'w'** acidental: Perde tudo que estava salvo! Talvez melhor seja **'a'**
- Esquecer de converter: Números viram texto → precisa converter de volta
- Formatação inconsistente: Dificulta a recuperação dos dados
- **Atenção**: Note que no exemplo `f.read()`, lemos o arquivo completo, com `\n`, por exemplo. A  lista também é lida com `;` que nós mesmos adicionamos ao escrever `f.write(f'{each};')` # each é o valor a ser escrito e `;` sempre vem depois!

6. Aplicações:
- Salvar configurações do usuário
- Genérico
- Guarda histórico de operações
- Exportar resultados para Excel/qualquer outro programa+
- Fazer backup de dados importantes



8. E se quisermos salvar uma lista de nomes? E um dicionário? Como faríamos?

## JSON

### muito similar--mas com texto mais legível

- Diferenças
1. `import json`
2. `file.json`
3. `json.dump` para salvar
4. `json.load` para ler


```python
import json

with open('my_obj.json', 'w') as f:
    json.dump(ob, f)
```

5. exemplo: `my_first_json`

## PICKLE

A. Só uso próprio do **python**. Melhor como arquivo temporário
B. Não use como transporte de arquivos (e-mail, envio), pois não inspecionável.
C. Similar a JSON e TXT.

```python
import pickle


# para salvar
with open('my_píckle', 'wb') as f:
    # passa o objeto e o handle (maçaneta)
    # note 'wb': writebytes
    pickle.dump(objeto_a_salvar, f)


# para ler
with open('my_pickle', 'rb') as f:
    # note 'rb': readbytes
    objeto_recuperado = pickle.load(f)
```

- Exemplo: my_first_pickle.py

### Exemplo de classes, objetos: Card(), Deck(), Hand(): `my_first_real_class.py`


*Pense em um exemplo de dados e salve em TXT. Em outro arquivo, leia, avalie e imprima o resultado. Inclua print(f'{}') para deixar claro os passos dados.*







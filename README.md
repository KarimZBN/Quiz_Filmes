# Quiz de Filmes

Este é um projeto de Quiz de Filmes desenvolvido em Python usando a biblioteca Tkinter para a interface gráfica. O quiz faz perguntas sobre suas preferências de filmes e recomenda filmes com base nas suas respostas.

## Funcionalidades

- Perguntas sobre preferências de filmes
- Recomendações de filmes baseadas nas respostas
- Interface gráfica amigável
- Vários gêneros de filmes, incluindo Ação, Comédia, Drama, Ficção Científica, Terror, Romance, Comédia Romântica, Fantasia, Musical, Aventura, Documentário e Mistério

## Requisitos

- Python 3.x
- Bibliotecas `tkinter` e `PIL`

## Instalação

1. Clone o repositório:
    ```
    git clone https://github.com/seu-usuario/quiz_filmes.git
    cd quiz_filmes
    ```

2. Instale as bibliotecas necessárias:
    ```
    pip install pillow
    ```
## Executando o Projeto
Para executar o projeto, simplesmente execute o arquivo `run.sh`:
ou
Abra o arquivo `quiz_ui.py` em um editor de texto como o VSCode e execute-o.

## Estrutura do Projeto

```
quiz_filmes/
├── filmes.json
├── perguntas.json
├── quiz_logic.py
├── quiz_ui.py
├── run.sh
└──path
     └──cartazes
```
- `filmes.json`: Arquivo JSON contendo a lista de filmes e seus gêneros.
- `perguntas.json`: Arquivo JSON contendo a lista de perguntas do quiz.
- `quiz_logic.py`: Script Python contendo a lógica do quiz.
- `quiz_ui.py`: Script Python contendo a interface gráfica do quiz.
- `run.sh`: Script para executar o quiz.
- `path\cartazes`: Pasta que armazena imagens de posters dos filmes.

## Arquivo de Perguntas (perguntas.json)
O arquivo `perguntas.json` contém as perguntas do quiz. Cada pergunta é um objeto JSON com os seguintes campos:

- `pergunta`: O texto da pergunta.
- `tipo`: O tipo de pergunta (neste caso, todas são de opinião).
- `generos`: Lista de gêneros que a pergunta aborda.
- Exemplo:
```
[
    {"pergunta": "Quanto você gosta de filmes cheios de cenas de ação intensas?", "tipo": "opiniao", "generos": ["ação", "terror"]},
    {"pergunta": "Quanto você gosta de filmes onde o protagonista enfrenta desafios físicos e emocionais?", "tipo": "opiniao", "generos": ["ação", "drama", "terror"]},
    ...
]
```
## Arquivo de Filmes (`filmes.json`)
O arquivo filmes.json contém a lista de filmes. Cada filme é um objeto JSON com os seguintes campos:

- `titulo`: O título do filme.
- `genero`: O gênero do filme.
- `imagem`: O caminho para a imagem do cartaz do filme.
Exemplo:
```
[
    {"titulo": "Mad Max (Saga)", "genero": "ação", "imagem": "path/cartazes/madmax.png"},
    {"titulo": "John Wick", "genero": "ação", "imagem": "path/cartazes/johnwick.png"},
    ...
]
```
## Funcionalidades Detalhadas
### Perguntas
O quiz apresenta perguntas ao usuário sobre suas preferências de filmes. As perguntas abrangem vários gêneros, incluindo ação, comédia, drama, ficção, terror, romance e comédia-romântica.

### Recomendações
Com base nas respostas, o aplicativo calcula as porcentagens de compatibilidade para cada gênero e recomenda filmes. Os filmes recomendados são exibidos com seus respectivos cartazes.

### Detalhes
O usuário pode optar por ver detalhes das porcentagens de compatibilidade dos gêneros, mostrando como cada gênero se alinha com suas preferências.

### Refazer Quiz
Após completar o quiz, o usuário pode optar por refazê-lo, resetando todas as respostas e perguntas.

## Créditos
Desenvolvido por Karim Alzeben e Vinicius Nessler para o curso de Engenharia de Software da Univille.

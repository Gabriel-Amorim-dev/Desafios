<img width="877" height="471" alt="Android Compact - 1" src="https://github.com/user-attachments/assets/ee8813d9-d3e6-4e45-a7af-19bd39241d04" />



# 🪙 Cara ou Coroa - Jogo em Python

Um jogo de Cara ou Coroa no terminal, feito em Python, com múltiplos modos de jogo, sistema de ranking em CSV e suporte a múltiplos jogadores!

---

## 🎯 Objetivo

Esse projeto foi desenvolvido como uma forma de praticar **Programação Orientada a Objetos (POO)**, **manipulação de arquivos**, **tratamento de exceções**, e **experiência interativa no terminal**. É ideal para aprender e se divertir jogando com amigos ou contra a IA.

---

## 🚀 Funcionalidades

## Funcionalidades Principais

* **Múltiplos Modos de Jogo:**
    * **PC vs PC:** Duas inteligências artificiais se enfrentam.
    * **PC vs Player:** Você desafia o computador.
    * **Player vs Player:** Duelo entre dois jogadores humanos.
    * **Insanidade ⚡:** Um modo caótico e imprevisível com resultados inesperados.
    * **Competição 🏆:** Jogue com amigos, acumule pontos e veja quem domina o ranking!
* **Sistema de Ranking:** O modo Competição salva as pontuações dos jogadores em um arquivo `ranking.csv`, permitindo que você acompanhe quem é o mestre do Cara ou Coroa.
* **Interface de Console Interativa:** Navegue pelos modos de jogo através de um menu simples no terminal.
* **🔄 Atualização automática dos pontos dos jogadores**
* **🧾 Visualização do ranking com nomes e pontuação**
* **🛠️ Tratamento de exceções para entradas inválidas**
* **⏳ Efeitos com `time.sleep()` para maior imersão**

---

## Como Jogar

### Pré-requisitos

Para rodar este jogo, você precisará ter o **Python 3** instalado em seu sistema.

### Instalação e Execução

1.  **Clone o Repositório (ou baixe os arquivos):**
2.  ```bash
      git clone https://github.com/Gabriel-Amorim-dev/Desafios.git # Clona o repositório principal 
      cd Desafios/Python/cara_Ou_Coroa # Navegue até a pasta do jogo
    ```
    
3.  **Execute o Jogo:**
    ```bash
    python cara_coroa.py
    ```
### Menu Principal

Ao iniciar o jogo, você verá o seguinte menu:
```
Bem vindo ao Cara Ou Coroa com Python, aqui você pode jogar por horas!
```
=============================== MODOS DE JOGO
[1] PC vs PC

Dois computadores jogam entre si.

[2] PC vs PLAYER

Você joga contra o computador.

[3] PLAYER vs PLAYER

Dois jogadores humanos se enfrentam.

[4] INSANIDADE ⚡

Um modo caótico e imprevisível.

[5] COMPETIÇÃO

Os jogadores se enfrentam e competem pela maior pontuação.

[6] RANKING

Exibição das pontuações do Modo Competição.

[7] SAIR

Nossos jogos acabam por aqui!.

===============================


Basta digitar o número correspondente ao modo de jogo que deseja e seguir as instruções no console.

---

## Estrutura do Código

O código é modularizado em funções para cada modo de jogo e funcionalidades auxiliares:

* `modo_ia_vs_ia()`: Lógica para o modo PC vs PC.
* `modo_ia_vs_player()`: Lógica para o modo PC vs Player.
* `modo_player_vs_player()`: Lógica para o modo Player vs Player.
* `modo_insanidade()`: Lógica para o modo Insanidade.
* `modo_competicao()`: Lógica para o modo Competição, incluindo a criação de objetos `Jogador`.
* `ranking()`: Função para exibir o ranking salvo.
* `salvar_ranking(jogadores)`: Função responsável por ler, atualizar e salvar o ranking no `ranking.csv`.
* `sair()`: Mensagem de encerramento do jogo.
* `error()`: Tratamento de erros para entradas inválidas.

---

## Desenvolvimento

### Tecnologias Utilizadas

* Python 3.10

### Bibliotecas Padrão

* `random`: Para simular a escolha da moeda (`choice`).
* `time`: Para pausas (`sleep`) que melhoram a experiência do usuário.
* `csv`: Para manipulação do arquivo de ranking (`ranking.csv`).
* `os`: Para verificar a existência do arquivo de ranking.

---

## Contribuição

Ainda estou aprendendo e me aprimorando como programador, então contribuições são sempre bem-vindas! Se você tiver ideias para novos modos de jogo, melhorias de código, correção de bugs, ou qualquer outra coisa, sinta-se à vontade para:

1.  **Fork** este repositório.
2.  Crie uma nova **branch** (`git checkout -b feature/nome-da-feature`).
3.  Faça suas **alterações**.
4.  Comite suas alterações (`git commit -m 'Adiciona nova feature'`).
5.  Envie para a branch (`git push origin feature/nome-da-feature`).
6.  Abra um **Pull Request**.

---

## Licença

Este projeto está sob a licença [MIT License](LICENSE).

---

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

* **Gabriel-Amorim-Dev** - ([https://github.com/Gabriel-Amorim-dev](https://github.com/Gabriel-Amorim-dev))

---

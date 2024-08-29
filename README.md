# 📷 Flask API - Autenticação JWT e Transferência de Imagens

![Flask](https://img.shields.io/badge/Flask-v2.0-blue) ![JWT](https://img.shields.io/badge/JWT-Authentication-green) ![Python](https://img.shields.io/badge/Python-v3.9-blue)

🚀 Este projeto demonstra minhas habilidades como desenvolvedor backend utilizando o **Flask** para criar uma API segura com **JWT** (JSON Web Token) e recursos avançados de transferência de imagem. Este projeto é **original** e foi concebido a partir de estudos aprofundados, pesquisas, livros e insights adquiridos ao longo da minha trajetória profissional.

---

## 📋 Sobre o Projeto

Este repositório contém uma API Flask que autentica usuários e permite o download seguro de imagens mediante um token JWT. O projeto é composto por um servidor e um cliente Flask que exemplifica a interação com a API para login e transferência de imagem.

### 🧰 Tecnologias Utilizadas

- **Flask** - Micro framework web para Python.
- **JWT** - Implementação de autenticação baseada em tokens.
- **Python** - Linguagem de programação usada no desenvolvimento.
- **UUID** - Utilizado para gerar nomes únicos para imagens baixadas.
- **Requests** - Biblioteca para fazer requisições HTTP no cliente.

### 🎯 Objetivos

- Demonstrar o uso de **JWT** para autenticação segura.
- Exibir habilidades de manipulação e transferência de arquivos através de uma API RESTful.
- Mostrar proficiência em bibliotecas Python e gerenciamento de dados fora dos formatos tradicionais.

## ⚙️ Como Usar

### Pré-requisitos

- **Python 3.9+**
- **Bibliotecas**: `Flask`, `pyjwt`, `requests`

### Passo a Passo

1. **Clone este repositório**:
    ```bash
    git clone https://github.com/evolucaoit/Flask_API_IMG_Transfer.git
    cd Flask_API_IMG_Transfer
    ```

2. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o servidor Flask**:
    ```bash
    python apiflaskserverimage.py
    ```
   O servidor iniciará em `http://localhost:777`.

4. **Execute o cliente para realizar login e baixar uma imagem**:
    ```bash
    python client-flask-get-imagem.py
    ```

### 🔐 Autenticação JWT

O endpoint `/login` recebe credenciais e retorna um token JWT válido por uma hora. Este token é então usado para autenticar a requisição ao endpoint `/img-download`, que transfere uma imagem protegida.

## 📌 Referências

Este projeto é 100% original e todos os textos e documentações foram cuidadosamente escritos e estilizados usando ferramentas de IA como ChatGPT e Google Gemini API.

### 📚 Outros Projetos

Explore outros projetos em meu [GitHub](https://github.com/chaos4455). Cada repositório é desenvolvido com a intenção de trazer soluções originais e inovadoras baseadas em práticas modernas de desenvolvimento.

## 📫 Contato

- **GitHub**: [chaos4455](https://github.com/chaos4455)
- **LinkedIn**: [itilmgf](https://br.linkedin.com/in/itilmgf)

---

🔍 **Nota**: Todos os projetos hospedados no meu GitHub são **autoriais**, criados a partir de estudos e práticas originais. Nenhum deles é um tutorial copiado ou apenas uma reprodução; são projetos inovadores que refletem meu crescimento contínuo na área de tecnologia e desenvolvimento.


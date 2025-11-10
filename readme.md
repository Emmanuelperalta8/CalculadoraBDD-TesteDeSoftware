Perfeito, Peralta! Aqui está um README.md completo e bem formatado para você incluir no seu repositório do GitHub — explicando o projeto, os testes BDD e a interface gráfica moderna da calculadora:

# 🧮 Calculadora BDD - Teste de Software

Este projeto foi desenvolvido como parte da disciplina de **Teste de Software**, com o objetivo de aplicar **BDD (Behavior Driven Development)** utilizando a ferramenta **Behave** e criar uma **interface gráfica moderna** para uma calculadora funcional.

---

## 🚀 Funcionalidades

A calculadora permite realizar operações básicas e avançadas:

- ➕ **Soma**
- ➖ **Subtração**
- ✖️ **Multiplicação**
- ➗ **Divisão** (com tratamento de erro para divisão por zero)
- √ **Raiz quadrada** (com tratamento de erro para números negativos)
- 📊 **Cálculo de média** de uma lista de números

---

## 🧩 Estrutura do Projeto



📁 Teste de Sof. - Calculadora
│
├── 📁 features/ # Cenários de teste em linguagem Gherkin
│ ├── calculadora.feature # Descrição dos testes BDD
│
├── 📁 src/ # Código-fonte principal
│ ├── calculadora.py # Classe com a lógica da calculadora
│ ├── app.py # Interface gráfica com ttkbootstrap
│
├── 📁 tests/ # Testes automatizados (se necessário)
│
├── README.md # Este arquivo :)
└── requirements.txt # Dependências do projeto


---

## 🧠 Tecnologias Utilizadas

- **Python 3.10+**
- **Behave** – Framework BDD
- **tkinter** e **ttkbootstrap** – Interface gráfica moderna
- **math** – Operações matemáticas básicas

---

## 🧪 Testes BDD (Behavior Driven Development)

Os testes seguem o formato **Gherkin**, simulando o comportamento do usuário interagindo com a calculadora.

Exemplo de cenário:

```gherkin
Funcionalidade: Operações básicas da calculadora
  Para realizar cálculos simples
  Como um usuário
  Eu quero usar a calculadora para somar números

  Cenário: Somar dois números
    Dado que iniciei a calculadora
    Quando somo 5 e 3
    Então o resultado deve ser 8


Para executar os testes, use:

python -m behave


Todos os cenários são validados pela classe Calculadora, garantindo o funcionamento correto das operações e tratamento de exceções.

💻 Interface Gráfica

A interface foi criada com ttkbootstrap, oferecendo um visual moderno e responsivo.

Para executar a interface:
python -m src.app


Ou:

cd src
python app.py

⚙️ Instalação

Clone o repositório:

git clone https://github.com/seuusuario/calculadora-bdd.git
cd calculadora-bdd


Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
venv\Scripts\activate  # no Windows


Instale as dependências:

pip install behave ttkbootstrap


Execute os testes ou a aplicação.

🧑‍💻 Autor

Emmanuel Peralta
📘 Projeto desenvolvido para a disciplina de Teste de Software
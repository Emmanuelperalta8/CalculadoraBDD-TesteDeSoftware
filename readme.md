🚀 1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/Calculadora-BDD.git
cd Calculadora-BDD

⚙️ 2️⃣ Instalar as dependências

(garanta que você esteja com o Python 3.10+)

pip install -r requirements.txt

🧠 3️⃣ Rodar os testes BDD (com Behave)

Isso executa todos os cenários Gherkin do diretório features/.

python -m behave


Se tudo estiver certo, você verá a saída:

1 feature passed, 0 failed
32 scenarios passed, 0 failed

💻 4️⃣ Executar a interface gráfica da calculadora

Esse comando abre a calculadora moderna com ttkbootstrap:

python -m src.app


Ou, se preferir rodar diretamente:

cd src
python app.py

🧩 Resumo rápido dos comandos
git clone https://github.com/seu-usuario/Calculadora-BDD.git
cd Calculadora-BDD
pip install -r requirements.txt
python -m behave
python -m src.app

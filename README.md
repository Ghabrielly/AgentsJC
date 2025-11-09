Como rodar o projeto
1️⃣ Instalar as dependências

Abra o terminal na pasta do projeto e rode:

pip install crewai  
pip install crewai-tools  
pip install google-genai  
pip install python-dotenv

2️⃣ Criar o arquivo .env

Na raiz do projeto, crie um arquivo chamado .env e coloque dentro:

GEMINI_API_KEY=sua_chave_do_gemini  
SERPER_API_KEY=sua_chave_do_serper

3️⃣ Onde pegar as chaves

🔹 Gemini (Google AI): https://aistudio.google.com/app/apikey

🔹 Serper (ferramenta de busca): https://serper.dev/

4️⃣ Verificar as variáveis no código

No arquivo crew.py, confira se essas linhas estão dentro da classe:

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")  
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")

5️⃣ Rodar o projeto

Para executar o projeto, use:

python main.py run

6️⃣ (Opcional) Rodar com uma empresa específica

No arquivo main.py, você pode alterar o nome da empresa:

inputs = {"empresa": "Petrobras"}  
EquipeDeAnaliseFinanceiraIa().crew().kickoff(inputs=inputs)
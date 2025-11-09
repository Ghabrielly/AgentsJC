import os
from dotenv import load_dotenv
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperScrapeWebsiteTool, SerperDevTool
from google import genai

# 🔹 Carrega variáveis do .env
load_dotenv()

@CrewBase
class EquipeDeAnaliseFinanceiraIa:
    """Equipe de Análise Financeira com IA"""

    # 🔑 Chaves vindas do .env
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")

    # Nome do modelo Gemini
    MODEL_NAME = "gemini-2.0-flash"

    def __init__(self):
        # Inicializa o cliente do Gemini
        self.gemini_client = genai.Client(api_key=self.GEMINI_API_KEY)

    def _create_llm(self):
        """Cria um wrapper do LLM pra CrewAI usando o Gemini."""
        return LLM(
            model=self.MODEL_NAME,
            api_key=self.GEMINI_API_KEY,
            temperature=0.7,
            provider="google"  # só pra indicar que é do Google
        )

    # === Agentes ===

    @agent
    def julia___analista_de_dados_financeiros(self) -> Agent:
        return Agent(
            config=self.agents_config["julia___analista_de_dados_financeiros"],
            tools=[SerperScrapeWebsiteTool()],
            llm=self._create_llm(),
        )

    @agent
    def pedro___analista_de_sentimento_de_mercado(self) -> Agent:
        return Agent(
            config=self.agents_config["pedro___analista_de_sentimento_de_mercado"],
            tools=[SerperDevTool()],
            llm=self._create_llm(),
        )

    @agent
    def key___jornalista_financeiro_senior(self) -> Agent:
        return Agent(
            config=self.agents_config["key___jornalista_financeiro_senior"],
            tools=[],
            llm=self._create_llm(),
        )

    # === Tarefas ===

    @task
    def coleta_de_dados_financeiros(self) -> Task:
        return Task(config=self.tasks_config["coleta_de_dados_financeiros"])

    @task
    def analise_de_sentimento_de_mercado(self) -> Task:
        return Task(config=self.tasks_config["analise_de_sentimento_de_mercado"])

    @task
    def redacao_do_artigo_final(self) -> Task:
        return Task(config=self.tasks_config["redacao_do_artigo_final"])

    # === Crew ===

    @crew
    def crew(self) -> Crew:
        """Cria a equipe de análise financeira com IA"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

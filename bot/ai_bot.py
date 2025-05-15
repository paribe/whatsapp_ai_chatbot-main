import os
from decouple import config
from datetime import datetime
import pytz

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma  # from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        self.__chat = ChatGroq(model='llama3-70b-8192')
        self.__retriever = self.__build_retriever()

    def __saudacao_por_horario(self):
        fuso_sp = pytz.timezone('America/Sao_Paulo')
        hora_atual = datetime.now(fuso_sp).hour
        if 5 <= hora_atual < 12:
            return "Bom dia"
        elif 12 <= hora_atual < 18:
            return "Boa tarde"
        else:
            return "Boa noite"

    def __build_retriever(self):
        from langchain_core.documents import Document

        class DummyRetriever:
            def invoke(self, question):
                return [
                    Document(
                        page_content="Informações sobre o seu dia ... se for de dia diga Bom dia, se for à tarde diga Boa tarde, se for à noite diga Boa noite.",
                        metadata={}
                    )
                ]

        return DummyRetriever()

    def __build_messages(self, history_messages, question):
        messages = []
        for message in history_messages:
            message_class = HumanMessage if message.get('fromMe') else AIMessage
            messages.append(message_class(content=message.get('body')))
        messages.append(HumanMessage(content=question))
        return messages

    def invoke(self, history_messages, question):
        saudacao = self.__saudacao_por_horario()
        SYSTEM_TEMPLATE = f'''
        {saudacao}! Responda as perguntas dos usuários com base no contexto abaixo.
        Você é um assistente especializado em conversar com pessoas em vários idiomas e assuntos. Seja objetivo nas respostas, com informações
        claras e diretas. Foque em ser natural e humanizado, como um diálogo comum entre duas pessoas.
        Leve em consideração também o histórico de mensagens da conversa com o usuário.
        Responda sempre em português brasileiro.

        <context>
        {{context}}
        </context>
        '''

        docs = self.__retriever.invoke(question)
        question_answering_prompt = ChatPromptTemplate.from_messages(
            [
                ('system', SYSTEM_TEMPLATE),
                MessagesPlaceholder(variable_name='messages'),
            ]
        )
        document_chain = create_stuff_documents_chain(self.__chat, question_answering_prompt)
        response = document_chain.invoke(
            {
                'context': docs,
                'messages': self.__build_messages(history_messages, question),
            }
        )
        return response

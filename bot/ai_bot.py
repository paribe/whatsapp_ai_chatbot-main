import os
from decouple import config
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma  # from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_groq import ChatGroq
from langchain_groq import ChatGroq
# from langchain_community.chat_models import ChatGroq
# from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        #self.__chat = ChatGroq(model='llama-3.1-70b-versatile')
        self.__chat = ChatGroq(model='llama3-70b-8192')
        self.__retriever = self.__build_retriever()
        
    def __build_retriever(self):
        # Versão simplificada que não depende do PyTorch
        from langchain_core.documents import Document
    
        class DummyRetriever:
            def invoke(self, question):
                # Cria um objeto Document em vez de um dicionário simples
                return [
                    Document(
                       # page_content="Informações sobre o treinamento Django Master da PycodeBR.",
                        page_content="Informações sobre o seu dia ... se for de dia diga Bom dia se for a tarde diaga Boa tarde se for a noite diga Boa noite",
                        metadata={}
                    )
                ]
        
        return DummyRetriever()
    '''
    def __build_retriever(self):
        persist_directory = '/app/chroma_data'
        embedding = HuggingFaceEmbeddings()
        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding,
        )
        return vector_store.as_retriever(
            search_kwargs={'k': 30},
        )
    '''
    
    def __build_messages(self, history_messages, question):
        messages = []
        for message in history_messages:
            message_class = HumanMessage if message.get('fromMe') else AIMessage
            messages.append(message_class(content=message.get('body')))
        messages.append(HumanMessage(content=question))
        return messages
    
    def invoke(self, history_messages, question):
        SYSTEM_TEMPLATE = '''
        Responda as perguntas dos usuários com base no contexto abaixo.
        Você é um assistente especializado em conersar com pessoas em varios idomaos e assuntos.Seja objetivo nas respostas, com informações
        claras e diretas. Foque em ser natural e humanizado, como um diálogo comum entre duas pessoas.
        Leve em consideração também o histórico de mensagens da conversa com o usuário.
        Responda sempre em português brasileiro.
        
        <context>
        {context}
        </context>
        '''
        
        docs = self.__retriever.invoke(question)
        question_answering_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    'system',
                    SYSTEM_TEMPLATE,
                ),
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
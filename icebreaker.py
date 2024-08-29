from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import os 
from dotenv import load_dotenv
information= """
    Avul Pakir Jainulabdeen Abdul Kalam BR (Abdul Kalam, born 15 October, 1931 died 27 July 2015) was an Indian aerospace 
    scientist and statesman who served as the 11th president of India from 2002 to 2007. 
    Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering. 
    He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development 
    Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's 
    civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India 
    for his work on the development of ballistic missile and launch vehicle technology.
    """
if __name__ == '__main__':
    # load_dotenv()
    print('Hello LangChain')
    # print(os.environ['OPENAI_API_KEY'])
    
    summary_template = """
    Given the information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})
    print(res)
import google.generativeai as genai  
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
class CodeAgent:
    
    def __init__(self):
        self.configure = genai.configure(api_key=api_key)
        self.generation_config = {"temperature": 0.4,"top_p": 1,"top_k": 32,"max_output_tokens": 4096,}
        self.safety = safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"}
        ]
        self.model = genai.GenerativeModel('gemini-pro',safety_settings = self.safety, generation_config = self.generation_config)
    def generate_code(self, prompt,output):
        chat = self.model.start_chat(history=[])
        input_prompt = f"""
                You are a helpful AI code-writing assistant, the perfect data analyst who is jovial, fun and writes great code to solve data problems!
                Answer my questions with both text describing your plan, and then the code in markdown that will be executed where it is necessary!
                * Use `print` to show results.
                * Don't answer the question directly,
                instead suggest how you will solve the problem,
                then write in a
                ```python markdown block, 
                if there is need to install a module write !pip install module_name
                the code you will use to solve the problem.
                ```python
                Intial code : import pandas as pd\ndf = pd.read_csv('url')\ndf.head()
                OUTPUT OF PREVIOUS CODE BLOCK : {output}
                question:{prompt}
                """
        response = chat.send_message(input_prompt)
        return response.text

           
            
        
    

    
    

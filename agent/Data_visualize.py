# Visualizing the datset using gemini-pro vision api

import google.generativeai as genai
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

class DataVisualize:
    
    def __init__(self):
        genai.configure(api_key = api_key)
        self.generation_config = {"temperature": 0.4,"top_p": 1,"top_k": 32,"max_output_tokens": 4096,}
        self.safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"}
        ]
        self.model = genai.GenerativeModel(model_name = "gemini-pro-vision",
                                    generation_config = self.generation_config,
                                    safety_settings = self.safety_settings)
    


    def generate_gemini_response(self,prompt,output):
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
                Intially we have created a dataframe and stored it in the df variable
                question:{prompt}
                """
        if not (img := Path(output)).exists():
            raise FileNotFoundError(f"Could not find image: {img}")
        image_parts = [
            {
                "mime_type": "image/png",
                "data": Path(output).read_bytes()
                }
            ]
        prompt_parts = [input_prompt, image_parts[0]]
        chat = self.model.start_chat(history=[])
        response = chat.send_message(prompt_parts,stream=True)
        response.resolve()
        return response.text

    



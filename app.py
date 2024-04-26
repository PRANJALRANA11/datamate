### Tomorrow work  2- append history of output 3- add visualize  4- gradio
from agent.Code_Agent import CodeAgent
from Kernel.Kernel import Kernel
from agent.refine_code import RefineCode
from data_gathering.load_dataset import GithubSearch
from agent.Data_visualize import DataVisualize
from fastapi import FastAPI

app = FastAPI()

origins = [
    # "http://localhost:3000",
    # "http://localhost:3001",
    "*"
]



@app.get("/load_datasets")
async def root():
    DataGathering = GithubSearch()
    res = DataGathering.search_github("Apple stocks")
    return {"datasets" : res}


def main():
    DataGathering = GithubSearch()
    data = DataVisualize()
    kernel = Kernel()
    # Search for the dataset and formating it
    res = DataGathering.search_github("Apple stocks")
    format_res = DataGathering.format_items(res)
    # Load the dataset
    code, output = kernel.execute_code(f"import pandas as pd\ndf = pd.read_csv('{format_res[0]['fullurl']}')\ndf.head()")


     
    # Give the prompt to generate refine and execute the code
    for i in range(4):
        if output == "imageToSaved.png":
            print("visual")
            prompt = input("enter the prompt")
            code =data.generate_gemini_response(prompt,output)
            refine_code = RefineCode(code)
            code = refine_code.refine()
            code, output = kernel.execute_code(code[1])
            if output != 'imageToSaved.png':
                codeAgent.generate_code(prompt,output)
            else:
                data.generate_gemini_response(prompt,output)
        else:
            print("code")
            prompt = input("enter the prompt")
            codeAgent = CodeAgent()
            code = codeAgent.generate_code(prompt,output)
            refine_code = RefineCode(code)
            code = refine_code.refine()
            code, output = kernel.execute_code(code[1])
            if output != 'image_path':
                codeAgent.generate_code(prompt,output)
            else:
                data.generate_gemini_response(prompt,output)
    




        
if __name__ == "__main__":
        main()
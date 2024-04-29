### Tomorrow work  2- append history of output 3- add visualize  4- gradio
from agent.Code_Agent import CodeAgent
from Kernel.Kernel import Kernel
from agent.refine_code import RefineCode
from data_gathering.load_dataset import GithubSearch
from agent.Data_visualize import DataVisualize
from fastapi import FastAPI
from code_interpret.code_interpret import  Interpreter

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
    dataset = input("Which dataset you want to load from internet \n")
    print(f"fetching {dataset}...")
    res = DataGathering.search_github("Apple stocks")
    format_res = DataGathering.format_items(res)
    # Load the dataset
    print("loading the dataset...")
    code, output = kernel.execute_code(f"import pandas as pd\ndf = pd.read_csv('{format_res[0]['fullurl']}')\ndf.head()")
    print(f"{dataset} dataset loaded successfully!")
    init_code = f"import pandas as pd\ndf = pd.read_csv('{format_res[0]['fullurl']}')\ndf.head()"
    total_code = init_code


    # Give the prompt to generate refine and execute the code
    for i in range(4):
        if output == "imageToSaved.png":
            print("visual")
            prompt = input("what would you like to do more with dataset \n")
            code =data.generate_gemini_response(prompt,output)
            refine_code = RefineCode(code)
            code = refine_code.refine()
            total_code += code[1]
            code, output = kernel.execute_code(total_code)
            if output != 'imageToSaved.png':
                codeAgent.generate_code(prompt,output)
            else:
                data.generate_gemini_response(prompt,output)
        else:
            if i == 1:
                print("code")
                prompt = input("what would you like to do with dataset \n")
                codeAgent = CodeAgent()
                code = codeAgent.generate_code(prompt,output,init_code)
                refine_code = RefineCode(code)
                code = refine_code.refine()
                total_code += code[1]
                if_error, output = kernel.execute_code(total_code)
                if if_error == "Yes":
                    print("Running Interpreter iteration 1")
                    inter_code = Interpreter().generate_code(total_code,output)
                    refine_code = RefineCode(inter_code)
                    code = refine_code.refine()
                    if_error, output = kernel.execute_code(code[1])
                    if if_error == "Yes":
                        print("Running Interpreter iteration 2")
                        inter_code =   Interpreter().generate_code(total_code,output)
                        refine_code = RefineCode(inter_code)
                        code = refine_code.refine()
                        if_error, output = kernel.execute_code(code[1])
                        if if_error == "Yes":
                            print("Running Interpreter iteration 3")
                            inter_code =   Interpreter().generate_code(total_code,output)
                            refine_code = RefineCode(inter_code)
                            code = refine_code.refine()
                            if_error, output = kernel.execute_code(code[1])

                if output != 'image_path':
                    codeAgent.generate_code(prompt,output)
                else:
                    data.generate_gemini_response(prompt,output)
                    
            print("code")
            prompt = input("what would you like to do with dataset \n")
            codeAgent = CodeAgent()
            code = codeAgent.generate_code(prompt,output)
            refine_code = RefineCode(code)
            code = refine_code.refine()
            total_code += code[1]
            if_error, output = kernel.execute_code(total_code)
            if if_error == "Yes":
                print("Running Interpreter iteration 1")
                inter_code = Interpreter().generate_code(total_code,output)
                refine_code = RefineCode(inter_code)
                code = refine_code.refine()
                if_error, output = kernel.execute_code(code[1])
                if if_error == "Yes":
                    print("Running Interpreter iteration 2")
                    inter_code =   Interpreter().generate_code(total_code,output)
                    refine_code = RefineCode(inter_code)
                    code = refine_code.refine()
                    if_error, output = kernel.execute_code(code[1])
                    if if_error == "Yes":
                        print("Running Interpreter iteration 3")
                        inter_code =   Interpreter().generate_code(total_code,output)
                        refine_code = RefineCode(inter_code)
                        code = refine_code.refine()
                        if_error, output = kernel.execute_code(code[1])

                if output != 'image_path':
                    codeAgent.generate_code(prompt,output)
                else:
                    data.generate_gemini_response(prompt,output)
    




        
if __name__ == "__main__":
        main()
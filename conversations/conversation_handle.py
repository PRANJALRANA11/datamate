
from data_gathering.load_dataset import GithubSearch
from Kernel.Kernel import Kernel
from code_interpret.code_interpret import  Interpreter
from agent.Data_visualize import DataVisualize
from agent.Code_Agent import CodeAgent
from agent.refine_code import RefineCode


DataGathering = GithubSearch()
kernel = Kernel()
data = DataVisualize()

def searching_dataset(dataset_name):
        res = DataGathering.search_github(dataset_name)
        format_res = DataGathering.format_items(res)
        return format_res
def adding_dataset(selected_dataset_url):
    code, output = kernel.execute_code(f"import pandas as pd\ndf = pd.read_csv('{selected_dataset_url}')\ndf.head()")
    init_code = f"import pandas as pd\ndf = pd.read_csv('{selected_dataset_url}')\ndf.head()"
    total_code = init_code
    return total_code,output
    
def Conversation_agent(prompt,output,code=None):
        if output == "imageToSaved.png":
            print("visual")
            code = data.generate_gemini_response(prompt,output)
            refine_code = RefineCode(code)
            code = refine_code.refine()
            total_code += code[1]
            text = code[0]
            code, output = kernel.execute_code(total_code)
            if output != 'imageToSaved.png':
                codeAgent.generate_code(prompt,output)
            else:
                data.generate_gemini_response(prompt,output)
            return total_code , output , text
        else:
                print("code")
                codeAgent = CodeAgent()
                code = codeAgent.generate_code(prompt,output,init_code)
                refine_code = RefineCode(code)
                code = refine_code.refine()
                total_code += code[1]
                text = code[0]
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
                return total_code , output , text
                    
          
    
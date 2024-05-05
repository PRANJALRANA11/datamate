
from fastapi import FastAPI
from conversations.conversation_handle import searching_dataset , adding_dataset , Conversation_agent
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    # "http://localhost:3000",
    # "http://localhost:3001",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/search_datasets")
async def search_data(dataset_name):
    try:
        res =  searching_dataset(dataset_name)
        return {"datasets" : res}
    except Exception as e:
        return e

@app.get("/load_dataset/")
async def load_data(dataset_url):
    try:
        code , output = adding_dataset(dataset_url)
        return {"code" : code, "output" : output}
    except  Exception as e:
        return e

@app.get("/chat_with_data/")
async def chat_data(prompt,output,code):
    try:
        code , output , text = Conversation_agent(prompt,output,code)
        return {"code" : code, "output" : output,"text":text}
    except Exception as e:
        return e






    
    # res = searching_dataset("Apple stocks")
    # code , output = adding_dataset(res[0]['fullurl'])
    # code , output , text = Conversation_agent("do univariant analysis between volume and high by plotting scatterplot",output,code)
    # print(Conversation_agent("could you tell me the corelation",output,code))



        
if __name__ == "__main__":
        main()

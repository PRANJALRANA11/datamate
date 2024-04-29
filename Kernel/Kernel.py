# Description: This file is used to execute the code in the notebook and display the output in the form of an image and text.
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from IPython.display import Image, display
import base64
import json




class Kernel:
    def __init__(self):
        pass
    def execute_code(self, code):
        # Create a new notebook
        notebook = nbformat.v4.new_notebook()
        # Add a code cell with some code

        cell = nbformat.v4.new_code_cell(source=code)
        notebook.cells.append(cell)
        nbformat.write(notebook, 'my_notebook.ipynb')

        # Execute the notebook
        try:
            with open('my_notebook.ipynb') as f:
                nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            ep.preprocess(nb)
        except Exception as e:
            error_json = {'message': str(e)}
            print("Error in executing code", error_json)
            return "Yes", error_json
        output_data = {}
        for i in range(len(nb.cells[0].outputs)):
            if nb.cells[0].outputs[i].output_type == 'display_data':
                image_path = nb.cells[0].outputs[i].data['image/png']
                with open("imageToSaved.png", "wb") as fh:
                    fh.write(base64.b64decode(image_path.strip()))
                    display(Image('imageToSaved.png'))
                return code, 'imageToSaved.png'
            if nb.cells[0].outputs[i].output_type == 'stream':
                text = nb.cells[0].outputs[i].text
                output_data['code'] = text
                print(output_data['code'])
                return code, output_data['code']
            
            if nb.cells[0].outputs[i].output_type == 'execute_result':
                text = nb.cells[0].outputs[i].data['text/plain']
                output_data['code'] = text
                return code, output_data['code']
            print("hello")
        # Display the image
        # with open("imageToSaved.png", "wb") as fh:
        #     fh.write(base64.b64decode(image_path.strip()))
        #     display(Image('imageToSaved.png'))

        


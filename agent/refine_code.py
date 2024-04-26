import re

class RefineCode:
    def __init__(self, code):
        self.code = code
        self.pattern_inter = r'error:(.*?)\ncodeBlock: (.*?)\n'
        self.pattern = r'```python(.*?)```'
    def refine(self):
        code_blocks = re.findall(self.pattern, self.code, re.DOTALL)
        code_blocks2 = re.sub(self.pattern, '', self.code, flags=re.DOTALL)
        refine_code = []
        print("Text from the prompt:")
        print(code_blocks2.strip())
        text_block = code_blocks2.strip()
        print("Python code blocks:")
        clean_code = ""
        for code_block in code_blocks:
            print(code_block.strip())
            clean_code = clean_code + code_block.strip()
            print("code ends")
        refine_code.append(text_block)
        refine_code.append(clean_code)
        return refine_code

    
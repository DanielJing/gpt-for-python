import os
import openai
openai.api_key = os.environ.get('OPENAI_API_KEY')
gpt3 = openai.Model.get("gpt-3.5-turbo")
completion = openai.Completion.create( engine="gpt-3.5-turbo", 
             prompt="blablabla...", 
             max_tokens=100, temperature=0.5, )
generated_text = completion.text

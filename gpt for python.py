import os
import openai
openai.api_key = os.environ.get('OPENAI_API_KEY')
gpt3 = openai.Model.get("text-curie-001")
completion = openai.Completion.create( engine="text-curie-001", 
             prompt="blablabla", 
             max_tokens=100, temperature=0.5, )
generated_text = completion.text
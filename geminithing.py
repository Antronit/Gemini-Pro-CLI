import pathlib
import textwrap

import google.generativeai as genai
model = genai.GenerativeModel('gemini-pro')

# Used to store your API key
apikey='empty'

# stores your question
asked='hi'

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

print('What is your API key\n')
input(apikey)
genai.configure(api_key=apikey)

chat = model.start_chat(history=[])
chat
print('What do you want to ask Gemini Pro')
input(asked)
chat.send_message(asked)
response = chat.send_message(asked)
to_markdown(response.text)

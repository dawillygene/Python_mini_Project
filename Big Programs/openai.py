# Use OpenAI API to generate code
import openai
openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Write a Python function to reverse a string."}]
)
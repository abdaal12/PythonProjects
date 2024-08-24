import os
import google.generativeai as genai
genai.configure(api_key="AIzaSyDk2-PEdDqPg7hhQrsYJRJqIzZiK-PbWk0")
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat()


ipt=input("Please Provide some information about the person what you have")
inpt1=input("Insta_facebook_bio")
inpt2=input("Insta_facebook_posts")
inpt3=input("Insta_facebook_status")
inpt4=input("Other information if you have")
if inpt4=="":
    inpt4="this is data about person which we have"
#inmain="tell something about this person according to their social media data which is{inpt1},{inpt2},{inpt3},{inpt4},answer in 5 points only"    
prompt = f"Based on the provided social media data, here is a summary:\n\nBio: {inpt1}\nPosts: {inpt2}\nStatus: {inpt3}\nOther Info: {inpt4}\n\nProvide insights in 5 points."
#response = chat_session.send_message(prompt)
try:
    response = chat_session.send_message(prompt)
except Exception as e:
    print(f"An error occurred: {e}")
#print(response.text)
response_text = response.text.strip()
print("Key Insights:")
for i, point in enumerate(response_text.split('\n'), 1):
    print(f"{i}. {point}")


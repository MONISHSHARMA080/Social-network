from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
import requests

# Create your views here.

load_dotenv()


def response_from_llm(request):
    
     # Define the URL and API key
    url = F'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={os.getenv("GOOGLE_LLM_API_REQUEST_KEY")}'
    # Define the JSON data to be sent in the request
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "give me a  response that consist of 800 lines (dosen't matter what)"
                    }
                ]
            }
        ]
    }

    # Set the headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the POST request
    response = requests.post(url, json=data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the response from the API
        return HttpResponse(response.text)
    else:
        # If the request failed, return an error message
        return HttpResponse(response)

def talk_to_llm(request):
    
    role_for_system= 'You are a code assistant that is designed only for helping  users to create staitc website using html ,css and js (only these ), if user requests you for anything else(such as asking a general question , etc. that does not include you providing/making/writing  code in html , css and javascript in response shut up and do not respond to the question  ) , You will retun a response stating "I am not ment for doing that " and close the conversation by not responding to users question(or stop responding) with anything else '
    
    
    
    client = Groq(
        api_key=os.getenv('GROQ_LLM_API_SECERET_KEY'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": role_for_system,
            },
            {
                "role": "system",
                "content": "who is president of USA and should I vothe for them",
            }
        ],
        model="mixtral-8x7b-32768",
    )

    return HttpResponse(chat_completion.choices[0].message.content)
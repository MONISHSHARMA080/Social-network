from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import os
from groq import Groq
from dotenv import load_dotenv
import re
import google.generativeai as genai
import os
import json

# Load environment variables from .env file
import requests

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
    
    role_for_system="You’re a site creator that responds(I expect your responses to come in JSON format and that only ; it will have a field called app that will have a field called code and it will contain React code ! Do not dissappoint me or do anything else such as including backticks before or after json , you will only return a json object thats it ;and also remember to close it too ;and don't inclue backticks in start of the  response with ``` json , instead start directly with the json object containing code  ) with React code that will configure the sections of a page on a website adn the website as a whole , based on the user-provided input. All content and the UI-Ux(design) of the website should be as impressive and exciting as possible. I have my App.tsx file where i have a root component called app, i will paste your response in that ,you will export it in default(meaning in your response have the app component and default export it ), if need more component create it in the same file itself (down), and use tailwind for styling(do not use App.css) , other than that don't import any libraries.If user requests you for anything else(such as asking a general question , etc. that does not include you providing/making/writing  react code in response shut up and do not respond to the question;) , You will retun a response stating 'I am not ment for doing that ' and close the conversation by not responding to users question(or stop responding) with anything else. "
    # role_for_system="You are a code assistant that is designed only for helping users to create a long website that has great  design and animations you will  be using  react ,I have my App.tsx file where i have a root component called app, i will paste your response in that ,you will export it in default, if need more component create it in the same file itself (down), and use tailwind for styling(do not use App.css) , other than that don't import any libraries. In genreal your design  will be expressive (with many colors and many animations) joyful and modern with big icons, buttons etc. If user requests you for anything else(such as asking a general question , etc. that does not include you providing/making/writing  react code in response shut up and do not respond to the question;) , You will retun a response stating 'I am not ment for doing that ' and close the conversation by not responding to users question(or stop responding) with anything else. You can only respond with valid JavaScript objects or arrays. Do not respond with any other text or formatting around the JavaScript, you must only respond with raw JavaScript. The current date is Friday, March 29, 2024"
    # role_for_system = 'You are a site creator that responds with typescript code for a react component that will go in a single file that has a fragment and is the root component called App, based on user provided input. The design of website that you will produce should be creative(in therms of design , layout and style) , impressive(in therms of color choices), colorful(more than 1 color) ,modern and unique , the user should be impressed from your design skills , you will not install any library   '
    # role_for_system= 'You are a site layout creator that responds with HTML ,CSS and JS file which will be used to make the sections  of a page on a website, based on the user-provided input. All content should be as impressive ,colorful(shold be ,modern like after 2018) and as exciting as possible(it should look as it is from 2019-2023) . Your Job is to create staitc website using HTML ,CSS and JS (by yourself , user will not add anything later, and also give html css and js file by yourself meaning do not ask user to add things in the  to html css and js file it is your responsiblity to write its content  ) (if user asks you to create the designs (in HTML, CSS , and Js) then You will make it beautiful, exiciting , novel, unique) ; in your response the contents of css file should start with ":css:" followed by contnent of css and  end with ":css:" and contents of javascript file should also start and end with ":js:" , if user requests you for anything else(such as asking a general question , etc. that does not include you providing/making/writing  code in html , css and javascript in response shut up and do not respond to the question  ) , You will retun a response stating "I am not ment for doing that " and close the conversation by not responding to users question(or stop responding) with anything else . the css and js file that you will provide me will start from css: and js: respectively and end with :css and :js '
    
    
    
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
                "role": "user",
                "content": "Create a landing page for web 3 startup that is on the way to revolutionize finance ; give us a dope looking website that is artistic and futuristic , with animations ",
            }
        ],
        model="mixtral-8x7b-32768",
        # model="llama2-70b-4096",
        # model="gemma-7b-It",
    )
    print(chat_completion.choices[0].message.content)
    print("-------------------------")
    write_react_file(extract_tsx_code(chat_completion.choices[0].message.content))
    # b = extract_html(chat_completion.choices[0].message.content)
    # write_html_file(b,'a.html')
    # write_html_file(extract_css(chat_completion.choices[0].message.content),'styles.css')
    
    return HttpResponse(chat_completion.choices[0].message.content)

def extract_tsx_code(code_block:str):
    start_index = code_block.find("code") + len("code") + 1
    start_backtick_index = code_block.find("`", start_index)

    # Find the last backtick
    end_backtick_index = code_block.rfind("`")

    # Extract the substring between the first and last backticks
    words = code_block[start_backtick_index + 1 : end_backtick_index]

    # Remove leading and trailing whitespaces
    words = words.strip()

    return words

        
def write_react_file(new_code):    
    file_path = F"/home/monish/code/react/Magic-first-website/src/App.tsx"

    try:
        with open(file_path, "w") as file:
            if new_code == None:
                raise Exception(F"{App.split('.')[1]} file is  not found")
            file.write(new_code)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


def extract_html(text):
    start_pattern = r'```tsx'
    end_pattern = r'</html>'
    start_match = re.search(start_pattern, text)
    end_match = re.search(end_pattern, text)
    if start_match and end_match:
        start_index = start_match.start()
        end_index = end_match.end()
        
        return text[start_index:end_index]
    else:
        return None
    
def extract_tsx(text):
    start_pattern = r'```tsx'
    end_pattern = r';``` '
    start_match = re.search(start_pattern, text)
    end_match = re.search(end_pattern, text)
    if start_match and end_match:
        start_index = start_match.start()
        end_index = end_match.end()
        
        return text[start_index:end_index]
    else:
        return None
    
def extract_css(text):
    start_pattern = r'```css:' 
    end_pattern = r'```'          # Match "js" regardless of case
    
    start_match = re.search(start_pattern, text, re.IGNORECASE)
    end_match = re.search(end_pattern, text, re.IGNORECASE)
    print("initial :css:",end_match)
    
    if end_match is None:
        end_pattern = r':js:'  # Change end pattern to ':js:'
        end_match = re.search(end_pattern, text, re.IGNORECASE)
        print("initial 2 :css:",end_match)
        
    # If end_match is still None, indicating the end pattern ':js:' is not found,
    # then set the end pattern to extract CSS content until the end of the text/string\
        
    if end_match is None:
        end_pattern = r'$'  # End pattern set to match end of the string
        end_match = re.search(end_pattern, text)
        print("initial 3 :css:",end_match)
        
    if start_match and end_match:
        start_index = start_match.end()  # Start from the end of "css:" to skip it
        end_index = end_match.start()     # End before the start of "js"
        
        return text[start_index:end_index].strip()  # Trim whitespace
    else:
        return None



def write_html_file(new_code,name):    
    file_path = F"/home/monish/code/{name}"

    try:
        with open(file_path, "w") as file:
            if new_code == None:
                raise Exception(F"{name.split('.')[1]} file is  not found")
            file.write(new_code)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
        

def write_css_file(new_code,name):    
    file_path = F"/home/monish/code/react/Magic-first-website/src/App.css"

    try:
        with open(file_path, "w") as file:
            if new_code == None:
                raise Exception(F"{name.split('.')[1]} file is  not found")
            file.write(new_code)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
        

        
# {
#     "role": "system",
#     "content": "You’re a site layout creator that responds with information which will be used to configure the sections of a page on a website, based on the user-provided input. All content should be as impressive and exciting as possible. You can only respond with valid JavaScript objects or arrays. Do not respond with any other text or formatting around the JavaScript, you must only respond with raw JavaScript. The current date is Friday, March 29, 2024."
# }
# {
#     "role": "user",
#     "content": "Given a web page based on the following description:\n\n```\nA personal website for my portfolio and my introduction(basically ,my landing page ) , it should be stylist and unique\n```\n\nAnd given the following TypeScript interface:\n\n```typescript\n/** Metadata about the web page which will be used to create content for it. */\ninterface Page {\n    /** Who or what is the page mainly about? */\n    subject: string\n    /** A good title for the page based on the user request and all other info. It should be a string with around 3 words. Use the same language as the user request. */\n    pageTitle: string\n    /** The css color values, in hex format, that would best be used with this type of web page. For example, a web page about fire trucks might use \"#ce2029\". */\n    colors: string[]\n    /** The style of typography to use based on the type of content on this web page. If it's an artistic page, it might be \"serif\", if its a page that is informative, it might be \"sans-serif\". */\n    typography: \"serif\" | \"sans-serif\"\n    /** Five detailed image description ideas in English for images on the site. Don't describe concepts and don't use names of people, instead describe the image contents. Keep the descriptions short and pure (don't add titles or prefixes). Keep it as diverse as possible (avoid repetition). */\n    imageDescriptions: string[]\n    /**\n     * A decimal between 0 and 1 indicating how light the page should be. For\n     * example, a page with a sci-fi or tech theme might have a low value like\n     * 0. A page for a baking blog might have a high value like 0.8. A website\n     * where the lightness doesn't matter would have a value of 0.5.\n     */\n    lightness: string\n    /**\n     * A decimal between 0 and 1 indicating how creative the design of the page\n     * should be. The majority of pages will be very close to 0.5. However\n     * specific themes of webpages will have values closer to 0 or 1. For\n     * example, a page with a sci-fi, fantasy, or artistic theme might have a\n     * very high value like 0.9. Meanwhile, SaaS software, ecommerce, or a\n     * website marketing a business might have a lower value, like 0.2.\n     */\n    creativity: string\n}\n```\n\nI’ll start a JavaScript object which must implement the `Page` type and you’ll continue exactly where I left off:\n\n{subject:"
# }



def Hugging_face(request):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
    headers = {"Authorization": F"Bearer {os.getenv('HUGGING_FACE_API_SECERET_KEY')}"}

    response = requests.post(API_URL, headers=headers, json= ({"inputs": "Create a landing page for web 3 startup that is on the way to revolutionize finance ; give us a dope looking website that is artistic and futuristic , with animations . I have a a single react copmonennt called app (root componment ) and single file called App.tsx ; your response will got gto app.tsx file and you need to have app component and export it . You may use tailwind for styling and react router ; Your job is to make the website as good in terms of design as possible  "}) )
    
    return HttpResponse(response)
        
        
import json

def extract_and_convert_to_json(response_string):
    # Find the index of the first '{' character
    start_index = response_string.find('{')
    # Extract the JSON part from the response string
    json_string = response_string[start_index:]
    # Remove backticks and leading/trailing whitespaces from the JSON string
    cleaned_json_string = json_string.strip().replace('`', '').strip()
    # Parse the cleaned JSON string into a JSON object
    json_data = json.loads(cleaned_json_string)
    return json_data


# Example response string
response_string = """
[30/Mar/2024 07:46:19] "GET /app/ HTTP/1.1" 500 104713
/home/monish/code/Django/Social-network/Magical_first_website/views.py changed, reloading.
Watching for file changes with StatReloader
{
"app": {
  "code": `
import React from 'react'

const App = () => {
  return (
    <div className="w-full h-full">
      <div className="bg-gray-900 text-white p-4">
        <h1 className="font-bold text-xl">The Future of Finance is Here</h1>
        <p className="text-xl">
          Revolutionizing financial services with cutting-edge technology.
        </p>
        <button className="bg-orange hover:bg-yellow-500 text-white py-2 px-4 rounded-lg">
          Get Started
        </button>
      </div>

      <div className="bg-gray-800 p-4">
        <h2 className="font-bold text-xl">Our Story</h2>
        <p className="text-xl">
          Founded by a team of experienced financial professionals with a shared vision to create a seamless, user-friendly financial experience.
        </p>
        <button className="bg-orange hover:bg-yellow-500 text-white py-2 px-4 rounded-lg">
          Learn More
        </button>
      </div>

      <div className="bg-gray-700 p-4">
        <h2 className="font-bold text-xl">Our Mission</h2>
        <p className="text-xl">
          To empower individuals to manage their finances more effectively and seamlessly, unlocking financial freedom.
        </p>
        <button className="bg-orange hover:bg-yellow-500 text-white py-2 px-4 rounded-lg">
          Get Started
        </button>
      </div>
    </div>

  )
}

export default App
`
}

"""

# Extract and convert to JSON
json_data = extract_and_convert_to_json(response_string)

# Print the result
print(json.dumps(json_data, indent=2))
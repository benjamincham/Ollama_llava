from openai import OpenAI
import base64

### Replace image_path with your image path
image_path = 'YOUR_IMAGE.jpg'

def image_to_base64_with_prefix(local_path):
    with open(local_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/jpeg;base64,{encoded_string}"


image_data = image_to_base64_with_prefix(image_path)

client = OpenAI(base_url="http://localhost:8000/v1", api_key="sk-1234")
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_data,
                    },
                },
                {"type": "text", "text": "how many girls are wearing blue?give me their coordinates"},
            ],
        }
    ]
)

print(response.choices[0].message.content)
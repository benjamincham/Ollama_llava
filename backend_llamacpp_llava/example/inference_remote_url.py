from openai import OpenAI

### Replace image_url with your image url
image_url = 'https://static1.straitstimes.com.sg/s3fs-public/styles/large30x20/public/articles/2017/04/13/singapore_lim_yaohui_0.jpg?VersionId=IYMtiyFDb_X01mgTxt1OlzFV_qQyIyLr&itok=uA13ZR2Q'

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
                        "url": image_url,
                    },
                },
                {"type": "text", "text": "Detect every humans in the image. Create an array for the results, For each human, append the coordinates in xmin,y_min,x_max and ymax format into the array."},
            ],
        }
    ],
)

print(response.choices[0].message.content)
import asyncio
from google import genai
from dotenv import load_dotenv
from fastmcp import Client
from PIL import Image
from io import BytesIO
import requests
import re

mcp_client = Client("http://localhost:8000/mcp")
gemini_client = genai.Client()

system_prompt = "You are an intelligent agent, you must provide your format in a json schema. Simply respond with the result as a json do not provide it in plaintext."

async def main():
    text = "Start"
    while text:
        text = input("What APOD would you like to see? ")
        async with mcp_client:
            response = await gemini_client.aio.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"Get me the APOD for {text}",
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[mcp_client.session],
                ),
            )
            print(response.text)
            pattern = re.compile(r"https://[^\s]+?\.jpg\b", re.IGNORECASE)
            url = pattern.findall(response.text)[0]
            response = requests.get(url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            image.show()

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
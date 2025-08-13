from fastmcp import FastMCP
from dotenv import load_dotenv
import utils
from typing import Annotated
from pydantic import Field

mcp = FastMCP("Nasa Servers")

@mcp.tool()
def get_apod(date:Annotated[str, Field(description="This must be formatted as %Y-%m-%d for example June 17th 2025 -> 2025-06-17 or June 17 2025 -> 2025-06-17 or 06/17/2025 -> 2025-06-17 or 6 17 2002 -> 2002-06-17")]) -> dict:
    return utils.fetch_apod_data(date=date)

if __name__ == "__main__":
    load_dotenv()
    mcp.run(transport="streamable-http", host="localhost", port=8000)
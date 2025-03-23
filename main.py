
from infrastructure.telegram.connect import main as tg_bot_main
from presentations.app import app
import asyncio
import uvicorn

async def main():
    asyncio.create_task(await tg_bot_main())
    asyncio.create_task(uvicorn.run(app))
    


if __name__ == "__main__":
    asyncio.run(main())

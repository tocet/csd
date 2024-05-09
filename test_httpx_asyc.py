import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://time.jsontest.com')
        print(response.text)

asyncio.run(main())
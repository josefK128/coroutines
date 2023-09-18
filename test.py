import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'https://www.example.com',
        'https://www.openai.com',
        'https://www.python.org'
    ]

    tasks = [fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)

    for url, response in zip(urls, responses):
        print(f"Response from {url}: {len(response)} characters")

if __name__ == "__main__":
    asyncio.run(main())

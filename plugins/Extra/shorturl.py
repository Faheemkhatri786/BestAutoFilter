# Module Added by @itzRenierb
# Coded by --> @RenierbBoTz

from pyrogram import Client, filters
import aiohttp
import validators  # Importing the validators library for URL validation

@Client.on_message(filters.command(["short"]))
async def short_cmnd(client, message):
    url = message.text.split(' ', 1)
    if len(url) < 2:
        await client.send_message(message.chat.id, "Please provide a valid URL. Usage: /short https://example.com")
        return

    url = url[1]

    # Validate the URL
    if not validators.url(url):
        await client.send_message(message.chat.id, "Please provide a valid absolute URL.")
        return

    tinyurl_api_url = f"http://tinyurl.com/api-create.php?url={url}"

    async with aiohttp.ClientSession() as session:
        async with session.get(tinyurl_api_url) as response:
            if response.status == 200:
                shortened_url = await response.text()
                await client.send_message(message.chat.id, f"Shortened URL: {shortened_url}", disable_web_page_preview=True)
            else:
                await client.send_message(message.chat.id, "An error occurred while shortening the URL. 🔗")

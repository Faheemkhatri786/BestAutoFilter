from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages, broadcast_messages_group
import asyncio
        
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
# https://t.me/GetTGLink/4178
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"╔════❰ Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ...❱═❍⊱❁۪۪\n║╭━━━━━━━━━━━━━━━➣\n║┣⪼𖨠 Tᴏᴛᴀʟ Usᴇʀs: `{total_users}`\n║┃\n║┣⪼𖨠 Cᴏᴍᴘʟᴇᴛᴇᴅ: `{done} / {total_users}`\n║┃\n║┣⪼𖨠 Sᴜᴄᴄᴇss: `{success}`\n║┃\n║┣⪼𖨠 Bʟᴏᴄᴋᴇᴅ: `{blocked}`\n║┃\n║┣⪼𖨠 Dᴇʟᴇᴛᴇᴅ: `{deleted}`\n║┃\n║┣⪼𖨠 Eʀʀᴏʀs Oᴄᴄᴜʀʀᴇᴅ: `0`\n║┃\n║┃⪼𖨠 ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs: `Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ`\n║╰━━━━━━━━━━━━━━━➣\n╚════❰<a href=https://t.me/Faheem21025492006>𒆜Oᴡɴᴇʀ Dᴇᴛᴀɪʟꜱ𒆜</a>❱══❍⊱❁۪۪", disable_web_page_preview=True)
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"╔════❰ Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ❱═❍⊱❁۪۪\n║╭━━━━━━━━━━━━━━━➣\n║┣⪼𖨠 Cᴏᴍᴘʟᴇᴛᴇᴅ Iɴ: `{time_taken} seconds`\n║┃\n║┣⪼𖨠 Tᴏᴛᴀʟ Usᴇʀs: `{total_users}`\n║┃║┣⪼𖨠 Cᴏᴍᴘʟᴇᴛᴇᴅ: `{done} / {total_users}`\n║┃\n║┣⪼𖨠 Sᴜᴄᴄᴇss: `{success}`\n║┃\n║┣⪼𖨠 Bʟᴏᴄᴋᴇᴅ: `{blocked}`\n║┃\n║┣⪼𖨠 Dᴇʟᴇᴛᴇᴅ: `{deleted}`\n║┃\n║┣⪼𖨠 Eʀʀᴏʀs Oᴄᴄᴜʀʀᴇᴅ: `0`\n║┃\n║┃⪼𖨠 ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs: `Cᴏᴍᴘʟᴇᴛᴇᴅ`\n║╰━━━━━━━━━━━━━━━➣\n║┃\n╚════❰<a href=https://t.me/Faheem21025492006>𒆜Oᴡɴᴇʀ Dᴇᴛᴀɪʟꜱ𒆜</a>❱══❍⊱❁۪۪", disable_web_page_preview=True)

@Client.on_message(filters.command("grp_broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_group(bot, message):
    groups = await db.get_all_chats()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ʏᴏᴜʀ ᴍᴇssᴀɢᴇs ᴛᴏ ɢʀᴏᴜᴘs...'
    )
    start_time = time.time()
    total_groups = await db.total_chat_count()
    done = 0
    failed =0

    success = 0
    async for group in groups:
        pti, sh = await broadcast_messages_group(int(group['id']), b_msg)
        if pti:
            success += 1
        elif sh == "Error":
                failed += 1
        done += 1
        if not done % 20:
            await sts.edit(f"╔════❰ Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ...❱═❍⊱❁۪۪\n║╭━━━━━━━━━━━━━━━➣\n║┣⪼𖨠 Tᴏᴛᴀʟ Gʀᴏᴜᴘs: `{total_groups}`\n║┃\n║┣⪼𖨠 Cᴏᴍᴘʟᴇᴛᴇᴅ: `{done} / {total_groups}`\n║┃\n║┣⪼𖨠 Sᴜᴄᴄᴇss: `{success}`\n║┃\n║┣⪼𖨠 Eʀʀᴏʀs Oᴄᴄᴜʀʀᴇᴅ: `0`\n║┃\n║┃⪼𖨠 ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs: `Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ`\n║┃\n║╰━━━━━━━━━━━━━━━➣\n╚════❰<a href=https://t.me/Faheem21025492006>𒆜Oᴡɴᴇʀ Dᴇᴛᴀɪʟꜱ𒆜</a>❱══❍⊱❁۪۪", disable_web_page_preview=True) 
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"╔════❰ Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ❱═❍⊱❁۪۪\n║╭━━━━━━━━━━━━━━━➣\n║┣⪼𖨠 Cᴏᴍᴘʟᴇᴛᴇᴅ Iɴ: `{time_taken} seconds`\n║┃\n║┣⪼𖨠 Tᴏᴛᴀʟ Gʀᴏᴜᴘs: `{total_groups}`\n║┃\n║┣⪼𖨠 Cᴏᴍᴘʟᴇᴛᴇᴅ: `{done} / {total_groups}`\n║┃\n║┣⪼𖨠 Sᴜᴄᴄᴇss: `{success}`║┣⪼𖨠 Sᴜᴄᴄᴇss: `{success}`\n║┃\n║┣⪼𖨠 Eʀʀᴏʀs Oᴄᴄᴜʀʀᴇᴅ: `0`\n║┃\n║┃⪼𖨠 ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs: `Cᴏᴍᴘʟᴇᴛᴇᴅ`\n║╰━━━━━━━━━━━━━━━➣ \n╚════❰<a href=https://t.me/Faheem21025492006>𒆜Oᴡɴᴇʀ Dᴇᴛᴀɪʟꜱ𒆜</a>❱══❍⊱❁۪۪", disable_web_page_preview=True)
        

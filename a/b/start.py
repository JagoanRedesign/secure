import os, asyncio, time, sys, re
from pyrogram import *
from pyrogram.types import *

SUDO_USERS = 1963422158
BOT = "chatbot"
TAI = "CAACAgUAAxkBAAEDrzBjUo9j31j-w3ufERk9urif_pUjPgACFgkAAlmwmFYy2cZceSTp4CoE"
counts = 900
LOG = -1001879930806

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ok"], prefixes="."))
async def start_spambot(c: Client, m: Message):
  try:
    await c.send_message(LOG, "GUA UDH JALAN")
    for _ in range(counts):
      await c.send_message(BOT, "/next")
      await asyncio.sleep(6)
      await c.send_sticker(BOT, TAI)
      await asyncio.sleep(2)
      await c.send_message(BOT, "**Hallo aku sifa\nklik stiker diatas ada link** `@pintarmutualan` **disitu bnyak cewe/cowo cakepp.**")
      await asyncio.sleep(3)
  except Exception as e:
    await c.send_message(LOG, f"**ERROR:** `{str(e)}`")
    return

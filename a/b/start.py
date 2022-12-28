from vanostraspam import HNDLR, SUDO_USERS

BOT = "chatbot"
TAI = "CAACAgUAAxkBAAEDrzBjUo9j31j-w3ufERk9urif_pUjPgACFgkAAlmwmFYy2cZceSTp4CoE"
counts = 900
LOG = -1001879930806

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes="."))
async def main(c: Client, m: Message):
  try:
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

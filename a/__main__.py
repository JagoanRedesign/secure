from pyrogram import idle
from uvloop import install
from a import bots, LOOP

async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("siapataudia")
        except Exception as a:
            print(f"{a}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    install()
    LOOP.run_until_complete(main())

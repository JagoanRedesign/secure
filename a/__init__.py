import asyncio
from pyrogram import Client
from config import *
from aiohttp import ClientSession

LOOP = asyncio.get_event_loop()
aiosession = ClientSession()
bot1 = (
    Client(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION1,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION1
    else None
)

bot2 = (
    Client(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION2,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION2
    else None
)

bot3 = (
    Client(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION3,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION3
    else None
)

bot4 = (
    Client(
        name="bot4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION4,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION4
    else None
)

bot5 = (
    Client(
        name="bot5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION5,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION5
    else None
)

bot6 = (
    Client(
        name="bot6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION6,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION6
    else None
)

bot7 = (
    Client(
        name="bot7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION7,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION7
    else None
)

bot8 = (
    Client(
        name="bot8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION8,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION8
    else None
)

bot9 = (
    Client(
        name="bot9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION9,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION9
    else None
)

bot10 = (
    Client(
        name="bot10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION10,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION10
    else None
)

bot11 = (
    Client(
        name="bot11",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION11,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION11
    else None
)

bot12 = (
    Client(
        name="bot12",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION12,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION12
    else None
)

bot13 = (
    Client(
        name="bot13",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION13,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION13
    else None
)

bot14 = (
    Client(
        name="bot14",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION14,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION14
    else None
)

bot15 = (
    Client(
        name="bot15",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION15,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION15
    else None
)

bot16 = (
    Client(
        name="bot16",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION16,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION16
    else None
)

bot17 = (
    Client(
        name="bot17",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION17,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION17
    else None
)

bot18 = (
    Client(
        name="bot18",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION18,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION18
    else None
)

bot19 = (
    Client(
        name="bot19",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION19,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION19
    else None
)

bot20 = (
    Client(
        name="bot20",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION20,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION20
    else None
)

bot21 = (
    Client(
        name="bot21",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION21,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION21
    else None
)

bot22 = (
    Client(
        name="bot22",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION22,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION22
    else None
)

bot23 = (
    Client(
        name="bot23",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION23,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION23
    else None
)

bot24 = (
    Client(
        name="bot24",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION24,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION24
    else None
)

bot25 = (
    Client(
        name="bot25",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION25,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION25
    else None
)

bot26 = (
    Client(
        name="bot26",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION26,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION26
    else None
)

bot27 = (
    Client(
        name="bot27",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION27,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION27
    else None
)

bot28 = (
    Client(
        name="bot28",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION28,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION28
    else None
)

bot29 = (
    Client(
        name="bot29",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION29,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION29
    else None
)

bot30 = (
    Client(
        name="bot30",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION30,
        plugins=dict(root="a/b"),
    )
    if STRING_SESSION30
    else None
)

bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, bot11, bot12, bot13, bot14, bot15, bot16, bot17, bot18, bot19, bot20, bot21, bot22, bot23, bot24, bot25, bot26, bot27, bot28, bot29, bot30] if bot]

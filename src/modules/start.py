from pymongo import MongoClient
from config import MONGO_DB_URI
import asyncio
import random
import os

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from src.database.chats_db import add_served_chat
from src import app

DATABASE = MongoClient(MONGO_DB_URI)
db = DATABASE["MAIN"]["USERS"]
collection = db["members"]

def add_user_database(user_id: int):
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})


@app.on_message(filters.new_chat_members, group=69)
async def tgkichudai(client, message):
    for member in message.new_chat_members:
        if member.id == client.me.id:
            await add_served_chat(message.chat.id)
            await message.reply("ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ !")


@app.on_message(filters.command("start"))
async def start(_, m: Message):
    add_user_database(m.from_user.id)
    await m.reply_photo("https://telegra.ph/file/a0d157254f58e0d1a8850.jpg", caption=f"""🥀 ʜᴇʏ {m.from_user.mention},\n\nᴛʜɪs ɪs {app.me.mention},\nᴛʜᴇ ᴍᴏsᴛ ᴜsᴇʟᴇss ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ.""",
                         reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ", url=f"https://t.me/{app.me.username}?startgroup=new")],
        [InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="help"), InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", callback_data="source_lele")]
    ]))

@app.on_callback_query(filters.regex("help"))
async def cb_func_help(_, query: CallbackQuery):
    await query.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ᴀɪ", callback_data="unx_ai"), InlineKeyboardButton(text="ɪᴍᴀɢᴇ ᴀɪ", callback_data="unx_imageai"), InlineKeyboardButton(text="ᴍɪᴅ ᴀɪ", callback_data="unx_midai")],
            [InlineKeyboardButton(text="ᴀʟɪᴠᴇ", callback_data="unx_alive"), InlineKeyboardButton(text="ᴇᴄʜᴏ", callback_data="unx_echo"), InlineKeyboardButton(text="ғɪɢʟᴇᴛ", callback_data="unx_figlet")],
            [InlineKeyboardButton(text="ɪᴍɢ", callback_data="unx_img"), InlineKeyboardButton(text="ᴘɪɴɢ", callback_data="unx_ping"), InlineKeyboardButton(text="ǫᴏᴜᴛʟʏ", callback_data="unx_qoutly")],
            [InlineKeyboardButton(text="sʜᴏʀᴛ ᴜʀʟ", callback_data="unx_shorturl"), InlineKeyboardButton(text="sᴛᴀʀᴛ", callback_data="unx_start_help"), InlineKeyboardButton(text="sɴᴀᴍᴇ", callback_data="unx_sname")],
            [InlineKeyboardButton(text="ʏᴏᴜᴛᴜʙᴇ", callback_data="unx_yt"), InlineKeyboardButton(text="ᴇᴅɪᴛᴍᴏᴅᴇ", callback_data="unx_editmode"), InlineKeyboardButton(text="sᴏɴɢ", callback_data="ux_song")],
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="go_back_to_start"), InlineKeyboardButton(text="ᴡᴇʙss", callback_data="unx_webss")]]))

@app.on_callback_query(filters.regex("unx_ai"))
async def cb_func_ai(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /ai : ᴜꜱᴇ ꜰʀᴇᴇ ᴀɪ ᴡɪᴛʜᴏᴜᴛ ᴀᴘɪ ᴋᴇʏ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))
        
@app.on_callback_query(filters.regex("unx_imageai"))
async def cb_func_imageai(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /imagine : ɢɪᴠᴇ ᴘʀᴏᴍᴘᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ 𝟾ᴋ ᴀɪ ɪᴍᴀɢᴇs.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_midai"))
async def cb_func_midai(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /mid : ɢɪᴠᴇ ᴘʀᴏᴍᴘᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴍɪᴅ ᴀɪ ɪᴍᴀɢᴇs.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_alive"))
async def cb_func_alive(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /alive : sʜᴏᴡs ᴛʜᴇ ᴀʟɪᴠᴇ sᴛᴀᴛᴜs ᴏғ ᴛʜᴇ ʙᴏᴛ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_echo"))
async def cb_func_imageai(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /echo : sᴇɴᴅs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))
    
@app.on_callback_query(filters.regex("unx_figlet"))
async def cb_func_figlet(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /figlet : ɢᴇɴᴇʀᴀᴛᴇs ᴀ ғɪɢʟᴇᴛ ᴏғ ɢɪᴠᴇɴ ɴᴀᴍᴇ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_img"))
async def cb_func_img(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /img : sʜᴏᴡs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ɪᴍᴀɢᴇ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_ping"))
async def cb_func_ping(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /ping : sʜᴏᴡs ᴛʜᴇ ᴘɪɴɢ ʟᴀᴛᴇɴᴄʏ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_qoutly"))
async def cb_func_qoutly(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /q : ᴍᴀᴋᴇ's ᴀ ǫᴜᴏᴛᴇ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_shorturl"))
async def cb_func_shorturl(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /shorturl : sʜᴏʀᴛᴇɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴜʀʟ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_start_help"))
async def cb_func_starthelp(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /start : sᴛᴀʀᴛs ᴍᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴍʏ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))
    
@app.on_callback_query(filters.regex("unx_sname"))
async def cb_func_sname(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /sname : ᴅᴇᴄᴏᴅᴇs ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ᴡɪᴛʜ ᴜɴɪᴅᴇᴄᴏᴅᴇ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_yt"))
async def cb_func_unxyt(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /yt : ʟɪɴᴋ ᴏʀ ɴᴀᴍᴇ ᴏғ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))
    
@app.on_callback_query(filters.regex("unx_editmode"))
async def cb_func_editmode(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /editmode : ᴇᴅɪᴛᴍᴏᴅᴇ ᴏɴ/ᴏғғ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴇᴅɪᴛᴇᴅ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ɢʀᴏᴜᴘs.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("ux_song"))
async def cb_func_song(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /song : ᴜsᴇ sᴏɴɢ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴍᴜsɪᴄ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("unx_webss"))
async def cb_func_webss(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /webss : ᴄᴀᴘᴛᴜʀᴇs ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ sɪᴛᴇ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help")]]))

@app.on_callback_query(filters.regex("go_back_to_start"))
async def cb_func_back(_, query: CallbackQuery):
    check_user = collection.find_one({"user_id": query.from_user.id})
    if not check_user:
        add_user_database(query.from_user.id)
    await query.message.edit_text(text=f"""🥀 ʜᴇʏ {query.from_user.mention},\n\nᴛʜɪs ɪs {app.me.mention},\nᴛʜᴇ ᴍᴏsᴛ ᴜsᴇʟᴇss ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ.""",        
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ", url=f"https://t.me/{app.me.username}?startgroup=new")
                    ],
                    [
                        InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="help"),
                        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", callback_data="source_lele")
                    ]
                ]
            )
    )


@app.on_callback_query(filters.regex("source_lele"))
async def cb_func_sourcelele(_, query: CallbackQuery):
    await query.edit_message_media(media="CgACAgQAAx0CfK48pwABAe7hZiShdptz-vg7wf9j1a4C7XX6c_8AAtcCAALPLw1TdAXNVQkONjseBA", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="go_back_to_start")]]))

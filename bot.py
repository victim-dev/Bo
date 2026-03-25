# bot.py

import asyncio
import time
import logging
import traceback

from pyrogram import idle
from core.client import app
from core.logger import log
from core.crash import install_crash_handler
from core.loader import load_modules

# Silence verbose logs (keep as is)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session").setLevel(logging.WARNING)
logging.getLogger("pyrogram.dispatcher").setLevel(logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.WARNING)

async def main():
    log.info("🚀 Starting Userbot...")
    install_crash_handler()

    await app.start()
    log.info("✅ Client started")

    me = await app.get_me()
    app.owner_id = me.id
    app.start_time = time.time()

    log.info(f"👤 Logged in as: {me.first_name} (@{me.username})")
    log.info(f"🆔 Owner ID: {app.owner_id}")

    # Load modules (this also updates LOADED_MODULES and FAILED_MODULES)
    await load_modules(app)

    log.info("🔥 Bot is fully operational")
    log.info("💡 Use .help to see modules")

    await idle()

    log.info("🛑 Shutting down...")
    await app.stop()
    log.info("❌ Bot stopped")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Stopped manually.")
    except Exception:
        print("💥 Fatal error:\n", traceback.format_exc())
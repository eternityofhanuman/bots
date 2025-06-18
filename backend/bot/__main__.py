import asyncio
from telegram.ext import Application
from .handlers.start import start_handler
from .handlers.marketplace import offer_handler
from .handlers.escrow import escrow_handler
from .handlers.fees import advance_fee_handler
from .handlers.support import support_handler, register_support_handlers
from .handlers.offer_search import search_offer_handler
from .handlers.support_ticket import submit_ticket_handler
from .handlers.wallet_balance import wallet_balance_handler
from .config import Config

def main():
    """Bot entrypoint."""
    application = Application.builder().token(Config.TELEGRAM_TOKEN).build()
    application.add_handler(start_handler)
    application.add_handler(offer_handler)
    application.add_handler(escrow_handler)
    application.add_handler(advance_fee_handler)
    # Register support and extra handlers
    register_support_handlers(application)

    print("Bot is running. Press Ctrl+C to exit.")
    application.run_polling()

if __name__ == "__main__":
    main()

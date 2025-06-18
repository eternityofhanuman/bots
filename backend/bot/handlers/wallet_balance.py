from telegram.ext import MessageHandler, filters
from ..blockchain.wallet import WalletManager

async def wallet_balance(update, context):
    text = update.message.text.strip().split()
    if len(text) < 2:
        await update.message.reply_text("Please provide the currency and address in your message.\nकृपया करेंसी और एड्रेस भेजें।")
        return
    currency, address = text[0], text[1]
    balance = WalletManager.get_wallet_balance(currency, address)
    await update.message.reply_text(f"Balance for {address} ({currency}): {balance}\n\nयह आपके वॉलेट का बैलेंस है।")

wallet_balance_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, wallet_balance)

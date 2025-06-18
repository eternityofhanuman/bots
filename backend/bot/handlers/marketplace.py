from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler
from ..marketplace.offer import create_offer

async def offer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Parse conversational intent (e.g., "I want to sell 0.1 BTC")
    args = context.args
    # ...parse args for offer details...
    offer = await create_offer(update.effective_user.id, args)
    # Professional, trust-building message
    msg = (
        f"Thank you for choosing our escrow service!\n"
        f"Your offer for {offer['amount']} {offer['currency']} has been created.\n\n"
        "हमारी टीम आपके लेन-देन को सुरक्षित और तेज़ बनाती है।\n"
        "We ensure your transaction is safe and fast.\n\n"
        "To proceed, please confirm your intent. Once you are ready, we will provide the advance fee details.\n"
        "(Advance fee is required only at the final step, after you are satisfied with our process.)"
    )
    keyboard = [
        [InlineKeyboardButton("Proceed to Advance Fee", callback_data=f"pay_fee_{offer['id']}")]
    ]
    await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))

offer_handler = CommandHandler("offer", offer)

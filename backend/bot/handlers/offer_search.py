from telegram.ext import MessageHandler, filters, ConversationHandler
from telegram import ReplyKeyboardMarkup
from ..models.offer import Offer

# Conversation states
ASK_TYPE, ASK_AMOUNT, SHOW_OFFERS = range(3)

async def start_offer_search(update, context):
    reply_keyboard = [["Buy", "Sell"]]
    await update.message.reply_text(
        "Welcome! What would you like to do today?\n\n" +
        "आप क्या करना चाहते हैं? (Buy/Sell)\n\n" +
        "Please choose:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return ASK_TYPE

async def ask_amount(update, context):
    context.user_data['type'] = update.message.text
    await update.message.reply_text(
        "How much USDT do you want to buy or sell?\n\n" +
        "आप कितने USDT खरीदना या बेचना चाहते हैं?\n\n" +
        "Please enter the amount:"
    )
    return ASK_AMOUNT

async def show_offers(update, context):
    amount = update.message.text
    context.user_data['amount'] = amount
    offer_type = context.user_data.get('type', 'Buy')
    # Search offers (simple filter by type and amount)
    offers = Offer.objects.filter(amount=float(amount), status="open")[:3]
    if not offers:
        await update.message.reply_text(
            "No matching offers found.\nकोई ऑफर नहीं मिला। Please try a different amount."
        )
        return ConversationHandler.END
    msg = (
        f"Here are some {offer_type.lower()} offers for {amount} USDT:\n\n"
    )
    for offer in offers:
        msg += f"ID: {offer.offer_id}, {offer.amount} {offer.currency}, Status: {offer.status}\n"
    msg += ("\nIf you want to proceed, just reply 'Yes'.\n"
             "अगर आप आगे बढ़ना चाहते हैं, तो 'Yes' लिखें।")
    await update.message.reply_text(msg)
    return SHOW_OFFERS

async def end_offer_search(update, context):
    await update.message.reply_text(
        "Thank you for using our escrow service!\n\n"
        "धन्यवाद!\n\n"
        "If you want to start again, just type anything."
    )
    return ConversationHandler.END

search_offer_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex("(?i)(buy|sell)"), start_offer_search)],
    states={
        ASK_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_amount)],
        ASK_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, show_offers)],
        SHOW_OFFERS: [MessageHandler(filters.Regex("(?i)yes"), end_offer_search)],
    },
    fallbacks=[MessageHandler(filters.ALL, end_offer_search)],
)

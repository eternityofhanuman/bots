from fastapi import FastAPI
from .routes import offer, wallet, fee, support

app = FastAPI(
    title="Crypto Escrow Backend API",
    description="API for managing offers, wallets, fees, and support."
)

app.include_router(offer.router, prefix="/api/offers")
app.include_router(wallet.router, prefix="/api/wallets")
app.include_router(fee.router, prefix="/api/fees")
app.include_router(support.router, prefix="/api/support")

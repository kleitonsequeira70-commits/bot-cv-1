import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# O token gerado pelo BotFather (vip_capeverd_bot)
TOKEN = "8834388263:AAE4ne1XZdW7ANAKgoTo7m4bE5nu9R6FjTk"

async def bacbo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Comando para enviar o sinal do Bac Bo:
    Exemplo: /bacbo Vermelho ou /bacbo Azul ou /bacbo Empate
    """
    args = context.args
    if not args:
        await update.message.reply_text(
            "⚠️ **Uso incorreto!**\n"
            "Exemplo de uso correto:\n"
            "`/bacbo Vermelho`\n"
            "`/bacbo Azul`\n"
            "/bacbo Empate",
            parse_mode="Markdown"
        )
        return
    
    # Pega a cor/aposta informada
    aposta = " ".join(args).capitalize()
    
    mensagem = (
        "🎲 *NOVO SINAL - BAC BO* 🎲\n\n"
        f"🔴🔵 *Entrada Confirmada:* {aposta}\n"
        "🎯 *Estratégia:* Proteção no Empate recomendada\n\n"
        "🔗 *Disponível no Casino ao Vivo (Bet365)*\n"
        "⚠️ Gerencie sua banca com responsabilidade!"
    )
    
    await update.message.reply_text(mensagem, parse_mode="Markdown")

if _name_ == "_main_":
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Adiciona o comando /bacbo
    app.add_handler(CommandHandler("bacbo", bacbo))
    
    print("Bot do Bac Bo rodando e pronto para receber comandos...")
    app.run_polling()

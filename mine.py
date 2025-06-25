import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext

# 🔐 Własny token z @ApteczkaDDLBOT
 # ← Zmień na swój

# Usunięto źle wcięte i nieprzypisane cytaty

# Logi
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Komenda /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hej... czemu mnie budzisz? 😩")

# Odpowiedź losowa w stylu Piwnicy
def echo(update: Update, context: CallbackContext) -> None:
    odpowiedz = random.choice(ODPOWIEDZI)
    update.message.reply_text(odpowiedz)

# Główna funkcja
def main():
    # Stworzenie instancji Updatera i Dispatchera
    app = ApplicationBuilder().token("8182943260:AAFYRmPOFHZxUlSVciqP5FAFJ9g9UpMXEdo").build()
    # Komendy Piwnicy
    app.add_handler(CommandHandler("start", start))
    # Upewnij się, że funkcje status, skrot, aparta, fredro, krzysiek, drop, adam, kebabdom, piwnica są zdefiniowane
    # W obecnym kodzie nie są, co spowoduje NameError. Dodałem przykładowe definicje poniżej.
    # Jeśli masz już te funkcje w innych komórkach, możesz usunąć te przykładowe.
#     # Pamiętaj, aby wszystkie funkcje handlerów były zdefiniowane PRZED wywołaniem main().
#     # app.add_handler(CommandHandler("status", status)) # Funkcja 'status' nie zdefiniowana
#     #app.add_handler(CommandHandler("skręt",  skręt))
#     app.add_handler(CommandHandler("aparta", aparta))
#     app.add_handler(CommandHandler("fredro", fredro))
#     app.add_handler(CommandHandler("krzysiek", krzysiek))
#     app.add_handler(CommandHandler("drop", drop))
#     app.add_handler(CommandHandler("adam", adam))
#     app.add_handler(CommandHandler("kebabdom", kebabdom))
#     app.add_handler(CommandHandler("piwnica", piwnica))
# 
#     # Odpowiedź na zwykłe wiadomości (opcjonalnie)
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, main_handler))
    # Zauważyłem, że sekcja main jest powtórzona. Usunąłem duplikat i połączyłem handlery.

    #updater.start_polling()
    print("🟢 Bot działa i mówi jak z Piwnicy!")
    app.run_polling()

# Przykładowe definicje funkcji handlerów, jeśli nie są zdefiniowane gdzie indziej
# Jeśli masz je zdefiniowane w innych komórkach, usuń poniższy blok
def status(update: Update, context: CallbackContext):
    update.message.reply_text("Status: Działam!")

def skrot(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(SKRĘT_QUOTES))

def aparta(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(APARTA_QUOTES))

def fredro(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(FREDRO_QUOTES))

def krzysiek(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(KRZYSIEK_QUOTES))

def drop(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(DROP_QUOTES))

def adam(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(ADAM_QUOTES))

def kebabdom(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(KEBABDOM_QUOTES))

def piwnica(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(ODPOWIEDZI))

def main_handler(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if any(słowo in text for słowo in ["głodny", "zmęczony", "nie mam", "spalony"]):
        update.message.reply_text(random.choice(KEBABDOM_QUOTES))
    else:
        update.message.reply_text(random.choice(ODPOWIEDZI))  # fallback


# --- Historie Piwnicy ---
# Upewnij się, że te listy są zdefiniowane PRZED wywołaniem funkcji, które ich używają (np. main)
SKRĘT_QUOTES = [
    "Mam skręta czy nie mam już?",
    "To był ostatni skręt... życie stracone.",
    "Nie wiem, co jeszczesz gadać... wszystko wiruje."
]
APARTA_QUOTES = [
    "Nie ma nic na Aparta, wyrzucają nas!",
    "Kto zamknął drzwi?! Adam! Otwórz!",
    "W Apartach jest gorzej niż w mojej głowie."
]

FREDRO_QUOTES = [
    "Oddajesz mi apteczkę. Teraz.",
    "Fredro nie pyta. Fredro patrzy. Fredro zabiera apteczkę.",
    "Za słaby temat. Apteczka wraca do mnie."
]

KRZYSIEK_QUOTES = [
    "Dałem iPad za 70 zł... bo nie było co jeść. Teraz chcę 120 zł.",
    "iPad to nie tylko gadżet. To symbol naszej wspólnej traumy.",
    "Nie jestem wkurzony. Jestem strategiczny."
]

DROP_QUOTES = [
    "Adam jedzie po dropa!",
    "Drop był... ale nie ten.",
    "Nie ma już żadnego dropa. Tylko puste opakowania."
]

ADAM_QUOTES = [
    "Jadę po dropa... ale nie wiem gdzie to jest.",
    "Makatusin działa na wszystko. Nawet na dryf.",
    "Fredro mnie ignoruje. Krzysiek chce iPad. A ja chcę tylko... normalności."
]

KEBABDOM_QUOTES = [
    "Mieszkam w Kebab Dom. To nie jest kebab. To jest katedra.",
    "Nie pamiętam, jak tu trafiłem. Ale bułka była ciepła.",
    "W Kebab Dom nie ma reguł. Tylko menu. I jeszcze jeden stół, który się chwieje."
]

# Cała lista do losowych odpowiedzi
ODPOWIEDZI = SKRĘT_QUOTES + APARTA_QUOTES + FREDRO_QUOTES + KRZYSIEK_QUOTES + DROP_QUOTES + ADAM_QUOTES + KEBABDOM_QUOTES


if __name__ == '__main__':
    main()
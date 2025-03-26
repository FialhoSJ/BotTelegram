import telebot

chave_API = "7808569120:AAEAGDUrR-89Khc7NTUo4XZJq5l6piGSU08"
bot = telebot.TeleBot(chave_API)

@bot.message_handler(commands=["sobre"])
def sobre(mensagem):
    texto_sobre = """
🚀 Meus Interesses:

    📊 Ciência de Dados & 🤖 Machine Learning: Explorando dados e criando soluções inteligentes!

    💻 Simulação Computacional & 🧮 Modelagem Matemática: Resolvo problemas complexos com matemática e tecnologia.

    🔧 Desenvolvimento de Software & ⚙️ Algoritmos: Criando soluções inovadoras para desafios do dia a dia.

    🌱 Energias Renováveis & ♻️ Sustentabilidade: Buscando soluções mais verdes e sustentáveis para o futuro.

    🌐 Criação de Sistemas & 💻 Sites Web: Transformando ideias em realidade na web.

**🔬 Grupo de Pesquisa:**
Sou membro do **Grupo de Pesquisa Gradiente de Modelagem Matemática e Simulação Computacional (GMSC)**. Meu objetivo é continuar contribuindo para o avanço do conhecimento e para o desenvolvimento de soluções tecnológicas que impactem positivamente nossa sociedade.
    """
    bot.reply_to(mensagem, texto_sobre)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Oi! 👋 Me encontre nas minhas redes sociais:

    Instagram 📸: https://www.instagram.com/_fialhosj_/.

    LinkedIn 💼: https://www.linkedin.com/in/felipe-fialho-915515299/.

    GitHub 💻: https://github.com/FialhoSJ.

    Lattes 📚:  http://lattes.cnpq.br/9739668942108635.

    Não perca nada, me siga por lá! 😉
    
    Para saber mais sobre mim, clique em /sobre
    """
    bot.reply_to(mensagem, texto)

bot.polling()
import discord
from discord.ext import commands
import os
import smtplib
from email.mime.text import MIMEText

Hello = {"привет", "дарова", "здравствуй"}
client = discord.Client()
bot = commands.Bot(command_prefix='*', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Я готов сэр!!!')

@bot.command()
async def on_member_join(member):
    await member.send(f'Здравствуйте ,я могу выполнять команды, но для того что бы их вызвать перед командай нужно поставить "*"')
    await member.send(f'Команды:\n1.тест-Создана для проверки работаю ли я.\n2.Jarvis-эта команда вызывает это сообщение.\n3.абгрэйд-эта команда-инструкция по усовершенствования меня.\n4.абгрэйдап-команда котороя сввязывает вас с разработчикам(при использованиии этой команды не по назначению будет бан.\n')

@bot.command()
async def тест(ctx):
    await ctx.send('Всё ок')

@bot.command()
async def абгрэйд(ctx):
    await ctx.send(f'Для того что бы дать мне абгэид вам нужно написать "*абгрэйдап" и дальше через пробел команды для абгрэйда например:\n"абгрэйдап хочуи добавить команду рандом котороя будет выдовать рандомное чесло от 1 до 100"')

@bot.command()
async def абгрэйдап(ctx, *, arg):
    def send_email(message):
        sender = 'adgar335@gmail.com'
        pasword = 'cdtnrf335576'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        try:
            server.login(sender, pasword)
            msg = MIMEText(message)
            msg['Subject'] = 'Новые команды бота'
            server.sendmail(sender, sender, msg.as_string())


            return 'Сообщение отправлено'
        except Exception as _ex:
            return f'{_ex}\nПроверьте вашь логин или пароль!'

    def main():
        message = arg
        print(send_email(message=message))

    if __name__=='__main__':
        main()
    await ctx.send('Я отправил это разработчику он посмотрит и ответит вам')


@bot.command()
async def Jarvis(ctx):
    await ctx.send(f'Здравствуйте {ctx.author.name},я могу выполнять команды, но для того что бы их вызвать перед командай нужно поставить "*"')
    await ctx.send(f'Команды:\n1.тест-Создана для проверки работаю ли я.\n2.Jarvis-эта команда вызывает это сообщение.\n3.абгрэйд-эта команда-инструкция по усовершенствования меня.\n4.абгрэйдап-команда котороя сввязывает вас с разработчикам(при использованиии этой команды не по назначению будет бан.\n')


bot.run('OTQ3NDA4NjA1NjI2Mzg4NDkw.Yhs1BQ.6_e7MGOd23FO1qa8ivRrkZBKKMg')
#bot.run(os.getenv('TOKEN'))
# coding=<UTF-8>
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import discord
import time
import sys
import itertools
import datetime
import os

client = discord.Client()

bot_token = os.environ['BOT_TOKEN']

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='p!help | Pohanka bot'))
    verze = str(sys.version)
    verze = verze[:5]
    now = datetime.datetime.now()
    cas = "Čas - {}:{}:{}".format(now.hour, now.minute, now.second)
    datum = "Datum - {}.{}.{}".format(now.day, now.month, now.year)
    print("\n___________________________________________________________________________________")
    print("\n                                  |BOT PŘIHLÁŠEN|                                  ")
    print("___________________________________________________________________________________")
    print("\n>", datum, "|", cas)
    print("> Jméno -", client.user.name)
    print("> ID -", client.user.id)
    print("___________________________________________________________________________________")
    print("\n> Verze discord.py - ", discord.__version__)
    print("> Verze pythonu - ", verze)
    print("___________________________________________________________________________________")
    print("\n> Autor: Arbys")
    print("> ID - 228937604723113984")
    print("___________________________________________________________________________________")
    print("\n[ log: ]\n")
@client.event
async def on_message(message):
    import random
    import time
    import json
    import datetime
    now = datetime.datetime.now()
    if message.author.id in open("bany.txt").read():
        banned = ":x: **|** Nemůžeš použít tento příkaz, jsi **zabanován**!"
        await client.send_message(message.channel, banned)
    else:
        if message.content.startswith("p!help") or message.content.startswith("!Help") or message.content.startswith("!HELP"):
            em = discord.Embed(title=':robot: **|**  Všechny příkazy Pohanka BOTA:', colour=0xcc0000)
            await client.send_message(message.channel, embed=em)
            await client.send_message(message.channel, "**Prefix** • `p!`\n\n**Příkazy** • `p!help` **|** `p!about` **|** `p!img` **|** `p!recept` **|** `p!fakt` **|** `p!sebrat` **|** `p!inv` **|** `p!top`\n\n*Použij p!help* `příkaz` *aby ses o příkazu dozvěděl více informací.*")
        elif message.content.startswith("p!about") or message.content.startswith("!About") or message.content.startswith("!ABOUT"):
            with open(__file__, "r", encoding='UTF-8') as f:
                kod = len(f.readlines())
            abouti = "```\n• Bota vytvořil Arbys \n• Bot obsahuje {} řádků kódu \n• Vývoj bota začal dne 20.3.2018 \n• Bot běží na verzi - 3.0 (poslední update - 30.3.2018) \n• Spolupracovali - Reggie, SystemeR```".format(kod)
            await client.send_message(message.channel, abouti)
        elif message.content.startswith("p!fakt"):
            nowtime = "[ {}.{}, {}:{}:{} ]".format(now.day, now.month, now.hour, now.minute, now.second)
            log = "{} | Uživatel {}#{} s ID {} si zobrazil fakt!".format(nowtime, message.author.display_name, message.author.discriminator, message.author.id)
            print(log)
            img = ":question: **|** *Jeden fakt o pohance pro tebe,* {} !".format(message.author.mention)
            await client.send_message(message.channel, img)
            fakty = ["> Pohanka se v česku začala pěstovat na přelomu 12. a 13. století","> Pohanka je rod rostlin z čeledi rdesnovitých","> Pohanka se kromě přípravy pokrmů používá také na zelené hnojení","> Pohanka neobashuje lepek","> Pohanka je významný zdroj rutinu","> Pohanka je díky obsaženým bílkovinám považována za rovnocennou náhražku masa","> Jednou z jejích vlastností je také protirakovinové působení","> Pohanka zvyšuje odolnost sliznic","> Pohanka je téměř jediná ekologicky čistá potravina (neobsahuje nitráty / pesticidy / herbicidy)","> Pohance se skvěle daří i bez hnojiv a poradí si sama se škůdci","> Pohanka je nejvíce na světě rozšířena v Rusku a Indii","> Pohanka byla v Indii známá už před 2500 lety"]
            fakt = random.choice(fakty)
            await client.send_message(message.channel, fakt)
        elif message.content.startswith("p!top"):
            x = open("pohanka.txt").read()
            x = x.replace("'", "\"")
            x = json.loads(x)
            st = []
            for i, t in enumerate(sorted(x.items(), key=lambda x: x[1], reverse=True), 1):
                st.append(('{}.  | {} - {} kusů pohanky\n'.format(i, (await client.get_user_info(t[0])).name, t[1])))
            minuslen = len(st) - 10
            pluslen = 9 - len(st)
            if len(st) > 10:
                del(st[-minuslen:])
            elif len(st) < 10:
                for y in range(pluslen):
                    i += 1
                    st.append('{}.  | _____ - 0 kusů pohanky\n'.format(i))
            i += 1
            st.append('{}. | _____ - 0 kusů pohanky\n'.format(i))
            st.append('```')
            st.insert(0, ":chart_with_upwards_trend: **|** **Pohanka TOP list:\n\n**")
            st.insert(1, "```")
            msg = ''.join(st)
            await client.send_message(message.channel, msg)
        elif message.content.startswith("p!img"):
            nowtime = "[ {}.{}, {}:{}:{} ]".format(now.day, now.month, now.hour, now.minute, now.second)
            log = "{} | Uživatel {}#{} s ID {} si zobrazil obrázek!".format(nowtime, message.author.display_name, message.author.discriminator, message.author.id)
            print(log)
            img = ":camera: **|** *Jeden obrázek pohanky pro tebe,* {} !".format(message.author.mention)
            await client.send_message(message.channel, img)
            pohanky = ["https://1gr.cz/fotky/lidovky/14/022/lnc460/MC515557_shutterstock_125333078.jpg", "http://kgdolu.eu/wp-content/uploads/2017/05/pohanka.jpg", "http://www.centrumkrmiv.cz/resize/domain/centrumkrmiv/files/pohanka-svetla.jpg?w=1024&h=768", "https://i.iinfo.cz/images/448/pohanka-p-1-prev.jpg", "https://www.vegmania.cz/sites/default/files/pohanka.jpg", "http://www.nasevyziva.cz/img_data_arch/1/1310118887cla_pohanka.jpg", "http://www.jidlosnadno.cz/files/prod_images/temp_big/pohanka-dusena.jpg", "https://1380806386.rsc.cdn77.org/images/0/0aa6da22b189ad71/2/awa-superfoods-pohanka-loupana-500g-bezlepkova.jpg", "http://www.ordinace.cz/img/articles/16b9/pohanka2.jpg", "http://www.bio-life.cz/text_img/2525ZTg.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3SKqgQWbeTydWcYgNnxzYPAq7FVWq0wjPywTBrf-RGJisMM5f9Q", "https://cdn.myshoptet.com/usr/www.farmarskykoutek.cz/user/shop/big/60.jpg?56e45c9d", "https://cit.vfu.cz/vegetabilie/plodiny/czech/Pohanka.jpg"]
            pohanka = random.choice(pohanky)
            await client.send_message(message.channel, pohanka)
        elif message.content.startswith("p!recept"):
            nowtime = "[ {}.{}, {}:{}:{} ]".format(now.day, now.month, now.hour, now.minute, now.second)
            log = "{} | Uživatel {}#{} s ID {} si zobrazil recept!".format(nowtime, message.author.display_name, message.author.discriminator, message.author.id)
            print(log)
            text = ":fork_and_knife: **|** *Jeden recept s pohankou pro tebe,* {} !".format(message.author.mention)
            await client.send_message(message.channel, text)
            r = random.randint(1,5)
            if r == 1:
                title = "Pohanková polévka"
                em = discord.Embed(title=title, colour=0xffffff)
                await client.send_message(message.channel, embed=em)
                x = await client.send_message(message.channel, "*Pokud chceš zobrazit celý recept zde, klikni na* **modrý symbol** (🔵) *pod zprávou. Pokud ho chceš zobrazit na internetu, klikni na* **červený symbol** (🔴) *pod zprávou.*")
                recept = "**Ingredience:** \n```•10 dkg másla\n•10 dkg žampionů\n•1 l vody\n•1 lžička sekané petrželky\n•10 dkg petržele\n•10 dkg celeru\n•10 dkg pohanky\n•10 dkg mrkve```**\n\nPostup:**```Kořenovou zeleninu očistíme a nastrouháme. Kdo má rád žampiony, může přidat nakrájené čerstvé. Kdo má rád hodně zeleniny, nic nezkazí když přidá i pórek nebo balíček mražené zeleniny. Pohanku na másle osmažíme. Zalijeme ji vodou, přidáme nastrouhanou kořenovou zeleninu, masox a vaříme asi 15 minut. Pak polévku vypneme. Do pohankové polévky přidáme najemno nakrájenou petrželku nebo pažitku a podáváme teplou.```"
                net = "https://zena.aktualne.cz/volny-cas/chcete-lehkou-veceri-vyzkousejte-recepty-s-pohankou/r~i:article:771528/"
            elif r == 2:
                title = "Pohanková kaše"
                em = discord.Embed(title=title, colour=0xffffff)
                await client.send_message(message.channel, embed=em)
                x = await client.send_message(message.channel, "*Pokud chceš zobrazit celý recept zde, klikni na* **modrý symbol** (🔵) *pod zprávou. Pokud ho chceš zobrazit na internetu, klikni na* **červený symbol** (🔴) *pod zprávou.*")
                recept = "**Ingredience:** \n```•100 g pohanky\n•100 g uzeného boku (nebo jiného uzeného masa, případně špeku)\n•1 menší cibule\n•2 stroužky česneku\n•100 g brynzy\n•sůl```**\n\nPostup:**```Pohanku přeberte, propláchněte na cedníku, vsypte do menšího katrůlku a zalijte 250 ml vroucí vody. Osolte velkorysou špetkou soli, přiveďte společně k varu a pod pokličkou zvolna povařte 5 minut. Poté pohanku odstavte, neodkrývejte a nechte stát 20 minut. Za tu dobu by měla změknout, nabýt na objemu a vstřebat všechnu vodu. Zatímco se pohanka dusí, nakrájejte uzené maso na kostičky, česnek nadrobno a cibuli nahrubo. Do pánve vhoďte nejprve maso, podlijte jednou lžící vody a na středně silném plameni zahřívejte, až maso pustí vlastní tuk. Pokud použijete maso libové, téměř bez tuku, budete muset přidat lžíci sádla. Poté zesilte plamen a maso krátce osmahněte, aby místy zezlátlo. Pak přidejte cibuli a česnek, opět trochu ztlumte plamen a za občasného promíchání nechte změknout a zesklovatět. Do masovo-cibulové směsi vmíchejte uvařenou pohanku. Rozdělte do misek, posypte brynzou, případně nešetřete čerstvými bylinkami.```"
                net = "https://www.kucharkaprodceru.cz/pohanka-recepty/"
            elif r == 3:
                title = "Valašský kontrabáš"
                em = discord.Embed(title=title, colour=0xffffff)
                await client.send_message(message.channel, embed=em)
                x = await client.send_message(message.channel, "*Pokud chceš zobrazit celý recept zde, klikni na* **modrý symbol** (🔵) *pod zprávou. Pokud ho chceš zobrazit na internetu, klikni na* **červený symbol** (🔴) *pod zprávou.*")
                recept = "**Ingredience:** \n```•200 g pohanky\n•1 kg brambor\n•1 větší mrkev\n•250 g uzeného masa\n•4 stroužky česneku\n•1 větší cibule\n•1 vrchovatá lžička sušené majoránky\n•200 g brynzy nebo výraznějšího sýra (například čedaru)\n•sůl\n•kysané zelí k podávání```**\n\nPostup:**```Pohanku uvařte. Maso, cibuli a česnek též připravte úplně stejně, postupně je opečte v pánvi. Troubu začněte předehřívat na 200 stupňů. Zatímco se vaří pohanka, oloupejte mrkev a brambory. Brambory nakrájejte na kostky velikosti sousta, mrkev na 3-4 špalíčky. Obojí uvařte společně v osolené vodě doměkka, zhruba 10 minut. Uvařenou mrkev vyjměte a nakrájejte na kostičky, přidejte k uzenému masu. Brambory slijte a rozšťouchejte nahrubo. Společně smíchejte dušenou pohanku, směs s uzeným masem, šťouchané brambory, a směs nasypte do pekáčku. Posypte rozdrobenou brynzou nebo strouhaným sýrem, vložte do horké trouby a pečte 20 minut do zezlátnutí. Podávejte s kysaným zelím, případně s kyselou okurkou, sypte bylinkami.```"
                net = "https://www.kucharkaprodceru.cz/pohanka-recepty/"
            elif r == 4:
                title = "Pohankový maňas"
                em = discord.Embed(title=title, colour=0xffffff)
                await client.send_message(message.channel, embed=em)
                x = await client.send_message(message.channel, "*Pokud chceš zobrazit celý recept zde, klikni na* **modrý symbol** (🔵) *pod zprávou. Pokud ho chceš zobrazit na internetu, klikni na* **červený symbol** (🔴) *pod zprávou.*")
                recept = "**Ingredience:** \n```•100 g pohanky\n•10 g sušených hub\n•400 g brambor\n•100 g škvarků```**\n\nPostup:**```Sušené houby zalijte 300 ml vroucí vody, zakryjte a nechte aspoň 30 minut stát a nabobtnat. Pohanku mezitím uvařte stejně jako v receptu na pohankovou kaši. Brambory oloupejte a nakrájejte na malé kostičky. Troubu nechte předehřát na 180 stupňů.Smíchejte dušenou pohanku, houby i s nálevem a syrové brambory. Nasypte do zapékací mísy, urovnejte povrch a zasypte nahrubo nasekanými škvarky. Vložte do trouby a zapečte 30 minut, až povrch zrůžoví.```"
                net = "https://www.kucharkaprodceru.cz/pohanka-recepty/"
            elif r == 5:
                title = "Dobrůtka z pohanky"
                em = discord.Embed(title=title, colour=0xffffff)
                await client.send_message(message.channel, embed=em)
                x = await client.send_message(message.channel, "*Pokud chceš zobrazit celý recept zde, klikni na* **modrý symbol** (🔵) *pod zprávou. Pokud ho chceš zobrazit na internetu, klikni na* **červený symbol** (🔴) *pod zprávou.*")
                recept = "**Ingredience:** \n```•1  hrnek pohanka\n•1  lžíce rostlinný olej\n•1  ks cibule\n•2  stroužek česnek\n•1  špetka sůl\n•1  špetka majoránka\n•1  špetka oregáno\n•1  lžíce kečup - jemný\n•150  g tavený sýr asi 1 kostka, může být i light```**\n\nPostup:**```Na lžíci oleje nechat zesklovatět nakrájenou cibulku, pak přisypat pohanku a nechat chviličku opražit. Pak zalít horkou vodou (cca dvojnásobné množství co pohanky), přidat sůl, majoránku, dobromysl a až začne voda vřít, odstavit z ohně a nechat bez varu dojít (lze zabalit třeba do utěrky nebo pod peřinu). Když je pohanka měkká, přidáme prolisovaný česnek, kečup a měkký sýr, který se v horké pohance krásně roztaví. Dobře promícháme a máme rychlou večeři (či přílohu k masu), nebo je možno všechno rozmixovat a získat tak pomazánku, kterou mažeme na celozrnný chléb a zdobíme zeleninou.```"
                net = "https://www.recepty.cz/recept/dobrutka-z-pohanky-14113"
            await client.add_reaction(x, "🔵") 
            await client.add_reaction(x, "🔴")
            def check(reaction, user):
                e = str(reaction.emoji)
                return e.startswith(('🔵', '🔴'))
            res = await client.wait_for_reaction(user=message.author, message=x, check=check)
            if res.reaction.emoji == "🔵":
                #ZDE
                await client.delete_message(x)
                await client.send_message(message.channel, recept)
            elif res.reaction.emoji == "🔴":
                #NET
                await client.delete_message(x)
                await client.send_message(message.channel, ":speech_left: **|** *Recept je online na adrese zde:*")
                await client.send_message(message.channel, net)
            else:
                 await client.send_message(message.channel, "Omlouváme se, ale někde se stala chyba. Co nejdříve se na to podíváme.")
        elif message.content.startswith("p!sebrat"):
            x = open("pohanka.txt").read()
            x = x.replace("'", "\"")
            file = json.loads(x)
            y = open("delay.txt").read()
            y = y.replace("'", "\"")
            delay = json.loads(y)
            try: 
                balance = file[message.author.id]
            except KeyError:
                nowtime = "[ {}.{}, {}:{}:{} ]".format(now.day, now.month, now.hour, now.minute, now.second)
                log = "{} | Uživatel {}#{} s ID {} sebral pohanku!".format(nowtime, message.author.display_name, message.author.discriminator, message.author.id)
                print(log)
                now = datetime.datetime.now()
                now = time.mktime(now.timetuple())
                file[message.author.id] = "1"
                delay[message.author.id] = str(now)
                balance = int(file[message.author.id])
                sebral_onerror = "{}, úspěšně jsi sebral pohanku! Další můžeš sebrat za 3 hodiny!".format(message.author.mention)
                await client.send_message(message.channel, sebral_onerror)
                f = open("pohanka.txt","w")
                f.write(str(file))
                f.close()
                fd = open("delay.txt","w")
                fd.write(str(delay))
                fd.close()
            else:
                nowt = datetime.datetime.now()
                now = time.mktime(now.timetuple())
                if int((int(now)-(int(float((delay[message.author.id])))))) >= 10800:
                    nowtime = "[ {}.{}, {}:{}:{} ]".format(nowt.day, nowt.month, nowt.hour, nowt.minute, nowt.second)
                    log = "{} | Uživatel {}#{} s ID {} sebral pohanku!".format(nowtime, message.author.display_name, message.author.discriminator, message.author.id)
                    print(log)
                    balance = int(file[message.author.id])
                    balance += 1
                    file.update({message.author.id:balance})
                    delay[message.author.id] = str(now)
                    sebral_onregular = "{}, úspěšně jsi sebral **pohanku**! Další můžeš sebrat za *3 hodiny!* (množství pohanky zobrazíš pomocí `p!inv`)".format(message.author.mention)
                    await client.send_message(message.channel, sebral_onregular)
                    f = open("pohanka.txt","w")
                    f.write(str(file))
                    f.close()
                    fd = open("delay.txt","w")
                    fd.write(str(delay))
                    f.close()
                else:
                    uptime = int(((int(float((delay[message.author.id])))) + 10800) - int(now))
                    if uptime < 10800:
                        m = datetime.timedelta(seconds = uptime)
                        malo = "{}, pohanku lze sebrat jen jednou za 3 hodiny! Znovu jí můžeš sebrat za **{}**".format(message.author.mention, m)
                        await client.send_message(message.channel, malo)
                    else:
                        print("Error.")
        elif message.content.startswith("p!edit"):
            x = open("pohanka.txt").read()
            x = x.replace("'", "\"")
            file = json.loads(x)
            split = message.content.split(" ")
            if len(split) == 3:
                try:
                    s0 = str(split[0])
                except:
                    await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
                else:
                    try:
                        s1 = str(split[1])
                    except:
                        await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
                    else:
                        try:
                            s2 = int(split[2])
                        except:
                            await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
                        else:
                            ment = s1
                            a = "<@>"
                            a2 = "@"
                            if a2 in ment:
                                for char in a:
                                    ment = ment.replace(char,"")
                                if ment in open("pohanka.txt").read():
                                    logm = await client.get_user_info(ment)
                                    if s2 == 0:
                                        await client.send_message(message.channel, ":x: **|** Nemůžeš odebrat nebo přidat nulu!")
                                    elif s2 > 0:
                                        #kladné
                                        x = int(file[ment])
                                        x += s2
                                        file[ment] = x
                                        f = open("pohanka.txt","w")
                                        f.write(str(file))
                                        f.close()
                                        nowtime = "[ {}.{}, {}:{}:{} ]".format(now.day, now.month, now.hour, now.minute, now.second)
                                        #log = "{} | > > Administrátor {}#{} s ID {} přidal uživateli {}#{} s ID {} {} pohanky!".format(nowtime, message.author.display_name, message.author.discriminator, message.author.id, logm.name, logm.discriminator, s2)
                                        #print(log)
                                        await client.send_message(message.channel, ":white_check_mark:  **|** Pohanka byla úspěšně **přidána.**")
                                    else:
                                        #záporné
                                        x = int(file[ment])
                                        x -= abs(s2)
                                        file[ment] = x
                                        f = open("pohanka.txt","w")
                                        f.write(str(file))
                                        f.close()
                                        nowtime = "[ {}.{}, {}:{}:{} ]".format(now.day, now.month, now.hour, now.minute, now.second)
                                        #log = "{} | > > Administrátor {}#{} s ID {} odebral uživateli {}#{} s ID {} {} pohanky!".format(nowtime, message.author.display_name, message.author.discriminator, message.author.id, logm.name, logm.discriminator, s2)
                                        #print(log)
                                        await client.send_message(message.channel, ":white_check_mark:  **|** Pohanka byla úspěšně **odebrána.**")
                                else:
                                    await client.send_message(message.channel, ":x: **|** Uživatel není v databázi!")
                            else:
                                await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
            else:
                await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
        elif message.content == ("p!bany"):
            x = open("bany.txt","r")
            lines = x.readlines()
            lines = ' '.join(lines).replace('\n','').split()
            n = 0
            l = []
            while n < len(lines):
                user1 = await client.get_user_info(lines[n])
                l.append(user1.name + ", ")
                n += 1
            if len(l) == 0:
                msgbanned = "**Nikdo není zabanován**"
            else:
                banned = ''.join(l)
                msgbanned = "**Zabanovaní uživatelé:** {}".format(banned)
            await client.send_message(message.channel, msgbanned)
        elif message.content.startswith("p!ban"):
            split = message.content.split(" ")
            if len(split) == 2:
                try:
                    s0 = str(split[1])
                except:
                    await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
                else:
                    ment = s0
                    a = "<@>"
                    a2 = "@"
                    if a2 in ment:
                        for char in a:
                            ment = ment.replace(char,"")
                        try:
                            s1 = int(ment)
                        except:
                            await client.send_message(message.channel, ":x: **|** Takový uživatel na serveru není.")
                        else:
                            x = open("bany.txt", "a")
                            if ment in open("bany.txt").read():
                                await client.send_message(message.channel, ":x: **|** Tento uživatel už je zabanován.")
                            else:
                                x.write(str(ment) + "\n")
                                x.close()
                                banmsg = ":no_entry_sign: **|** Uživatel <@{}> byl **zabanován** administrátorem {}.".format(ment, message.author.name)
                                await client.send_message(message.channel, banmsg)
                    else:
                        await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
            else:
                await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
        elif message.content.startswith("p!unban"):
            split = message.content.split(" ")
            if len(split) == 2:
                try:
                    s0 = str(split[1])
                except:
                    await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
                else:
                    ment = s0
                    a = "<@>"
                    a2 = "@"
                    if a2 in ment:
                        for char in a:
                            ment = ment.replace(char,"")
                    else:
                        await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
                    x = open("bany.txt","r")
                    if ment in open("bany.txt").read():
                        lines = x.readlines()
                        x.close()
                        x = open("bany.txt","w")
                        for line in lines:
                            if line!="{}".format(ment)+"\n":
                                x.write(line)
                        x.close()
                        banmsg = ":no_entry_sign: **|** Uživatel <@{}> byl **unbanován** administrátorem {}.".format(ment, message.author.name)
                        await client.send_message(message.channel, banmsg)
                    else:
                        await client.send_message(message.channel, ":x: **|** Tento uživatel není zabanován.")
            else:
                await client.send_message(message.channel, ":x: **|** Špatně zadaný formát.")
        elif message.content.startswith("p!admin"):
            if message.author.id in open("admins.txt").read():
                await client.send_message(message.channel, ":envelope_with_arrow: **|** Admin příkazy jsem ti zaslal do **soukromé zprávy**!")
                prijemce = await client.get_user_info(message.author.id)
                await client.send_message(prijemce, "**Admin příkazy:**\n\n `p!edit mention cislo` - (přidá / odebere pokud je číslo záporné určité množství pohanky určítému uživateli) \n `p!ban mention` - (zakáže uživateli používat příkazy pohanka bota) \n `p!unban mention` - (odbanuje uživatele)")
            else:
                msg = ":x: **|** {}, ani to nezkoušej, tohle můžou jen **pohankový admini**!".format(message.author.mention)
                await client.send_message(message.channel, msg)
        elif message.content.startswith("p!inv"):
            x = open("pohanka.txt").read()
            x = x.replace("'", "\"")
            file = json.loads(x)
            pocet1 = file[message.author.id]
            pocet = "{}, máš u sebe **{}**ks pohanky!".format(message.author.mention, pocet1)
            await client.send_message(message.channel, pocet)
        elif message.content.startswith("p!"):
            tester = message.content.split(" ")
            tester = str(tester)
            a = "~ˇ^˘°˛`˙´˝!?:_<>*$ß¤÷×_''[]"
            for char in a:
                tester = tester.replace(char,"")
            tester = tester.lower()
            all = ["pimg", "phelp", "pabout", "pfakt", "pinv", "precept", "padmin"]
            if tester in all:
                neznam = ":x: **|** Takový příkaz neexistuje, ale pravděpodobně došlo jen k překlepu. Ujisti se v **p!help** že píšeš příkaz správně *(vše malými písmeny)*"
            else:
                neznam = ":x: **|** Bohužel, je mi líto, ale takový příkaz neznám. Zkus použít **p!help**"
            await client.send_message(message.channel, neznam)
#await client.send_message(message.channel, )
client.run(bot_token)

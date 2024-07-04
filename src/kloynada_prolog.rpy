label kloynada_prolog_start:
    $ save_name = ('Пролог')
    $ prolog_time()
    # $ persistent.sprite_time = "day"
    window hide
    show khata
    show prologue_dream
    # show prolog_text at center_text
    pause 5
    # hide prolog_text with fade
    window show
    $ day_time()
    $ persistent.sprite_time = "day"
    hide prologue_dream with fade
    show unblink with dissolve
    play ambience ambience_camp_center_day fadein 0.5
    scene khata with fade2
    "Я проснулся."
    "На часах 13:20"
    th "Чёт я рано сегодня"
    "Чёрт, как душно, нужно закрыть окно."
    scene basgolova with dissolve
    "За окном стоял постоянно один и тот же вид, который уже начал нагнетать. "
    "На улице щебечут птицы. Как они меня уже достали."
    "Справа росла вкусненькая клубника, и лишь один бассейн, с которым у меня связано много положительных воспоминаний, заставил улыбнуться."
    play sound condition_sound_on
    play sound_loop condition_sound fadeout 1.0
    "Я включил сплит систему."
    th "Вот так-то лучше!"
    scene khata with dissolve
    "Я пошёл умываться."
    scene vanna11 with dissolve
    stop ambience fadeout 0.5
    "Да, я умываюсь прямо в ванной. И что теперь?"
    play sound sfx_water_sink_stream
    "Я открыл кран"
    "Конечно мне не нравится умываться и зубы там чистить. Я же теряю время для игры в доту."
    th "Ну ладно, зато буду чистым."
    stop sound
    "Я закрыл кран. Теперь я полон энергии для игры в доту."
    play ambience ambience_camp_center_day fadein 0.5
    scene khata with dissolve
    "Так, вон комп. Я его с предыдущей ночи еще не выключил"
    "Я сразу же зашёл на свой любимый сервер в дискордике."
    stop ambience fadeout 0.5
    scene discord with dissolve
    play sound join_discord
    play music music_list["gentle_predator"] fadein 1
    dn "Дарова, лахи!"
    ml "ПРИВЕТ, ДЕНИС!"
    kl "АЛЁ?"
    k4 "ООО, ПОДСОСЫ ДЕНИСА ОТКЛИКНУЛИСЬ."
    vs "ПРИВЕТ..."
    ml "ДЕНЧИК, ТЫ НЕ ЗАБЫЛ, ЧТО СЕГОДНЯ ТУРИК ПО ДОТЕ?"
    dn "ЧЁ?{w} А, НЕТ КОНЕЧНО, КАК ТАКОЕ МОЖНО ЗАБЫТЬ?"
    k4 "ГО ПОТРЕНИМСЯ, ГАЙС. ТОК ВИКА ИДЁТ К МЕЛЬНИКУ НА ЛИНИЮ, ДАЙТЕ НОРМ САППОРТА."
    vs "ПАШЁЛ ТЫ…"
    dn "НУ ЛАДНО ДАМ ВАМ ШАНС, ПОЙДЁМ ПАБЧИК СЫГРАЕМ"
    "Конечно же , перед тем как пойти трениться я решил включить свою любимую музыку."
    stop music fadeout 1.0
    play sound join_discord
    pause 1.0
    play music lvvp
    "Я прописал команду на включение моей любимой нексюши. Кайф для ушей."
    th "Наконец-то послушаю ее, а то яндекс плюс закончился."
    k4 "ОПАЧКИ, ВОТ ЭТО МУЗОН."
    ml "ЧЁ ЗА ГОВНО? ОФНИ."
    stop music
    play sound disconnect_ds
    "Так как у Саши даунича был \"диджей\", он прописал стоп. Пускай сосёт, музыка лучшая."
    scene dota_opening with dissolve
    pause 1.0
    scene dota_menu_sf
    play music music_list["gentle_predator"] fadein 1
    "Я открыл доту и мы пошли трениться."
    scene dota_training with dissolve
    th "Эх , как же хочется пикнуть акса, пойти на сложную, и поняшиться с вражеским керри"
    pause (1)
    scene dota_menu_sf with dissolve
    "Но, на время этого турнира я мидер, да и тройку отжать у кулича у меня ни была ни одного аута. Ой, один аут был, он же на керри."
    "После двух игр оставалась 30 минут до турнира, мы приготовили двойные пики и морально готовились к играм."
    scene dota_tournament_roshan with dissolve
    "Прошло пару часов и вместе несколько игр, они были лёгкие, я даже начал считать себя лучшим мидером в мире. То есть, как я всегда и считал."
    "Вот мы и вышли в гранд-финал, я был одновременно рад и шокирован: перед турниром я не думал о результате; я думал лишь о том, сколько сделает мельник фидов из 10."
    "Особенно весёлым моментом мне показалось то, когда Мельник передайвил, и Никита порофлил."
    k4 "Мельник опять фидит , может его уже забаним?!"
    dn "Блин, первый нормальный колл за сегодня."
    si "~ Хоть мельник фидит, у меня появлется шанс выиграть деньги. ~"
    ml "Я БЫ УБИВАЛ ЕСЛИ БЫ МНЕ КРЕСТ ДАЛИ, СПАСИБО САППОРТАМ. НИКИТА ПРОСТО ДАУН, ДАЖЕ НА ТУРНИРЕ ТОКСИЧИШЬ."
    "Говорил Александрия, сбавляя звук на каждом слове."
    k4 "АЛО КОНЧЕНЫЙ! Ты понимаешь, что это шутки?"
    "Кулич мгновенно успокоился."
    vs "Как я могла дать крест, может хватит ссориться !"
    kl "Не, мельник реально даун!"
    "Дальше всё было, как во сне. Смешных рофлов больше не было . Да и мы всё же на турнире, кенты не стали долго обсуждать, кто самый конченый(это и так очевидно). "
    show basgolova_bw with dissolve
    show prologue_dream
    "Во время игры мне почему-то часто вспоминался тот вид из окна, мне казалось это странным, но эмоций особо не было."
    "В моём  \"Brain\" как будто произошёл тайм-скип ."
    hide basgolova_bw
    hide prologue_dream
    dn "Думаю, их пик сильнее в лейте."
    ml "Согласен, надо побыстрее заканчивать."
    k4 "На скорострелычах!"
    "Захихикал Кайлич."
    "В этот момент я представил эхидную улыбку на лице \"Лучшей тройки\". Думаю, не стоит пытаться над ним рофлить. Хоть Никиту вывести трудно, но возможно, а если он будет на дизморали, выиграть будет невозможно . Даже трясущиеся руки Мельника не спасут."
    kl "Нам действительно надо что-то делать!"
    th "Спасибо, кэп."
    k4 "Кулич: Можем пойти на авантюрного рошана , но желательно поставить варды."
    kl "Где обсы пятёрка, почему они все в нашем лесу ?"
    ml "Давайте смоканемся !"
    vs "Смока нет …"
    k4 "мля... Почему нет смоков ни в таверне , ни у вас в бэкпаке , а , Вика?!"
    th "Пригорел Никита."
    vs "Я варды ставила…"
    th "Фейспалм..."
    si "Вам не надо тянуть, идите уже на рошу ."
    "Я думаю, все поняли байт \"Псевдо-интеллектуала\" . Было ясно , что он надеется на массовый фид под рошаном ."
    "Он действительно был не обязан болеть за нас , ведь поспорил с каждым на большие деньги. Но сидеть в дс и байтить друзей в надежде на слив, это слишком. Впрочем, тогда у меня не было времени думать о его словах."
    "Крики мельника вернули меня в реальность."
    ml "Я ФИЖУУУ, ХЕЛП, ПОЧЕМУ СУ.., ПОЧЕМУ МНЕ НИКТО НЕ МОЖЕТ ПОМОЧЬ?"
    dn "Хватит умирать в соло, даунич!"
    "У меня в тот момент действительно бомбануло. Тут же начался файт ."
    play sound disconnect_ds
    stop music fadeout 1.0
    "Но вдруг \"чпок\" и я оказываюсь в главном меню, и слышу звук выхода из дс ."
    scene dota_menu_sf with dissolve
    dn "Ебуч... сраный интернет !"
    th "Надеюсь все поняли, что произошло и сразу поставили паузу. У меня где-то 4 минуты."
    scene khata with dissolve
    "Обычно в такой ситуации я просто надеюсь на силу Рандома. Но в этот раз я сильно волновался, и сразу начал переподключать Wi-Fi роутер."
    "От этого увлекательного занятия меня отвёл телефонный звонок."
    play sound_loop bumer_sound fadein 0.5
    th "Найс тайминг, блин."
    # scene phone_call_from_si
    "Увидев то, что мне звонит Славик, я сразу ответил, но… он сказал совсем не то, что я ожидал услышать."
    stop sound_loop fadeout 0.5
    scene khata with dissolve
    play music music_list["no_tresspassing"] fadein 1.0
    si "Слушай, тут такое дело."
    dn "Я здесь, у меня инет вырубил, щас зайду."
    "Я уже собирался сбросить, но Слава сказал :"
    si "Стой! Мне нужно поговорить с тобой один на один."
    "После этой фразы я увидел, как на роутере горит лампочка , означающая наличие интернета . Я уже хотел сбросить звонок , как я обычно делаю с Мельником, но Славик заставил отнять минуту моей жизни ."
    si "Ты отлично знаешь, что мы поспорили на деньги, но если ты не зайдёшь, я дам тебе больше, чем ты получишь за 1 место ."
    dn "Хах. Ты думаешь, денег будет достаточно ? Меня можно купить ? Ты идиот ?"
    si "Помнишь тот ДС-сервер на котором я админ и который мы хотели бахнуть, если ты сейчас поможешь мне, я отплачу тебе тем же, думаю, ты понимаешь о чём я."
    "Предложение Славы звучало привлекательно. Мне как раз нужны деньги, заполучив их, я бы смог избавиться от overwolf, но друзей кидать я не хочу. Хотя… рейд сервера - развлечение для всех. Но и, наверное, тильт от поражения на турнире…"
    dn "Секунду, дай подумать."

    menu:
        "Зайти в дискорд и доиграть турнир и после него рассказать о \"проишествии\" со Славой":

            $ si_score -= 3
            $ ml_score += 1
            $ k4_score += 1
            $ vs_score += 1
            $ dn_score += 1
            $ kl_score += 1
            $ ms_score += 1

            jump kloynada_prolog_si_say_no

        "Продолжить играть турнир, но не говорить о звонке.":

            jump kloynada_prolog_si_dont_say

        "Послушать Славу, получить деньги и долгожданный рейд сервера.":

            $ si_score += 3
            $ ml_score -= 1
            $ k4_score -= 1
            $ vs_score -= 1
            $ dn_score -= 1
            $ kl_score -= 1
            $ ms_score -= 1

            jump kloynada_prolog_si_say_yes


label kloynada_prolog_si_say_no:

    "Подумав несколько секунд, я невероятно разозлился. Человек, которого я хоть чуть уважал и считал другом, заставляет меня кинуть других друзей за бабки и \"бах\"?"
    "Нет уж, увольте! Если мне захочется бахнуть сервер, я приду в деревню, либо к опытной львице Лере."
    th "В Серове все дауны?"
    dn "Я не ожидал от тебя такого, и теперь с радостью забаню тебя на клоунаде!"
    si "Ну мен… ты же понимаешь, я не хочу проигрывать такую сумму. В общем, человек такое существо, которому…"
    "Я не дослушал эту крысу, и резко перебил его."
    dn "Я уже захожу в дс, и поверь, сейчас я всем расскажу, какой ты конченый на самом деле."
    si "Дай я попытаюсь тебе объяснить, не сбрасывай.., ненадо … , почему ты, ты такой..."
    # play sound stop_callsi
    stop music fadeout 2.0
    "Я не стал продолжать диалог и сразу сбросил вызов. Дискорд как обычно загружался недолго, но за это время я на 100 процентов понял , что обязан рассказать о поступке Славы."
    play music music_list["two_glasses_of_melancholy"] fadein 1.0
    th "Такая тварь не должна обитать на клоунаде."
    "И вот я подключаюсь к звонку."
    play sound join_discord
    scene discord with dissolve
    ml "Слава богу ты живой!"
    "Эта \"Слава\" меня затригеррило."
    k4 "Ты уже в тильте?"
    kl "Давай заходи, балбес, одна пауза блин осталась!"
    scene dota_opening with dissolve
    dn "Ха… Мне сейчас звонил один рофлочелик и просил вас кинуть, что скажете..."
    ms "Это кто был? Мельник?"
    k4 "Было ожидаемо, вряд ли кто-то захочет сливать такие деньги."
    ml "Это что... Серьёзно Славик?"
    ml "Чел ты реально конченый, я рад что Денис оказался умнее тебя, Можешь со мной больше не общаться"
    kl "Не я с этим дауном и так не хотел общатся, а теперь… ещё и в рот ему хочется насрать."
    "В голосах всех кроме Максима чувствовалось желания натоксичить на Орловского, Вероника промолчала… \"Ничего нового\" . Я бы и сам высказал говнорю пару ласковых, но подумав я сказал следующее."
    dn "После нашего выигрыша предлагаю устроить кое-какое голосование."
    si "Ну я же объяснил, зачем, человек такое существо, каждый хочет выгоды, ты сам поступил как крыса, смысл, смысл банить меня."
    "Я не хотел его слушать, был зол на него, исходя из этого я его сразу замутил."
    # scene dota_menu_reconnect
    ml "Хорош! Он не имеет право здесь говорить."
    k4 "Слава, ну что ж ты, фраер, интеллект не заюзал…"
    # scene dota_tournament
    "Я зашёл на последнем тайм-ауте , мы выиграли драку из-за большого преимущества в нетворсе , забрали аегис , а за тем и вражеский трон."
    "За этот промежуток времени ничего интересного в игре не произошло, все говорили только по инфе, дебилоид сидел в муте."
    stop music fadeout 0.5
    play music music_list["so_good_to_be_careless"] fadein 1.0
    # scene desktop_23_35 with dissolve
    "Я посмотрел на часы — 23:35."
    th "Неужели Мельнику разрешили так долго играть, как он смог отпроситься?"
    "Победа! +20000 тысяч осколков на моём балансе!"
    # scene dota_win_20k
    ml "Повезло, что у меня уехали родители."
    scene dota_menu_sf with dissolve
    dn "Найс тайминг, только об этом подумал"
    ml "У меня скоро родители приедут, всем спасибо за игру."
    play sound disconnect_ds
    scene discord with dissolve
    kl "Иди проспись."
    ms "Спокойной ночи чучело и все нормальные люди, я тоже спать."
    play sound disconnect_ds
    k4 "Отлично сыграли , а теперь по кроваткам, гейс."
    play sound disconnect_ds
    vs "Всем споки."
    play sound disconnect_ds
    "Слава, хотя нет, Орловский просто вышел из ДС, про него похоже все забыли. Ладно проведём голосование позже. В дискорде остался только я. Что ж, титан одиночества - титан навсегда!"
    play sound disconnect_ds
    scene khata with dissolve
    play sound_loop condition_sound fadein 1.0
    th "Одному мне делать нечего, пойду лягу пораньше спать."
    stop sound_loop fadeout 1.0
    show blink


    jump kloynada_first_start


label kloynada_prolog_si_dont_say:

    "Поразмыслив несколько секунд, я был в шоке, не думал то что Слава способен на такое."
    th "Все друзья Мельника дауны."
    "Сегодня я был в хорошем настроение и не хотел токсичить на кого-то или вводить друзей в тильт."
    stop music fadeout 0.5
    play music music_list["everyday_theme"] fadein 1.0 fadein 1
    dn "Рофлочел ты понимаешь что ты у меня просишь ?"
    si "Ты понимаешь, какие это деньги ?"
    dn "Слушай, помогать я тебе не собираюсь, отдашь всем проигранные деньги тогда поговорим."
    si "Ну мен... это шутка , рофл , прикол , понимаешь ?"
    "Наверное после моих слов это даун представил как улетит с клоунады на \"Банановые острова\". По голосу я понял то что он хотел оправдаться "
    "В любом случае я не хочу рассказывать о его поступке."
    th "Зачем этим лохам настроение портить, пусть хоть турик на позитиве выиграют."
    dn "Ладно… Бедолага, дам тебе шанс."
    si "Н-ну я объясняю , я не всерьёз."
    dn "Слушай не доводи меня, а то я тебе реально ЗАБАНЮ."
    si "Спасибо конечно , но это всего…"
    "Не дослушав Славу я отключился от звонка и зашёл в дс."
    scene discord
    play sound join_discord
    ml "Здарова, Денис."
    k4 "Жёстко тильтанул?"
    kl "Что за бедолага зашёл?"
    dn "Зашёл вас закерить, не надо?"
    k4 "Пошёл нафег."
    vs "У нас одна пауза осталась, ЗАХОДИ УЖЕ."
    "Я сразу же зашёл в доту . Было немного не по себе от того что я скрывая разговор со славой , но об говорить я не собирался."
    scene dota_opening with dissolve
    pause (4)
    # scene dota_menu_reconnect with dissolve
    pause (3)
    # scene dota_tournament with dissolve
    th "Я же всё-таки не балабол."
    "Но эти мысли не помешали мне закерить."

    # scene desktop_23_35
    "После окончания игры я посмотел на часы — 23:35"
    # scene dota_win_20k
    th "Не зря так долго играли, 20000 тысяч. СЮДАААААА?"
    scene discord with dissolve
    stop music fadeout 0.5
    play music music_list["so_good_to_be_careless"] fadein 1.0
    "Из моих размышлений меня выбили разговоры друзей и Мельника."
    ml "Не, ну я закерил."
    dn "Найс энигма тройка 10-17."
    k4 "Зато какой импакт, 0 ошибок."
    ml "Не импакт реально был."
    dn "Ты про меня?"
    ml "Про кулича."
    kl "Мельник впервые не подсосал."
    ml "Мда…"
    k4 "Мда."
    "Передразнил кулич."
    "Игра была потная, мне захотелось спать."
    dn "Спокойной ночи бедолаги."
    k4 "Как-то рано сегодня."
    th "Не то слово."
    # SLEEP
    scene khata with dissolve
    pause 1.0

    show blink
    "Не думаю что без меня долго сидели в дс. В это время все кроме меня спят. Я сразу отправился в мир сновидений не успев об этом подумать."
    ""

    jump kloynada_first_start


label kloynada_prolog_si_say_yes:

    dn "Кидать друзей… это по-даунски."
    si "Ты же понимаешь сколько я могу тебе дать. Тысяч 25 где-то. Плюс… отличный рейдик."
    "Желание лёгких денег и рейда пробирало насквозь. Я понимал, что это неправильно но всё же…"
    dn "Ладно… Всё ради рейда!"
    stop music fadeout 0.5
    play music music_list["into_the_unknown"] fadein 1.0
    si "Отлично, рад, что мы нашли общий язык."
    dn "Но если ты меня обманешь, соболезную тебе. Ты сразу же вылетишь с клоунады."
    si "Прям как Мельник в окно, какой байт? Думаю, ты сам понимаешь, какие это деньги"
    dn "Ну, сливать специально я не собираюсь."
    th "Я же не клоун, хорошо, что в той катке на дровке кулич заруинил. А шмотки на земеле сами сломались."
    si "Фидить не нужно! Просто не заходи в доту и в дс где-то 10 минут, без мидера они не выиграют."
    dn "Ладно, только первый и последний раз я кого-то кидаю."
    si "Как скажешь!"
    "Я всё сделал по заветам Вячеслава."
    th "Чёрт, на что я вообще согласился? Я же и так при деньгах…"
    "10 минут казались вечностью, плюс… {w} звонки от друзей, на которые я не отвечал.{w} Не отвечал из-за сделки. Сделки с Дьяволом. Ну, мне так казалось на тот момент."
    "Или от стыда я не брал трубку, я даже для себе не определился, скорее всего всё вместе."
    "Я посмотрел на часы."
    th "Пора заходить."
    stop music fadeout 0.5
    "Звук подключения к звонку и крики в мою сторону."
    play music music_list["you_won_t_let_me_down"] fadein 1.0

    scene discord with dissolve
    play sound join_discord
    "Это было не удивительно."
    th "Если бы Мельник так заруинил вряд ли он остался бы на клоунаде."
    "Никогда не думал что меня будут обвинять на моём же сервере, впрочем я не пытался вслушиваться в эти разговоры, я сам понимал что чувствовали в тот момент мои друзья."
    si "Я же говорил что у вас не получится выиграть."
    "Вячеслав зловеще засмеялся."
    si "Не спорьте, если не уверены в себе!"
    k4 "Чел… Все были уверены в себе, ты реально думаешь мы бы слили 5в5? Не строй из себя дурачка, ты, вроде, умный."
    "После этой фразы все утихли, тильт ребят только нарастал."
    ml "Ещё и деньги этому дауну отдавать."
    "Мне не хотелось оправдываться и ничего говорить."
    dn "Извините… я же не виноват, что у меня оффнули интернет…"
    kl "Не, ну просто чел заруинил."
    k4 "Как всегда."
    stop music fadeout 0.5
    "Мне не хотелось сидеть в дискорде. Хотелось быстрее выйти со звонка."
    # Change music.
    play music music_list["smooth_machine"]fadein 1.0
    dn "Наверное, пойду спать."
    k4 "Как-то рано."
    vs "Заруинил и уходит."
    ms "Я считаю, мы из-за Мельника слили."
    ml "Молча сиди, даун с 1 рекрутом."
    k4 "Молча сиди, даун с 2 стражем."
    ml "В отличие от него я керри на турике."
    k4 "Не волнуйся, это твой последний турнир на керри."
    ml "Ой, всё, заткнись, даун."
    "Заплакал Александр."
    "У меня не оставалось сил слушать нытьё своих друзей, потому что ныли они из-за меня. Так ещё конфликт двух корешей выбил всю мораль из меня."
    th "Какой же я кидок…"
    dn "Пойду я спать, простите ещё раз."
    k4 "Ага, сладких снов. Я удаляю доту 2."
    dn "Спокойной ночи. Ну как же обидно, господи!!! Ну почему Денис…"
    "Кричал мельник издалека, пиная себя по голове."
    kl "Спокойной, спасибо за руин."
    play sound disconnect_ds
    "Вика вышла, ничего не сказав."
    ms "Дайте мне мид пж сыграть некст турнир, у меня интернет надёжный."
    play sound disconnect_ds
    # scene pc_desktop
    scene khata with dissolve
    "После этих слов я вышел с дискорда.{w} Чувствовал себя невероятно уставшим за сегодня. Было обидно за поражение на турнире, но конечно же это был не последний наш турик."
    th "То ли ещё будет!"
    stop sound_loop fadeout 1.0
    show blink
    "Я примкнул к объятиям Морфея."
    ""

    jump kloynada_first_start
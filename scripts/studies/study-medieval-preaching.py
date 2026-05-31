# -*- coding: utf-8 -*-
"""Content module for study-medieval-preaching.html.

Jonathan Adams and Jussi Hanska (eds.), *The Jewish-Christian Encounter in
Medieval Preaching* (Routledge Research in Medieval Studies 6, 2014/2015).
"""

RHYTHM_ZH = """        <strong>① 学者说什么</strong>—— 用作者们的研究概述这一议题；<br/>
        <strong>② 关键经文</strong>—— 一处与之相关、需重新聆听的圣经；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，校正失真的视角；<br/>
        <strong>④ 基督徒视角</strong>—— 我们今天该如何悔改、如何重新讲道；<br/>
        <strong>⑤ 诚实的提问</strong>—— 留给你与小组省察的问题。"""

RHYTHM_EN = """        <strong>① What the Scholars Say</strong> — the issue, in the contributors' research;<br/>
        <strong>② Key Scripture</strong> — a related text we must hear again;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that corrects a distorted lens;<br/>
        <strong>④ A Christian Lens</strong> — how we today must repent and preach differently;<br/>
        <strong>⑤ Honest Questions</strong> — questions for you and your group to examine."""


def step(label_zh, label_en, *body):
    return {"label_zh": label_zh, "label_en": label_en, "body": list(body)}

def p(zh, en):
    return {"type": "p", "zh": zh, "en": en}

def bq(zh, en, cite=None):
    return {"type": "blockquote", "zh": zh, "en": en, "cite": cite}

def ul(*items):
    return {"type": "ul", "items": [{"zh": z, "en": e} for z, e in items]}

S1, S1E = "① 学者说什么", "① What the Scholars Say"
S2, S2E = "② 关键经文", "② Key Scripture"
S3, S3E = "③ 希伯来语之眼", "③ Through Hebrew Eyes"
S4, S4E = "④ 基督徒视角", "④ A Christian Lens"
S5, S5E = "⑤ 诚实的提问", "⑤ Honest Questions"


study = {
    "title_tag": "《中世纪讲道中的犹太-基督相遇》研习指南 · Medieval Preaching — Study Guide · 妥拉之光",
    "meta_desc": "A Christian study guide to The Jewish-Christian Encounter in Medieval Preaching (Adams & Hanska, eds.) — eight bilingual lessons on the “hermeneutical Jew,” forced sermons, Augustine's witness doctrine, anti-Jewish libels, and how to preach today without contempt.",
    "og_title": "The Jewish-Christian Encounter in Medieval Preaching — A Christian Study Guide",
    "og_desc": "Eight bilingual lessons through a scholarly study of how medieval Christian preaching constructed “the Jew” — read as a call to repentance and a different way of preaching.",
    "cover_alt": "The Jewish-Christian Encounter in Medieval Preaching — Study Guide",
    "tagline_zh": "研习指南 · 悔改与重述 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · Repentance &amp; Retelling · 2026 · 5 · 31",
    "headline_zh": "中世纪讲道中的<br/>犹太-基督相遇",
    "headline_en": "The Jewish-Christian<br/>Encounter in Preaching",
    "deck_zh": "八堂课程，直面一段沉重的历史：中世纪的教会讲台如何塑造、扭曲、并伤害了犹太民族的形象。这不是为了定罪，而是为了悔改——让今天的我们，学会以真理与爱，重新讲述福音。",
    "deck_en": "Eight lessons facing a heavy history: how the medieval pulpit shaped, distorted, and wounded the image of the Jewish people. Not to condemn, but to repent — so that we, today, learn to retell the Gospel in truth and in love.",
    "byline_zh": "基于乔纳森·亚当斯 (Jonathan Adams) 与尤西·汉斯卡 (Jussi Hanska) 编《中世纪讲道中的犹太-基督相遇》(Routledge, 2014)",
    "byline_en": "Based on The Jewish-Christian Encounter in Medieval Preaching, edited by Jonathan Adams and Jussi Hanska (Routledge Research in Medieval Studies 6, 2014)",
    "readtime_zh": "约 50 分钟通读",
    "readtime_en": "~50 min read-through",
    "book_url": "https://www.routledge.com/9780367600143",
    "book_link_zh": "购买原书 · Routledge",
    "book_link_en": "Get the Book · Routledge",
    "cta_url": "https://www.routledge.com/9780367600143",
    "cta_zh": "购买《中世纪讲道中的犹太-基督相遇》原书 · Routledge",
    "cta_en": "Get the Book — The Jewish-Christian Encounter in Medieval Preaching · Routledge",

    "lead_zh": "这是一本严肃的学术论文集，由乔纳森·亚当斯 (Jonathan Adams) 与尤西·汉斯卡 (Jussi Hanska) 编辑，源自 2011 年在罗马召开的会议「论犹太人、向犹太人、由犹太人的讲道」。它研究一个我们常常宁愿回避的题目：在中世纪——讲道是「大众传媒之王」的时代——基督教的讲台是如何谈论犹太人的。学者们发现，那讲台上的「犹太人」，往往不是真实的、活生生的邻舍，而是一个被构造出来的「神学符号」：一个来自「遥远的、被想象出来的时空」的人物，存在的唯一目的，是反衬并印证基督教的教导。这份指南，邀请爱犹太民族的基督徒，诚实地直面这段历史。",
    "lead_en": "This is a serious scholarly collection, edited by Jonathan Adams and Jussi Hanska, arising from a 2011 conference in Rome on “Preaching on the Jews, for the Jews, and by the Jews.” It studies a subject we often prefer to avoid: how, in the Middle Ages — when preaching was the “mass medium par excellence” — the Christian pulpit spoke about Jews. The scholars find that the “Jew” on that pulpit was often not a real, living neighbor but a constructed theological symbol: a figure from a “distant, imagined time and place” whose only purpose was to set off and verify Christian teaching. This guide invites Christians who love the Jewish people to face that history honestly.",

    "intro": [
        p("为什么爱犹太民族的我们，要去读一本关于反犹讲道的书？因为爱，必须从真相开始。「爱我民」(Ahavat Ammi) 不能建立在对历史的遗忘之上。这本书让我们看清：教会两千年来「轻蔑的教导」(teaching of contempt) 大半不是通过高深的神学著作传播的，而是通过每个主日、在每座村庄的讲台上，一句一句讲给不识字的会众听的。要悔改，先要知道我们到底说过什么、又是怎么说的。",
          "Why should we who love the Jewish people read a book about anti-Jewish preaching? Because love must begin with truth. <em>Ahavat Ammi</em> — “love of my people” — cannot be built on forgetting history. This book shows us clearly that the Church's two-thousand-year “teaching of contempt” spread mostly not through learned theological treatises, but from the pulpit of every village, every Sunday, line by line, to congregations who could not read. To repent, we must first know what we actually said — and how we said it."),
        p("本指南共 <strong>八堂课</strong>，循着书中的主要议题展开。每一堂遵循同样的五部分节奏：",
          "The guide is structured as <strong>eight lessons</strong>, following the book's major themes. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句提醒：这堂课会让人不舒服。请不要带着自义去读「中世纪的他们」，而要带着省察去读「今天的我们」。同样的扭曲，今天仍可能在我们的讲道、教导甚至祷告里悄悄复活。",
          "A word of caution: this study will be uncomfortable. Do not read it with self-righteousness about “those medievals,” but with self-examination about “us, today.” The same distortions can still quietly revive in our preaching, our teaching, even our prayers."),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "讲台——中世纪的大众传媒",
            "title_en": "The Pulpit — Medieval Mass Media",
            "steps": [
                step(S1, S1E,
                    p("编者首先提醒我们：讲道很可能是整个中世纪「最重要的文学体裁」。在绝大多数人不识字的世界里，讲道连同教堂艺术与戏剧，是「无可争议的大众传媒之王」。1215 年第四次拉特兰大公会议明确规定，必须借「合格而频繁的讲道」教导平信徒。于是，普通会众关于「犹太人是谁」的全部观念，几乎都来自讲台。这是一个关键的洞见：偏见不是抽象地飘在空气里的，它是被「讲」出来的——一个主日接一个主日，被一位有权柄、受尊敬的声音，灌输进千百万人的心里。",
                      "The editors first remind us: preaching was likely “the most important literary genre” of the entire Middle Ages. In a world where most people could not read, the sermon — together with church art and theatre — was “the mass medium par excellence.” The Fourth Lateran Council (1215) decreed that the laity must be taught through “qualified and frequent preaching.” So an ordinary congregation's entire idea of “who the Jews are” came almost wholly from the pulpit. This is a crucial insight: prejudice does not float abstractly in the air; it is <em>preached</em> — Sunday after Sunday, poured into the hearts of millions by an authoritative, respected voice.")),
                step(S2, S2E,
                    bq("「凡好树都结好果子，惟独坏树结坏果子……所以凭着他们的果子，就可以认出他们来。」",
                       "“Every good tree bears good fruit, but a bad tree bears bad fruit... Thus, by their fruit you will recognize them.”",
                       "《马太福音》7:17-20 · Matthew 7:17-20")),
                step(S3, S3E,
                    p("<strong>לָשׁוֹן · lashon</strong>——「舌头」「语言」。犹太智慧传统极其看重「舌头的力量」：箴言说「生死在舌头的权下」(《箴言》18:21)，而 <em>lashon hara</em>（恶舌、毁谤之言）被视为最严重的罪之一——拉比说它「一次杀死三个人：说的人、听的人、被说的人」。中世纪的讲台，正是 <em>lashon hara</em> 的大规模、有组织、披着圣职外衣的版本。它提醒我们：用神的话语之名所说的话，若是扭曲与轻蔑，其杀伤力只会更大，而非更小。",
                      "<strong>לָשׁוֹן · lashon</strong> — “tongue,” “language.” The Jewish wisdom tradition takes the power of the tongue with utmost seriousness: “death and life are in the power of the tongue” (Proverbs 18:21), and <em>lashon hara</em> (“the evil tongue,” slander) is counted among the gravest sins — the rabbis say it “kills three at once: the speaker, the listener, and the one spoken of.” The medieval pulpit was <em>lashon hara</em> in mass, organized form, clothed in priestly office. It reminds us: words spoken in the name of God's word, if they are distortion and contempt, do not wound less, but more.")),
                step(S4, S4E,
                    p("今天传讲神话语的人——牧师、传道、主日学老师、写作的人——必须从这一课学到敬畏。讲台是有真实权柄的。我们随口说出的一句关于「法利赛人」「犹太人」「旧约的神」的轻蔑话，可能在听众心里种下几十年都拔不掉的偏见。这一课不是要我们噤声，而是要我们带着「舌头能定生死」的敬畏去开口。果子会暴露树。我们讲道结出的，究竟是「爱我民」的果子，还是不知不觉延续了「轻蔑的教导」的果子？",
                      "Anyone who proclaims God's word today — pastors, preachers, Sunday-school teachers, writers — must learn reverence from this lesson. The pulpit carries real authority. One offhand contemptuous remark about “the Pharisees,” “the Jews,” or “the God of the Old Testament” can plant in a listener's heart a prejudice that decades will not pull out. This lesson does not call us to silence, but to speak with the fear that “the tongue holds life and death.” Fruit exposes the tree. What does our preaching bear — the fruit of <em>Ahavat Ammi</em>, or an unwitting continuation of the teaching of contempt?")),
                step(S5, S5E,
                    ul(
                        ("我是否曾在讲道、教导或随意的言谈中，用『法利赛人』『犹太人式的』等词作为负面的标签？",
                         "Have I ever used “Pharisee” or “Jewish-style” as negative labels in preaching, teaching, or casual talk?"),
                        ("如果『舌头能定生死』，我对自己（尤其在有权柄的位置上）所说的话，是否足够敬畏？",
                         "If “the tongue holds life and death,” do I treat my own words — especially from a place of authority — with enough reverence?"),
                        ("我的教导结出的『果子』是什么？它把听众引向爱犹太民族，还是引向轻看？",
                         "What “fruit” does my teaching bear? Does it lead hearers toward loving the Jewish people, or toward contempt?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "「释经学上的犹太人」——一个被构造的影子",
            "title_en": "The “Hermeneutical Jew” — A Constructed Shadow",
            "steps": [
                step(S1, S1E,
                    p("这本书最重要的概念，是「想象的」或「神学的」相遇。学者们指出，许多中世纪讲道里出现的「犹太人」，与讲道者身边真实的犹太邻舍几乎没有关系。他是一个「来自遥远、被构造出来的时空的人物」，存在的唯一功能，是「反衬并印证基督教的教导」。学界称之为「释经学上的犹太人」(the hermeneutical Jew)：一个被发明出来、用作神学道具的影子。最危险之处正在于此——会众恨的、惧怕的、嘲笑的，是这个虚构的人物；可这份情绪，却会原封不动地泼到街角那位真实的、有血有肉的犹太人身上。",
                      "The book's most important concept is the “imaginary” or “theological” encounter. The scholars show that the “Jew” appearing in many medieval sermons had almost nothing to do with the real Jewish neighbor living near the preacher. He was “a figure from a distant, constructed time and place,” whose sole function was to “set off and verify Christian teaching.” Scholars call this the “hermeneutical Jew”: an invented shadow used as a theological prop. Here lies the deepest danger — what the congregation hated, feared, and mocked was this fictional figure; yet that emotion would spill, unchanged, onto the real, flesh-and-blood Jew at the street corner.")),
                step(S2, S2E,
                    bq("「不可作假见证陷害你的邻舍。」",
                       "“You shall not give false testimony against your neighbor.”",
                       "《出埃及记》20:16 · Exodus 20:16")),
                step(S3, S3E,
                    p("<strong>רֵעַ · rea</strong>——「邻舍」「同伴」。「要爱<em>邻舍 (rea)</em> 如己」(《利未记》19:18) 里的，正是这个词——一个具体的、就在你身边的、真实的人。「释经学上的犹太人」之所以是一种属灵的暴力，恰恰因为它<em>取消了邻舍</em>：它用一个想象的符号，替换掉了那位神命令我去爱的、真实的 <em>rea</em>。第九诫禁止「作假见证陷害邻舍」——而把一整个民族缩减成一个神学道具，正是规模最大的「假见证」。爱的第一步，是拒绝接受关于邻舍的虚构版本，坚持去认识那个真实的人。",
                      "<strong>רֵעַ · rea</strong> — “neighbor,” “fellow.” It is this very word in “love your <em>neighbor (rea)</em> as yourself” (Leviticus 19:18) — a concrete, real person right beside you. The “hermeneutical Jew” is a kind of spiritual violence precisely because it <em>abolishes the neighbor</em>: it replaces the real <em>rea</em> God commands me to love with an imagined symbol. The ninth commandment forbids “false testimony against your neighbor” — and reducing a whole people to a theological prop is false testimony on the largest scale. The first step of love is to refuse the fictional version of one's neighbor and insist on knowing the real person.")),
                step(S4, S4E,
                    p("「释经学上的犹太人」并未随中世纪而消失。今天的基督徒讲道里，仍可能活着一个虚构的「旧约的犹太人」——律法主义的、刻板的、属灵迟钝的——专门用来反衬「我们恩典的福音」何等优越。每当我们为了把某个道理讲得更漂亮，而把「犹太人」「法利赛人」当作现成的反面教材，我们就在重演同一个错误：用一个影子取代了真人。悔改，意味着拆掉讲台上那个虚构的犹太人，去认识、尊重并爱那真实的犹太民族——他们是神立约的子民，是我们信仰之根所在。",
                      "The “hermeneutical Jew” did not vanish with the Middle Ages. In Christian preaching today there may still live a fictional “Old Testament Jew” — legalistic, rigid, spiritually dull — kept on hand to flatter “our gospel of grace” by contrast. Whenever we use “the Jews” or “the Pharisees” as a ready-made foil to make a point land better, we re-enact the same error: replacing a real people with a shadow. Repentance means dismantling that fictional Jew on the pulpit, and coming to know, honor, and love the real Jewish people — God's covenant people, in whom the root of our own faith is found.")),
                step(S5, S5E,
                    ul(
                        ("在我心中（或我的讲道里），是否住着一个虚构的『旧约犹太人』，专门用来反衬基督教的优越？",
                         "Does a fictional “Old Testament Jew” live in my mind (or my preaching), kept to flatter Christianity by contrast?"),
                        ("我认识真实的犹太人、了解今天活生生的犹太信仰吗？还是我对『犹太人』的全部印象都来自二手的、被构造的形象？",
                         "Do I know real Jewish people and living Jewish faith today — or is my entire impression of “the Jews” secondhand and constructed?"),
                        ("『不可作假见证陷害邻舍』——把一整个群体简化为符号，是否就是一种大规模的『假见证』？",
                         "“Do not bear false testimony against your neighbor” — is reducing a whole group to a symbol a kind of mass “false testimony”?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "「真理的见证人」——奥古斯丁的双刃定义",
            "title_en": "“Witness to the Truth” — Augustine's Double-Edged Doctrine",
            "steps": [
                step(S1, S1E,
                    p("书中追溯到，犹太人在基督教世界里的地位，由奥古斯丁奠定：他赋予犹太人「真理之见证 (testimonium veritatis)」的角色。因为犹太人保存了希伯来圣经（其中含有关于耶稣的预言），又「见证」了道成肉身与复活的历史背景，所以基督教社会应当「保护」他们——但同时让他们处于「臣服与屈辱」的地位，作为「拒绝弥赛亚」的活教材。这是一个双刃的定义：一方面，它确实在许多时刻保护了犹太社群不被彻底消灭；另一方面，它把犹太人冻结在「被打败的见证人」这一卑屈角色里，为日后无数的羞辱埋下了神学根据。",
                      "The book traces the Jews' place in Christendom back to Augustine, who gave them the role of “witness to the truth (testimonium veritatis).” Because the Jews preserved the Hebrew Scriptures (containing the prophecies about Jesus) and “witnessed” the historical setting of the Incarnation and Resurrection, Christian society should “protect” them — but keep them in “subjugation and humiliation” as a living lesson of those who “rejected the Messiah.” It is a double-edged doctrine: on one hand it genuinely protected Jewish communities from outright destruction at many moments; on the other, it froze the Jews into the demeaning role of “defeated witnesses,” laying the theological groundwork for countless later humiliations.")),
                step(S2, S2E,
                    bq("「就着拣选说，他们为列祖的缘故是蒙爱的。因为神的恩赐和选召是没有后悔的。」",
                       "“As far as election is concerned, they are loved on account of the patriarchs, for God's gifts and his call are irrevocable.”",
                       "《罗马书》11:28-29 · Romans 11:28-29")),
                step(S3, S3E,
                    p("<strong>בְּרִית · brit</strong>——「约」。奥古斯丁的定义把犹太人看作「过去的见证人」，仿佛神与他们的故事已经结束、只剩下作反面教材的余热。但希伯来圣经的核心词是 <em>brit</em>——神向亚伯拉罕、向以色列所立的、「永远的约」。保罗在《罗马书》11 章斩钉截铁地宣告：神并没有弃绝祂的百姓；他们「为列祖的缘故是蒙爱的」，因为「神的恩赐和选召是没有后悔的」。这正是「真理见证人」定义中缺失的那一半：犹太人不是一段已经翻篇的历史见证，而是一群此刻仍活在神不收回之约中的、蒙爱的立约子民。",
                      "<strong>בְּרִית · brit</strong> — “covenant.” Augustine's doctrine cast the Jews as “witnesses of the past,” as if God's story with them were finished, useful only as a cautionary afterglow. But the central word of the Hebrew Bible is <em>brit</em> — the “everlasting covenant” God made with Abraham and with Israel. Paul declares flatly in Romans 11 that God has not rejected his people; they are “loved on account of the patriarchs,” for “God's gifts and call are irrevocable.” This is exactly the missing half of the “witness” doctrine: the Jews are not the historical witness of a closed chapter, but a beloved covenant people still living, this very hour, inside a covenant God will not revoke.")),
                step(S4, S4E,
                    p("奥古斯丁的「保护却屈辱」是一种「居高临下的容忍」——而这正是今天许多基督徒对犹太民族态度的隐秘模板：「我们不逼迫他们，但他们终究是『错过了弥赛亚』的、需要被我们纠正的人。」《罗马书》11 章拆毁这种姿态。保罗用「橄榄树」的比喻警告外邦信徒：你不过是被接上去的野枝，「不可向旧枝子夸口」，因为「不是你托着根，乃是根托着你」(《罗马书》11:18)。正确的姿态不是居高临下的容忍，而是带着感恩的谦卑——我们的整个信仰，是嫁接在以色列的约这棵老树上的。",
                      "Augustine's “protect but humiliate” is a “condescending tolerance” — and that is the hidden template for how many Christians still relate to the Jewish people: “We don't persecute them, but after all they are the ones who ‘missed the Messiah’ and need us to correct them.” Romans 11 demolishes this posture. Paul warns Gentile believers with the image of the olive tree: you are only a wild branch grafted in, “do not boast over those branches,” for “you do not support the root, but the root supports you” (Romans 11:18). The right posture is not condescending tolerance but grateful humility — our whole faith is grafted onto the old tree of Israel's covenant.")),
                step(S5, S5E,
                    ul(
                        ("我对犹太民族的态度，是『居高临下的容忍』，还是『感恩的谦卑』？这两者的区别在哪里？",
                         "Is my attitude toward the Jewish people “condescending tolerance” or “grateful humility”? What is the difference?"),
                        ("我是否把犹太人当作『过去的见证人』，而非『此刻仍活在不收回之约中的蒙爱子民』？",
                         "Do I treat the Jews as “witnesses of the past” rather than “a beloved people still living in an irrevocable covenant”?"),
                        ("『不是你托着根，乃是根托着你』——这句话如何改变我对自己信仰来源的认识？",
                         "“You do not support the root, but the root supports you” — how does this change how I understand the source of my own faith?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "缺席的少数——为一群不在场的人「画像」",
            "title_en": "The Absent Minority — Portraits of People Who Were Not There",
            "steps": [
                step(S1, S1E,
                    p("乔纳森·亚当斯研究中世纪丹麦的讲道，得出一个令人不安的发现：丹麦当时几乎没有犹太人居住，然而丹麦的讲道里却充满了关于「犹太人」的形象与指控。换言之，会众对「犹太人」最强烈的印象，竟来自一群他们一辈子可能从未谋面的人。这正是「想象的相遇」最纯粹、也最可怕的形态：当真实的人完全缺席，那个被构造的「犹太人」就再没有任何现实可以校正它、反驳它。偏见在真空中长得最快、最离奇。书中所记的种种荒诞指控，很多就生长在这样「无人可对质」的土壤里。",
                      "Jonathan Adams studies medieval Danish preaching and reaches an unsettling finding: almost no Jews lived in Denmark at the time, yet Danish sermons were full of images and accusations about “the Jews.” In other words, a congregation's strongest impression of “the Jew” came from a people they might never meet in their whole lives. This is the purest and most frightening form of the “imaginary encounter”: when the real people are entirely absent, the constructed “Jew” has no reality left to correct or contradict it. Prejudice grows fastest and most bizarrely in a vacuum. Many of the absurd accusations the book records grew precisely in this soil where “no one could be confronted.”")),
                step(S2, S2E,
                    bq("「先听的似乎有理；但邻舍来到，就察出实情。」",
                       "“In a lawsuit the first to speak seems right, until someone comes forward and cross-examines.”",
                       "《箴言》18:17 · Proverbs 18:17")),
                step(S3, S3E,
                    p("<strong>אֱמֶת · emet</strong>——「真理」「真实」「可靠」。它的字根含有「稳固、立得住」的意味：<em>emet</em> 是经得起对质、站得住脚的真实。《箴言》18:17 道出一个朴素却深刻的智慧：单方面的陈述听起来总是「有理」的，直到另一方到场对质。中世纪那群「缺席的犹太人」，永远没有机会「到场对质」——所以关于他们的谎言能畅通无阻。寻求 <em>emet</em>，就意味着永不满足于只听一面之词，永远为「另一方」留一个到场说话的位置。",
                      "<strong>אֱמֶת · emet</strong> — “truth,” “reality,” “reliability.” Its root carries the sense of “firm, able to stand”: <em>emet</em> is the kind of truth that withstands cross-examination, that holds its ground. Proverbs 18:17 voices a plain but profound wisdom: a one-sided account always sounds “right” — until the other party arrives to be cross-examined. The “absent Jews” of the Middle Ages never got the chance to “arrive and be heard,” so lies about them ran unopposed. To seek <em>emet</em> means never to be content with one side of the story, always to keep a seat open for “the other party” to come and speak.")),
                step(S4, S4E,
                    p("这一课对今天的我们极其切身。我们大多数人，对许多群体（不只是犹太人）的看法，都建立在「缺席的相遇」之上——我们从新闻、社媒、二手转述里，认识了一个我们从未真正接触过的「他们」。这与中世纪丹麦的讲道，结构上一模一样。福音呼召我们走一条更艰难、却更有爱的路：去真正认识那个真实的人，让真实的相遇去校正那被构造的形象。对基督徒而言，这尤其意味着：不要满足于「关于犹太人的神学」，而要寻求「与犹太人真实的相遇」。",
                      "This lesson is intensely personal for us today. Most of us form our view of many groups (not only Jews) on the basis of “absent encounters” — we come to know a “them” we have never truly met, through news, social media, and secondhand report. Structurally, this is identical to medieval Danish preaching. The Gospel calls us to a harder but more loving road: to actually know the real person, and let real encounter correct the constructed image. For Christians this especially means: do not settle for “a theology about Jews,” but seek “a real encounter with Jewish people.”")),
                step(S5, S5E,
                    ul(
                        ("我对某些群体的强烈看法，有多少建立在『从未真正相遇』的二手印象之上？",
                         "How much of my strong opinion about certain groups rests on secondhand impressions, with no real encounter?"),
                        ("我是否愿意为『另一方』留一个『到场对质』的位置，还是满足于只听对我方便的那一面？",
                         "Am I willing to keep a seat open for “the other side to be heard,” or content to hear only the side convenient to me?"),
                        ("我能采取什么具体一步，去经历一场与犹太民族『真实的相遇』，而非『想象的相遇』？",
                         "What concrete step can I take toward a “real encounter” with the Jewish people, rather than an “imagined” one?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "强迫聆听——被逼坐在讲道之下的犹太人",
            "title_en": "Forced to Listen — Jews Compelled Under the Sermon",
            "steps": [
                step(S1, S1E,
                    p("编者特别指出，「相遇」也包括一种残酷的、物理性的形态：在中世纪欧洲许多地方，犹太人被「强制出席」基督教的讲道。教会希望借此使他们「归信」。想象那个场景：一群犹太人被律法强迫，坐在教堂里，听一篇专门为驳斥、羞辱他们的信仰而写的讲道——既不能离开，也不能回应。这是一种披着「宣教」外衣的羞辱。所谓的「劝归信的讲道」(conversionary sermons)，往往不是出于爱的邀请，而是一种以权力为后盾的强制。它暴露了一个深刻的扭曲：把「传福音」变成了「压制」。",
                      "The editors stress that “encounter” also took a cruel, physical form: in many parts of medieval Europe, Jews were “compelled to attend” Christian sermons. The Church hoped this would “convert” them. Picture the scene: a group of Jews forced by law to sit in a church and hear a sermon written precisely to refute and humiliate their faith — unable to leave, unable to respond. It is humiliation dressed as mission. The so-called “conversionary sermons” were often not an invitation of love but a coercion backed by power. They expose a deep distortion: turning “evangelism” into “suppression.”")),
                step(S2, S2E,
                    bq("「只要心里尊主基督为圣。有人问你们心中盼望的缘由，就要常作准备，以温柔、敬畏的心回答各人。」",
                       "“In your hearts revere Christ as Lord. Always be prepared to give an answer to everyone who asks you for the reason for the hope that you have. But do this with gentleness and respect.”",
                       "《彼得前书》3:15 · 1 Peter 3:15")),
                step(S3, S3E,
                    p("<strong>רָצוֹן · ratzon</strong>——「意愿」「甘心」「悦纳」。圣经里真实的信仰，总是关乎 <em>ratzon</em>——出于自愿、甘心献上的回应。诗篇说赞美要从「甘心乐意的子民」(《诗篇》110:3) 中涌出；保罗说捐献要「甘心乐意」，「不要勉强」(《哥林多后书》9:7)。强迫聆听、强制归信，从根本上违背了信仰的本性：被强迫的「相信」，根本不是信。神自己尚且赐人自由去回应或拒绝祂的爱，没有任何一篇讲道，有权剥夺听者的 <em>ratzon</em>。",
                      "<strong>רָצוֹן · ratzon</strong> — “will,” “willingness,” “favor.” Real faith in Scripture always concerns <em>ratzon</em> — a freely given, willing response. The psalm says praise rises from “a freely willing people” (Psalm 110:3); Paul says giving should be “willing,” “not under compulsion” (2 Corinthians 9:7). Forced listening and coerced conversion violate the very nature of faith: a “belief” that is compelled is not belief at all. God himself grants people freedom to respond to or refuse his love; no sermon has the right to strip its hearers of their <em>ratzon</em>.")),
                step(S4, S4E,
                    p("彼得前书 3:15 是基督徒见证的黄金准则，它每一个字都与「强迫聆听」针锋相对：见证是「回答<em>问你们的</em>人」（出于对方的发问，而非我方的强加），是关乎「盼望的缘由」（是邀请人进入盼望，而非定人的罪），并且要「以温柔、敬畏的心」（不是以权力施压）。中世纪的强制讲道，把这三样全部颠倒了。这一课呼召我们省察自己的见证方式：我是在「邀请」，还是在「强加」？是在「回答真诚的发问」，还是在「赢得一场对方无法退场的辩论」？真正的福音，永远尊重听者说「不」的自由。",
                      "1 Peter 3:15 is the golden rule of Christian witness, and every word of it stands against “forced listening”: witness is “answering <em>those who ask you</em>” (prompted by their question, not imposed by us), it concerns “the reason for hope” (inviting people into hope, not condemning them), and it must be done “with gentleness and respect” (not with the pressure of power). Medieval forced preaching inverted all three. This lesson calls us to examine our own way of witnessing: am I “inviting” or “imposing”? Answering a sincere question, or winning a debate the other side cannot walk out of? The true Gospel always honors the hearer's freedom to say “no.”")),
                step(S5, S5E,
                    ul(
                        ("我分享信仰时，是在『邀请』，还是在某种程度上『强加』——利用关系、地位或情绪的压力？",
                         "When I share my faith, do I “invite,” or to some degree “impose” — using the pressure of relationship, status, or emotion?"),
                        ("『以温柔、敬畏的心回答各人』——我的见证真的有这两样吗，尤其面对不同信仰的人？",
                         "“With gentleness and respect” — does my witness truly have both, especially toward people of another faith?"),
                        ("如果被强迫的『相信』根本不是信，这如何重塑我对『成功的福音工作』的理解？",
                         "If a compelled “belief” is not belief at all, how does that reshape what I count as “successful” evangelism?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "诽谤的诞生——当讲道点燃暴力",
            "title_en": "The Birth of Libel — When Preaching Ignites Violence",
            "steps": [
                step(S1, S1E,
                    p("书中记载，从十二世纪起，犹太-基督关系急转直下，出现了一系列骇人的「反犹诽谤」：血祭诽谤、亵渎圣体、投毒水井、食人、行巫术、与魔鬼往来。与此同时，多明我会与方济各会的修士开始大量讲反犹的道，要求把犹太人「要么归信，要么驱逐」。这些诽谤经由讲台传遍乡野，直接点燃了实实在在的暴力：第一次十字军（1096 年）途中对莱茵兰犹太社群的屠杀，以及黑死病（约 1348 年）期间因「犹太人投毒」谣言而起的遍及全欧的杀戮。话语，结出了血的果子。",
                      "The book records that from the twelfth century, Jewish-Christian relations took a sharp turn for the worse, with a series of horrifying “anti-Jewish libels”: ritual murder, host desecration, well-poisoning, cannibalism, sorcery, commerce with the devil. At the same time, Dominican and Franciscan friars began preaching vehemently anti-Jewish sermons, demanding that Jews “either convert or be expelled.” These libels spread through the countryside from the pulpit and directly ignited real violence: the massacres of Rhineland Jewish communities during the First Crusade (1096), and the Europe-wide killings during the Black Death (c. 1348) fueled by rumors that “the Jews poisoned the wells.” Words bore fruit in blood.")),
                step(S2, S2E,
                    bq("「这些事我都恨恶……就是吐谎言的假见证，并弟兄中布散纷争的人。」",
                       "“There are things the LORD hates... a false witness who pours out lies and a person who stirs up conflict in the community.”",
                       "《箴言》6:16-19 · Proverbs 6:16-19")),
                step(S3, S3E,
                    p("<strong>דַּם · dam</strong>——「血」。最恶毒的诽谤之一是「血祭诽谤」：诬告犹太人为宗教仪式而杀害基督徒儿童取血。这是何等黑暗的讽刺——因为希伯来圣经恰恰极其严厉地禁止「吃血」、禁止流无辜人的血：「流人血的，他的血也必被人所流」(《创世记》9:6)，「不可流无辜人的血」是律法反复的呼喊。把一项律法本身最严禁的罪，反过来栽赃给守这律法的民族，是「假见证」的极致。<em>dam</em>——无辜者的血——在圣经里会「从地里发出哀声」(《创世记》4:10)；而那从十字军到大屠杀所流的犹太人的血，至今仍在向教会的良心发问。",
                      "<strong>דַּם · dam</strong> — “blood.” One of the most vicious libels was the “blood libel”: the false charge that Jews murdered Christian children for blood in their rituals. What dark irony — for the Hebrew Bible most strictly forbids “eating blood” and forbids shedding innocent blood: “whoever sheds human blood, by humans shall their blood be shed” (Genesis 9:6); “do not shed innocent blood” is a repeated cry of the Law. To pin onto a people the very sin their own Law most severely forbids is false witness at its extreme. In Scripture <em>dam</em> — innocent blood — “cries out from the ground” (Genesis 4:10); and the Jewish blood shed from the Crusades to the Shoah still questions the conscience of the Church.")),
                step(S4, S4E,
                    p("这一课不允许任何「话语是无害的」的幻想。《箴言》把神所恨恶的事并列：「吐谎言的假见证」与「布散纷争的人」并肩而立——因为前者必然导向后者。讲台上的诽谤，从来不会停在听众的耳朵里；它会走到街上，拿起石头与火把。对今天的我们，这是一记重锤：我们容许在自己心里、教会里、网络上流传的关于犹太人（或任何群体）的「故事」，绝不是中立的。每一个未经查证就接受、转述的偏见，都是在为某一处的暴力添柴。悔改，从拒绝传播谎言开始。",
                      "This lesson permits no illusion that “words are harmless.” Proverbs lists what God hates side by side: “a false witness who pours out lies” stands next to “one who stirs up conflict” — because the first inevitably leads to the second. Libel on the pulpit never stops in the listener's ear; it walks out into the street and picks up stones and torches. For us today this is a hammer blow: the “stories” about Jews (or any group) we allow to circulate in our hearts, our churches, our feeds are never neutral. Every prejudice we accept and pass on unverified adds fuel to violence somewhere. Repentance begins with refusing to spread lies.")),
                step(S5, S5E,
                    ul(
                        ("我是否曾在未经查证的情况下，相信并转述关于某个群体的负面『故事』？",
                         "Have I ever believed and passed on a negative “story” about a group without verifying it?"),
                        ("『假见证』与『布散纷争』被并列为神所恨恶的——这如何改变我对『只是说说而已』的看法？",
                         "“False witness” and “stirring up conflict” are listed together as things God hates — how does that change my view of words that are “just talk”?"),
                        ("无辜者的血『从地里发出哀声』。教会该如何面对从十字军到大屠杀所流的犹太人的血？",
                         "Innocent blood “cries out from the ground.” How should the Church face the Jewish blood shed from the Crusades to the Shoah?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "由犹太人讲的道——一个被遗忘的传统",
            "title_en": "Preaching by the Jews — A Forgotten Tradition",
            "steps": [
                step(S1, S1E,
                    p("这本书没有只把犹太人写成沉默的受害者。编者特别用篇幅介绍了「由犹太人讲的道」——一个深厚、悠久、却常被基督教世界忽略的传统。犹太讲道 (derashah) 的历史「至少可追溯两千年」。面对基督教的反犹讲道，犹太群体也在自己的会堂里讲道、教导、回应，坚固本族的信心。书中甚至提到混用希伯来语与本地语言的「马卡龙式讲道」。这一章是一个重要的提醒：在那场不对等的「相遇」中，犹太人从不只是被言说的客体；他们是有自己的声音、自己的智慧、自己的属灵传统的、活的主体。",
                      "This book does not write the Jews merely as silent victims. The editors give space to “preaching by the Jews” — a deep, ancient tradition often ignored by the Christian world. The history of Jewish preaching (the <em>derashah</em>) “goes back at least two thousand years.” Facing Christian anti-Jewish sermons, Jewish communities preached, taught, and responded in their own synagogues, strengthening the faith of their people. The book even mentions “macaronic sermons” mixing Hebrew with the local vernacular. This chapter is a vital reminder: in that unequal “encounter,” Jews were never merely the object spoken about; they were living subjects with their own voice, their own wisdom, and their own spiritual tradition.")),
                step(S2, S2E,
                    bq("「这些话……你也要殷勤教训你的儿女。无论你坐在家里，行在路上，躺下，起来，都要谈论。」",
                       "“These commandments... Impress them on your children. Talk about them when you sit at home and when you walk along the road, when you lie down and when you get up.”",
                       "《申命记》6:6-7 · Deuteronomy 6:6-7")),
                step(S3, S3E,
                    p("<strong>דְּרָשׁ · derash</strong>——「寻求」「探究」「讲解」。犹太讲道 <em>derashah</em> 与解经法 <em>midrash</em> 都来自这个字根：它的精神是「殷勤地探究经文、把它讲解出来」。这正是耶稣本人所行的——祂在拿撒勒的会堂里站起来读《以赛亚书》，然后「讲解」(路加福音 4)；祂在以马忤斯的路上「把……的话都给他们讲解明白了」(《路加福音》24:27)。耶稣是一位犹太的 darshan（讲道者）。当基督徒重新发现「由犹太人讲的道」这一传统，我们其实是在重新发现我们自己的主所站立其中的那个讲坛。",
                      "<strong>דְּרָשׁ · derash</strong> — “to seek,” “to inquire,” “to expound.” Both Jewish preaching (<em>derashah</em>) and the interpretive method (<em>midrash</em>) come from this root: its spirit is “to inquire diligently into the text and expound it.” This is exactly what Jesus himself did — he stood up in the synagogue at Nazareth to read Isaiah and then “expounded” it (Luke 4); on the road to Emmaus he “explained to them what was said in all the Scriptures” (Luke 24:27). Jesus was a Jewish <em>darshan</em>, a preacher. When Christians rediscover the tradition of “preaching by the Jews,” we are in fact rediscovering the very pulpit in which our own Lord stood.")),
                step(S4, S4E,
                    p("这一课邀请基督徒走出「只把犹太教看作基督教的背景板」的习惯，转而以「学习者」的谦卑姿态，承认我们有许多可以向犹太的讲道与解经传统领受的。我们讲道的形式——读经、讲解、应用——本身就承袭自会堂。从拉比们「殷勤探究每一个字」的态度，到他们带着问题与经文摔跤的勇气，都能丰富、校正、深化我们的讲台。「爱我民」不只是为过去的伤害悔改，更是带着尊重，向这个仍然活着、仍在 derash（探究）神话语的民族，谦卑学习。",
                      "This lesson invites Christians out of the habit of treating Judaism as “merely the backdrop to Christianity,” and into the humble posture of a “learner,” acknowledging how much we have to receive from the Jewish traditions of preaching and interpretation. The very form of our preaching — read, expound, apply — is inherited from the synagogue. From the rabbis' habit of “inquiring diligently into every word” to their courage to wrestle with the text through questions, there is much that can enrich, correct, and deepen our pulpit. <em>Ahavat Ammi</em> is not only repenting of past harm, but humbly learning, with respect, from a people who are still alive and still doing <em>derash</em> — inquiring into God's word.")),
                step(S5, S5E,
                    ul(
                        ("我是否只把犹太教当作基督教的『背景』，而从未想过可以谦卑地向它学习？",
                         "Do I treat Judaism only as Christianity's “background,” never imagining I could humbly learn from it?"),
                        ("耶稣是一位犹太讲道者(darshan)。认识祂讲道、解经的犹太脉络，如何丰富我读福音书的方式？",
                         "Jesus was a Jewish preacher (darshan). How does knowing the Jewish context of his preaching and exegesis enrich the way I read the Gospels?"),
                        ("『殷勤探究每一个字』——犹太解经的这份认真，如何挑战我读经的方式？",
                         "“Inquire diligently into every word” — how does the seriousness of Jewish interpretation challenge the way I read Scripture?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "重新讲道——以真理与爱述说",
            "title_en": "Preaching Anew — Telling It in Truth and Love",
            "steps": [
                step(S1, S1E,
                    p("读完这本书，基督徒不能只停在「惊骇」与「羞愧」里。这段历史的全部重量，是要把我们推向一个决定：从今往后，我们要怎样讲道、怎样教导、怎样谈论神立约的子民？学者们的研究，把一面镜子举到我们面前——镜中不只是「中世纪的他们」，也是「随时可能重蹈覆辙的我们」。这本书既是一份控诉，也是一份邀请：邀请教会拆毁那个虚构的「释经学上的犹太人」，停止「轻蔑的教导」，并学会以一种全新的方式——既诚实面对历史，又满有「爱我民」之心——去重新讲述这唯一的福音。",
                      "Having finished this book, Christians cannot stop at shock and shame. The full weight of this history is meant to press us toward a decision: from now on, how will we preach, teach, and speak of God's covenant people? The scholars' research holds up a mirror — and in it is not only “those medievals” but “us, ever liable to repeat them.” This book is both an indictment and an invitation: an invitation for the Church to dismantle the fictional “hermeneutical Jew,” to stop the teaching of contempt, and to learn a wholly new way — honest about history, and full of <em>Ahavat Ammi</em> — to retell the one Gospel.")),
                step(S2, S2E,
                    bq("「惟用爱心说诚实话，凡事长进，连于元首基督。」",
                       "“Speaking the truth in love, we will grow to become in every respect the mature body of him who is the head, that is, Christ.”",
                       "《以弗所书》4:15 · Ephesians 4:15")),
                step(S3, S3E,
                    p("<strong>חֶסֶד וֶאֱמֶת · chesed ve'emet</strong>——「慈爱与诚实」。这一对词在希伯来圣经里反复同行，是神品格的核心：祂是「有怜悯、有恩典……有丰盛的慈爱和诚实 (chesed ve'emet)」的神 (《出埃及记》34:6)。<em>Chesed</em>（坚定不移的、立约的爱）与 <em>emet</em>（真实、可靠）从不彼此对立——在神那里，最深的爱与最硬的真理是同一回事。这正是医治这段历史的钥匙：中世纪的讲道，既无 <em>emet</em>（满是谎言），也无 <em>chesed</em>（满是轻蔑）。「用爱心说诚实话」(以弗所书 4:15)，正是 <em>chesed ve'emet</em> 的回响：既不为了「友善」而粉饰历史的真相，也不为了「真理」而失去爱的温度。",
                      "<strong>חֶסֶד וֶאֱמֶת · chesed ve'emet</strong> — “lovingkindness and truth.” This pair walks together repeatedly in the Hebrew Bible, at the very heart of God's character: he is “compassionate and gracious... abounding in love and faithfulness (chesed ve'emet)” (Exodus 34:6). <em>Chesed</em> (steadfast, covenant love) and <em>emet</em> (truth, reliability) are never opposed — in God, the deepest love and the hardest truth are one and the same. This is the key to healing this history: medieval preaching had neither <em>emet</em> (it was full of lies) nor <em>chesed</em> (it was full of contempt). “Speaking the truth in love” (Ephesians 4:15) is the echo of <em>chesed ve'emet</em>: neither whitewashing the truth of history for the sake of being “nice,” nor losing the warmth of love for the sake of “truth.”")),
                step(S4, S4E,
                    p("这是整份指南的终点，也是一个起点。我们走过了讲台的权柄、被构造的「犹太人」、奥古斯丁的双刃定义、缺席者的画像、强迫的聆听、流血的诽谤、以及被遗忘的犹太讲道传统。如今，路摆在我们面前。愿我们成为这样一群基督徒：为教会的过去深深悔改，却不陷入瘫痪的自责；以真理面对历史，却以慈爱拥抱犹太民族；重新发现福音的犹太根源，并带着「爱我民」(Ahavat Ammi) 的心，去讲一篇配得上我们那位犹太弥赛亚的道。愿这八堂课，使我们的讲台，从今往后，结出生命而非死亡的果子。",
                      "This is the end of the whole guide, and also a beginning. We have walked through the authority of the pulpit, the constructed “Jew,” Augustine's double-edged doctrine, portraits of the absent, forced listening, bloody libel, and the forgotten tradition of Jewish preaching. Now the road lies before us. May we become Christians who repent deeply of the Church's past without sinking into paralyzed self-reproach; who face history with truth yet embrace the Jewish people with love; who rediscover the Jewish roots of the Gospel and, with a heart of <em>Ahavat Ammi</em>, preach a sermon worthy of our Jewish Messiah. May these eight lessons make our pulpit, from this day on, bear the fruit of life and not of death.")),
                step(S5, S5E,
                    ul(
                        ("『用爱心说诚实话』——在谈论这段历史时，我更容易丢掉哪一样：诚实(emet)，还是爱(chesed)？",
                         "“Speaking the truth in love” — in speaking of this history, which am I more likely to drop: truth (emet) or love (chesed)?"),
                        ("具体而言，从今以后我会如何不同地谈论犹太人、犹太教、以及福音的犹太根源？",
                         "Concretely, how will I speak differently from now on about Jews, Judaism, and the Jewish roots of the Gospel?"),
                        ("『爱我民』(Ahavat Ammi) 对我意味着什么？它会要求我采取哪一个具体的行动？",
                         "What does <em>Ahavat Ammi</em> — “love of my people” — mean for me? What one concrete action does it ask of me?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "为一个重新学习讲道的教会祝祷",
    "closing_title_en": "A Blessing for a Church Relearning How to Preach",
    "closing_zh": "「愿耶和华使祂的脸光照你，赐恩给你。」<br/><br/>愿你不再让那个虚构的「犹太人」住在你的讲台、你的心里；<br/>愿你为「轻蔑的教导」所流的血而哀恸、而悔改；<br/>愿你以慈爱与诚实 (chesed ve'emet)，<br/>重新认识那真实的、蒙爱的、立约的犹太民族——<br/>你信仰之根所在的那棵老橄榄树。<br/><br/>愿你记得：托着你的，不是你，乃是那根。<br/>愿你从今以后所讲的每一篇道，<br/>都配得上那位站在拿撒勒会堂里、展开书卷的犹太拉比——耶稣 (Yeshua)。",
    "closing_en": "“The LORD make his face shine upon you and be gracious to you.”<br/><br/>May you no longer let the fictional “Jew” dwell on your pulpit or in your heart.<br/>May you grieve and repent of the blood shed by the teaching of contempt.<br/>May you, in lovingkindness and truth (chesed ve'emet),<br/>come to know the real, beloved, covenant people of Israel —<br/>the old olive tree in which the root of your faith is found.<br/><br/>Remember: it is not you who support the root, but the root that supports you.<br/>And may every sermon you preach from this day on<br/>be worthy of the Jewish rabbi who stood in the synagogue at Nazareth and unrolled the scroll — Yeshua.",
}

# -*- coding: utf-8 -*-
"""Content module for study-jewish-gospels.html.

Daniel Boyarin, *The Jewish Gospels: The Story of the Jewish Christ*,
foreword by Jack Miles (The New Press, 2012).
"""

RHYTHM_ZH = """        <strong>① 作者说什么</strong>—— 用博亚林自己的语境概述他的论点；<br/>
        <strong>② 关键经文</strong>—— 他所读的圣经依据；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，连接两个传统；<br/>
        <strong>④ 基督徒视角</strong>—— 这一发现如何更新我们读福音书的眼光；<br/>
        <strong>⑤ 诚实的提问</strong>—— 可以继续追问、默想的问题。"""

RHYTHM_EN = """        <strong>① What the Author Says</strong> — Boyarin's argument in his own frame;<br/>
        <strong>② Key Scripture</strong> — the biblical text he is reading;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that bridges the two traditions;<br/>
        <strong>④ A Christian Lens</strong> — how the discovery renews the way we read the Gospels;<br/>
        <strong>⑤ Honest Questions</strong> — questions to keep asking and to contemplate."""


def step(label_zh, label_en, *body):
    return {"label_zh": label_zh, "label_en": label_en, "body": list(body)}

def p(zh, en):
    return {"type": "p", "zh": zh, "en": en}

def bq(zh, en, cite=None):
    return {"type": "blockquote", "zh": zh, "en": en, "cite": cite}

def ul(*items):
    return {"type": "ul", "items": [{"zh": z, "en": e} for z, e in items]}

S1, S1E = "① 作者说什么", "① What the Author Says"
S2, S2E = "② 关键经文", "② Key Scripture"
S3, S3E = "③ 希伯来语之眼", "③ Through Hebrew Eyes"
S4, S4E = "④ 基督徒视角", "④ A Christian Lens"
S5, S5E = "⑤ 诚实的提问", "⑤ Honest Questions"


study = {
    "title_tag": "《犹太福音书》研习指南 · The Jewish Gospels — Study Guide · 妥拉之光",
    "meta_desc": "A study guide to Daniel Boyarin's The Jewish Gospels — eight bilingual lessons showing how the divine Messiah, the Son of Man, and even the suffering Messiah were already Jewish ideas before Jesus, read with Hebrew eyes.",
    "og_title": "The Jewish Gospels — A Study Guide",
    "og_desc": "Eight bilingual lessons through Daniel Boyarin's The Jewish Gospels: the divine Son of Man, the suffering Messiah, and Jesus the Torah-faithful Jew — Christianity as a path Judaism took.",
    "cover_alt": "The Jewish Gospels: The Story of the Jewish Christ — Study Guide",
    "tagline_zh": "研习指南 · 弥赛亚的犹太根源 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · The Jewish Roots of Messiah · 2026 · 5 · 31",
    "headline_zh": "犹太福音书<br/>研习指南",
    "headline_en": "The Jewish Gospels<br/>A Study Guide",
    "deck_zh": "八堂课程，跟随顶尖塔木德学者博亚林 (Daniel Boyarin) 一个惊人的论证：那位「神性的弥赛亚」、那位驾云而来的「人子」、甚至那位「受苦的弥赛亚」——这些常被视为基督教「发明」的核心观念，其实在耶稣之前，早已是犹太人自己的盼望。",
    "deck_en": "Eight lessons following the eminent Talmud scholar Daniel Boyarin's startling argument: the “divine Messiah,” the “Son of Man” who comes on the clouds, and even the “suffering Messiah” — ideas often taken as Christian “inventions” — were, before Jesus, already the hope of the Jews themselves.",
    "byline_zh": "基于丹尼尔·博亚林 (Daniel Boyarin)《犹太福音书——犹太基督的故事》(The New Press, 2012；杰克·迈尔斯 Jack Miles 作序)",
    "byline_en": "Based on The Jewish Gospels: The Story of the Jewish Christ by Daniel Boyarin, foreword by Jack Miles (The New Press, 2012)",
    "readtime_zh": "约 55 分钟通读",
    "readtime_en": "~55 min read-through",
    "book_url": "https://thenewpress.com/books/jewish-gospels",
    "book_link_zh": "购买原书",
    "book_link_en": "Get the Book",
    "cta_url": "https://thenewpress.com/books/jewish-gospels",
    "cta_zh": "购买《犹太福音书》原书 · The New Press",
    "cta_en": "Get the Book — The Jewish Gospels · The New Press",

    "lead_zh": "这份指南陪你读博亚林 (Daniel Boyarin) 的《犹太福音书》——一部由当代最重要的犹太学者之一写成、却令许多基督徒既惊讶又感动的著作。博亚林是加州大学伯克利分校的塔木德文化教授，一位虔诚的正统派犹太人。他的核心论点震撼而温柔：我们以为最「基督教」、最与犹太教对立的那些观念——神竟有「第二位格」、弥赛亚是神又是人、弥赛亚要受苦受死来赎罪——其实<em>没有一样</em>是凭空的「发明」。它们全都深深扎根于第二圣殿时期犹太人自己的圣经默想里。换句话说，福音书是一卷彻头彻尾的<em>犹太</em>书。",
    "lead_en": "This guide walks you through Daniel Boyarin's <em>The Jewish Gospels</em> — a work by one of today's foremost Jewish scholars that nonetheless startles and moves many Christians. Boyarin is professor of Talmudic culture at UC Berkeley and a devout Orthodox Jew. His central argument is jolting and tender: the ideas we take to be most “Christian” and most opposed to Judaism — that God has a “second figure,” that the Messiah is both God and man, that the Messiah must suffer and die to atone — are <em>not one of them</em> a Christian “invention.” They are all deeply rooted in Second Temple Jewish meditation on their own Scriptures. In other words, the Gospels are a thoroughly <em>Jewish</em> book.",

    "intro": [
        p("博亚林写道：「与其把基督教看作一个全新的发明，不如把它看作犹太教所走的众多道路之一——一条与拉比犹太人所走的那条同样古老的路。」这不是要消解福音的尊贵，恰恰相反，他说这「自有一种威严」。对相信耶书亚的我们而言，这本书是一份意外的礼物：一位犹太学者，用最严谨的学术，帮我们重新看见我们的主有多么彻底地是一位犹太人。",
          "Boyarin writes: “Rather than seeing Christianity as a new invention, seeing it as one of the paths that Judaism took — a path as ancient in its sources as the one that rabbinic Jews trod — has a majesty of its own.” This does not dissolve the dignity of the Gospel; on the contrary, he says it “has a majesty of its own.” For those of us who believe in Yeshua, this book is an unexpected gift: a Jewish scholar, with the most rigorous scholarship, helping us see afresh just how thoroughly Jewish our Lord is."),
        p("本指南共 <strong>八堂课</strong>，循着书中的核心论证展开。每一堂遵循同样的五部分节奏：",
          "The guide is structured as <strong>eight lessons</strong>, following the book's central argument. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句提醒：博亚林是犹太人，不是基督徒；他并不宣称耶稣就是弥赛亚。但他诚实的学术，反而为我们清除了一个巨大的误解——「相信一位神性的、受苦的弥赛亚，就等于背离了犹太教」。愿这八堂课，使你更深地爱那位犹太的耶书亚，也更有底气、更温柔地与犹太朋友谈论祂。",
          "A word of note: Boyarin is a Jew, not a Christian; he does not claim Jesus is the Messiah. But his honest scholarship clears away a vast misunderstanding — that “to believe in a divine, suffering Messiah is to depart from Judaism.” May these eight lessons make you love the Jewish Yeshua more deeply, and speak of him with Jewish friends more confidently and more tenderly."),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "两个名号——「神的儿子」与「人子」",
            "title_en": "Two Titles — “Son of God” and “Son of Man”",
            "steps": [
                step(S1, S1E,
                    p("博亚林一开篇就颠覆了一个我们以为理所当然的常识。大多数基督徒以为：「神的儿子」指耶稣的<em>神性</em>，「人子」指祂的<em>人性</em>。博亚林指出，在《马可福音》里，事情几乎正好相反。「神的儿子」是希伯来圣经里<em>地上君王</em>的古老称号——大卫家的、被膏立的、有血有肉的以色列王（诗篇 2 篇：「你是我的儿子，我今日生你」指的是登基之日）。而「人子」——那个看似谦卑的称号——反倒指向《但以理书》7 章里那位驾着天云而来、被赐予永远国度、万民都要敬拜的<em>神性</em>救赎者。换言之：「神的儿子」标示祂是君王弥赛亚，「人子」标示祂是神的一部分。",
                      "Boyarin overturns a commonplace we take for granted. Most Christians assume “Son of God” denotes Jesus' <em>divinity</em> and “Son of Man” his <em>humanity</em>. Boyarin shows that in the Gospel of Mark it is nearly the reverse. “Son of God” is the ancient Hebrew-Bible title for the <em>earthly king</em> — the anointed, flesh-and-blood king of David's line (Psalm 2: “You are my son; this day I have begotten you” means the day of enthronement). And “Son of Man” — that seemingly humble title — points to the <em>divine</em> Redeemer of Daniel 7 who comes on the clouds of heaven, is given an everlasting kingdom, and is worshiped by all nations. In short: “Son of God” marks him as King-Messiah; “Son of Man” marks him as a part of God.")),
                step(S2, S2E,
                    bq("「我观看,见有一位像人子的,驾着天云而来,被领到亘古常在者面前……得了权柄、荣耀、国度,使各方、各国、各族的人都事奉他。」",
                       "“There before me was one like a son of man, coming with the clouds of heaven... He was given authority, glory and sovereign power; all nations and peoples of every language worshiped him.”",
                       "《但以理书》7:13-14 · Daniel 7:13-14")),
                step(S3, S3E,
                    p("<strong>בַּר אֱנָשׁ · bar enash</strong>——「人子」（亚兰文）。这个词字面就是「一个人的样子」，却在《但以理书》7 章里指向一位<em>非人</em>的、驾云的、配受敬拜的天上之君。博亚林指出，正因为这位「像人子的」被领到「亘古常在者」（那位坐宝座的老者）面前、并与祂同得荣耀与国度，犹太人早已在思想一个惊人的可能：神的宝座旁，还有「第二位」。福音书称耶稣为「人子」，不是在淡化祂，而是在用犹太人最高的弥赛亚密码，宣告祂的神性。",
                      "<strong>בַּר אֱנָשׁ · bar enash</strong> — “son of man” (Aramaic). The phrase literally means “one in the form of a human,” yet in Daniel 7 it points to a <em>non-human</em>, cloud-riding, worship-worthy heavenly king. Boyarin notes that precisely because this “one like a son of man” is brought before the “Ancient of Days” (the elder seated on the throne) and shares his glory and kingdom, Jews were already pondering a staggering possibility: beside God's throne, a “second figure.” When the Gospels call Jesus “Son of Man,” they are not toning him down — they are proclaiming his divinity in the Jews' highest messianic code.")),
                step(S4, S4E,
                    p("这一课为基督徒打开了福音书的一扇门。当耶稣在公会面前说「你们必看见<em>人子</em>坐在那权能者的右边，驾着天上的云降临」(可 14:62)，大祭司立刻撕裂衣服喊「僭妄」——因为他<em>完全听懂了</em>：耶稣是在引用《但以理书》7 章，宣称自己就是那位与神同坐、配受敬拜的「人子」。耶稣对自己神性最直接的宣告，用的不是希腊哲学的语言，而是希伯来先知的异象。读懂了「人子」，我们才读懂了耶稣是怎样在祂自己的犹太处境里，宣告自己是谁。",
                      "This lesson opens a door into the Gospels. When Jesus tells the council, “you will see the <em>Son of Man</em> sitting at the right hand of the Mighty One and coming on the clouds of heaven” (Mark 14:62), the high priest instantly tears his robes and cries “blasphemy” — because he <em>fully understood</em>: Jesus is quoting Daniel 7, claiming to be the “Son of Man” who sits with God and is worthy of worship. Jesus' most direct claim to divinity uses not the language of Greek philosophy but the vision of a Hebrew prophet. Only when we grasp “Son of Man” do we grasp how Jesus, within his own Jewish setting, declared who he is.")),
                step(S5, S5E,
                    ul(
                        ("我一直以为『人子』是指耶稣的人性。这个被颠倒过来的发现，如何改变我读福音书的方式？",
                         "I always thought “Son of Man” meant Jesus' humanity. How does this reversal change the way I read the Gospels?"),
                        ("耶稣用《但以理书》7章宣告自己。我是否常忽略，耶稣最深的自我宣告其实深植于希伯来圣经？",
                         "Jesus declares himself through Daniel 7. Do I often miss that Jesus' deepest self-claims are rooted in the Hebrew Bible?"),
                        ("大祭司一听就懂了。今天若我真听懂『人子』的分量，会如何回应那位坐在权能者右边的主？",
                         "The high priest understood at once. If I truly grasped the weight of “Son of Man,” how would I respond to the One seated at the right hand of Power?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "神宝座旁的「第二位」——但以理的异象",
            "title_en": "The “Second Figure” Beside the Throne — Daniel's Vision",
            "steps": [
                step(S1, S1E,
                    p("博亚林深入《但以理书》7 章那个「不安」的细节：异象里有<em>不止一个</em>宝座。一位是「亘古常在者」，一位白发的老者，坐在宝座上；而那位「像人子的」被驾着天云领来，与祂一同得国、得荣耀、受敬拜。博亚林指出，这幅画面酷似古代近东「老王向少王传位」的图景，也像古代神话里「老神向少神交棒」。但在以色列严格的一神信仰里，这就制造了一个深刻的张力：怎么会有「两位」都配坐宝座、都配受敬拜，而以色列又始终坚持「耶和华我们神是独一的主」？这张力，正是后来「神性弥赛亚」观念的温床。",
                      "Boyarin probes the “unsettling” detail of Daniel 7: the vision has <em>more than one</em> throne. One is the “Ancient of Days,” a white-haired elder seated on the throne; and the “one like a son of man” is brought on the clouds to share with him kingdom, glory, and worship. Boyarin notes the scene resembles the ancient Near Eastern image of an elder king passing the torch to a younger one, and the mythic passing from older gods to younger. But within Israel's strict monotheism this creates a deep tension: how can there be “two” both worthy of the throne and of worship, while Israel insists “the LORD our God is one”? That tension is the very seedbed of the later idea of a divine Messiah.")),
                step(S2, S2E,
                    bq("「我观看,见有宝座设立,上头坐着亘古常在者……见有一位像人子的,驾着天云而来。」",
                       "“As I looked, thrones were set in place, and the Ancient of Days took his seat... and there before me was one like a son of man, coming with the clouds of heaven.”",
                       "《但以理书》7:9, 13 · Daniel 7:9, 13")),
                step(S3, S3E,
                    p("<strong>כָּרְסָוָן · karsavan</strong>——「众宝座」（亚兰文，复数）。博亚林强调这个复数极其关键：经文说的是「众宝座」，不是一个。后来的拉比对此极为警惕，发展出反对「天上有两个权能 (shtei rashuyot)」的严厉教导——这本身就证明：当时确有犹太人，从但以理的「众宝座」读出了神宝座旁那「第二位」。这场犹太人内部关于「神是否可以有第二位格」的古老辩论，远早于基督教，也正是基督教「父与子」之信仰所生长的犹太土壤。",
                      "<strong>כָּרְסָוָן · karsavan</strong> — “thrones” (Aramaic, plural). Boyarin stresses the plural is crucial: the text says “thrones,” not one. Later rabbis grew so wary of this that they developed stern teaching against “two powers in heaven” (<em>shtei rashuyot</em>) — which itself proves that some Jews were reading a “second figure” beside God's throne out of Daniel's “thrones.” This ancient inner-Jewish debate over whether God could have a second figure long predates Christianity, and is the very Jewish soil in which the Christian faith of “Father and Son” grew.")),
                step(S4, S4E,
                    p("对基督徒而言，这是一个解放性的发现。三位一体常被当作「基督教强加给犹太一神论的外来物」。但博亚林表明：神的「独一」之内仍可有「复数」的奥秘，这个问题早在耶稣之前就在犹太人心里翻腾了。基督教所宣告的「父与子」，不是对以色列一神信仰的背叛，而是对以色列圣经里那个一直悬而未决的奥秘——「众宝座」「第二位」——的一种回答。我们敬拜坐在父右边的耶书亚，不是拜了「第二位神」，而是认信那位独一真神所启示的、祂自己宝座旁的荣耀。",
                      "For Christians this is a liberating discovery. The Trinity is often treated as “a foreign thing Christianity imposed on Jewish monotheism.” But Boyarin shows that within God's “oneness” there could still be a mystery of “plurality,” and that this question churned in Jewish hearts long before Jesus. The “Father and Son” that Christianity proclaims is not a betrayal of Israel's monotheism but an answer to a mystery left open in Israel's own Scriptures — the “thrones,” the “second figure.” To worship Yeshua seated at the Father's right hand is not to worship “a second god,” but to confess the glory the one true God revealed beside his own throne.")),
                step(S5, S5E,
                    ul(
                        ("『天上有两个权能』的辩论早于基督教。这如何改变我对『三位一体是否违背一神论』的理解？",
                         "The “two powers in heaven” debate predates Christianity. How does that change how I understand whether the Trinity violates monotheism?"),
                        ("拉比后来严厉反对这种读法,恰恰证明它曾存在。被禁止的解读,有时正是被遗忘的真相吗？",
                         "The rabbis' later stern opposition proves the reading once existed. Is a forbidden interpretation sometimes a forgotten truth?"),
                        ("我能否在『耶和华是独一的』与『敬拜坐在父右边的子』之间,安然持守这奥秘？",
                         "Can I rest in the mystery between “the LORD is one” and worshiping the Son seated at the Father's right hand?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "并非只有耶稣——以诺与以斯拉笔下的犹太弥赛亚",
            "title_en": "Not Jesus Alone — The Jewish Messiahs of Enoch and Ezra",
            "steps": [
                step(S1, S1E,
                    p("博亚林进一步证明：对「人子」式神性救赎者的盼望，绝非耶稣独有。在第一世纪前后的犹太文献——《以诺一书》（特别是「比喻篇」）与《以斯拉四书》——里，那位「人子」「被拣选者」「弥赛亚」被描绘成一位先存的、隐藏在神面前、要在末日显现、施行审判与救赎的天上之君。换言之，当耶稣的同代犹太人听见「人子」时，他们脑海中浮现的，已经是一位<em>神性的、末世的弥赛亚</em>。耶稣并不是凭空抛出一个新概念，祂是踏入了一个早已铺好的、活生生的犹太期待。",
                      "Boyarin further shows that the hope for a “Son of Man”-style divine Redeemer was by no means unique to Jesus. In Jewish texts from around the first century — <em>1 Enoch</em> (especially the “Parables”) and <em>4 Ezra</em> — the “Son of Man,” “the Chosen One,” “the Messiah” is portrayed as a pre-existent figure hidden before God, to be revealed at the end of days to execute judgment and redemption. In other words, when Jesus' contemporaries heard “Son of Man,” what came to mind was already a <em>divine, end-time Messiah</em>. Jesus did not toss out a new concept from nowhere; he stepped into a living Jewish expectation already laid out.")),
                step(S2, S2E,
                    bq("「他被拣选、藏在神面前,在世界受造以先……众人的心要被祂搅动。」",
                       "“He was chosen and hidden in God's presence before the creation of the world... and all who dwell on the earth will fall down and worship before him.”",
                       "《以诺一书》48 章（释义）· 1 Enoch 48 (paraphrase)")),
                step(S3, S3E,
                    p("<strong>נִבְחָר · nivchar</strong>——「被拣选者」。这是《以诺一书》给那位天上人子的核心称号之一。它与以赛亚书里神的「仆人」「我所拣选的」(赛 42:1) 直接呼应——而福音书在耶稣受洗、登山变像时，天上的声音正是说：「这是我的爱子（或：我所拣选的），我所喜悦的，你们要听祂。」(路 9:35) 同一条「被拣选者」的线，从以赛亚、穿过以诺、落在耶稣身上。福音书不是在引用一套陌生的希腊概念，而是在弹奏一首犹太人耳熟能详的旋律。",
                      "<strong>נִבְחָר · nivchar</strong> — “the Chosen One.” This is one of <em>1 Enoch</em>'s central titles for the heavenly Son of Man. It echoes directly God's “servant,” “my chosen one” in Isaiah (Isa 42:1) — and at Jesus' baptism and transfiguration the voice from heaven says exactly, “This is my Son, whom I have chosen; listen to him” (Luke 9:35). The same thread of “the Chosen One” runs from Isaiah, through Enoch, and lands on Jesus. The Gospels are not quoting a foreign set of Greek concepts but playing a melody Jewish ears knew well.")),
                step(S4, S4E,
                    p("这一课拆掉了一道我们常立的假墙：「犹太人的弥赛亚只是个属世的政治君王，神性的弥赛亚是基督徒后来加上去的。」博亚林表明，事实远比这丰富：在耶稣的时代，犹太人的弥赛亚盼望里，<em>既有</em>属世的大卫之子，<em>也有</em>天上的神性人子，两者甚至彼此交织。这意味着，第一批相信耶稣的犹太门徒，并不需要「离开犹太教」才能敬拜一位神性的弥赛亚——他们是在自己民族最深的盼望里，认出了那位他们一直在等候的「被拣选者」。",
                      "This lesson tears down a false wall we often build: “the Jews' Messiah was merely an earthly political king; a divine Messiah was something Christians added later.” Boyarin shows the truth is far richer: in Jesus' day, Jewish messianic hope held <em>both</em> the earthly son of David <em>and</em> the heavenly divine Son of Man, even interwoven. This means the first Jewish disciples who believed in Jesus did not need to “leave Judaism” to worship a divine Messiah — they recognized, in their own people's deepest hope, the “Chosen One” they had long awaited.")),
                step(S5, S5E,
                    ul(
                        ("我是否曾以为『神性的弥赛亚』是基督徒后加的？以诺与以斯拉的证据如何挑战这个假设？",
                         "Did I assume a “divine Messiah” was a later Christian addition? How does the evidence of Enoch and Ezra challenge that?"),
                        ("第一批犹太门徒不需『离开犹太教』就敬拜弥赛亚。这如何改变我对『信耶稣 = 不再做犹太人』的看法？",
                         "The first Jewish disciples didn't have to “leave Judaism” to worship the Messiah. How does that change my view that “believing in Jesus = no longer being Jewish”?"),
                        ("『被拣选者』这条线从以赛亚到以诺到耶稣。这如何让我更敬畏圣经叙事的连贯与深度？",
                         "The thread of “the Chosen One” runs from Isaiah to Enoch to Jesus. How does that deepen my awe at the coherence of Scripture's story?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "耶稣守洁食——一位忠于妥拉的加利利犹太人",
            "title_en": "Jesus Kept Kosher — A Torah-Faithful Galilean Jew",
            "steps": [
                step(S1, S1E,
                    p("许多人读《马可福音》7 章，以为耶稣在那里「废除了洁食律法」「宣告一切食物都洁净」。博亚林作为塔木德专家，给出了一个截然不同、却更贴近文本的读法。他指出，那场争论的焦点根本不是「该不该守洁食」，而是法利赛人的一项<em>口传传统</em>——饭前洗手的礼仪规条。耶稣不是在攻击妥拉，恰恰相反，祂是在<em>捍卫</em>妥拉的本意，斥责法利赛人「拘守人的传统，离弃神的诫命」（例如用「各耳板」的誓言来逃避奉养父母的诫命）。博亚林笔下的耶稣，是一位<em>保守的、忠于妥拉的</em>加利利犹太人，在为成文妥拉的真义而与耶路撒冷来的人争辩。",
                      "Many read Mark 7 as Jesus “abolishing the food laws” and “declaring all foods clean.” Boyarin, a Talmud specialist, offers a very different reading, closer to the text. He shows the dispute was not about “whether to keep kosher” at all, but about a Pharisaic <em>oral tradition</em> — the ritual of hand-washing before meals. Jesus is not attacking Torah; on the contrary, he is <em>defending</em> its true intent, rebuking the Pharisees for “holding to human tradition and abandoning the command of God” (e.g., using the “Corban” vow to evade the command to honor one's parents). Boyarin's Jesus is a <em>conservative, Torah-faithful</em> Galilean Jew, contending for the real meaning of the written Torah against people who came from Jerusalem.")),
                step(S2, S2E,
                    bq("「你们诚然是废弃神的诫命,要守自己的遗传……摩西说:当孝敬父母……你们倒说:人若对父母说,我所当奉给你的,已经作了各耳板。」",
                       "“You have let go of the commands of God and are holding on to human traditions... For Moses said, ‘Honor your father and your mother’... but you say that if anyone declares that what might have been used to help their parents is Corban...’”",
                       "《马可福音》7:8-11 · Mark 7:8-11")),
                step(S3, S3E,
                    p("<strong>קָרְבָּן · korban</strong>——「献给神的供物」。耶稣举的正是这个词：有人用「我的财物已是 <em>korban</em>（归神了）」的誓言为借口，逃避奉养年迈父母的妥拉诫命。耶稣的指控极其犹太、极其先知：你们用一条<em>人造的</em>誓言规条，架空了神<em>亲口</em>颁布的第五诫。这正是希伯来先知一贯的呼声——「我喜爱怜恤，不喜爱祭祀」(何 6:6)。耶稣站在阿摩司、何西阿、以赛亚的行列里，捍卫律法的<em>心</em>，对抗那使律法落空的「人的遗传」。",
                      "<strong>קָרְבָּן · korban</strong> — “an offering devoted to God.” Jesus cites this very word: someone uses the vow “what I have is already <em>korban</em> (devoted to God)” as a pretext to evade the Torah command to support aging parents. Jesus' charge is intensely Jewish and prophetic: you have used a <em>man-made</em> vow-rule to hollow out the fifth commandment God <em>spoke with his own mouth</em>. This is the constant cry of the Hebrew prophets — “I desire mercy, not sacrifice” (Hos 6:6). Jesus stands in the line of Amos, Hosea, and Isaiah, defending the <em>heart</em> of the Law against the “tradition of men” that nullifies it.")),
                step(S4, S4E,
                    p("这一课温柔地纠正了基督徒一个根深蒂固的误读——把耶稣描绘成「反律法的革命者」，仿佛祂来是要废掉那「沉重的犹太律法」。博亚林（一位犹太学者！）帮我们看清：耶稣明明说「莫想我来要废掉律法……我来不是要废掉,乃是要成全」(太 5:17)，祂是在<em>律法之内</em>、为律法的真义而战。当我们不再把「犹太人 vs 耶稣」「律法 vs 恩典」简单对立，我们才第一次看见福音书里那位真实的、守安息日、过节期、忠于妥拉、又满有先知怒火的犹太拉比。认识这位耶稣，是认识祂的第一步。",
                      "This lesson gently corrects a deep-rooted Christian misreading — painting Jesus as “an anti-law revolutionary,” as if he came to abolish the “heavy Jewish law.” Boyarin (a Jewish scholar!) helps us see clearly: Jesus plainly said, “Do not think that I have come to abolish the Law... I have not come to abolish but to fulfill” (Matt 5:17); he fights <em>within</em> the Law, for its true meaning. When we stop pitting “Jews vs. Jesus” and “law vs. grace” against each other, we see for the first time the real Jewish rabbi of the Gospels — Sabbath-keeping, feast-celebrating, Torah-faithful, and full of prophetic fire. To know this Jesus is the first step to knowing him.")),
                step(S5, S5E,
                    ul(
                        ("我是否把耶稣读成了一位『反律法的革命者』？《马太福音》5:17如何拦阻这种读法？",
                         "Have I read Jesus as “an anti-law revolutionary”? How does Matthew 5:17 resist that reading?"),
                        ("耶稣捍卫律法的『心』,对抗使律法落空的『人的遗传』。我自己有哪些『遗传』正架空着神的诫命？",
                         "Jesus defends the “heart” of the Law against “human tradition” that nullifies it. What “traditions” of mine might hollow out God's commands?"),
                        ("看见一位守妥拉、过节期的犹太耶稣,如何改变我与祂的关系，以及我读福音书的方式？",
                         "Seeing a Torah-keeping, feast-celebrating Jewish Jesus — how does it change my relationship with him and my reading of the Gospels?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "受苦的弥赛亚——一个犹太的观念",
            "title_en": "The Suffering Messiah — A Jewish Idea",
            "steps": [
                step(S1, S1E,
                    p("这是全书最大胆、也最动人的一章。通行的看法（博亚林引用了犹太史家克劳斯纳的经典表述）是：「受苦、受死、赎罪的弥赛亚」是基督徒在耶稣被钉之后,为了解释这桩丑闻而<em>事后发明</em>的，并且是把本指「以色列受苦」的《以赛亚书》53 章<em>篡改</em>成了「弥赛亚受苦」。博亚林斩钉截铁地说：「这个流行的看法必须被彻底拒绝。」他论证：「受苦受辱的弥赛亚」这一观念，在耶稣降世<em>之前</em>就毫不陌生地存在于犹太教中，并且一直延续到近代早期。一个会受苦、会替众人赎罪的弥赛亚，犹太人读起来毫无障碍——因为它本就是从圣经的细读（midrash）中长出来的。",
                      "This is the boldest and most moving chapter. The standard view (Boyarin cites the Jewish historian Joseph Klausner's classic statement) is that a “suffering, dying, atoning Messiah” was <em>invented after the fact</em> by Christians to explain the scandal of Jesus' crucifixion, and that they <em>distorted</em> Isaiah 53 — originally about “Israel's suffering” — into “the Messiah's suffering.” Boyarin flatly declares: “This commonplace view has to be rejected completely.” He argues that the idea of a humiliated, suffering Messiah was not at all alien within Judaism <em>before</em> Jesus, and remained current well into the early modern period. A Messiah who would suffer and vicariously atone gave Jews no difficulty — because it grew from a close reading (midrash) of Scripture itself.")),
                step(S2, S2E,
                    bq("「他诚然担当我们的忧患……哪知他为我们的过犯受害,为我们的罪孽压伤……耶和华使我们众人的罪孽都归在他身上。」",
                       "“Surely he took up our pain and bore our suffering... he was pierced for our transgressions, he was crushed for our iniquities... and the LORD has laid on him the iniquity of us all.”",
                       "《以赛亚书》53:4-6 · Isaiah 53:4-6")),
                step(S3, S3E,
                    p("<strong>מִדְרָשׁ · midrash</strong>——「探究、解读」，犹太人把不同经卷彼此对照、引出新意的释经方法。博亚林的关键洞见是：把《以赛亚书》53 章「受苦的仆人」与《但以理书》7 章「得荣耀的人子」<em>并读</em>，从而得出「一位<em>先受苦、后得荣耀</em>的弥赛亚」——这正是地道的、犹太式的 <em>midrash</em>。换言之，福音书呈现耶稣「受苦、受死、复活、得荣耀」，用的不是外来的逻辑，而是第二圣殿犹太人最熟悉的读经法。受苦的弥赛亚不是反犹太的丑闻，而是犹太人细读自己圣经时,本就可能、也确实得出的结论。",
                      "<strong>מִדְרָשׁ · midrash</strong> — “inquiry, interpretation,” the Jewish method of reading by setting different scriptures side by side to draw out new meaning. Boyarin's key insight: reading the “suffering servant” of Isaiah 53 <em>together with</em> the “glorified Son of Man” of Daniel 7, and so deriving a Messiah who <em>first suffers, then is glorified</em> — this is thoroughly Jewish <em>midrash</em>. In other words, when the Gospels present Jesus as “suffering, dying, rising, glorified,” they use not a foreign logic but the very method of reading most familiar to Second Temple Jews. The suffering Messiah is not an anti-Jewish scandal but a conclusion Jews could — and did — reach by reading their own Scriptures closely.")),
                step(S4, S4E,
                    p("对基督徒，尤其对向犹太朋友作见证的我们，这一章是巨大的鼓励。我们常被告知：「十字架是绊脚石——犹太人永远无法接受一位受苦的弥赛亚。」博亚林（再说一次，他是犹太人）温柔地推翻了这个绝对化的说法。当然，最终是否承认<em>这一位</em>受苦者就是弥赛亚，是信心的抉择；但「受苦的弥赛亚」这个观念本身，从来不是反犹太的。这意味着，我们传讲十字架时，不是在传一个与以色列圣经格格不入的外来故事，而是在揭示她自己最深的盼望——那位「为我们的过犯受害」的仆人，正是她所等候的那一位。",
                      "For Christians, and especially for those of us witnessing to Jewish friends, this chapter is a vast encouragement. We are often told: “The cross is a stumbling block — Jews can never accept a suffering Messiah.” Boyarin (again, a Jew) gently overturns that absolute claim. Of course, whether to confess that <em>this</em> sufferer is the Messiah is a decision of faith; but the idea of a “suffering Messiah” itself was never anti-Jewish. This means that when we proclaim the cross, we are not preaching a foreign story alien to Israel's Scriptures, but unveiling her own deepest hope — that the servant “pierced for our transgressions” is the very One she awaits.")),
                step(S5, S5E,
                    ul(
                        ("我是否相信『犹太人永远无法接受受苦的弥赛亚』？博亚林的证据如何挑战这个绝对化的说法？",
                         "Do I believe “Jews can never accept a suffering Messiah”? How does Boyarin's evidence challenge that absolute claim?"),
                        ("把以赛亚书53章与但以理书7章并读,得出『先受苦、后得荣耀』的弥赛亚——这种读经法如何丰富我自己读圣经？",
                         "Reading Isaiah 53 with Daniel 7 yields a Messiah who first suffers, then is glorified. How might that way of reading enrich my own study of Scripture?"),
                        ("如果十字架揭示的是以色列自己最深的盼望,这如何改变我向犹太朋友述说福音的方式？",
                         "If the cross unveils Israel's own deepest hope, how does that change how I tell the Gospel to a Jewish friend?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "基督教——犹太教所走的一条路",
            "title_en": "Christianity — A Path That Judaism Took",
            "steps": [
                step(S1, S1E,
                    p("把前面几章汇拢，博亚林给出他全书的总论点：与其把基督教看作一个突然的、外来的「新发明」，不如把它理解为「犹太教所走的众多道路之一」。在第二圣殿时期,「犹太教」并非铁板一块,而是百花齐放：有法利赛人、撒都该人、爱色尼人、奋锐党、以诺式的群体……以及那些跟随耶稣的犹太人。相信「神性的、受苦的、驾云再来的弥赛亚」的犹太人，与后来发展出拉比传统的犹太人，本是同一棵大树上分出的、同样古老的枝子。博亚林说，这样看，「自有一种威严」——它把基督教归还给了它的犹太家族。",
                      "Gathering the previous chapters, Boyarin states his thesis: rather than seeing Christianity as a sudden, foreign “new invention,” understand it as “one of the paths that Judaism took.” In the Second Temple period, “Judaism” was not monolithic but wildly diverse: Pharisees, Sadducees, Essenes, Zealots, Enochic circles... and the Jews who followed Jesus. The Jews who believed in a “divine, suffering Messiah who would return on the clouds” and the Jews who later developed the rabbinic tradition were branches, equally ancient, off the same great tree. Boyarin says that seeing it this way “has a majesty of its own” — it returns Christianity to its Jewish family.")),
                step(S2, S2E,
                    bq("「若干枝子被折下来,你这野橄榄得接在其中……你不要向旧枝子夸口……不是你托着根,乃是根托着你。」",
                       "“If some of the branches have been broken off, and you, though a wild olive shoot, have been grafted in among the others... do not consider yourself superior... you do not support the root, but the root supports you.”",
                       "《罗马书》11:17-18 · Romans 11:17-18")),
                step(S3, S3E,
                    p("<strong>שֹׁרֶשׁ · shoresh</strong>——「根」。保罗在《罗马书》11 章用「橄榄树的根」来描述外邦信徒与以色列的关系——而博亚林的学术，恰恰从历史的层面印证了保罗的属灵图画：我们的信仰确实是<em>嫁接</em>在以色列那棵古树上的。那「根」不只是一段背景或前史，它是托着我们的生命之源。认识福音书有多犹太，就是认识我们的信仰离了那「根」便无法存活。每一次我们试图把基督教从它的犹太根上「切下来」，我们切断的，正是滋养我们自己的那条命脉。",
                      "<strong>שֹׁרֶשׁ · shoresh</strong> — “root.” In Romans 11 Paul uses “the root of the olive tree” to describe Gentile believers' relationship to Israel — and Boyarin's scholarship confirms, on the historical level, Paul's spiritual picture: our faith truly is <em>grafted</em> onto Israel's ancient tree. That “root” is not merely background or prehistory; it is the source of life that holds us up. To see how Jewish the Gospels are is to see that our faith cannot survive cut off from that “root.” Every time we try to sever Christianity from its Jewish root, what we cut is the very lifeline that nourishes us.")),
                step(S4, S4E,
                    p("这一课对今天的教会有深远的意义。两千年来,「基督教 vs 犹太教」的对立框架,孕育了无数的「轻蔑的教导」与逼迫。博亚林的工作,从学术上拆毁了这个框架的根基:它表明,最初根本没有一道把「犹太」与「基督」一刀两断的界线。这不是要抹平真实的信仰差异（耶稣是不是弥赛亚,仍是核心的分野）,而是要把这场对话重新安放在「家庭」的语境里——同一棵树、同一个根、同一本圣经。带着这样的认识,我们才能既忠于福音,又满怀「爱我民」(Ahavat Ammi) 之心,去爱那承载着我们之根的犹太民族。",
                      "This lesson carries deep meaning for the Church today. For two thousand years, the framework of “Christianity vs. Judaism” bred countless “teachings of contempt” and persecution. Boyarin's work dismantles the scholarly foundation of that framework: it shows there was, at first, no clean line cleaving “Jewish” from “Christian.” This is not to flatten real differences of faith (whether Jesus is the Messiah remains the central divide), but to reset the conversation in the context of <em>family</em> — one tree, one root, one Scripture. With that understanding, we can be both faithful to the Gospel and full of <em>Ahavat Ammi</em> — love for the Jewish people who carry our root.")),
                step(S5, S5E,
                    ul(
                        ("『最初没有一道把犹太与基督一刀两断的界线』——这如何改变我看待犹太教与基督教关系的方式？",
                         "“At first there was no clean line cleaving Jewish from Christian” — how does that change how I see the relationship between Judaism and Christianity?"),
                        ("『不是你托着根,乃是根托着你』。我对那承载着我之根的犹太民族,怀着怎样的态度？",
                         "“You do not support the root, but the root supports you.” What is my posture toward the Jewish people who carry my root?"),
                        ("把对话从『对立』重置为『家庭』,既不抹平差异,又满有爱——这在实践中对我意味着什么？",
                         "Resetting the conversation from “opposition” to “family,” without flattening difference yet full of love — what does that mean for me in practice?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "用犹太人的眼睛重读福音书",
            "title_en": "Rereading the Gospels with Jewish Eyes",
            "steps": [
                step(S1, S1E,
                    p("博亚林全书在方法上给了我们一份珍贵的礼物：他示范了如何<em>用第一世纪犹太人的眼睛</em>去读福音书。当我们摘下后世神学的眼镜,回到耶稣自己的处境,许多熟悉的经文就焕然一新:「人子」不再只是「谦卑的人」,而是驾云的神性君王;马可福音 7 章不再是「废除律法」,而是先知式地捍卫律法的心;十字架不再是反犹太的丑闻,而是以赛亚与但以理交汇的成全。福音书没有变,变的是我们的眼睛——从「外邦人后来的框架」,换回了「耶稣同代人的框架」。",
                      "Methodologically, Boyarin gives us a precious gift: he demonstrates how to read the Gospels <em>with the eyes of a first-century Jew</em>. When we take off the lenses of later theology and return to Jesus' own setting, many familiar texts come alive anew: “Son of Man” is no longer merely “the humble human” but the cloud-riding divine King; Mark 7 is no longer “abolishing the Law” but prophetically defending its heart; the cross is no longer an anti-Jewish scandal but the fulfillment where Isaiah and Daniel meet. The Gospels have not changed; our eyes have — from “the later Gentile framework” back to “the framework of Jesus' contemporaries.”")),
                step(S2, S2E,
                    bq("「于是从摩西和众先知起,凡经上所指着自己的话,都给他们讲解明白了。」",
                       "“And beginning with Moses and all the Prophets, he explained to them what was said in all the Scriptures concerning himself.”",
                       "《路加福音》24:27 · Luke 24:27")),
                step(S3, S3E,
                    p("<strong>פְּשָׁט · peshat</strong> 与 <strong>דְּרָשׁ · derash</strong>——犹太释经的两个层次:「字面/平实的意思」与「探究/引申的意思」。福音书既扎根于圣经的 <em>peshat</em>（耶稣真实地活在历史中、守妥拉、行神迹），也充满 <em>derash</em>（把摩西、众先知、诗篇里的线索,汇聚在弥赛亚身上）。复活后,耶稣在以马忤斯的路上所做的,正是一场最伟大的 <em>derash</em>:「从摩西和众先知起……讲解」自己。学会用这两只眼睛读经,我们读福音书,就从「读一本关于耶稣的书」,变成「与耶稣一同读整本希伯来圣经」。",
                      "<strong>פְּשָׁט · peshat</strong> and <strong>דְּרָשׁ · derash</strong> — the two levels of Jewish interpretation: “the plain/literal sense” and “the inquired/derived sense.” The Gospels are rooted both in the <em>peshat</em> of Scripture (Jesus really lived in history, kept Torah, worked wonders) and full of <em>derash</em> (gathering the threads of Moses, the Prophets, and the Psalms onto the Messiah). After the resurrection, what Jesus does on the road to Emmaus is the greatest <em>derash</em> of all: “beginning with Moses and all the Prophets,” he expounds himself. Learning to read with both eyes turns our reading of the Gospels from “reading a book about Jesus” into “reading the whole Hebrew Bible together with Jesus.”")),
                step(S4, S4E,
                    p("这一课邀请我们养成一个终身的习惯:每读一段福音书,就问「一个第一世纪的犹太听众,会怎么听这句话?」这个简单的问题,会不断把我们从浅薄的、去犹太化的读法里救出来。它会让我们看见耶稣每一个动作背后的节期、每一句话背后的经文、每一个比喻背后的拉比辩论。博亚林作为一位「局外的」犹太学者,反倒帮「局内的」基督徒,擦亮了一双我们本不该失去的眼睛。带着这双眼睛,圣经会重新成为一片活的、深不见底的海洋。",
                      "This lesson invites a lifelong habit: with every Gospel passage, ask “how would a first-century Jewish listener have heard this?” That simple question keeps rescuing us from shallow, de-Judaized readings. It lets us see the feast behind each of Jesus' actions, the Scripture behind each saying, the rabbinic debate behind each parable. Boyarin, an “outsider” Jewish scholar, helps “insider” Christians polish a pair of eyes we should never have lost. With those eyes, Scripture becomes again a living, fathomless sea.")),
                step(S5, S5E,
                    ul(
                        ("『一个第一世纪的犹太听众会怎么听这句话?』——我愿意养成在每段经文前都这样问的习惯吗？",
                         "“How would a first-century Jewish listener have heard this?” — am I willing to make a habit of asking this of every passage?"),
                        ("耶稣在以马忤斯『从摩西和众先知起』讲解自己。我读旧约时,有在其中寻见祂吗？",
                         "On the Emmaus road Jesus expounds himself “beginning with Moses and the Prophets.” Do I seek him in the Old Testament when I read it?"),
                        ("一位犹太学者帮基督徒擦亮了眼睛。我是否愿意谦卑地向犹太传统学习,以更深地认识我的主？",
                         "A Jewish scholar helped Christians polish their eyes. Am I willing to humbly learn from the Jewish tradition to know my Lord more deeply?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "犹太的基督——分别的真相与合一的盼望",
            "title_en": "The Jewish Christ — Honest Difference and the Hope of Unity",
            "steps": [
                step(S1, S1E,
                    p("在终章与结语里,博亚林并未假装犹太人与基督徒之间没有真实的分歧。他自己并不承认耶稣是弥赛亚;那道分界——「这一位拿撒勒人,到底是不是那位应许的弥赛亚?」——依然真实存在。但博亚林清除了那些<em>虚假</em>的分界:不是「神性 vs 人性」,不是「受苦 vs 得胜」,不是「律法 vs 恩典」,也不是「犹太 vs 基督」。当这些假墙被一一拆除,剩下的,是一个清晰而个人的问题——以及一个真实而温柔的相遇:两个本是一家的群体,终于可以彼此真正地聆听。",
                      "In the final chapter and epilogue, Boyarin does not pretend there is no real difference between Jews and Christians. He himself does not confess Jesus as Messiah; that dividing line — “is this Nazarene the promised Messiah or not?” — remains real. But Boyarin clears away the <em>false</em> divides: not “divinity vs. humanity,” not “suffering vs. triumph,” not “law vs. grace,” not “Jewish vs. Christian.” When these false walls are dismantled one by one, what remains is a clear and personal question — and a real, tender encounter: two communities that were one family, finally able to truly listen to each other.")),
                step(S2, S2E,
                    bq("「弟兄和睦同居,是何等地善,何等地美……因为在那里有耶和华所命定的福,就是永远的生命。」",
                       "“How good and pleasant it is when God's people live together in unity!... For there the LORD bestows his blessing, even life forevermore.”",
                       "《诗篇》133:1, 3 · Psalm 133:1, 3")),
                step(S3, S3E,
                    p("<strong>יֵשׁוּעַ · Yeshua</strong>——「耶和华是拯救」。走完整本书,我们看见这个名字所承载的一切,有多么彻底地是犹太的:那驾云的人子、那被拣选者、那受苦的仆人、那守妥拉的拉比、那大卫的子孙——全都在这一个犹太的名字里汇合。博亚林作为犹太人,把耶书亚还给了犹太的故事;而我们作为信徒,在这个被还原的、彻底犹太的耶书亚身上,反而更清楚地看见了我们所信、所爱、所敬拜的那一位。最犹太的耶稣,正是最真实的耶稣。",
                      "<strong>יֵשׁוּעַ · Yeshua</strong> — “The LORD is salvation.” Having finished the book, we see how thoroughly Jewish all that this name carries is: the cloud-riding Son of Man, the Chosen One, the suffering Servant, the Torah-keeping rabbi, the son of David — all converge in this one Jewish name. Boyarin, a Jew, returns Yeshua to the Jewish story; and we, as believers, see in this restored, thoroughly Jewish Yeshua more clearly the One we believe, love, and worship. The most Jewish Jesus is the most real Jesus.")),
                step(S4, S4E,
                    p("这是整份指南的终点,也是一个祷告。我们透过一位犹太学者的眼睛,重新发现了福音书的犹太心跳;每一个曾被当作「基督教对犹太教之背离」的核心信仰,反倒成了它们之间最深的连结。愿这八堂课塑造我们:成为既忠于「耶书亚是主」之信仰、又满怀「爱我民」之心的人;带着学术所赐的谦卑与清明,去爱犹太民族,为以色列认识她自己的弥赛亚而祷告;并满怀盼望地等候那一日——那一家人终于在同一位犹太的基督里,弟兄和睦同居,蒙耶和华命定永远的福。",
                      "This is the end of the whole guide, and a prayer. Through a Jewish scholar's eyes we have rediscovered the Jewish heartbeat of the Gospels; every core belief once taken as “Christianity's departure from Judaism” turns out to be the deepest bond between them. May these eight lessons shape us into people both faithful to the confession that “Yeshua is Lord” and full of <em>Ahavat Ammi</em>; loving the Jewish people with the humility and clarity scholarship grants, praying that Israel will know her own Messiah, and waiting in hope for the day when that one family, at last, lives together in unity in the one Jewish Christ, and the LORD bestows his blessing — life forevermore."),),
                step(S5, S5E,
                    ul(
                        ("哪些是基督徒与犹太人之间『虚假的分界』,哪些是『真实的分界』?分清这两者为何重要？",
                         "Which divides between Christians and Jews are “false,” and which is “real”? Why does telling them apart matter?"),
                        ("『最犹太的耶稣,正是最真实的耶稣』——这趟旅程,如何更新了我对我所敬拜之主的认识？",
                         "“The most Jewish Jesus is the most real Jesus” — how has this journey renewed my knowledge of the Lord I worship?"),
                        ("走完全书,我会以什么具体的方式,带着爱与盼望,与犹太朋友谈论这位犹太的弥赛亚？",
                         "Having finished the book, in what concrete way will I speak of this Jewish Messiah with Jewish friends, in love and hope?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "为那犹太的基督、为合一的盼望祝祷",
    "closing_title_en": "A Blessing for the Jewish Christ, and the Hope of Unity",
    "closing_zh": "「愿耶和华使祂的脸光照你,赐恩给你。」<br/><br/>愿你看过福音书的犹太心跳,<br/>就更深地爱那位驾云的人子、那位受苦的仆人、<br/>那位守妥拉的拉比、那位大卫的子孙——<br/>耶书亚 (Yeshua),那位「耶和华是拯救」的主。<br/><br/>愿那曾被撕裂的两半,在同一个根上重新被认出;<br/>愿你既忠于真理,又满有爱我民之心;<br/>并满怀盼望地等候那一日——<br/>那一家人在同一位犹太的基督里,弟兄和睦同居,<br/>蒙耶和华命定永远的福。",
    "closing_en": "“The LORD make his face shine upon you and be gracious to you.”<br/><br/>Having seen the Jewish heartbeat of the Gospels,<br/>may you love more deeply the cloud-riding Son of Man, the suffering Servant,<br/>the Torah-keeping rabbi, the son of David —<br/>Yeshua, the Lord whose name is “The LORD is salvation.”<br/><br/>May the two halves once torn apart be recognized again on one root;<br/>may you be both faithful to the truth and full of love for his people;<br/>and may you wait in hope for the day —<br/>when that one family lives together in unity in the one Jewish Christ,<br/>and the LORD bestows his blessing: life forevermore.",
}

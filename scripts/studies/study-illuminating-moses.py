# -*- coding: utf-8 -*-
"""Content module for study-illuminating-moses.html.

Jane Beal (ed.), *Illuminating Moses: A History of Reception from Exodus to
the Renaissance* (Brill, Leiden, 2014).
"""

RHYTHM_ZH = """        <strong>① 学者说什么</strong>—— 用书中学者的研究，呈现某一传统如何「接收」摩西；<br/>
        <strong>② 关键经文</strong>—— 这一接收所扎根的圣经；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，照亮摩西的形象；<br/>
        <strong>④ 基督徒视角</strong>—— 这位摩西如何指向弥赛亚；<br/>
        <strong>⑤ 诚实的提问</strong>—— 留给你与小组默想的问题。"""

RHYTHM_EN = """        <strong>① What the Scholars Say</strong> — how a tradition “received” Moses, in the book's research;<br/>
        <strong>② Key Scripture</strong> — the biblical ground of that reception;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that lights up the figure of Moses;<br/>
        <strong>④ A Christian Lens</strong> — how this Moses points to the Messiah;<br/>
        <strong>⑤ Honest Questions</strong> — questions for you and your group to contemplate."""


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
    "title_tag": "《照亮摩西》研习指南 · Illuminating Moses — Study Guide · 妥拉之光",
    "meta_desc": "A study guide to Jane Beal's Illuminating Moses — eight bilingual lessons tracing the figure of Moses across Jewish and Christian reception from Exodus to the Renaissance, and how the prophet, lawgiver, and mediator points to the Messiah.",
    "og_title": "Illuminating Moses — A Study Guide",
    "og_desc": "Eight bilingual lessons through Jane Beal's Illuminating Moses: the reception of Moses across Torah, Prophets, the New Testament, the Fathers, Maimonides, and the contemplative tradition — read with Hebrew eyes.",
    "cover_alt": "Illuminating Moses: A History of Reception from Exodus to the Renaissance — Study Guide",
    "tagline_zh": "研习指南 · 摩西的接受史 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · The Reception of Moses · 2026 · 5 · 31",
    "headline_zh": "照亮摩西<br/>研习指南",
    "headline_en": "Illuminating Moses<br/>A Study Guide",
    "deck_zh": "八堂课程，跟随简·比尔 (Jane Beal) 主编的这部学术文集，追踪「摩西」这一形象如何被一代代犹太人与基督徒不断「接收」、诠释、效法——从《出埃及记》，经众先知、新约、教父、迈蒙尼德，直到文艺复兴；并看见这位先知、立法者与中保，如何处处指向那位「像摩西的先知」——弥赛亚。",
    "deck_en": "Eight lessons following Jane Beal's scholarly volume, tracing how the figure of Moses was received, interpreted, and imitated by generations of Jews and Christians — from Exodus through the Prophets, the New Testament, the Fathers, Maimonides, and on to the Renaissance — and seeing how this prophet, lawgiver, and mediator points to the “prophet like Moses,” the Messiah.",
    "byline_zh": "基于简·比尔 (Jane Beal) 主编《照亮摩西——从《出埃及记》到文艺复兴的接受史》(Brill, Leiden, 2014)",
    "byline_en": "Based on Illuminating Moses: A History of Reception from Exodus to the Renaissance, edited by Jane Beal (Brill, Leiden, 2014)",
    "readtime_zh": "约 55 分钟通读",
    "readtime_en": "~55 min read-through",
    "book_url": "https://brill.com/display/title/20771",
    "book_link_zh": "购买原书 · Brill",
    "book_link_en": "Get the Book · Brill",
    "cta_url": "https://brill.com/display/title/20771",
    "cta_zh": "购买《照亮摩西》原书 · Brill",
    "cta_en": "Get the Book — Illuminating Moses · Brill",

    "lead_zh": "这份指南陪你读比尔 (Jane Beal) 主编的《照亮摩西》——一部由众多学者合写、追踪摩西「接受史」的文集。它的核心问题朴素却深刻：为什么摩西如此重要？为什么一千多年来，地域、族裔、信仰各异的群体，都不约而同地回到这一个人身上，从他身上汲取律法、解经与教育的典范？比尔指出，摩西的形象「激发了极不相同、甚至彼此冲突的回应」。这本书像一面多棱镜，让我们看见同一位摩西，如何在犹太与基督教的不同传统里，折射出不同却彼此呼应的光。",
    "lead_en": "This guide walks you through Jane Beal's <em>Illuminating Moses</em> — a multi-author volume tracing the “reception history” of Moses. Its central question is plain yet profound: why was Moses so important? Why, for over a thousand years, did groups differing widely in geography, ethnicity, and faith all return to this one man, drawing from him a model of law, interpretation, and education? Beal notes that the figure of Moses “inspired very different, even conflicting, responses.” The book is a prism, letting us see how one Moses refracts different yet echoing light across the Jewish and Christian traditions.",

    "intro": [
        p("对相信耶书亚的我们而言，这本书有一份特别的价值。耶稣自己说：「摩西……是指着我写的。」(约 5:46) 整本新约都浸透着摩西——逾越节的羔羊、旷野的铜蛇、西奈的约、那位「像摩西的先知」。要更深地认识弥赛亚，我们就不能绕过摩西。追踪摩西如何被一代代人「照亮」，我们其实是在追踪一束光，它最终聚焦在那位比摩西更大者身上。",
          "For those of us who believe in Yeshua, this book holds a special value. Jesus himself said, “Moses... wrote about me” (John 5:46). The whole New Testament is steeped in Moses — the Passover lamb, the bronze serpent in the wilderness, the covenant at Sinai, the “prophet like Moses.” To know the Messiah more deeply, we cannot bypass Moses. Tracing how Moses was “illuminated” by generation after generation, we are in fact tracing a beam of light that finally focuses on the One greater than Moses."),
        p("本指南共 <strong>八堂课</strong>，沿着摩西被「接收」的历程展开。每一堂遵循同样的五部分节奏：",
          "The guide is structured as <strong>eight lessons</strong>, following the journey of Moses' reception. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句提醒：这是一段跨越千年的旅程。你不必记住每一位学者、每一个时代。只要带着一个问题往前走就够了——「这位摩西，在向我指着谁？」",
          "A word of note: this is a journey across a thousand years. You need not remember every scholar or every era. It is enough to carry one question forward — “to whom is this Moses pointing me?”"),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "妥拉中的摩西——先知、立法者、中保",
            "title_en": "Moses in the Torah — Prophet, Lawgiver, Mediator",
            "steps": [
                step(S1, S1E,
                    p("书的第一篇（米勒 Robert Miller）追溯摩西在五经里的多重身份。后世一切对摩西的「接收」，都源于此处那个层次极其丰富的原型：他是被从尼罗河水中救起的婴孩，是在荆棘火中蒙召的牧人，是站在法老面前的解放者，是在西奈领受妥拉的中保，是为悖逆的百姓代求、甚至愿被「从神的册上涂抹」的牧者。学者们指出，正是这种「集多重角色于一身」的丰满，使摩西成为后世取之不尽的典范——立法者效法他、解经者引用他、神秘家默想他。",
                      "The book's first essay (Robert Miller) traces Moses' many roles across the Pentateuch. Every later “reception” of Moses springs from the richly layered original here: the infant drawn from the Nile, the shepherd called in the burning bush, the liberator standing before Pharaoh, the mediator who receives the Torah at Sinai, the shepherd who intercedes for a rebellious people — willing even to be “blotted out of God's book.” Scholars note that it is exactly this fullness — many roles in one person — that made Moses an inexhaustible model for later ages: lawgivers imitated him, interpreters cited him, mystics contemplated him.")),
                step(S2, S2E,
                    bq("「以后以色列中再没有兴起先知像摩西的;他是耶和华面对面所认识的。」",
                       "“Since then, no prophet has risen in Israel like Moses, whom the LORD knew face to face.”",
                       "《申命记》34:10 · Deuteronomy 34:10")),
                step(S3, S3E,
                    p("<strong>מֹשֶׁה · Moshe</strong>——「摩西」。法老的女儿给他起这名，说「因我把他从水里拉出来」（出 2:10，<em>mashah</em>「拉出」）。这名字本身就是一则预言：那从水中被「拉出」的孩子，长大后要把整个民族从红海的水中「拉出来」、得拯救。希伯来圣经常常用一个人名字的意思，预示他一生的使命。摩西——「被拉出来的人」「拉人出来的人」——他的名字,已经在低声诉说出埃及与救赎的故事。",
                      "<strong>מֹשֶׁה · Moshe</strong> — “Moses.” Pharaoh's daughter names him, saying “I drew him out of the water” (Exod 2:10, from <em>mashah</em>, “to draw out”). The name is itself a prophecy: the child “drawn out” of the water would grow up to “draw out” an entire nation through the waters of the Red Sea, to salvation. The Hebrew Bible often uses the meaning of a person's name to foreshadow their life's mission. Moses — “the drawn-out one,” “the one who draws out” — his very name already whispers the story of Exodus and redemption.")),
                step(S4, S4E,
                    p("摩西的三重身份——先知、立法者、中保——正是新约用来描绘耶书亚的三个核心镜头，只是每一样都被「成全」到更大。耶稣是那位比摩西更大的<em>先知</em>（祂不只传神的话,祂就是「道」）；是妥拉的<em>成全者</em>（「我来不是要废掉,乃是要成全」）；是那唯一的<em>中保</em>，「在神和人中间,只有一位中保,乃是降世为人的基督耶稣」(提前 2:5)。摩西愿意为百姓被「涂抹」，耶书亚则真的为我们被「涂抹」——担当了我们的罪。看懂了妥拉里的摩西，我们就握住了读懂耶书亚的第一把钥匙。",
                      "Moses' threefold identity — prophet, lawgiver, mediator — is precisely the three lenses the New Testament uses to portray Yeshua, each one “fulfilled” to something greater. Jesus is the <em>prophet</em> greater than Moses (he does not merely speak God's word; he <em>is</em> the Word); the <em>fulfiller</em> of Torah (“I have not come to abolish but to fulfill”); and the one <em>mediator</em>, “for there is one God and one mediator between God and mankind, the man Christ Jesus” (1 Tim 2:5). Moses was willing to be “blotted out” for the people; Yeshua truly was “blotted out” for us — bearing our sin. To grasp the Moses of the Torah is to hold the first key to reading Yeshua.")),
                step(S5, S5E,
                    ul(
                        ("摩西集先知、立法者、中保于一身。这三重角色,如何帮我更立体地认识耶书亚？",
                         "Moses unites prophet, lawgiver, and mediator. How do these three roles help me know Yeshua more fully?"),
                        ("摩西愿为百姓被『从神册上涂抹』。这种舍己的代求,如何预表了十字架？",
                         "Moses was willing to be “blotted out of God's book” for the people. How does that self-giving intercession foreshadow the cross?"),
                        ("一个名字('摩西'='被拉出来')就预示了一生的使命。这如何让我更细心地读圣经的细节？",
                         "A single name (“Moses” = “drawn out”) foreshadows a whole mission. How does that make me read Scripture's details more attentively?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "先知书与圣卷中的摩西——那不灭的标准",
            "title_en": "Moses in the Prophets and Writings — The Enduring Standard",
            "steps": [
                step(S1, S1E,
                    p("第二篇（霍尔姆 Tawny Holm）追踪摩西在希伯来圣经其余部分的「回声」。摩西虽在《申命记》末了去世，他的身影却贯穿整部圣经:先知们以「摩西的律法」为审判与盼望的标准;诗篇记念他在裂口中代求(诗 106:23);玛拉基书在旧约最后呼吁:「你们当记念我仆人摩西的律法」(玛 4:4)。学者指出,摩西成了以色列的「试金石」——衡量君王、先知、百姓的那把尺。整本希伯来圣经,几乎都活在摩西所立之约的张力里:守约则蒙福,背约则受咒。",
                      "The second essay (Tawny Holm) traces the “echoes” of Moses across the rest of the Hebrew Bible. Though Moses dies at the end of Deuteronomy, his presence runs through the whole Bible: the prophets take “the law of Moses” as the standard of both judgment and hope; the Psalms remember him interceding “in the breach” (Ps 106:23); Malachi closes the Old Testament with the call, “Remember the law of my servant Moses” (Mal 4:4). Scholars note that Moses became Israel's “touchstone” — the measure of kings, prophets, and people. Nearly the whole Hebrew Bible lives within the tension of the covenant Moses mediated: keep it and be blessed, break it and be cursed.")),
                step(S2, S2E,
                    bq("「你们当记念我仆人摩西的律法,就是我在何烈山为以色列众人所吩咐他的律例典章。」",
                       "“Remember the law of my servant Moses, the decrees and laws I gave him at Horeb for all Israel.”",
                       "《玛拉基书》4:4 · Malachi 4:4")),
                step(S3, S3E,
                    p("<strong>עֶבֶד · eved</strong>——「仆人」。圣经一次次称摩西为「<em>耶和华的仆人 (eved Adonai)</em>」——这是希伯来圣经里最高的尊荣之一。但「仆人」这条线并未停在摩西身上:它流向以赛亚书里那位「受苦的仆人」,最终汇聚在那位「取了奴仆的形像」、「存心顺服以至于死」的弥赛亚身上(腓 2:7-8)。摩西是「耶和华的仆人」,他预表着那位终极的「仆人」。在圣经里,真正的伟大,从来都穿着仆人的衣裳。",
                      "<strong>עֶבֶד · eved</strong> — “servant.” Scripture repeatedly calls Moses “the <em>servant of the LORD (eved Adonai)</em>” — one of the highest honors in the Hebrew Bible. But the thread of “servant” does not stop at Moses: it flows toward the “suffering servant” of Isaiah, and finally converges on the Messiah who “took the form of a servant” and “humbled himself, becoming obedient to death” (Phil 2:7-8). Moses is “the servant of the LORD,” foreshadowing the ultimate “Servant.” In Scripture, true greatness always wears the clothing of a servant.")),
                step(S4, S4E,
                    p("玛拉基书把旧约的最后一页,定格在两个名字上:「记念<em>摩西</em>的律法」,以及「我必差遣先知<em>以利亚</em>到你们那里去」(玛 4:4-5)。而新约的山顶——登山变像——恰恰让<em>摩西与以利亚</em>一同显现在耶稣身边,与祂谈论祂将要在耶路撒冷成就的「出去」(exodos,路 9:31)！整本旧约结束时翘首以待的律法与先知,在那座山上,围绕着耶书亚汇合。摩西指向的那位,终于亲自站在了画面的中央。",
                      "Malachi freezes the last page of the Old Testament on two names: “Remember the law of <em>Moses</em>,” and “I will send the prophet <em>Elijah</em> to you” (Mal 4:4-5). And the mountaintop of the New Testament — the Transfiguration — has exactly <em>Moses and Elijah</em> appear beside Jesus, speaking with him of the “exodus” (<em>exodos</em>, Luke 9:31) he was about to accomplish at Jerusalem! The Law and the Prophets, on tiptoe at the close of the Old Testament, converge around Yeshua on that mountain. The One Moses pointed to finally stands in the center of the frame himself.")),
                step(S5, S5E,
                    ul(
                        ("摩西是衡量以色列的『试金石』。在我的生命里,有没有这样一把来自神话语的、不灭的标准？",
                         "Moses was Israel's “touchstone.” Is there such an enduring standard from God's word in my life?"),
                        ("『仆人』这条线从摩西流向受苦的仆人弥赛亚。真正的伟大穿着仆人的衣裳——这如何挑战我对『伟大』的定义？",
                         "The “servant” thread runs from Moses to the suffering-servant Messiah. True greatness wears servant's clothing — how does that challenge my definition of greatness?"),
                        ("登山变像时,摩西与以利亚和耶稣谈论祂的『出去(exodos)』。这如何让我看见旧约与新约的合一？",
                         "At the Transfiguration, Moses and Elijah speak with Jesus of his “exodus.” How does that show me the unity of the Old and New Testaments?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "「像我的先知」——新约中的摩西",
            "title_en": "“A Prophet Like Me” — Moses in the New Testament",
            "steps": [
                step(S1, S1E,
                    p("第三篇（斯温 Larry Swain）展示摩西如何成为新约的「中心人物」之一。新约处处以摩西为底色:马太福音把耶稣描绘成「新摩西」——同样躲过暴君屠婴、同样从埃及被召出来、同样在山上颁布教导;约翰福音把耶稣比作旷野里被举起的铜蛇(约 3:14);希伯来书则郑重地把耶稣与摩西并列又超越——「他比摩西算是更配多得荣耀……摩西为仆人,基督为儿子」(来 3:3-6)。学者指出,新约作者并非要贬低摩西,恰恰相反,他们是借着这位最受尊崇的先知,来说明耶稣的身份。",
                      "The third essay (Larry Swain) shows how Moses became a “central figure” of the New Testament. The New Testament is everywhere shaded by Moses: Matthew paints Jesus as a “new Moses” — likewise escaping a tyrant's slaughter of infants, likewise called out of Egypt, likewise delivering teaching on a mountain; John likens Jesus to the bronze serpent lifted up in the wilderness (John 3:14); Hebrews solemnly sets Jesus alongside and above Moses — “Jesus has been found worthy of greater honor than Moses... Moses was faithful as a servant, but Christ as the Son” (Heb 3:3-6). Scholars note the New Testament writers do not belittle Moses; on the contrary, they use this most-revered prophet to explain who Jesus is.")),
                step(S2, S2E,
                    bq("「耶和华你的神要从你们弟兄中间,给你兴起一位先知像我,你们要听从他。」",
                       "“The LORD your God will raise up for you a prophet like me from among you, from your fellow Israelites. You must listen to him.”",
                       "《申命记》18:15 · Deuteronomy 18:15")),
                step(S3, S3E,
                    p("<strong>נָבִיא כָּמֹנִי · navi kamoni</strong>——「一位像我的先知」。这是摩西自己留下的、指向未来的应许(申 18:15)。它在以色列中点燃了一个绵延千年的盼望:有一位将要来的、「像摩西」的终极先知。到了耶稣的时代,这盼望已极其炽热——众人追问施洗约翰:「你是那位先知吗?」(约 1:21) 而使徒彼得在圣殿里宣讲时,直接引用这节经文,宣告耶书亚就是摩西所预言的「那位先知」(徒 3:22)。摩西亲手指向了一位要来的、比他更大者——而那位,就是耶书亚。",
                      "<strong>נָבִיא כָּמֹנִי · navi kamoni</strong> — “a prophet like me.” This is the forward-pointing promise Moses himself left (Deut 18:15). It kindled in Israel a hope spanning a thousand years: a coming, ultimate prophet “like Moses.” By Jesus' day the hope burned hot — people pressed John the Baptist, “Are you the Prophet?” (John 1:21). And when the apostle Peter preached in the Temple, he quoted this very verse, declaring Yeshua to be the “Prophet” Moses foretold (Acts 3:22). Moses himself pointed to a coming One greater than himself — and that One is Yeshua.")),
                step(S4, S4E,
                    p("这一课揭示了一个美妙的真理:旧约与新约之间,不是「废除与取代」的关系,而是「应许与成全」的关系。摩西不是被耶稣「取消」了,而是亲手把接力棒递了过去——「你们要听从<em>他</em>」。整本新约对摩西的「接收」,可以浓缩成一句话:那位摩西所盼望、所预言、所预表的「像我的先知」,已经来了。读懂这一点,我们就不会再把「摩西的律法」与「基督的恩典」当作敌人,而会看见它们本是同一个故事的开头与高潮。",
                      "This lesson reveals a beautiful truth: the relationship between Old and New Testaments is not “abolish and replace” but “promise and fulfillment.” Moses is not “cancelled” by Jesus but hands him the baton — “you must listen to <em>him</em>.” The whole New Testament's reception of Moses can be distilled to one sentence: the “prophet like me” whom Moses hoped for, foretold, and foreshadowed has come. Grasp this, and we will no longer treat “the law of Moses” and “the grace of Christ” as enemies, but see them as the opening and the climax of one and the same story.")),
                step(S5, S5E,
                    ul(
                        ("摩西亲手指向一位『像我的先知』,并说『你们要听从他』。我是否在听从那位摩西所预言的先知？",
                         "Moses pointed to “a prophet like me” and said “you must listen to him.” Am I listening to the Prophet Moses foretold?"),
                        ("旧约与新约是『应许与成全』,而非『废除与取代』。这如何改变我读两约的方式？",
                         "Old and New Testaments are “promise and fulfillment,” not “abolish and replace.” How does that change how I read both?"),
                        ("马太把耶稣描绘成『新摩西』。还有哪些旧约人物或事件,在新约里指向耶稣？",
                         "Matthew paints Jesus as a “new Moses.” What other Old Testament figures or events point to Jesus in the New?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "教父手中的摩西——预表与影儿",
            "title_en": "Moses in the Hands of the Fathers — Type and Shadow",
            "steps": [
                step(S1, S1E,
                    p("接下来的几篇（霍尔 Christopher Hall 论教父，库波-查基论逾越节礼仪）展示早期教会如何「接收」摩西:主要透过<em>预表论 (typology)</em>。教父们在摩西的一生里,处处看见基督的「影儿」:逾越节的羔羊预表基督的牺牲;过红海预表洗礼;旷野的吗哪预表生命的粮;磐石出水预表那「磐石就是基督」(林前 10:4);铜蛇被举起预表十字架。逾越节礼仪更把出埃及的整个叙事,编织进了复活节的庆典。对教父而言,摩西的故事不是「过去的旧约」,而是一幅处处闪烁着基督之光的活画。",
                      "The next essays (Christopher Hall on the Fathers, Cuppo-Csaki on the Paschal liturgy) show how the early Church “received” Moses: chiefly through <em>typology</em>. The Fathers saw the “shadow” of Christ everywhere in Moses' life: the Passover lamb foreshadows Christ's sacrifice; the crossing of the Red Sea foreshadows baptism; the manna in the wilderness foreshadows the bread of life; the water from the rock foreshadows the “rock that was Christ” (1 Cor 10:4); the bronze serpent lifted up foreshadows the cross. The Paschal liturgy wove the entire Exodus narrative into the celebration of Easter. For the Fathers, Moses' story was not “the bygone Old Testament” but a living picture shimmering everywhere with the light of Christ.")),
                step(S2, S2E,
                    bq("「这些事都是我们的鉴戒……他们都从一块磐石喝了灵水,所喝的是出于跟随他们的灵磐石;那磐石就是基督。」",
                       "“These things occurred as examples for us... they drank from the spiritual rock that accompanied them, and that rock was Christ.”",
                       "《哥林多前书》10:6, 4 · 1 Corinthians 10:6, 4")),
                step(S3, S3E,
                    p("<strong>צֵל · tzel</strong>——「影子」。希伯来书说,旧约的礼仪「是将来美事的<em>影儿 (skia / tzel)</em>,不是本物的真像」(来 10:1)。这个意象极其精准:影子是真实的,它确实由那物投下;但影子也指向那投影者本身。教父的预表论,本质上就是在「读影子」——他们透过摩西所投下的影子,辨认出那投下影子的实体:基督。这并不贬低旧约;恰恰相反,一个影子越是清晰、越是有形,越说明那投影的实体何等真实、何等荣美。",
                      "<strong>צֵל · tzel</strong> — “shadow.” Hebrews says the Old Testament rites are “a <em>shadow (skia / tzel)</em> of the good things to come, not the realities themselves” (Heb 10:1). The image is exact: a shadow is real — it is genuinely cast by the object; yet a shadow also points to the one casting it. The Fathers' typology is, at heart, “reading the shadow” — through the shadow Moses casts, discerning the substance that casts it: Christ. This does not diminish the Old Testament; on the contrary, the clearer and more defined a shadow, the more it shows how real and glorious the casting substance is.")),
                step(S4, S4E,
                    p("教父的预表论提醒今天的基督徒:整本旧约,都在向耶稣「下沉」。但这里也需要分辨与谦卑。健康的预表论,是顺着新约作者已经划出的线（保罗明说「磐石就是基督」）去看;而不是任凭想象,把每一个细节都强行寓意化。比尔的书把教父这一传统呈现出来,既让我们领受其中的丰盛——旧约处处有基督——也提醒我们,这种读法在历史上有时也滑向了对犹太人「字面之约」的轻看。带着「爱我民」的心读预表,我们既看见影子所指向的基督,也尊重那投下影子的、真实而美好的妥拉本身。",
                      "The Fathers' typology reminds Christians today that the whole Old Testament “leans toward” Jesus. But discernment and humility are needed here too. Healthy typology follows the lines the New Testament writers already drew (Paul plainly says “the rock was Christ”), rather than allegorizing every detail at will. Beal's book presents this patristic tradition so that we both receive its richness — Christ is everywhere in the Old Testament — and are reminded that this way of reading sometimes slid, historically, into contempt for the Jews' “literal” covenant. Reading typology with a heart of <em>Ahavat Ammi</em>, we see the Christ the shadow points to, while honoring the real and good Torah that casts it.")),
                step(S5, S5E,
                    ul(
                        ("逾越节羔羊、过红海、旷野吗哪——这些『影儿』如何加深我对基督的认识？",
                         "The Passover lamb, the Red Sea crossing, the wilderness manna — how do these “shadows” deepen my knowledge of Christ?"),
                        ("健康的预表论顺着新约的线,而非任凭想象。我如何在『丰盛』与『过度寓意』之间保持分辨？",
                         "Healthy typology follows the New Testament's lines, not free imagination. How do I keep discernment between “richness” and “over-allegorizing”?"),
                        ("一个清晰的影子,反而证明实体的真实。这如何让我更珍惜、而非轻看旧约？",
                         "A clear shadow proves the reality of the substance. How does that make me treasure, rather than belittle, the Old Testament?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "至高的先知——迈蒙尼德与中世纪犹太哲学中的摩西",
            "title_en": "The Supreme Prophet — Moses in Medieval Jewish Philosophy",
            "steps": [
                step(S1, S1E,
                    p("克莱塞尔 (Howard Kreisel) 那一篇,带我们进入中世纪犹太哲学如何「接收」摩西,尤其是迈蒙尼德 (Maimonides)。在迈蒙尼德的体系里,摩西被置于一个独一无二的高度:他是「先知中的先知」,是唯一「面对面」、「不用谜语」与神说话的人(民 12:8)。其他先知藉异象、异梦领受,摩西却以最清明、最直接的方式领受;因此唯有摩西所传的妥拉,具有永恒、不可更改的权威。对迈蒙尼德而言,摩西的预言是人类心智所能达到的、与神契合的最高峰。",
                      "Howard Kreisel's essay leads us into how medieval Jewish philosophy “received” Moses, especially Maimonides. In Maimonides' system, Moses is placed at a unique height: he is “the prophet of prophets,” the only one to speak with God “face to face,” “not in riddles” (Num 12:8). Other prophets received through vision and dream, but Moses received in the clearest, most direct way; therefore only the Torah Moses transmitted carries eternal, unalterable authority. For Maimonides, Moses' prophecy is the highest peak of communion with God the human mind can reach.")),
                step(S2, S2E,
                    bq("「我要与他面对面说话,乃是明说,不用谜语,并且他必见我的形像。」",
                       "“With him I speak face to face, clearly and not in riddles; he sees the form of the LORD.”",
                       "《民数记》12:8 · Numbers 12:8")),
                step(S3, S3E,
                    p("<strong>פָּנִים אֶל פָּנִים · panim el panim</strong>——「面对面」。这是希伯来圣经形容摩西与神之亲密的核心短语,也是迈蒙尼德推崇摩西的根据。然而,这里藏着一个动人的张力:《出埃及记》33 章里,摩西恳求「求你显出你的荣耀给我看」,神却说「你不能看见我的面,因为人见我的面不能存活」——摩西所能见的,只是神「背后」的荣耀。「面对面」是真实的亲密,却仍隔着一层。这层「未得见的面」,正是整本圣经悬而未决的渴望:几时,人能真正看见神的面？",
                      "<strong>פָּנִים אֶל פָּנִים · panim el panim</strong> — “face to face.” This is the core phrase for Moses' intimacy with God, and the ground of Maimonides' exaltation of him. Yet here lies a moving tension: in Exodus 33, Moses pleads “show me your glory,” but God says “you cannot see my face, for no one may see me and live” — what Moses could see was only the glory of God's “back.” “Face to face” is real intimacy, yet still through a veil. That “unseen face” is the unresolved longing of the whole Bible: when will a person truly see the face of God?")),
                step(S4, S4E,
                    p("迈蒙尼德把摩西高举为「不可超越的至高先知」——这恰恰让新约的宣告显得格外大胆。希伯来书开篇说:「神既在古时藉着众先知多次多方地晓谕列祖,就在这末世,藉着<em>他儿子</em>晓谕我们。」(来 1:1-2) 摩西是「面对面」却仍隔着帕子的先知;而约翰福音宣告:「从来没有人看见神,只有在父怀里的独生子将他表明出来。」(约 1:18) 摩西渴望却未能得见的「神的面」,在耶书亚里向我们显明了——「人看见了我,就是看见了父」(约 14:9)。那位至高的先知所翘首以待的,正是道成肉身的弥赛亚。",
                      "Maimonides exalts Moses as “the unsurpassable supreme prophet” — which makes the New Testament's claim all the bolder. Hebrews opens: “In the past God spoke to our ancestors through the prophets at many times and in various ways, but in these last days he has spoken to us by <em>his Son</em>” (Heb 1:1-2). Moses was the “face to face” prophet, yet still behind a veil; and John's Gospel declares, “No one has ever seen God, but the one and only Son... has made him known” (John 1:18). The “face of God” Moses longed for but could not see is shown to us in Yeshua — “whoever has seen me has seen the Father” (John 14:9). The One the supreme prophet awaited is the incarnate Messiah.")),
                step(S5, S5E,
                    ul(
                        ("摩西『面对面』却仍只见神的『背后』。这层『未得见的面』,如何成为指向道成肉身的渴望？",
                         "Moses was “face to face” yet saw only God's “back.” How does that “unseen face” become a longing pointing to the Incarnation?"),
                        ("迈蒙尼德把摩西高举为至高先知。希伯来书却说神『藉着他儿子』说话。这两者如何并存又有别？",
                         "Maimonides exalts Moses as supreme prophet; Hebrews says God speaks “through his Son.” How do these coexist yet differ?"),
                        ("『人看见了我,就是看见了父』。我是否真的透过耶书亚,认识那位摩西渴望得见的神的面？",
                         "“Whoever has seen me has seen the Father.” Do I truly come to know, through Yeshua, the face of God that Moses longed to see?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "摩西之死——一个被反复默想的奥秘",
            "title_en": "The Death of Moses — A Mystery Long Contemplated",
            "steps": [
                step(S1, S1E,
                    p("米克瓦 (Rachel Mikva) 与舍恩费尔德 (Devorah Schoenfeld) 的两篇,探讨拉比与中世纪传统如何「接收」摩西之死这一沉重的奥秘。摩西领百姓走了四十年,却因在米利巴水边的过犯,不得进入应许之地,只能从尼波山远远眺望,然后死在摩押地,「葬在……谷中,只是到今日没有人知道他的坟墓」(申 34:6)。这个结局让历世历代的犹太释经者既困惑又着迷:神为何不让祂最忠心的仆人进入安息?拉比们写下大量动人的米大示,想象摩西如何与死亡「讨价还价」、如何不舍、如何最终在神的亲吻中安息。",
                      "The essays by Rachel Mikva and Devorah Schoenfeld explore how rabbinic and medieval traditions “received” the heavy mystery of Moses' death. Moses led the people for forty years, yet because of his transgression at the waters of Meribah, he was not allowed to enter the Promised Land — only to gaze from afar atop Mount Nebo, then die in Moab, “buried... in the valley, but to this day no one knows where his grave is” (Deut 34:6). This ending both troubled and fascinated Jewish interpreters across the centuries: why would God not let his most faithful servant enter the rest? The rabbis wrote vast and moving midrashim, imagining how Moses “bargained” with death, how he grieved, how at last he was taken in the kiss of God.")),
                step(S2, S2E,
                    bq("「摩西……死在摩押地,正如耶和华所说的。耶和华将他埋葬在……谷中,只是到今日没有人知道他的坟墓。」",
                       "“And Moses... died there in Moab, as the LORD had said. He buried him in Moab, in the valley... but to this day no one knows where his grave is.”",
                       "《申命记》34:5-6 · Deuteronomy 34:5-6")),
                step(S3, S3E,
                    p("<strong>מְנוּחָה · menuchah</strong>——「安息」。摩西一生都在寻求那「安息之地」,却未能亲身进入。希伯来书拾起了这个主题:摩西所给的「安息」(进入迦南)只是预表,真正的、终极的「安息」尚在前头——「这样看来,必另有一安息日的安息,为神的子民存留」(来 4:9)。摩西的故事因此变成一个深刻的盼望:连最伟大的先知,也需要一位<em>带来真安息</em>的人。约书亚(Yehoshua,与「耶书亚」同名)领百姓进了那地的影子;而真正的约书亚——耶书亚——要领神所有的子民,进入那永远的安息。",
                      "<strong>מְנוּחָה · menuchah</strong> — “rest.” All his life Moses sought that “place of rest,” yet could not enter it himself. Hebrews takes up the theme: the “rest” Moses gave (entering Canaan) was only a foreshadowing; the true, ultimate “rest” still lies ahead — “there remains, then, a Sabbath-rest for the people of God” (Heb 4:9). Moses' story thus becomes a profound hope: even the greatest prophet needed One who would <em>bring the true rest</em>. Joshua (<em>Yehoshua</em>, the same name as “Yeshua”) led the people into the shadow of that land; and the true Joshua — Yeshua — would lead all God's people into the eternal rest.")),
                step(S4, S4E,
                    p("摩西在尼波山的眺望,是整本圣经最令人心碎也最有盼望的画面之一。心碎,是因为他望得见、却进不去;有盼望,是因为这恰恰说明:旧约本身,无法把人领进那最终的应许。律法是美善的引路人,却不能成为终点。它把我们带到约旦河边,然后郑重地把接力棒,交给那位与摩西同站在变像山上、要成就更大「出去」的耶书亚。摩西未葬之地无人知晓,但那位为我们死、又复活的弥赛亚,祂空的坟墓,全世界都知道。",
                      "Moses' gaze from Mount Nebo is among the most heartbreaking yet hope-filled images in all of Scripture. Heartbreaking, because he could see but not enter; hope-filled, because it shows precisely this: the Old Testament itself cannot bring people into the final promise. The Law is a good guide, but it cannot be the destination. It brings us to the bank of the Jordan, then solemnly hands the baton to the Yeshua who stood with Moses on the mount of Transfiguration and would accomplish the greater “exodus.” No one knows the place of Moses' grave; but the empty tomb of the Messiah who died and rose for us — the whole world knows.")),
                step(S5, S5E,
                    ul(
                        ("摩西望得见应许之地,却进不去。这如何说明律法是『引路人』而非『终点』？",
                         "Moses could see the Promised Land but not enter it. How does that show the Law is a “guide,” not the “destination”?"),
                        ("约书亚(Yehoshua)与耶书亚同名,都『领人进入安息』。这个名字的呼应,对我意味着什么？",
                         "Joshua (Yehoshua) shares the name Yeshua, and both “lead into rest.” What does that echo of names mean to me?"),
                        ("摩西的坟墓无人知晓,弥赛亚的空坟全世界都知道。这个对比,给了我怎样的盼望？",
                         "No one knows Moses' grave; the whole world knows the Messiah's empty tomb. What hope does that contrast give me?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "发光的脸与帕子——西奈与默观的攀登",
            "title_en": "The Shining Face and the Veil — Sinai and the Contemplative Ascent",
            "steps": [
                step(S1, S1E,
                    p("比尔自己那一篇（论基督教默观传统）展示:摩西攀登西奈、进入云中与神相会、脸面因此发光——成为后世神秘家与默观者眼中,「与神联合」的至高典范。从尼撒的贵格利,到中世纪的神秘家,再到亚维拉的德兰,他们一次次回到摩西的「黑暗中的攀登」(进入西奈山顶那遮蔽的密云),把它读作灵魂向神攀升、最终在「神圣的黑暗」中与神相遇、相爱的图像。摩西在这里不再只是立法者,而是「默观的先驱」——那位敢于进入神临在之云的人。",
                      "Beal's own essay (on the Christian contemplative tradition) shows how Moses' ascent of Sinai — entering the cloud to meet God, his face shining as a result — became, for later mystics and contemplatives, the supreme model of “union with God.” From Gregory of Nyssa, through the medieval mystics, to Teresa of Avila, they returned again and again to Moses' “ascent into the darkness” (entering the thick cloud at Sinai's summit), reading it as an image of the soul climbing toward God and meeting — and loving — him at last in the “divine darkness.” Here Moses is no longer merely the lawgiver but the “pioneer of contemplation” — the one who dared enter the cloud of God's presence.")),
                step(S2, S2E,
                    bq("「摩西手里拿着两块法版下西奈山的时候,不知道自己的面皮因耶和华和他说话就发了光。」",
                       "“When Moses came down from Mount Sinai with the two tablets... he was not aware that his face was radiant because he had spoken with the LORD.”",
                       "《出埃及记》34:29 · Exodus 34:29")),
                step(S3, S3E,
                    p("<strong>קָרַן · qaran</strong>——「发光 / 放射光芒」。摩西的脸「发光」,以致他不得不蒙上帕子(出 34:33)。保罗在《哥林多后书》3 章,正是以这个「帕子」为核心,作了一篇精彩的解读:摩西脸上那渐渐褪去的荣光,需要帕子遮盖;但在基督里,帕子被除去了——「我们众人既然敞着脸得以看见主的荣光,好像从镜子里返照,就变成主的形状,荣上加荣」(林后 3:18)。摩西的荣光是借来的、会褪的、要遮盖的;基督里的荣光是内住的、长存的、且要把我们也改变成祂的样式。",
                      "<strong>קָרַן · qaran</strong> — “to shine / send out rays.” Moses' face “shone,” so that he had to cover it with a veil (Exod 34:33). In 2 Corinthians 3, Paul makes a brilliant interpretation centered on that very “veil”: the fading glory on Moses' face needed a veil to cover it; but in the Messiah, the veil is removed — “we all, with unveiled faces, contemplating the Lord's glory, are being transformed into his image with ever-increasing glory” (2 Cor 3:18). Moses' glory was borrowed, fading, and to be covered; the glory in the Messiah is indwelling, lasting, and transforms us, too, into his likeness.")),
                step(S4, S4E,
                    p("这一课把我们从「读关于神的知识」,带向「被神的荣光改变」。默观传统提醒我们:认识神,终极而言不是头脑的攀登,而是脸面的转变——是「敞着脸」,让那位曾向摩西显现、又在耶书亚里完全彰显的荣光,一点一点地把我们「变成主的形状」。摩西从山上下来,脸上带着神的光;而藉着内住的圣灵,每一个仰望基督的人,也都在领受这同一道光,直到那荣光不再需要任何帕子,因为我们要「面对面」地见祂(林前 13:12)——成全摩西一生最深的渴望。",
                      "This lesson carries us from “reading knowledge about God” to “being changed by God's glory.” The contemplative tradition reminds us that, ultimately, knowing God is not an ascent of the mind but a transformation of the face — “with unveiled faces,” letting the glory that appeared to Moses and is fully revealed in Yeshua change us, little by little, “into his image.” Moses came down the mountain with God's light on his face; and through the indwelling Spirit, everyone who gazes on Christ receives that same light, until the glory needs no veil at all, for we will see him “face to face” (1 Cor 13:12) — fulfilling Moses' deepest lifelong longing.")),
                step(S5, S5E,
                    ul(
                        ("摩西的荣光会褪、需遮盖;基督里的荣光长存、要改变我。我的脸,正被什么光所照亮？",
                         "Moses' glory faded and was veiled; the glory in Christ lasts and changes me. By what light is my face being illumined?"),
                        ("认识神是『脸面的转变』,而非只是『头脑的攀登』。我的属灵生活,更偏重哪一边？",
                         "Knowing God is a “transformation of the face,” not merely an “ascent of the mind.” Which does my spiritual life lean toward?"),
                        ("『敞着脸得以看见主的荣光』——我愿意除去哪些『帕子』,好让基督的荣光改变我？",
                         "“With unveiled faces contemplating the Lord's glory” — what “veils” am I willing to remove so Christ's glory can change me?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "比摩西更大者——一束光的归宿",
            "title_en": "One Greater Than Moses — Where the Light Comes Home",
            "steps": [
                step(S1, S1E,
                    p("从中世纪的经院神学（阿奎那把摩西尊为「犹太人的首席教师」）,到中古英语的神秘剧,再到文艺复兴诗人、政治家、艺术家以摩西为「典范或刻板印象」的种种运用——比尔的书,在终章把这条千年长河汇拢。摩西的形象,如此丰富、如此有弹性,以致每一个时代、每一个群体,都能在他身上照见自己的需要与盼望。但贯穿这一切「接收」的,始终有一条隐秘的主线:几乎每一个认真对待摩西的人,最终都被他引向一个「超越他」的盼望——盼望一位更大的先知、更真的中保、更终极的安息、更不褪的荣光。",
                      "From medieval scholasticism (Aquinas honoring Moses as “the chief teacher of the Jews”), through the Middle English mystery plays, to the Renaissance poets, politicians, and artists who used Moses as “type or stereotype” — Beal's book, in its final chapters, gathers this thousand-year river. The figure of Moses is so rich and so elastic that every age and group could see its own needs and hopes reflected in him. Yet through all this “reception” runs one hidden main line: nearly everyone who took Moses seriously was finally led by him to a hope that “surpassed him” — the hope of a greater prophet, a truer mediator, a more ultimate rest, a more unfading glory.")),
                step(S2, S2E,
                    bq("「律法本是藉着摩西传的;恩典和真理都是由耶稣基督来的。」",
                       "“For the law was given through Moses; grace and truth came through Jesus Christ.”",
                       "《约翰福音》1:17 · John 1:17")),
                step(S3, S3E,
                    p("<strong>גֹּאֵל · go'el</strong>——「救赎主、至近的亲属」。摩西是以色列伟大的<em>解放者</em>,把百姓从为奴之地领出来;但希伯来圣经盼望的,是一位更终极的 <em>go'el</em>——一位以血缘之亲的身份,付上代价,把人从死亡与罪的捆绑中赎回的救赎主。整本《照亮摩西》所追踪的那束光,最终聚焦于此:摩西所是、所行、所预表的一切——先知、立法者、中保、解放者——都在那位「比摩西更大者」身上得了成全。律法藉摩西<em>传</em>来,恩典和真理藉耶书亚<em>来到</em>。摩西是那根指向太阳的手指;耶书亚是太阳本身。",
                      "<strong>גֹּאֵל · go'el</strong> — “redeemer, near kinsman.” Moses is Israel's great <em>liberator</em>, leading the people out of the land of slavery; but what the Hebrew Bible hopes for is a more ultimate <em>go'el</em> — a Redeemer who, as a blood-kinsman, pays the price to ransom people from the bondage of death and sin. The beam of light traced through all of <em>Illuminating Moses</em> finally focuses here: all that Moses was, did, and foreshadowed — prophet, lawgiver, mediator, liberator — is fulfilled in the One “greater than Moses.” The law was <em>given</em> through Moses; grace and truth <em>came</em> through Yeshua. Moses is the finger pointing to the sun; Yeshua is the sun itself.")),
                step(S4, S4E,
                    p("这是整份指南的终点,也是一束光的归宿。我们跟随摩西的形象,走过了妥拉、先知、新约、教父、迈蒙尼德、默观传统与文艺复兴——而在每一站,他都在向前方指。愿这八堂课塑造我们:既深深敬重那位「耶和华面对面所认识」的伟大先知摩西,又清楚地看见,他一生的全部荣光,都是为了把我们引向那位比他更大的弥赛亚耶书亚;并带着「爱我民」之心,与那承载着摩西、承载着妥拉的犹太民族同行,一起翘首等候那一日——当摩西所渴望得见的神的面,向万民完全显明,众人都要面对面地认识祂。",
                      "This is the end of the whole guide, and where a beam of light comes home. Following the figure of Moses, we have journeyed through Torah, Prophets, the New Testament, the Fathers, Maimonides, the contemplative tradition, and the Renaissance — and at every station he points ahead. May these eight lessons shape us to deeply honor the great prophet Moses, “whom the LORD knew face to face,” and to see clearly that all his lifelong glory was to lead us to the Messiah greater than himself, Yeshua; and, with a heart of <em>Ahavat Ammi</em>, to walk alongside the Jewish people who carry Moses and the Torah, awaiting together the day when the face of God that Moses longed to see is fully revealed to all peoples, and all will know him face to face."),),
                step(S5, S5E,
                    ul(
                        ("『律法藉摩西传,恩典真理藉耶稣来』——这节经文如何总括了整本书的旅程？",
                         "“The law was given through Moses; grace and truth came through Jesus” — how does this verse sum up the whole book's journey?"),
                        ("几乎每个认真对待摩西的人,都被他引向一个『超越他』的盼望。摩西把我引向了谁？",
                         "Nearly everyone who took Moses seriously was led to a hope “beyond him.” To whom does Moses lead me?"),
                        ("『摩西是指向太阳的手指,耶书亚是太阳本身』。我是否有时停在了手指上,而忘了仰望太阳？",
                         "“Moses is the finger pointing to the sun; Yeshua is the sun.” Do I sometimes stop at the finger and forget to look up at the sun?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "为那比摩西更大者祝祷",
    "closing_title_en": "A Blessing for the One Greater Than Moses",
    "closing_zh": "「愿耶和华向你仰脸,赐你平安。」<br/><br/>愿你跟随过摩西被照亮的千年长河,<br/>就更清楚地看见那束光的归宿——<br/>那位比摩西更大的先知、更真的中保、<br/>那位带来真安息、不褪荣光的弥赛亚:<br/>耶书亚 (Yeshua)。<br/><br/>律法藉摩西传来,<br/>恩典和真理藉耶书亚来到;<br/>愿你既敬重那指路的手指,<br/>又敞着脸,被那太阳的荣光,<br/>一点一点改变成主的形状。",
    "closing_en": "“The LORD lift up his countenance upon you, and give you peace.”<br/><br/>Having followed the thousand-year river in which Moses was illumined,<br/>may you see more clearly where the light comes home —<br/>the prophet greater than Moses, the truer mediator,<br/>the Messiah who brings the true rest and the unfading glory:<br/>Yeshua.<br/><br/>The law was given through Moses,<br/>grace and truth came through Yeshua;<br/>may you honor the finger that points the way,<br/>and, with unveiled face, be changed into his image,<br/>by the glory of that Sun, from glory to glory.",
}

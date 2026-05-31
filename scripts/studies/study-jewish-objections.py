# -*- coding: utf-8 -*-
"""Content module for study-jewish-objections.html.

Michael L. Brown, *Answering Jewish Objections to Jesus, Volume 5: Traditional
Jewish Objections* (Purple Pomegranate Productions, 2015 ed.; orig. Baker, 2010).
"""

RHYTHM_ZH = """        <strong>① 反对的声音</strong>—— 用传统犹太教自己的语气陈述这一异议；<br/>
        <strong>② 布朗的回应</strong>—— 布朗以圣经与历史作出的答复；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，照亮争论的核心；<br/>
        <strong>④ 弥赛亚的视角</strong>—— 这一议题如何指向耶书亚 (Yeshua)；<br/>
        <strong>⑤ 诚实的提问</strong>—— 留给你与小组带着爱继续追问的问题。"""

RHYTHM_EN = """        <strong>① The Objection</strong> — the challenge, stated in traditional Judaism's own voice;<br/>
        <strong>② Brown's Response</strong> — his answer from Scripture and history;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that lights up the heart of the debate;<br/>
        <strong>④ A Messianic Lens</strong> — how the question points to Yeshua;<br/>
        <strong>⑤ Honest Questions</strong> — questions to keep asking, in love, alone or in a group."""


def step(label_zh, label_en, *body):
    return {"label_zh": label_zh, "label_en": label_en, "body": list(body)}

def p(zh, en):
    return {"type": "p", "zh": zh, "en": en}

def bq(zh, en, cite=None):
    return {"type": "blockquote", "zh": zh, "en": en, "cite": cite}

def ul(*items):
    return {"type": "ul", "items": [{"zh": z, "en": e} for z, e in items]}

S1, S1E = "① 反对的声音", "① The Objection"
S2, S2E = "② 布朗的回应", "② Brown's Response"
S3, S3E = "③ 希伯来语之眼", "③ Through Hebrew Eyes"
S4, S4E = "④ 弥赛亚的视角", "④ A Messianic Lens"
S5, S5E = "⑤ 诚实的提问", "⑤ Honest Questions"


study = {
    "title_tag": "《回答犹太人对耶稣的异议》研习指南 · Answering Jewish Objections to Jesus — Study Guide · 妥拉之光",
    "meta_desc": "A study guide to Michael Brown's Answering Jewish Objections to Jesus, Vol. 5 (Traditional Jewish Objections) — eight bilingual lessons on the Oral Torah, rabbinic authority, the sufficiency of tradition, and how every objection points back to Yeshua.",
    "og_title": "Answering Jewish Objections to Jesus — A Study Guide",
    "og_desc": "Eight bilingual lessons through Michael Brown's Vol. 5 (Traditional Jewish Objections): the Oral Torah, rabbinic authority, and the case for Yeshua — read with love and Hebrew eyes.",
    "cover_alt": "Answering Jewish Objections to Jesus, Vol. 5 — Study Guide",
    "tagline_zh": "研习指南 · 弥赛亚护教 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · Messianic Apologetics · 2026 · 5 · 31",
    "headline_zh": "回答犹太人对<br/>耶稣的异议",
    "headline_en": "Answering Jewish<br/>Objections to Jesus",
    "deck_zh": "八堂课程，跟随弥赛亚犹太学者迈克尔·布朗 (Michael Brown) 第五卷《传统的异议》，温柔而坚定地面对最常见的反对之声——口传妥拉、拉比的权柄、传统的自足——并看见每一个异议，最终都把我们引回那位犹太弥赛亚耶书亚 (Yeshua)。",
    "deck_en": "Eight lessons following Messianic Jewish scholar Michael Brown's Volume 5, Traditional Jewish Objections — meeting the most common challenges gently but firmly (the Oral Torah, rabbinic authority, the self-sufficiency of tradition) and seeing how every objection finally leads back to the Jewish Messiah, Yeshua.",
    "byline_zh": "基于迈克尔·布朗 (Michael L. Brown)《回答犹太人对耶稣的异议·第五卷：传统的异议》(Purple Pomegranate Productions, 2015)",
    "byline_en": "Based on Answering Jewish Objections to Jesus, Volume 5: Traditional Jewish Objections by Michael L. Brown (Purple Pomegranate Productions, 2015)",
    "readtime_zh": "约 55 分钟通读",
    "readtime_en": "~55 min read-through",
    "book_url": "https://askdrbrown.org/store",
    "book_link_zh": "购买原书",
    "book_link_en": "Get the Book",
    "cta_url": "https://askdrbrown.org/store",
    "cta_zh": "购买《回答犹太人对耶稣的异议》第五卷",
    "cta_en": "Get the Book — Answering Jewish Objections to Jesus, Vol. 5",

    "lead_zh": "这份指南陪你读迈克尔·布朗 (Michael L. Brown) 五卷本巨著《回答犹太人对耶稣的异议》的最后一卷——专门回应「传统的异议」，也就是建立在拉比犹太教与口传妥拉之上的反对。布朗本身是一位犹太信徒，拥有近东语言与文学博士学位，几十年来与拉比、反传教士公开辩论。他在书的开篇就郑重声明：「我对传统犹太教怀有极深的敬意……以下的批评，不是出自反犹者，而是出自一个敬畏神、深爱自己同胞的犹太人——爱到愿意说出那即使刺痛人的真理。」这不是一本攻击犹太教的书，而是一封写给以色列、满载敬意与盼望的恳谈。",
    "lead_en": "This guide walks you through the final volume of Michael L. Brown's five-volume work <em>Answering Jewish Objections to Jesus</em> — the one answering “traditional objections,” those built on rabbinic Judaism and the Oral Torah. Brown is himself a Jewish believer with a doctorate in Near Eastern languages and literatures, who has debated rabbis and anti-missionaries publicly for decades. He states at the outset: “I have great respect for traditional Judaism... the criticisms that follow are not those of an anti-Semite, but of a God-fearing Jew who loves his people deeply — deeply enough to present the truth even when it hurts.” This is not a book that attacks Judaism, but a letter of deep respect and hope, written to Israel.",

    "intro": [
        p("布朗甚至坦言，他相信「犹太教是人类创造过的最伟大的宗教」——它忠于独一的真神，以遵行妥拉为生命的根基，孕育了崇高的伦理、坚强的家庭与世代的传承。正因如此，他的异议才更值得认真聆听：它们不是出于轻看，而是出于「还有一条更美的路——在弥赛亚里、在新约里、在圣灵里的生命之路」这一深信。",
          "Brown even admits he believes “Judaism is the greatest religion man has ever made” — loyal to the one true God, making Torah-observance the foundation of life, cultivating lofty ethics, strong families, and continuity across generations. That is exactly why his objections deserve a careful hearing: they spring not from contempt but from a conviction that “there is an even better way — the way of life in the Messiah, of the new covenant, of the Spirit.”"),
        p("本指南共 <strong>八堂课</strong>，把书中十八条「传统异议」归纳为八组核心议题。每一堂遵循同样的五部分节奏：",
          "The guide is structured as <strong>eight lessons</strong>, grouping the book's eighteen “traditional objections” into eight core themes. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句提醒：这是一片需要温柔的土地。读这本书不是为了「赢得辩论」，而是为了「在爱中说诚实话」。愿这份指南装备你，既忠于真理，又满有对犹太民族的爱 (Ahavat Ammi)。",
          "A word of caution: this is tender ground. We read this book not to “win an argument” but to “speak the truth in love.” May this guide equip you to be faithful to the truth and full of love for the Jewish people — <em>Ahavat Ammi</em>."),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "「那条从摩西而来、未曾断绝的链子」——口传妥拉",
            "title_en": "“The Unbroken Chain Back to Moses” — The Oral Torah",
            "steps": [
                step(S1, S1E,
                    p("（异议 6.1–6.2）「我们拥有一条权威的、从摩西在西奈山起就未曾断绝的口传链条。神在赐下成文妥拉的同时，也口头赐下了口传妥拉。你算什么，竟来教我们解释自己的圣经？况且，妥拉本身就多次提到复数的『众妥拉』(Torot)——这显然指的就是成文的与口传的两部妥拉。」这是传统犹太教最根本的根基：拉比传统拥有与圣经同等、甚至更高的解释权威。",
                      "(Objections 6.1–6.2) “We have an authoritative, unbroken chain of oral tradition going back to Moses at Mount Sinai. When God gave the Written Torah, he also gave the Oral Torah orally. Who are you to teach us how to read our own Bible? Besides, the Torah itself refers several times to ‘Torahs’ in the plural (Torot) — obviously meaning the two Torahs, Written and Oral.” This is the deepest foundation of traditional Judaism: rabbinic tradition holds interpretive authority equal to, or higher than, Scripture itself.")),
                step(S2, S2E,
                    p("布朗的回应直截了当：「并不存在一条从摩西而来、未曾断绝的权威口传链条。那只是一个虔诚的神话，没有圣经的支持。」他承认以色列历史上确实有各种习俗与传统——有好、有坏、有中性的；这一点无人否认。但「口传妥拉早在西奈就以权威形式与成文妥拉一同被赐下」这一具体主张，却缺乏证据。他引用犹太学者埃弗里-佩克的话：拉比文献本身「并不体现」一个一路追溯到西奈的统一传统；它们「是其作者的产物」，是后世为了建立一套从他们的时代延续至今的信仰与实践体系而创作的。布朗的结论：唯有成文的神之话语，才是我们确定无误的向导。",
                      "Brown's response is direct: “There is no unbroken, authoritative chain of oral tradition going back to Moses. That is simply a pious myth without biblical support.” He grants that customs and traditions did exist throughout Israel's history — some good, some bad, some neutral; no one disputes that. But the specific claim that an authoritative Oral Torah was given alongside the Written one at Sinai lacks evidence. He cites Jewish scholar Alan Avery-Peck: the rabbinic writings do not “embody” a unitary tradition stretching back to Sinai; they are “the products of their authors,” crafted to carry Judaism from their day to ours. Brown's conclusion: the written Word of God alone is our sure guide.")),
                step(S3, S3E,
                    p("<strong>קַבָּלָה · kabbalah</strong>——「领受、传承下来的东西」。这个词（与神秘主义的「卡巴拉」同源）的本义就是「传统」。传统犹太教用《先贤篇》(Pirkei Avot) 开篇那句著名的话来支撑这条链子：「摩西在西奈领受了妥拉，传给约书亚，约书亚传给长老……」布朗并不否认「传承」本身的存在与价值；他质疑的是这条链子被赋予的<em>权威等级</em>——把人的传承，提升到与神默示的圣经同等的地位。圣经里 <em>kabbalah</em>（人所领受的）从来不该凌驾于 <em>Torah</em>（神所赐下的）之上。",
                      "<strong>קַבָּלָה · kabbalah</strong> — “that which is received, handed down.” This word (the same root as mystical “Kabbalah”) simply means “tradition.” Traditional Judaism supports the chain with the famous opening of <em>Pirkei Avot</em>: “Moses received the Torah at Sinai and handed it to Joshua, Joshua to the elders...” Brown does not deny that transmission exists or has value; he questions the <em>level of authority</em> assigned to it — elevating a human handing-down to equal standing with God-breathed Scripture. In the Bible, <em>kabbalah</em> (what humans receive) was never meant to outrank <em>Torah</em> (what God gives).")),
                step(S4, S4E,
                    p("耶书亚自己也面对过同样的张力。祂对法利赛人说：「你们为什么因着你们的<em>传统</em>，犯神的诫命呢？」又引以赛亚的话：「他们将人的吩咐当作道理教导人」(《马太福音》15:3, 9)。请注意：耶书亚不是在废弃妥拉——祂是在分辨「神的诫命」与「人的传统」，并坚持前者的至高权威。这正是布朗这一课的核心：把神所默示的话语，与人虔诚却会犯错的传承，分别开来。对今天的我们也一样：我们最深的根基，必须是神所说的话，而非任何「未曾断绝的链子」。",
                      "Yeshua faced this very tension. He asked the Pharisees, “Why do you break the command of God for the sake of your <em>tradition</em>?” and quoted Isaiah: “They worship me in vain; their teachings are merely human rules” (Matthew 15:3, 9). Note carefully: Yeshua is not abolishing Torah — he is distinguishing “the command of God” from “the tradition of men,” and insisting on the supremacy of the former. That is the heart of Brown's lesson: setting God's inspired word apart from a human, devout-but-fallible transmission. The same holds for us: our deepest foundation must be what God has said, not any “unbroken chain.”")),
                step(S5, S5E,
                    ul(
                        ("在我自己的信仰里，有哪些『传统』被我不自觉地提升到了与圣经同等的权威？",
                         "In my own faith, what “traditions” have I unconsciously elevated to the authority of Scripture itself?"),
                        ("耶书亚区分『神的诫命』与『人的传统』。我能在自己的群体里诚实地作出同样的分辨吗？",
                         "Yeshua distinguished “God's command” from “human tradition.” Can I make that same honest distinction within my own community?"),
                        ("布朗对传统犹太教既尊重又质疑。我能否学会这种『带着敬意的诚实』，而非轻看或盲从？",
                         "Brown both respects and questions traditional Judaism. Can I learn that “respectful honesty,” instead of contempt or blind acceptance?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "没有拉比，圣经就读不懂吗？",
            "title_en": "Is the Bible Unintelligible Without the Rabbis?",
            "steps": [
                step(S1, S1E,
                    p("（异议 6.3–6.4）「没有拉比的传统，妥拉（连同整本希伯来圣经）根本无法读懂。而且，根据《申命记》17:8–13，拉比拥有解释律法、教导我们如何生活的<em>唯一</em>权柄；谁不肯听从他们，谁就在神眼中犯了大罪。」这是一记双重的论证：先说圣经离了拉比就晦涩难解，再用圣经本身（申 17）来证明拉比拥有不容置疑的最高裁断权。",
                      "(Objections 6.3–6.4) “Without the rabbinic traditions, the Torah (and the whole Hebrew Bible) is unintelligible. Moreover, according to Deuteronomy 17:8–13, the rabbis have the <em>sole</em> authority to interpret the Law and tell us how to live; whoever refuses to listen to them is guilty of a serious sin before God.” It is a double argument: first that Scripture is obscure without the rabbis, then that Scripture itself (Deut 17) grants the rabbis unquestionable final authority.")),
                step(S2, S2E,
                    p("布朗承认圣经确实有难解之处，也承认有学问的教师极有价值。但「读不懂」是被夸大了：妥拉本身宣告它的话「不是太难、也不太远」，是人「可以遵行的」(申 30)。至于《申命记》17 章，布朗指出它设立的是<em>祭司与审判官</em>的司法体系，用以裁决具体的争讼案件——而不是授予后世的拉比一张可以创造、增添律法并自称无误的空白支票。把一段关于「司法上诉程序」的经文，扩张成「拉比对圣经拥有绝对解释垄断权」的依据，是远远超出了经文原意。神的确设立了教导的权柄，但没有任何人间权柄可以凌驾于神自己的话语之上。",
                      "Brown grants that Scripture has difficult passages and that learned teachers are genuinely valuable. But “unintelligible” is overstated: the Torah declares its own words “not too difficult, nor far off,” but something a person “may do” (Deut 30). As for Deuteronomy 17, Brown notes it establishes a <em>priestly and judicial</em> system to settle specific legal disputes — not a blank check for later rabbis to create and add laws and declare themselves infallible. To stretch a text about “a judicial appeals process” into “the rabbis hold an absolute interpretive monopoly over Scripture” goes far beyond its meaning. God did appoint teaching authority, but no human authority may stand over God's own word.")),
                step(S3, S3E,
                    p("<strong>שֹׁפֵט · shofet</strong>——「审判官、裁决者」。《申命记》17 章设立的是「祭司」与「<em>审判官</em> (shofet)」，在「难断的案件」上作出裁决。关键在于：这是一个<em>司法</em>职分，而非一个「无误的、能增补圣经的立法机构」。希伯来圣经里，最终的「审判官」始终是神自己——「审判全地的主，岂不行公义吗？」(《创世记》18:25)。一切人间的 <em>shofet</em> 都是在神的话语之下、向神负责地施行裁断，而非取代神的话语。",
                      "<strong>שֹׁפֵט · shofet</strong> — “judge, one who renders a verdict.” Deuteronomy 17 establishes “the priests” and “the <em>judge</em> (shofet)” to rule on “cases too difficult to decide.” The key point: this is a <em>judicial</em> office, not an “infallible legislature that can add to Scripture.” In the Hebrew Bible, the ultimate “Judge” is always God himself — “Will not the Judge of all the earth do right?” (Genesis 18:25). Every human <em>shofet</em> renders verdicts <em>under</em> God's word and accountable to him — never replacing it.")),
                step(S4, S4E,
                    p("耶书亚对此有一句意味深长的话：祂责备律法师「把知识的钥匙夺了去；自己不进去，正要进去的人，你们也阻挡他们」(《路加福音》11:52)。神从未打算让祂的百姓离了一个专业阶层就无法亲近祂的话语。先知耶利米所预言的新约的核心荣耀，正是：「他们各人不再教导自己的邻舍……因为他们从最小的到至大的，都必认识我」(《耶利米书》31:34)。在弥赛亚里，圣灵亲自把神的话语写在每一个信徒的心上——这不是废掉教师，而是让神的话语向每一颗谦卑的心敞开。",
                      "Yeshua had a piercing word on this: he rebuked the experts in the Law because “you have taken away the key to knowledge. You yourselves have not entered, and you have hindered those who were entering” (Luke 11:52). God never intended his people to be unable to approach his word without a professional class. The crowning glory of the new covenant Jeremiah foretold is exactly this: “No longer will they teach their neighbor... because they will all know me, from the least of them to the greatest” (Jeremiah 31:34). In the Messiah, the Spirit himself writes God's word on every believer's heart — not abolishing teachers, but opening God's word to every humble heart.")),
                step(S5, S5E,
                    ul(
                        ("我是否也曾觉得自己『读不懂圣经』，必须完全依赖某位权威才能亲近神的话？这种依赖在哪里是健康的，在哪里成了拦阻？",
                         "Have I felt I “can't understand the Bible” and must depend entirely on some authority to approach God's word? Where is that dependence healthy, and where does it become a barrier?"),
                        ("新约应许『他们都必认识我，从最小的到至大的』。这个应许如何改变我亲近神话语的方式？",
                         "The new covenant promises “they will all know me, from the least to the greatest.” How does that promise change the way I come to God's word?"),
                        ("教师有真实的价值，权威却不可凌驾神的话。我如何同时尊重良师，又直接来到神面前？",
                         "Teachers have real value, yet no authority may stand over God's word. How do I both honor good teachers and come directly to God myself?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "西奈永约与「假先知」的指控",
            "title_en": "The Eternal Sinai Covenant and the Charge of “False Prophet”",
            "steps": [
                step(S1, S1E,
                    p("（异议 6.5–6.6, 6.15）「我们有一个在西奈山赐下的永远之约。任何叫我们偏离这约的人，不是假先知，就是假教师，二者必居其一。圣经里像但以理这样的人物，明明就遵守着拉比的传统。况且，耶稣自己在《马太福音》23 章不也教导祂的犹太门徒，要听从坐在摩西位上的文士和法利赛人吗？换句话说，连耶稣都叫人遵守口传妥拉！」",
                      "(Objections 6.5–6.6, 6.15) “We have an eternal covenant given at Sinai. Anyone who tells us to deviate from it is either a false prophet or a false teacher. Biblical figures such as Daniel plainly kept the rabbinic traditions. And didn't Jesus himself, in Matthew 23, teach his Jewish followers to obey the scribes and Pharisees who sit in Moses' seat — in other words, to follow the Oral Law?”")),
                step(S2, S2E,
                    p("布朗逐一回应。论「永约」：西奈之约确实是真的、荣耀的；但希伯来圣经自己就预言了一个「<em>新</em>约」(耶 31)——所以指向新约的，并非「偏离」神，而正是神自己应许要做的事。论「但以理遵守拉比传统」：这是把后世的传统，时代错置地读进了一位早于拉比犹太教数百年的先知身上。论《马太福音》23 章：耶书亚说「凡他们所吩咐你们的，你们都要谨守遵行」，紧接着却严厉斥责他们「能说不能行」、把难担的重担放在人身上。布朗指出，耶书亚的重点是承认他们在当时拥有教导妥拉的<em>席位</em>，同时警告人不可效法他们的虚伪——这绝不等于为「口传妥拉具有西奈式权威」背书。",
                      "Brown answers each. On the “eternal covenant”: the Sinai covenant is real and glorious; but the Hebrew Bible itself foretells a “<em>new</em> covenant” (Jer 31) — so pointing to the new covenant is not “deviating” from God but precisely what God himself promised to do. On “Daniel kept rabbinic traditions”: this anachronistically reads later traditions back into a prophet who lived centuries before rabbinic Judaism. On Matthew 23: Yeshua says “do whatever they tell you,” then immediately denounces them sharply as those who “do not practice what they preach” and load heavy burdens on people. Brown notes Yeshua's point is to acknowledge that they held the teaching <em>seat</em> of Torah at that moment, while warning against imitating their hypocrisy — hardly an endorsement that the Oral Torah carries Sinai-level authority.")),
                step(S3, S3E,
                    p("<strong>בְּרִית חֲדָשָׁה · brit chadashah</strong>——「新约」。这个词不是基督徒发明的；它出自希伯来先知耶利米的口：「日子将到，我要与以色列家和犹大家另立<em>新约</em>」(《耶利米书》31:31)。这是整场争论的关键：弥赛亚信仰所宣告的「新约」，不是对西奈的背叛，而是西奈之约里早已埋下、并由犹太先知亲口预言的应许的成全。指控耶书亚的跟随者「偏离了永约」之前，必须先面对：是谁先说了「新约」这个词？是神自己。",
                      "<strong>בְּרִית חֲדָשָׁה · brit chadashah</strong> — “new covenant.” This phrase was not invented by Christians; it comes from the mouth of the Hebrew prophet Jeremiah: “The days are coming, declares the LORD, when I will make a <em>new covenant</em> with the house of Israel and the house of Judah” (Jeremiah 31:31). This is the crux of the whole debate: the “new covenant” that Messianic faith proclaims is not a betrayal of Sinai but the fulfillment of a promise already seeded within the Sinai covenant and spoken aloud by a Jewish prophet. Before charging Yeshua's followers with “deviating from the eternal covenant,” one must reckon with who said the words “new covenant” first: God himself.")),
                step(S4, S4E,
                    p("「假先知」的检验标准，恰恰来自妥拉本身：真先知所说必应验，且必引人去敬拜独一的真神（申 13, 18）。布朗的整套护教，正是要表明耶书亚通过了这个检验：祂应验了希伯来圣经的弥赛亚预言，并把万民引向以色列的神。所以问题被翻转了过来：那位预言并设立「新约」的，若正是赐下西奈之约的同一位神，那么拒绝祂所差来的弥赛亚，才是真正地「偏离了」神的心意。耶书亚不是来废掉律法，而是来成全它，并领我们进入那位先知所预言的、写在心上的约。",
                      "The test for a “false prophet” comes from Torah itself: a true prophet's words come to pass, and he leads people to worship the one true God (Deut 13, 18). Brown's whole case is that Yeshua passes this test: he fulfilled the Hebrew Bible's messianic prophecies and turned the nations toward the God of Israel. So the question is turned around: if the One who foretold and established the “new covenant” is the very same God who gave the Sinai covenant, then to reject the Messiah he sent is what truly “deviates” from God's heart. Yeshua came not to abolish the Law but to fulfill it, and to lead us into the heart-written covenant the prophet foretold.")),
                step(S5, S5E,
                    ul(
                        ("『新约』一词出自犹太先知耶利米之口。这如何改变我对『旧约 vs 新约』关系的理解？",
                         "The phrase “new covenant” comes from the Jewish prophet Jeremiah. How does that change how I understand the relationship between “old” and “new” covenants?"),
                        ("耶书亚在马太福音23章既承认教导者的席位，又斥责他们的虚伪。我能否在自己的群体里同样地『尊重职分却不盲从其人』？",
                         "In Matthew 23 Yeshua both acknowledges the teaching seat and rebukes hypocrisy. Can I likewise “respect the office without blindly following the person” in my community?"),
                        ("真先知的检验是『应验 + 引人归向真神』。耶书亚如何通过了这两项检验？",
                         "The test of a true prophet is “fulfillment + turning people to the true God.” How does Yeshua pass both?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "「我们的传统自给自足——我们不需要你的耶稣」",
            "title_en": "“Our Tradition Is Self-Sufficient — We Don't Need Your Jesus”",
            "steps": [
                step(S1, S1E,
                    p("（异议 6.8–6.9, 6.18）「我们的传统是完全自足的——我们有祷告书、有注释、有律法典籍、有习俗。犹太教绝不是一个死的宗教，它两千年来激励并保守了千百万我们的同胞。你尽管留着你的耶稣，我守我的犹太教。你那里没有任何我需要或想要的东西。」这或许是最有分量、也最动人的一条异议，因为它不是出于论证，而是出于一种饱满的、活生生的归属感。",
                      "(Objections 6.8–6.9, 6.18) “Our tradition is totally self-sufficient — we have our prayer books, our commentaries, our law codes, our customs. Judaism is anything but a dead religion; for two thousand years it has inspired and preserved millions of our people. You can keep your Jesus; I'll keep my Judaism. You have nothing I need or want.” This may be the weightiest and most moving objection of all, because it rests not on argument but on a full, living sense of belonging.")),
                step(S2, S2E,
                    p("布朗以极大的温柔回应。他<em>由衷</em>地称许犹太教：它忠于独一真神，以妥拉为生命根基，孕育了深厚的智慧、伦理、家庭与世代传承。他绝不轻看这一切。然而他也温柔地追问：一个宗教可以是美好的、深刻的、保守一个民族的——却仍然缺少那最核心的一样：罪得赦免的确据，以及与神面对面的和好，正如先知们所应许、并由弥赛亚以祂的死与复活所成就的。布朗自己作为犹太人，正是在耶书亚里寻见了他在传统中渴慕却未曾寻得的：不是一套更好的体系，而是一位救赎主。他说的从来不是「犹太教里没有美善」，而是「还有一位，是这一切美善最终所指向的」。",
                      "Brown responds with great tenderness. He <em>genuinely</em> commends Judaism: loyal to the one true God, making Torah the foundation of life, cultivating deep wisdom, ethics, family, and continuity. He does not belittle any of it. Yet he gently asks: a religion can be beautiful, profound, and people-preserving — and still lack the one thing at the center: the assurance of forgiveness of sins and reconciliation face-to-face with God, as the prophets promised and as the Messiah accomplished by his death and resurrection. Brown, a Jew himself, found in Yeshua what he longed for in the tradition but had not found there: not a better system, but a Redeemer. His claim is never “there is no good in Judaism,” but “there is One to whom all that good finally points.”")),
                step(S3, S3E,
                    p("<strong>דַּיֵּנוּ · dayenu</strong>——「这对我们就够了」。这是逾越节家宴中那首动人之歌的叠句：神为我们所行的每一件恩事，「单单这一件，就够了 (dayenu)」。这个词美得令人心醉，却也藏着这条异议的核心张力：「我所有的，已经够了。」布朗温柔地把这首歌的逻辑推到它的尽头——逾越节的羔羊、出埃及、西奈、应许之地……这一连串恩典本身，岂不都在向前指着一个尚未到来的、更大的救赎？「够了」是一种感恩，但若它变成「我无需再领受」，就可能拦阻人去领受神接下来要赐的那一位。",
                      "<strong>דַּיֵּנוּ · dayenu</strong> — “it would have been enough for us.” This is the refrain of the beloved Passover song: for each act of God's kindness, “that alone would have been enough (dayenu).” The word is achingly beautiful, yet it holds the tension at the heart of this objection: “What I have is already enough.” Brown gently presses the song's logic to its end — the Passover lamb, the Exodus, Sinai, the Promised Land... does not this very chain of gifts point forward to a still-greater redemption yet to come? “Enough” is a posture of gratitude; but if it becomes “I need receive nothing more,” it can keep one from receiving the One God means to give next.")),
                step(S4, S4E,
                    p("使徒保罗——一位「按律法上的义，是无可指摘的」法利赛人——正是亲身经历了这条异议的反面。他拥有传统所能给的一切，却写道：「只是我先前以为与我有益的，我现在因基督都当作有损的……为要得着基督」(《腓立比书》3:7-8)。请注意：保罗没有说他从前的根基是「垃圾」或「邪恶」；他说的是，与<em>认识弥赛亚</em>相比，那一切的「有益」都黯然失色了。这正是布朗想温柔传递的：不是要犹太人「丢弃」他们所珍爱的，而是邀请他们看见，那一切所渴慕、所预表的，已经在他们自己的弥赛亚耶书亚里成全了。",
                      "The apostle Paul — a Pharisee “faultless” in legal righteousness — lived out the reverse of this objection. He had everything the tradition could give, yet wrote: “Whatever were gains to me I now consider loss for the sake of the Messiah... that I may gain the Messiah” (Philippians 3:7-8). Note: Paul does not call his former foundation “garbage” or “evil”; he says that compared to <em>knowing the Messiah</em>, all its “gain” pales. That is exactly what Brown means to convey tenderly: not asking Jewish people to “discard” what they cherish, but inviting them to see that all it longs for and foreshadows is already fulfilled in their own Messiah, Yeshua.")),
                step(S5, S5E,
                    ul(
                        ("『你那里没有任何我需要的东西』——我自己的生命里，有没有一处也对神说着同样的话：『我已经够了』？",
                         "“You have nothing I need” — is there a place in my own life where I say the same to God: “I already have enough”?"),
                        ("布朗由衷称许犹太教的美善。我向不同信仰的人见证时，是先看见他们里面的美善，还是急于指出缺失？",
                         "Brown genuinely commends the good in Judaism. When I witness to people of another faith, do I first see the good in them, or rush to point out what's missing?"),
                        ("保罗不说传统是『垃圾』，而说与认识弥赛亚相比它『黯然失色』。这个分别，如何改变我谈论福音的语气？",
                         "Paul doesn't call the tradition “garbage” but says it “pales” next to knowing the Messiah. How does that distinction change the tone of how I speak of the Gospel?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "妥拉容易遵守吗？——《申命记》30 章",
            "title_en": "Is the Torah Easy to Keep? — Deuteronomy 30",
            "steps": [
                step(S1, S1E,
                    p("（异议 6.10）「根据《申命记》30:11–14，遵守妥拉并不困难——它是神赐给以色列的特别礼物，『这诫命……不是太难，也不太远』。这与基督教的观点完全相反：基督徒把律法看成一个不可能遵守的重担，甚至是一个咒诅。」这条异议直指一个常被基督徒误解的要点：律法在希伯来圣经里，是恩典、是礼物，是「使人活着」的道路，而非一套设计来压垮人的不可能任务。",
                      "(Objection 6.10) “According to Deuteronomy 30:11–14, keeping the Torah is not difficult — it is God's special gift to Israel: ‘this commandment... is not too hard for you, nor is it far off.’ This is completely contrary to the Christian view, which treats the Law as an impossible-to-keep burden, even a curse.” This objection targets a point Christians often misunderstand: in the Hebrew Bible, the Law is grace, gift, and a path “that you may live” — not an impossible task designed to crush people.")),
                step(S2, S2E,
                    p("布朗在这里出人意料地<em>同意</em>了一大半。他坚决反对那种把妥拉描绘成纯粹的「咒诅」或「神故意设下让人失败的圈套」的庸俗反律法主义——那不是圣经的教导。妥拉确实是恩典的礼物，是美善、圣洁、公义的。布朗的细致之处在于：他区分了「妥拉作为神良善的标准」与「堕落的人靠自己完全守全它的能力」。《申命记》30 章的「不太难」，是在呼召以色列<em>转向神、爱神、依靠祂的恩典</em>去行——而同一卷申命记也清醒地预言以色列必然失败、被掳，并需要神亲自为他们「行割礼，割去他们心里的污秽」(申 30:6)。换句话说，连妥拉本身都指向：人需要一颗被神更新的心。这一需要，正是新约的应许所要满足的。",
                      "Here Brown surprisingly <em>agrees</em> with much of it. He firmly rejects the crude antinomianism that paints the Torah as mere “curse” or a “trap God set for people to fail” — that is not biblical teaching. The Torah truly is a gracious gift: good, holy, and righteous. Brown's care lies in distinguishing “the Torah as God's good standard” from “fallen humanity's ability to keep it perfectly on its own.” The “not too hard” of Deuteronomy 30 is a call for Israel to <em>turn to God, love him, and obey by his grace</em> — and the same book of Deuteronomy soberly foretells that Israel will fail, be exiled, and need God himself to “circumcise their hearts” (Deut 30:6). In other words, even the Torah points beyond itself: people need a heart renewed by God. That need is exactly what the new covenant promises to meet.")),
                step(S3, S3E,
                    p("<strong>קָרוֹב · karov</strong>——「近」。「这话<em>离你甚近 (karov)</em>，就在你口中、在你心里」(申 30:14)。保罗在《罗马书》10 章直接引用了这节经文，而且把它读作指向<em>弥赛亚</em>与<em>信心的道</em>：那「近在口中、心里」的话，最终就是「你若口里认耶书亚为主、心里信神叫祂复活，就必得救」(罗 10:8-9)。换言之，保罗并不是在反对《申命记》30 章——他是在揭示它最深的意思：神所要的那种「近在心里」的顺服，唯有在弥赛亚里、藉着圣灵更新的心，才能真正活出来。",
                      "<strong>קָרוֹב · karov</strong> — “near.” “The word is <em>very near you (karov)</em>; it is in your mouth and in your heart” (Deut 30:14). Paul quotes this very verse in Romans 10 and reads it as pointing to the <em>Messiah</em> and the <em>word of faith</em>: the word “near, in your mouth and heart” turns out to be “if you confess with your mouth that Yeshua is Lord and believe in your heart that God raised him, you will be saved” (Rom 10:8-9). Paul is not contradicting Deuteronomy 30 — he is unveiling its deepest sense: the “near-to-the-heart” obedience God desires can only truly be lived out in the Messiah, through a heart renewed by the Spirit.")),
                step(S4, S4E,
                    p("这一课温柔地拆掉了一堵常见的墙。许多基督徒带着对「律法」的轻蔑读圣经，仿佛旧约是「行不通的坏消息」，新约才是「好消息」。布朗（与保罗一同）纠正了这一点：妥拉是良善的，问题从来不在律法，而在人心。新约的荣耀，不是「废掉那良善的律法」，而是「赐下一颗能去爱、去行那律法的新心」——「我要将我的律法放在他们里面，写在他们心上」(耶 31:33)。于是《申命记》30 章那「近在心里」的应许，在弥赛亚里、藉着内住的圣灵，第一次成为人真实的经历。",
                      "This lesson gently dismantles a common wall. Many Christians read Scripture with contempt for “the Law,” as if the Old Testament were “unworkable bad news” and the New the “good news.” Brown (with Paul) corrects this: the Torah is good; the problem was never the Law but the human heart. The glory of the new covenant is not “abolishing the good Law” but “giving a new heart that can love and live it” — “I will put my law within them, and write it on their hearts” (Jer 31:33). So the Deuteronomy 30 promise of a word “near to the heart” becomes, for the first time, a person's real experience — in the Messiah, through the indwelling Spirit.")),
                step(S5, S5E,
                    ul(
                        ("我是否带着对『律法』的轻蔑读旧约？布朗提醒我们：律法是良善的，问题在人心。这如何改变我读旧约的眼光？",
                         "Do I read the Old Testament with contempt for “the Law”? Brown reminds us the Law is good and the problem is the heart. How does that change how I read the Old Testament?"),
                        ("《申命记》30章说神的话『近在你心里』，保罗把它读作指向弥赛亚。神所要的顺服，离我的心有多近？",
                         "Deuteronomy 30 says God's word is “near, in your heart,” and Paul reads it as pointing to the Messiah. How near to my heart is the obedience God desires?"),
                        ("新约的应许是『一颗新心』，而非『一套更松的规矩』。我是在靠自己努力守规矩，还是在靠那颗被更新的心去爱？",
                         "The new covenant promises “a new heart,” not “looser rules.” Am I striving to keep rules by myself, or loving out of a renewed heart?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "犹太民族的存续与独特——一个民族两千年的见证",
            "title_en": "Jewish Survival and Uniqueness — Two Thousand Years of Witness",
            "steps": [
                step(S1, S1E,
                    p("（异议 6.11–6.13）「今天还能辨认出来的犹太人，全都是那些拒绝了基督教（或世俗主义）的人的后代——唯有守传统的犹太人，作为一个民族存活了下来。犹太教是独一无二的：在世上所有宗教中，唯独犹太教以一场全民族亲眼见证的公开启示为开端，无人能够更改这一事实。而且犹太教是理性的宗教，它说『用你的头脑』，而非『关掉你的头脑』。」这是一组以历史与理性为支点的有力论证。",
                      "(Objections 6.11–6.13) “The only identifiable Jews today are descendants of those who rejected Christianity (or secularism) — only traditional Jews survived as a people. Judaism is unique: of all the world's religions, only Judaism began with a public revelation witnessed by the entire nation, and no one can alter that fact. And Judaism is a rational religion — it says ‘use your mind,’ not ‘shut off your mind.’” This is a powerful cluster of arguments resting on history and reason.")),
                step(S2, S2E,
                    p("布朗对这些论点的回应充满敬意。论存续：犹太民族奇迹般的存留，他<em>完全</em>承认——这本身就是神信实守约的明证（与他立约的应许相合）。但他指出，「守传统」并非犹太人存续的唯一解释；遍布各地、各种各样的犹太群体（包括弥赛亚犹太信徒）同样是这个民族的真实成员。论西奈的公开启示：布朗珍视它，并认为它确实是真实历史；但他补充，弥赛亚信仰从不否认西奈，反而建立在西奈之上——耶书亚也在加利利、在众人面前公开行事、公开受死、并向五百多人显现。论理性：布朗本人正是凭着对证据、预言、历史的诚实查考，才信了耶书亚。他邀请的，恰恰是「用你的头脑」——把同样的理性，也用来诚实地查考弥赛亚的宣称。",
                      "Brown answers these with respect. On survival: he <em>fully</em> grants the miracle of Jewish preservation — itself a proof of God's covenant faithfulness (in line with his covenant promises). But he notes that “keeping tradition” is not the only explanation; diverse Jewish communities everywhere (including Messianic Jewish believers) are equally real members of the people. On Sinai's public revelation: Brown treasures it and holds it to be real history; but he adds that Messianic faith never denies Sinai — it is built on Sinai, and Yeshua too acted publicly in Galilee, died publicly, and appeared to more than five hundred. On reason: Brown himself came to faith in Yeshua precisely through an honest examination of evidence, prophecy, and history. What he invites is exactly “use your mind” — applying that same reason to an honest examination of the Messiah's claims.")),
                step(S3, S3E,
                    p("<strong>עַם סְגֻלָּה · am segulah</strong>——「特选的子民、珍宝般的产业」。神对以色列说：「你们要归我作<em>属我的子民 (am segulah)</em>」(出 19:5)。犹太民族的存续，确实是这「珍宝」身份的活见证。但布朗（与保罗在罗马书 11 章一同）会提醒我们：这份拣选是神的恩典，不是任何一群人的功劳；它是「不收回的」(罗 11:29)，因此它<em>必然</em>包括神要让以色列认识他们自己弥赛亚的心愿。这个民族被奇迹般地保守，不是为了停在原地，而是为了承受神在他们身上要成全的、那更大的救赎。",
                      "<strong>עַם סְגֻלָּה · am segulah</strong> — “a treasured people, a prized possession.” God says to Israel, “you will be my <em>treasured possession (am segulah)</em>” (Exod 19:5). Jewish survival truly is a living witness to this “treasure” identity. But Brown (with Paul in Romans 11) would remind us that this election is God's grace, not any group's achievement; it is “irrevocable” (Rom 11:29), and therefore it <em>necessarily</em> includes God's desire to bring Israel to know their own Messiah. This people is miraculously preserved not to stand still, but to inherit the greater redemption God means to fulfill in them.")),
                step(S4, S4E,
                    p("这一课为基督徒立下一个重要的姿态：对犹太民族的存续，我们的回应应当是<em>敬畏与感恩</em>，而非高傲。这个民族的存留，是神信实的证据，而我们外邦信徒是「被接上去的野橄榄枝」(罗 11)。同时，布朗示范了一种健康的护教：它从不要求人「关掉头脑」。弥赛亚信仰经得起最诚实的查考——预言的应验、历史的见证、空坟墓的证据。我们传讲耶书亚，不是要犹太人放弃理性或背弃西奈，而是邀请他们带着同样的理性与对真理的热爱，来认识那位西奈之约最终所指向的弥赛亚。",
                      "This lesson sets an important posture for Christians: our response to Jewish survival should be <em>awe and gratitude</em>, not arrogance. This people's endurance is evidence of God's faithfulness, and we Gentile believers are “wild olive branches grafted in” (Rom 11). At the same time, Brown models a healthy apologetic: one that never asks anyone to “shut off the mind.” Messianic faith withstands the most honest scrutiny — fulfilled prophecy, historical witness, the evidence of the empty tomb. We proclaim Yeshua not to ask Jewish people to abandon reason or forsake Sinai, but to invite them, with that same reason and love of truth, to know the Messiah to whom the Sinai covenant finally points.")),
                step(S5, S5E,
                    ul(
                        ("犹太民族奇迹般的存续，如何成为我对神信实的敬畏与感恩，而非高傲的理由？",
                         "How does the miracle of Jewish survival become for me a reason for awe and gratitude at God's faithfulness, rather than arrogance?"),
                        ("『用你的头脑，别关掉它』——我的信仰经得起诚实的理性查考吗？我害怕提问吗？",
                         "“Use your mind, don't shut it off” — does my faith withstand honest scrutiny? Am I afraid of questions?"),
                        ("作为被接上去的『野橄榄枝』，我对那承载着根的犹太民族，该有怎样的态度？",
                         "As a “wild olive branch” grafted in, what posture should I have toward the Jewish people who carry the root?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "新约里有的，拉比早就有了吗？",
            "title_en": "Is Everything Good in the New Testament Already in the Rabbis?",
            "steps": [
                step(S1, S1E,
                    p("（异议 6.14, 6.16–6.17）「新约里凡是好的，拉比犹太教里早就有了；凡是新的，就不是好的。真正『守这书』的人是传统犹太人——读读希伯来圣经，问问自己：『谁在遵行这些律法诫命？』是传统犹太人。况且《诗篇》19 篇说，妥拉本身就能『苏醒人心』、使人归正——我们已经有了那能救人的妥拉。」",
                      "(Objections 6.14, 6.16–6.17) “Anything good in the New Testament is already in Rabbinic Judaism; anything new is not good. Traditional Jews are the real ‘people of the Book’ — read the Hebrew Scriptures and ask, ‘Who keeps these laws and commandments?’ Traditional Jews. And Psalm 19 says the Torah itself ‘revives the soul’ and converts a person — we already have the Torah that saves.”")),
                step(S2, S2E,
                    p("布朗承认拉比文献里确有许多崇高的伦理教导，有些甚至与耶书亚的教导相呼应——这并不奇怪，因为它们都扎根于同一部希伯来圣经。但他指出两点：第一，「凡新的就不好」是一个站不住脚的预设——神自己应许要行「新事」、立「新约」、赐「新心」；新，并不等于坏。第二，也是最关键的：耶书亚所带来的，核心并非「一套新的伦理格言」，而是「祂自己」——祂亲身成全了预言，担当了世人的罪，从死里复活。拉比的智慧再崇高，也无法替你赎罪、无法胜过死亡。论《诗篇》19 篇：布朗指出，「妥拉苏醒人心」是真的、荣耀的——而妥拉所苏醒、所指向的那位，正是它的成全者弥赛亚。",
                      "Brown grants that rabbinic literature holds many lofty ethical teachings, some even echoing Yeshua's — no surprise, since both are rooted in the same Hebrew Bible. But he makes two points. First, “anything new is not good” is an indefensible assumption — God himself promises to do a “new thing,” make a “new covenant,” give a “new heart”; new does not mean bad. Second, and most crucial: what Yeshua brings at its core is not “a new set of ethical maxims” but “himself” — he personally fulfilled prophecy, bore the sins of the world, and rose from the dead. However lofty rabbinic wisdom is, it cannot atone for your sin or conquer death. On Psalm 19: Brown notes that “the Torah revives the soul” is true and glorious — and the One the Torah revives and points to is its fulfiller, the Messiah.")),
                step(S3, S3E,
                    p("<strong>מְשִׁיבַת נָפֶשׁ · meshivat nafesh</strong>——「苏醒人心 / 使灵魂回转」。《诗篇》19:7：「耶和华的妥拉全备，能<em>苏醒人心 (meshivat nafesh)</em>。」这是一个荣耀的真理。但布朗会温柔地追问：妥拉「苏醒」灵魂，是要把灵魂引向何处？妥拉像一面完美的镜子，既照出神的圣洁，也照出人的亏欠，从而把人的心引向那位能真正赦罪、真正更新灵魂的救赎主。<em>meshivat nafesh</em> 的终点，不是停在律法上，而是被律法引到弥赛亚面前——祂正是「叫灵魂苏醒」的牧者：「祂使我的灵魂苏醒 (yeshovev)」(诗 23:3)。",
                      "<strong>מְשִׁיבַת נָפֶשׁ · meshivat nafesh</strong> — “reviving the soul / restoring the inner being.” Psalm 19:7: “The Torah of the LORD is perfect, <em>reviving the soul (meshivat nafesh)</em>.” This is a glorious truth. But Brown would gently ask: when the Torah “revives” the soul, where is it leading the soul? The Torah is like a perfect mirror, showing both God's holiness and our shortfall, and so turning the heart toward the Redeemer who can truly forgive and renew the soul. The end of <em>meshivat nafesh</em> is not to stop at the Law, but to be led by the Law to the Messiah — the Shepherd who “revives my soul (yeshovev)” (Ps 23:3).")),
                step(S4, S4E,
                    p("这一课的核心，是一个温柔却决定性的分辨：基督信仰的中心，从来不是「一套更新更好的道德规范」，而是「一个位格」。如果耶书亚带来的只是更高的伦理，那么「拉比里早就有了」或许还能算一种回应。但福音的宣告是：耶书亚成全了妥拉所指向的一切，担当了妥拉所定的罪，并以复活胜过了妥拉所宣告的死亡的工价。所以问题不是「你的书里有没有好教导」，而是「谁能为你的罪付上代价、把你从死里救出来」。妥拉苏醒灵魂，把灵魂带到它一直在等候的那位牧者面前。",
                      "The heart of this lesson is a gentle but decisive distinction: the center of the faith is never “a newer, better moral code” but “a person.” If Yeshua brought only higher ethics, then “the rabbis already had it” might be some kind of answer. But the Gospel's claim is that Yeshua fulfilled all the Torah pointed to, bore the sin the Torah defined, and by resurrection overcame the wages of death the Torah declared. So the question is not “does your book have good teaching,” but “who can pay for your sin and raise you from death?” The Torah revives the soul — and leads the soul to the very Shepherd it has been waiting for.")),
                step(S5, S5E,
                    ul(
                        ("『凡新的就不好』——但神应许行新事、立新约、赐新心。我心里是否也有一种对『新』的恐惧，拦阻我领受神要做的事？",
                         "“Anything new is not good” — yet God promises new things, a new covenant, a new heart. Is there a fear of “the new” in me that keeps me from receiving what God wants to do?"),
                        ("基督信仰的中心是一个位格，而非一套规范。我的信仰，是在『遵守一套教导』，还是在『认识一位救主』？",
                         "The center of the faith is a person, not a code. Is my faith “keeping a set of teachings,” or “knowing a Savior”?"),
                        ("妥拉像镜子，照出神的圣洁与我的亏欠。它把我的灵魂引向了哪里？",
                         "The Torah is a mirror, showing God's holiness and my shortfall. Where has it led my soul?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "「你那里没有我需要的」——以及那位回答了一切的弥赛亚",
            "title_en": "“You Have Nothing I Need” — and the Messiah Who Answers It All",
            "steps": [
                step(S1, S1E,
                    p("（异议 6.18 与全书的总结）「你尽管留着你的耶稣，我守我的犹太教。你那里没有任何我需要或想要的东西。」布朗用这句话作为整套五卷本巨著的收尾——它既是一句拒绝，也是一扇仍然敞开的门。布朗深知，所有的论证、所有对预言与历史的诚实查考，最终都要落到这个最个人、最赤裸的问题上：我究竟需不需要一位救赎主？而他用整整一生、整整五卷书所要温柔传递的回答是：你所深爱、所珍惜的这一切美善，并没有要被夺走；它们正是在向你指出那一位——你自己的弥赛亚耶书亚。",
                      "(Objection 6.18 and the summit of the whole work) “You can keep your Jesus; I'll keep my Judaism. You have nothing I need or want.” Brown closes the entire five-volume work with this line — at once a refusal and a door still standing open. He knows that all the arguments, all the honest examination of prophecy and history, finally land on the most personal, naked question of all: do I, or do I not, need a Redeemer? And the answer he has labored a whole lifetime and five volumes to convey tenderly is this: all the good you love and treasure is not being taken away; it is pointing you to the One — your own Messiah, Yeshua.")),
                step(S2, S2E,
                    bq("「看哪，日子将到——这是耶和华说的——我要与以色列家和犹大家另立新约……我要赦免他们的罪孽，不再记念他们的罪恶。」",
                       "“The days are coming, declares the LORD, when I will make a new covenant with the house of Israel and the house of Judah... For I will forgive their wickedness and will remember their sins no more.”",
                       "《耶利米书》31:31, 34 · Jeremiah 31:31, 34")),
                step(S3, S3E,
                    p("<strong>יֵשׁוּעַ · Yeshua</strong>——「耶和华是拯救」。这是贯穿全书十八条异议、最终的那一个词。每一条异议——口传妥拉、拉比权柄、传统的自足、律法的难易、民族的存续、新约与旧约——归根结底，都绕着同一个核心打转：以色列需不需要、并且能不能领受那位名叫「拯救」的弥赛亚？耶书亚的名字本身，就是对「你那里没有我需要的」最温柔的回应：人最深、最普世、谁也无法靠传统或理性填满的需要，是<em>得救赎</em>；而这位弥赛亚的名字，就是这需要的答案。",
                      "<strong>יֵשׁוּעַ · Yeshua</strong> — “The LORD is salvation.” This is the final word beneath all eighteen objections of the book. Every objection — the Oral Torah, rabbinic authority, the sufficiency of tradition, the ease of the Law, the survival of the people, the new and old covenants — finally circles the same center: does Israel need, and can Israel receive, the Messiah whose name is “Salvation”? The very name Yeshua is the tenderest answer to “you have nothing I need”: humanity's deepest, most universal need — which no tradition or reason can fill — is to be <em>redeemed</em>; and the name of this Messiah is the answer to that need.")),
                step(S4, S4E,
                    p("这是整份指南的终点，也是一个邀请。我们走过了布朗对传统犹太教十八条异议的回应——每一处，他都既尊重又坚定，既诚实又满有爱。如今我们看见，他真正的目标从来不是「驳倒犹太教」，而是「为他所深爱的同胞，打开通往弥赛亚的门」。愿这八堂课塑造我们：成为一群既忠于真理、又满有「爱我民」(Ahavat Ammi) 之心的人；带着布朗那样的谦卑、温柔与坚定，去爱犹太民族，为他们祷告，并满怀盼望地等候那一日——以色列全家都认识他们自己的弥赛亚耶书亚，神所应许的新约在他们心中完全成全。",
                      "This is the end of the whole guide, and an invitation. We have walked through Brown's responses to eighteen objections of traditional Judaism — and at every point, he is both respectful and firm, both honest and full of love. We now see that his true aim was never “to refute Judaism” but “to open, for the people he deeply loves, the door to the Messiah.” May these eight lessons shape us into people both faithful to the truth and full of <em>Ahavat Ammi</em> — the love of his people; loving the Jewish people with Brown's humility, tenderness, and firmness, praying for them, and waiting in hope for the day when all Israel knows their own Messiah, Yeshua, and the new covenant God promised is fully fulfilled in their hearts.")),
                step(S5, S5E,
                    ul(
                        ("『你那里没有我需要的』——剥去一切论证，我自己是否真的承认：我需要一位救赎主？",
                         "“You have nothing I need” — stripped of all argument, do I myself truly admit that I need a Redeemer?"),
                        ("布朗的目标不是『驳倒』，而是『打开一扇门』。我向人见证时，是想赢，还是想爱？",
                         "Brown's aim was not “to refute” but “to open a door.” When I witness, do I want to win, or to love?"),
                        ("耶书亚的名字意思是『耶和华是拯救』。这个名字如何回答了这本书里全部十八条异议？",
                         "The name Yeshua means “the LORD is salvation.” How does that name answer all eighteen objections in this book?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "为以色列、为爱我民之心的祝祷",
    "closing_title_en": "A Blessing for Israel, and for a Heart of Ahavat Ammi",
    "closing_zh": "「愿耶和华赐福给你，保护你；愿耶和华使祂的脸光照你，赐恩给你。」<br/><br/>愿你既忠于真理，又满有温柔；<br/>愿你像布朗一样，深爱自己的同胞与犹太民族——<br/>爱到愿意说出那即使刺痛人的真理，<br/>也爱到愿意先看见他们里面的一切美善。<br/><br/>愿那位预言并设立新约的神，<br/>使以色列全家都认识他们自己的弥赛亚——<br/>耶书亚 (Yeshua)，那位名字就是「拯救」的主。<br/><br/>「耶和华是拯救」——愿这名成为你向以色列所传的好消息。",
    "closing_en": "“The LORD bless you and keep you; the LORD make his face shine upon you and be gracious to you.”<br/><br/>May you be both faithful to the truth and full of tenderness.<br/>May you, like Brown, deeply love your people and the people of Israel —<br/>loving enough to speak the truth even when it stings,<br/>and loving enough to see first all the good within them.<br/><br/>May the God who foretold and established the new covenant<br/>bring all Israel to know their own Messiah —<br/>Yeshua, the Lord whose very name is “Salvation.”<br/><br/>“The LORD is salvation” — may that name be the good news you carry to Israel.",
}

# -*- coding: utf-8 -*-
"""Content module for study-jewish-magic.html.

Yuval Harari, *Jewish Magic before the Rise of Kabbalah*, trans. Batya Stein
(Wayne State University Press, 2017; orig. Hebrew, *Early Jewish Magic*, 2010).
Read here with biblical discernment — a window into the world Scripture's
prohibitions on sorcery addressed, not an endorsement of the practice.
"""

RHYTHM_ZH = """        <strong>① 学者的世界</strong>—— 用哈拉里的研究呈现古代犹太魔法的图景；<br/>
        <strong>② 关键经文</strong>—— 一处与之相关、需重新聆听的圣经；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，照亮那个世界；<br/>
        <strong>④ 圣经的视角</strong>—— 圣经如何分辨、如何回应这一现象；<br/>
        <strong>⑤ 诚实的提问</strong>—— 留给你与小组省察的问题。"""

RHYTHM_EN = """        <strong>① The Scholar's World</strong> — the world of ancient Jewish magic, in Harari's research;<br/>
        <strong>② Key Scripture</strong> — a related text we must hear again;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that lights up that world;<br/>
        <strong>④ A Biblical Lens</strong> — how Scripture discerns and answers the phenomenon;<br/>
        <strong>⑤ Honest Questions</strong> — questions for you and your group to examine."""


def step(label_zh, label_en, *body):
    return {"label_zh": label_zh, "label_en": label_en, "body": list(body)}

def p(zh, en):
    return {"type": "p", "zh": zh, "en": en}

def bq(zh, en, cite=None):
    return {"type": "blockquote", "zh": zh, "en": en, "cite": cite}

def ul(*items):
    return {"type": "ul", "items": [{"zh": z, "en": e} for z, e in items]}

S1, S1E = "① 学者的世界", "① The Scholar's World"
S2, S2E = "② 关键经文", "② Key Scripture"
S3, S3E = "③ 希伯来语之眼", "③ Through Hebrew Eyes"
S4, S4E = "④ 圣经的视角", "④ A Biblical Lens"
S5, S5E = "⑤ 诚实的提问", "⑤ Honest Questions"


study = {
    "title_tag": "《卡巴拉兴起之前的犹太魔法》研习指南 · Jewish Magic before Kabbalah — Study Guide · 妥拉之光",
    "meta_desc": "A discerning Christian study guide to Yuval Harari's Jewish Magic before the Rise of Kabbalah — eight bilingual lessons on amulets, adjurations, incantation bowls, the Sword of Moses, and what Scripture says about the unseen realm and the power of the Name.",
    "og_title": "Jewish Magic before the Rise of Kabbalah — A Study Guide",
    "og_desc": "Eight bilingual lessons through Yuval Harari's scholarly study of ancient Jewish magic — amulets, adjuration of angels, the divine Name — read with biblical discernment and Hebrew eyes.",
    "cover_alt": "Jewish Magic before the Rise of Kabbalah — Study Guide",
    "tagline_zh": "研习指南 · 学术导读与属灵分辨 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · Scholarship &amp; Discernment · 2026 · 5 · 31",
    "headline_zh": "卡巴拉兴起之前的<br/>犹太魔法",
    "headline_en": "Jewish Magic before<br/>the Rise of Kabbalah",
    "deck_zh": "八堂课程，跟随学者尤瓦尔·哈拉里 (Yuval Harari)，走进晚期古代与早期伊斯兰时期那个充满护身符、咒语碗与「召唤天使」文书的犹太魔法世界——并带着属灵的分辨，透过圣经之光来观看：神的话语如何分辨「咒术」与「信靠」，以及那超乎一切权势之上的「名」。",
    "deck_en": "Eight lessons following scholar Yuval Harari into the world of late-antique and early-Islamic Jewish magic — its amulets, incantation bowls, and texts for “adjuring angels” — and looking at it through the light of Scripture: how God's word distinguishes sorcery from trust, and the Name that is above every power.",
    "byline_zh": "基于尤瓦尔·哈拉里 (Yuval Harari)《卡巴拉兴起之前的犹太魔法》(Wayne State University Press, 2017；希伯来文原版 2010)。本指南以圣经为分辨之尺，研读而非效法。",
    "byline_en": "Based on Jewish Magic before the Rise of Kabbalah by Yuval Harari, trans. Batya Stein (Wayne State University Press, 2017; orig. Hebrew, 2010). Read with Scripture as the measure of discernment — to understand, not to imitate.",
    "readtime_zh": "约 55 分钟通读",
    "readtime_en": "~55 min read-through",
    "book_url": "https://www.wsupress.wayne.edu/9780814339107/",
    "book_link_zh": "购买原书 · Wayne State UP",
    "book_link_en": "Get the Book · Wayne State UP",
    "cta_url": "https://www.wsupress.wayne.edu/9780814339107/",
    "cta_zh": "购买《卡巴拉兴起之前的犹太魔法》原书 · Wayne State University Press",
    "cta_en": "Get the Book — Jewish Magic before the Rise of Kabbalah · Wayne State University Press",

    "lead_zh": "先说清楚这份指南的立场：我们研读哈拉里 (Yuval Harari) 这部严谨的学术著作，是为了<em>认识</em>圣经所处身的那个真实世界，而绝非要<em>效法</em>其中的任何做法。圣经明确禁止行邪术、占卜、交鬼（《申命记》18:9–14）。然而，许多基督徒对「巫术」「魔法」只有一个模糊、卡通化的印象。哈拉里——希伯来大学训练出的顶尖学者——带我们看见那个真实存在过的世界：晚期古代与早期伊斯兰时期，犹太人中间流传着大量护身符、咒语碗、「召唤天使」的文书。透过这扇学术的窗，圣经里那些关于「不可行邪术」的诫命，会从抽象的禁令，变成有血有肉、迫切而真实的话语。",
    "lead_en": "Let this guide's stance be clear from the start: we read Yuval Harari's rigorous scholarly work to <em>understand</em> the real world Scripture inhabited — never to <em>imitate</em> any of its practices. The Bible plainly forbids sorcery, divination, and consulting spirits (Deuteronomy 18:9–14). Yet many Christians carry only a vague, cartoonish picture of “magic.” Harari — a leading scholar trained at the Hebrew University — shows us a world that actually existed: amulets, incantation bowls, and texts for “adjuring angels” circulating among Jews in late antiquity and the early Islamic period. Through this scholarly window, Scripture's commands against sorcery turn from abstract prohibitions into flesh-and-blood, urgent, real words.",

    "intro": [
        p("哈拉里这本书的一大贡献，是诚实地揭示「魔法」这个概念本身有多难界定。他指出，那些被现代学者称为「魔法」的文本，从不自称为「魔法」；而「巫术」(kishuf) 在古代犹太语境里，往往是用来指控<em>别人</em>的词——「魔法」永远是「别人那一套」。这恰恰逼我们去问一个对今天的信徒同样要紧的问题：祷告与咒语、圣人与术士、segulah（妙方）与 kishuf（巫术），它们的界线究竟在哪里？这条界线，圣经划得极其清楚——而认识那个模糊的世界，正能帮我们看清圣经所划的这条线为何如此重要。",
          "One of the book's great contributions is to expose honestly how hard the very concept of “magic” is to define. Harari notes that the texts modern scholars call “magic” never call <em>themselves</em> magic; and <em>kishuf</em> (“sorcery”) in the ancient Jewish context was often a word used to accuse <em>others</em> — “magic” is always “the other person's” practice. This forces a question just as urgent for believers today: where exactly is the line between a prayer and a spell, a holy man and a sorcerer, a <em>segulah</em> (remedy) and <em>kishuf</em> (sorcery)? Scripture draws that line with great clarity — and knowing the blurry world helps us see why the line Scripture draws matters so much."),
        p("本指南共 <strong>八堂课</strong>，循着书中的主要主题展开。每一堂遵循同样的五部分节奏：",
          "The guide is structured as <strong>eight lessons</strong>, following the book's major themes. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句郑重的提醒：本指南绝不提供、也绝不鼓励任何咒语、术法或仪式。我们读的是历史与圣经，目的是属灵的分辨、敬畏与对那独一真神的信靠。凡圣经所禁止的，我们一概弃绝。",
          "A solemn caution: this guide provides and encourages no spells, techniques, or rituals whatsoever. We read history and Scripture, for the sake of discernment, reverence, and trust in the one true God. Whatever Scripture forbids, we wholly renounce."),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "什么是「魔法」？——一条模糊的界线",
            "title_en": "What Is “Magic”? — A Blurry Line",
            "steps": [
                step(S1, S1E,
                    p("哈拉里以一个令人意外的坦白开篇：经过多年研究，他发现「魔法」其实极难定义。每当他提起「犹太魔法」，总有人立刻反应：「犹太魔法？没这回事！要么是犹太的，要么是魔法的。」可是——护身符呢？咒语呢？祝福与咒诅呢？使用圣名呢？解恶梦呢？诵念诗篇呢？门框上的经卷 (mezuzot) 呢？行神迹的圣人呢？这些「都是另一回事」。哈拉里敏锐地指出：「魔法」永远是「<em>另一回事</em>」——是别人那一套。被称为「魔法」的文本，从不自称魔法。于是，界定「魔法」这件事本身，就暴露了一个更深的问题：祷告与咒语、敬虔与术法，分界到底在哪里？",
                      "Harari opens with a surprising admission: after years of study, he found “magic” extraordinarily hard to define. Whenever he mentioned “Jewish magic,” someone would react at once: “Jewish magic? No such thing! Either magic or Jewish.” But — what of amulets? incantations? blessings and curses? the use of holy names? reversing bad dreams? reciting psalms? the <em>mezuzot</em> on doorposts? holy men who work wonders? “Well, that's another matter.” Harari sharply observes: “magic” is always “<em>the other matter</em>” — the other person's practice. Texts labeled “magic” never call themselves so. Defining “magic,” then, exposes a deeper question: where exactly is the line between a prayer and a spell, between devotion and technique?")),
                step(S2, S2E,
                    bq("「你们中间不可有……占卜的、观兆的、用法术的、行邪术的、用迷术的、交鬼的、行巫术的、过阴的。凡行这些事的，都为耶和华所憎恶。」",
                       "“Let no one be found among you who... practices divination or sorcery, interprets omens, engages in witchcraft, casts spells, or who is a medium or spiritist or who consults the dead. Anyone who does these things is detestable to the LORD.”",
                       "《申命记》18:10-12 · Deuteronomy 18:10-12")),
                step(S3, S3E,
                    p("<strong>כִּשּׁוּף · kishuf</strong>——「巫术、邪术、咒术」。哈拉里指出一个耐人寻味的事实：古代那些实际操作护身符与咒语的人，从不用 <em>kishuf</em> 来称呼自己所做的——<em>kishuf</em> 几乎总是一个<em>指控</em>性的词，是用来定<em>别人</em>罪的。这正凸显了圣经诫命的智慧与难处：神禁止 <em>kishuf</em>，但人心总倾向于把自己的做法称作「敬虔」「妙方」「祝福」，而把同样的事在别人身上称作「邪术」。圣经划界的标准，因此不在于「这看起来像不像魔法」，而在于一个更深的问题：我究竟是在<em>信靠顺服</em>那位独一的真神，还是在<em>操控调动</em>某种属灵力量来达成我自己的意愿？",
                      "<strong>כִּשּׁוּף · kishuf</strong> — “sorcery, witchcraft.” Harari points to a telling fact: the ancient people who actually made amulets and spoke incantations never called what they did <em>kishuf</em> — <em>kishuf</em> was almost always an <em>accusatory</em> word, used to condemn <em>others</em>. This highlights both the wisdom and the difficulty of the biblical command: God forbids <em>kishuf</em>, but the human heart always tends to call its own practice “devotion,” “remedy,” “blessing,” while calling the same thing in another “sorcery.” Scripture's dividing line, therefore, is not “does this look like magic,” but a deeper question: am I <em>trusting and obeying</em> the one true God, or <em>manipulating and mobilizing</em> some spiritual power to bend reality to my own will?")),
                step(S4, S4E,
                    p("圣经划下的那条线，比「魔法」与「宗教」的外在形式更深、更内在。两个人可以做同样的外在动作——一个点蜡烛、念经文，是出于谦卑地向神祷告、把一切交托祂的主权；另一个点同样的蜡烛、念同样的字，却是想<em>强迫</em>属灵世界按自己的意思运作。前者是敬拜，后者是巫术。这条界线划在人心的朝向上：是「愿你的旨意成就」，还是「愿我的旨意成就」。研读这个模糊的古代世界，最大的益处，就是逼我们诚实地省察：我所谓的「祷告」「属灵操练」，其内在的朝向，究竟是信靠的顺服，还是变相的操控？",
                      "The line Scripture draws is deeper and more inward than the outward forms of “magic” versus “religion.” Two people can perform the same outward act — one lights a candle and recites a text in humble prayer, entrusting everything to God's sovereignty; the other lights the same candle and recites the same words in an attempt to <em>compel</em> the spiritual world to do their bidding. The first is worship; the second is sorcery. The line runs through the orientation of the heart: “your will be done” or “my will be done.” The great benefit of studying this blurry ancient world is that it forces us to examine honestly: in what I call “prayer” or “spiritual practice,” is the inward orientation a trusting obedience, or a disguised control?")),
                step(S5, S5E,
                    ul(
                        ("『魔法永远是别人那一套』——我是否也容易宽待自己的做法，却严苛地论断别人的？",
                         "“Magic is always the other person's practice” — am I quick to excuse my own practices while harshly judging others'?"),
                        ("圣经划界的关键不在外在形式，而在人心：是信靠顺服，还是操控调动。我的『祷告』属于哪一种？",
                         "Scripture's line is not about outward form but the heart: trusting obedience, or manipulative control. Which is my “prayer”?"),
                        ("『愿你的旨意成就』与『愿我的旨意成就』——这两种朝向，如何分辨了敬拜与巫术？",
                         "“Your will be done” versus “my will be done” — how do these two orientations separate worship from sorcery?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "护身符与咒语碗——魔法的物质证据",
            "title_en": "Amulets and Incantation Bowls — The Material Evidence",
            "steps": [
                step(S1, S1E,
                    p("哈拉里的研究建立在大量真实的考古物证之上。他详细描述了出土的护身符 (amulets)：刻在金属薄片上、卷起来佩戴的咒文，用于「医治」「退烧」「求爱」「保护」。还有美索不达米亚的「咒语碗」(incantation bowls)：陶碗内壁以螺旋形写满亚兰文的咒语，碗底常画着被「捆绑」「锁住」的女妖或邪魔，倒扣埋在房屋的门槛或角落，意在「困住」害人的灵。这些不是抽象的理论，而是普通人在疾病、恐惧、爱情、噩梦面前，伸手抓取的具体器物。哈拉里强调：操作这些的人绝非「无知愚昧」——他们是识字的、有知识的行家。",
                      "Harari's research rests on a wealth of real archaeological evidence. He describes excavated amulets in detail: spells inscribed on thin metal sheets, rolled up and worn, “for healing,” “for fever that burns and does not stop,” “for love,” “for protection.” And the Mesopotamian incantation bowls: clay bowls written inside in a spiral of Aramaic spells, often with a “bound,” “chained” she-demon drawn at the center, buried upside-down at a house's threshold or corners to “trap” a harming spirit. These are not abstract theories but concrete objects ordinary people reached for in the face of sickness, fear, love, and nightmares. Harari stresses that those who made them were no “ignorant simpletons” — they were literate, knowledgeable experts.")),
                step(S2, S2E,
                    bq("「雅各家啊，来吧!我们在耶和华的光明中行走……你们充满了东方的风俗，作观兆的，像非利士人一样。」",
                       "“Come, descendants of Jacob, let us walk in the light of the LORD... They are full of superstitions from the East; they practice divination like the Philistines.”",
                       "《以赛亚书》2:5-6 · Isaiah 2:5-6")),
                step(S3, S3E,
                    p("<strong>קָמֵעַ · kame'a</strong>——「护身符」。这个词至今仍是希伯来语里「护身符」的常用词。护身符的逻辑是：把一段文字「装」起来佩戴，以为这文字本身就能挡灾、退病、招福。这里藏着一个深刻的属灵陷阱——把神圣的<em>话语</em>当作一件有自动功效的<em>物件</em>。值得注意的是，圣经确实命令以色列把神的话「系在手上为记号，戴在额上为经文」(申 6:8)，并写在门框上 (mezuzah)。但圣经的本意是<em>记念与顺服</em>——让神的话提醒人去爱神、行神的道；而护身符的逻辑，却悄悄把它扭曲成<em>功效与操控</em>——仿佛佩戴文字本身就能驱动一种力量。同样的字，朝向不同，便分出了敬拜与迷信。",
                      "<strong>קָמֵעַ · kame'a</strong> — “amulet.” The word is still the ordinary Hebrew word for “amulet” today. The logic of an amulet is to “package” a piece of text and wear it, as if the text itself could ward off disaster, drive out illness, draw good fortune. Here lies a deep spiritual trap — treating a holy <em>word</em> as an <em>object</em> with automatic power. Notably, Scripture does command Israel to bind God's words “as a sign on your hand and on your forehead” (Deut 6:8) and write them on the doorpost (mezuzah). But Scripture's intent is <em>remembrance and obedience</em> — God's word prompting a person to love God and walk in his ways; whereas the amulet's logic quietly twists it into <em>efficacy and control</em> — as if wearing the text itself drives a power. The same words, differently oriented, divide worship from superstition.")),
                step(S4, S4E,
                    p("这一课对今天的信徒是一面镜子。我们或许不戴亚兰文护身符，但「把神圣之物当作有自动功效的护符」这一冲动，从未消失：把十字架当幸运符、把某节经文当「保平安」的咒、把某种祷告词当成「只要照念就灵验」的公式。圣经的回应一以贯之：能保护、医治、拯救的，从来不是物件或文字本身，而是那位<em>活着的神</em>。「耶和华的名是坚固台，义人奔入便得安稳」(箴 18:10)——我们的避难所是一位<em>位格</em>，不是一道符咒。把信靠从「物」挪回到「神」，正是这一课的功课。",
                      "This lesson is a mirror for believers today. We may not wear Aramaic amulets, but the impulse to treat a holy thing as an automatic charm never died: a cross as a lucky token, a certain verse as a “safety” spell, a prayer formula as “just recite it and it works.” Scripture's answer is consistent: what protects, heals, and saves is never the object or the words themselves, but the <em>living God</em>. “The name of the LORD is a fortified tower; the righteous run to it and are safe” (Prov 18:10) — our refuge is a <em>person</em>, not a charm. To move trust back from “the thing” to “God himself” is the work of this lesson.")),
                step(S5, S5E,
                    ul(
                        ("我是否曾把某节经文、某个十字架、某句祷告词，当成『只要照做就灵验』的护符？",
                         "Have I ever treated a verse, a cross, or a prayer phrase as a charm that “works if I just do it right”?"),
                        ("圣经命令把神的话系在手上、写在门框上，用意是『记念顺服』。我对神的话，是记念，还是当护符？",
                         "Scripture commands binding God's words on the hand and doorpost, meaning “remembrance and obedience.” Is God's word to me a remembrance, or a charm?"),
                        ("『耶和华的名是坚固台』——我真正的避难所，是一位活着的神，还是某件让我安心的『属灵物件』？",
                         "“The name of the LORD is a fortified tower” — is my real refuge a living God, or some “spiritual object” that makes me feel safe?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "召唤天使——《奥秘之书》与「使役」的逻辑",
            "title_en": "Adjuring Angels — Sefer ha-Razim and the Logic of Command",
            "steps": [
                step(S1, S1E,
                    p("哈拉里研究的核心文献之一，是《奥秘之书》(Sefer ha-Razim，「众秘密之书」)。这类「指导手册」式的文献，列出了层层天界、各级天使的名字，并教人如何「使役」(adjure) 这些天使去完成各种目的——医治、得胜、求爱、知未来。其内在逻辑是惊人的：人不是<em>祈求</em>天使，而是凭着知道正确的名字与公式，去<em>命令</em>、<em>驱使</em>天使。哈拉里指出，这种「魔法」自认是一门<em>知识</em>与<em>技术</em>：只要掌握了正确的「秘密」（razim），就能调动属灵的层级为己所用。",
                      "One of Harari's central texts is <em>Sefer ha-Razim</em> (“the Book of Mysteries / Secrets”). These “instructional” treatises list tiered heavens and ranks of angels by name, and teach how to “adjure” those angels to accomplish various aims — healing, victory, love, knowledge of the future. Its inner logic is striking: a person does not <em>petition</em> the angels but, by knowing the right names and formulas, <em>commands</em> and <em>compels</em> them. Harari notes that this “magic” understood itself as a <em>knowledge</em> and a <em>technique</em>: master the correct “secrets” (<em>razim</em>), and you could mobilize the spiritual hierarchy for your own use.")),
                step(S2, S2E,
                    bq("「不可拜它们，也不可事奉它们……只要敬畏耶和华，专心诚实地事奉祂。」",
                       "“Do not worship them or serve them... But be sure to fear the LORD and serve him faithfully with all your heart.”",
                       "《撒母耳记上》12:21, 24 · 1 Samuel 12:21, 24")),
                step(S3, S3E,
                    p("<strong>הַשְׁבָּעָה · hashba'ah</strong>——「使役、起誓召唤、以誓言束缚」。它的字根与「七」(sheva) 及「起誓」(shava) 相关，本义近于「以神圣之誓约束某存有，迫其听命」。这正是「召唤天使」之术的属灵命脉，也正是它与圣经信仰<em>根本对立</em>之处。在圣经里，天使是神的<em>仆役</em>，「听从祂命令、成全祂旨意」(诗 103:20)——他们只听从神，不听从人。人若想凭「正确的名字与公式」去<em>使役</em>天使，等于僭夺了唯独属于神的权柄，把受造的灵体当作可被人调遣的工具。这不是信靠，而是一种披着属灵外衣的、对神主权的篡夺。",
                      "<strong>הַשְׁבָּעָה · hashba'ah</strong> — “adjuration; binding by oath; compelling invocation.” Its root relates to “seven” (<em>sheva</em>) and “to swear” (<em>shava</em>), with a sense close to “binding a being by a sacred oath to make it obey.” This is the spiritual lifeblood of “angel-adjuration” — and exactly where it stands in <em>fundamental opposition</em> to biblical faith. In Scripture, angels are God's <em>servants</em>, “who do his bidding, who obey his word” (Ps 103:20) — they obey God, not humans. To “adjure” angels by “the right names and formulas” is to usurp an authority belonging to God alone, treating created spirits as tools at human command. This is not trust but a usurpation of God's sovereignty, dressed in spiritual clothes.")),
                step(S4, S4E,
                    p("这一课揭示了魔法与信仰之间最关键的分水岭：<em>命令</em>还是<em>祈求</em>。魔法的世界观说：「我若掌握了正确的知识与公式，就能<em>命令</em>属灵力量。」圣经的世界观说：「我只能谦卑地<em>祈求</em>那位至高的主，并把结果交托给祂的智慧与良善。」前者把人放在中心，把属灵世界当成可操控的机器；后者把神放在中心，把人放在受造者谦卑信靠的位置。请注意《撒母耳记上》12 章的对比：撒母耳禁止百姓去追随「虚无、不能救人」的事物，转而呼召他们「专心诚实地事奉耶和华」。真信仰的核心动作，永远是<em>事奉神</em>，而非<em>差遣神</em>（或祂的天使）。",
                      "This lesson reveals the most decisive watershed between magic and faith: <em>command</em> or <em>petition</em>. The magical worldview says, “If I master the right knowledge and formulas, I can <em>command</em> spiritual powers.” The biblical worldview says, “I can only humbly <em>ask</em> the Most High Lord, and entrust the outcome to his wisdom and goodness.” The first puts the human at the center and treats the spiritual world as a controllable machine; the second puts God at the center and the human in the place of a creature's humble trust. Note the contrast in 1 Samuel 12: Samuel forbids the people to chase “useless idols that cannot save” and calls them instead to “serve the LORD faithfully with all your heart.” The core move of true faith is always to <em>serve God</em>, never to <em>dispatch God</em> (or his angels).")),
                step(S5, S5E,
                    ul(
                        ("魔法是『命令』属灵力量，信仰是『祈求』那位主。我的祷告，更接近哪一种姿态？",
                         "Magic “commands” spiritual powers; faith “petitions” the Lord. Which posture is my prayer closer to?"),
                        ("天使是『听从神命令』的仆役。我是否曾想用『正确的方法』去操控属灵的结果，而非交托给神？",
                         "Angels are servants who “obey God's word.” Have I ever tried to control a spiritual outcome by “the right method,” instead of entrusting it to God?"),
                        ("真信仰的核心是『事奉神』，而非『差遣神』。我的属灵生活里，谁在中心？",
                         "The core of true faith is to “serve God,” not to “dispatch God.” In my spiritual life, who is at the center?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "《摩西之剑》与「名」的能力",
            "title_en": "The Sword of Moses and the Power of the Name",
            "steps": [
                step(S1, S1E,
                    p("哈拉里讨论的另一部重要文献，是《摩西之剑》(Harba de-Moshe，「摩西之剑」)——一长串令人眼花缭乱的「圣名」(holy names) 与咒方的汇编。在这个世界里，「名字」被视为蕴含能力的核心：知道了某个天使、某个力量、乃至神的某个「秘名」的正确发音与写法，就被认为掌握了驱动它的钥匙。整套魔法体系，几乎都建立在「名字即能力」这一信念之上——掌握正确的「名」，便掌握了相应的属灵力量。",
                      "Another major text Harari discusses is the <em>Harba de-Moshe</em> (“the Sword of Moses”) — a dizzying compilation of “holy names” and spell-recipes. In this world, the “name” is held to contain power at its core: to know the correct pronunciation and spelling of an angel's name, a power's name, even one of God's “secret names,” was thought to grasp the key to driving it. Nearly the whole magical system rests on the belief that “the name is power” — master the right “name,” and you master the corresponding spiritual force.")),
                step(S2, S2E,
                    bq("「不可妄称耶和华你神的名；因为妄称耶和华名的，耶和华必不以他为无罪。」",
                       "“You shall not misuse the name of the LORD your God, for the LORD will not hold anyone guiltless who misuses his name.”",
                       "《出埃及记》20:7 · Exodus 20:7")),
                step(S3, S3E,
                    p("<strong>הַשֵּׁם · HaShem</strong>——「那名」。出于敬畏，犹太人至今不直呼神的圣名，而称之为 <em>HaShem</em>（「那名」）。这份敬畏极其美好，也极其重要——因为它正站在与魔法相反的一端。魔法想要<em>占有</em>并<em>使用</em>神的名作为能力的工具；而圣经的敬畏，是因着神的名太过圣洁，人当<em>俯伏敬拜</em>，而非<em>调用操控</em>。第三诫禁止「妄称（白白使用、滥用）耶和华的名」——而把神的名当作咒语公式去驱动力量，正是这一禁令所针对的核心。神的名不是一把可供人挥舞的「剑」，乃是当受敬畏的圣洁本身。",
                      "<strong>הַשֵּׁם · HaShem</strong> — “the Name.” Out of reverence, Jews to this day do not pronounce God's holy name but call it <em>HaShem</em> (“the Name”). This reverence is beautiful and vital — for it stands at the opposite pole from magic. Magic seeks to <em>possess</em> and <em>use</em> God's name as a tool of power; the reverence of Scripture, by contrast, is that the name is so holy that one must <em>fall down and worship</em>, not <em>invoke and control</em>. The third commandment forbids “misusing (taking in vain, abusing) the name of the LORD” — and using God's name as a spell-formula to drive power is precisely what that prohibition targets. God's name is not a “sword” for a person to wield, but holiness itself, to be revered.")),
                step(S4, S4E,
                    p("圣经对「名」的看法，与魔法截然不同却同样深刻：名字确实蕴含真实的能力——但那能力属于<em>名字的主人</em>，而非操控名字的术士。当摩西在荆棘火中问神的名，神回答「我是自有永有的」(出 3:14)——这名启示的是神<em>不可被掌控</em>的主权，而非一道可被念诵的公式。新约把这一点带到顶峰：「神将祂升为至高，又赐给祂那超乎万名之上的名，叫一切……无不屈膝」(腓 2:9-10)。请注意：在耶书亚的名里得能力，从来不是「掌握正确发音以驱动力量」，而是<em>降服</em>于那名所代表的主、信靠祂、奉祂的旨意祈求。前者是巫术，后者是敬拜。",
                      "Scripture's view of “the name” differs from magic's yet is just as profound: a name does carry real power — but that power belongs to <em>the one who bears the name</em>, not to the sorcerer who manipulates it. When Moses asks God's name at the burning bush, God answers “I AM WHO I AM” (Exod 3:14) — a name that reveals God's <em>uncontrollable</em> sovereignty, not a recitable formula. The New Testament brings this to its summit: “God exalted him and gave him the name that is above every name, that at the name of Yeshua every knee should bow” (Phil 2:9-10). Note: to find power in the name of Yeshua is never “mastering the right pronunciation to drive a force,” but <em>surrendering</em> to the Lord that name represents, trusting him, asking according to his will. The first is sorcery; the second is worship.")),
                step(S5, S5E,
                    ul(
                        ("犹太人以 HaShem(『那名』)称呼神，出于敬畏。我对神的名，是敬畏，还是当成可调用的工具？",
                         "Jews call God <em>HaShem</em> (“the Name”) out of reverence. Is God's name to me an object of reverence, or a tool to invoke?"),
                        ("奉耶书亚的名祈求，是『降服于祂』还是『掌握一道公式』？这个分别为何如此关键？",
                         "Praying in Yeshua's name — is it “surrendering to him” or “mastering a formula”? Why does that distinction matter so much?"),
                        ("名字的能力属于『名字的主人』，而非操控者。这如何改变我祷告时的心态？",
                         "A name's power belongs to “the one who bears it,” not the one who manipulates it. How does that change my heart in prayer?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "鬼魔与那看不见的领域",
            "title_en": "Demons and the Unseen Realm",
            "steps": [
                step(S1, S1E,
                    p("哈拉里的研究让一件事变得无可回避：晚期古代的犹太人，普遍相信一个真实、活跃、人口稠密的「看不见的领域」——其中有天使，也有鬼魔 (shedim)、害灵 (mazikin)、夜妖（如莉莉丝 Lilith）。咒语碗上画着被捆锁的女妖，护身符上写满抵御邪灵的咒文，这一切都见证：对那时的人而言，鬼魔不是迷信的隐喻，而是日常生活中真实的威胁——会致病、扰梦、害婴、攻击家庭。哈拉里作为历史学者，忠实地记录了这个被现代世俗心灵急于「祛魅」的属灵世界图景。",
                      "Harari's research makes one thing unavoidable: late-antique Jews widely believed in a real, active, densely populated “unseen realm” — peopled by angels, but also by demons (<em>shedim</em>), harming spirits (<em>mazikin</em>), and night-spirits (such as Lilith). The incantation bowls drawn with bound she-demons, the amulets covered with spells against evil spirits — all bear witness that, for people then, demons were no metaphor of superstition but a real, daily threat: causing sickness, disturbing sleep, harming infants, attacking households. As a historian, Harari faithfully records this picture of a spiritual world the modern secular mind is eager to “disenchant.”")),
                step(S2, S2E,
                    bq("「因我们并不是与属血气的争战，乃是与那些执政的、掌权的、管辖这幽暗世界的，以及天空属灵气的恶魔争战。」",
                       "“For our struggle is not against flesh and blood, but against the rulers, against the authorities, against the powers of this dark world and against the spiritual forces of evil in the heavenly realms.”",
                       "《以弗所书》6:12 · Ephesians 6:12")),
                step(S3, S3E,
                    p("<strong>שֵׁד · shed</strong>（鬼魔，复数 shedim）与 <strong>מַזִּיק · mazik</strong>（害灵，复数 mazikin）。圣经并不否认这个领域的真实——它只是<em>重新排定</em>了它的秩序。《申命记》32:17 说以色列「祭祀鬼魔 (shedim)，不是真神」；《诗篇》91 篇谈到「夜间的惊骇」「黑暗中行的瘟疫」。圣经从不假装鬼魔不存在；它郑重地承认那看不见的争战是真实的。但与魔法世界观的根本不同在于：圣经从不教人用咒语、护符或召唤去<em>对付</em>鬼魔——它教人<em>投靠</em>那位创造并掌管万灵的至高神。面对害灵，圣经的回答不是更强的咒术，而是「住在至高者隐密处的，必住在全能者的荫下」(诗 91:1)。",
                      "<strong>שֵׁד · shed</strong> (demon, pl. <em>shedim</em>) and <strong>מַזִּיק · mazik</strong> (harming spirit, pl. <em>mazikin</em>). Scripture does not deny the reality of this realm — it simply <em>reorders</em> it. Deuteronomy 32:17 says Israel “sacrificed to demons (<em>shedim</em>), not to God”; Psalm 91 speaks of “the terror of night” and “the pestilence that stalks in darkness.” Scripture never pretends demons do not exist; it soberly acknowledges that the unseen struggle is real. But the fundamental difference from the magical worldview is this: Scripture never teaches people to <em>handle</em> demons with spells, charms, or invocations — it teaches them to <em>take refuge</em> in the Most High God who created and rules all spirits. Against harming spirits, Scripture's answer is not a stronger spell, but “whoever dwells in the shelter of the Most High will rest in the shadow of the Almighty” (Ps 91:1).")),
                step(S4, S4E,
                    p("这一课向两种极端同时发出警告。一端是现代世俗主义：它干脆否认那看不见的领域，把一切都「祛魅」成心理或物理现象——圣经会说这太天真了，那争战是真实的。另一端正是哈拉里所研究的魔法世界：它过度迷恋那看不见的领域，终日忙于用护符与咒语去抵御、操控群灵——圣经会说这是另一种被捆绑，是把目光从神挪到了鬼魔身上。圣经走的是第三条路：清醒地承认黑暗权势的真实，却把全部的信靠与目光定睛于那位早已得胜的主。我们不靠咒术对抗黑暗，而是「靠主，倚赖祂的大能大力，穿戴神所赐的全副军装」(弗 6:10-11)。",
                      "This lesson warns against two extremes at once. One is modern secularism: it simply denies the unseen realm, “disenchanting” everything into the psychological or physical — Scripture would call this naïve; the struggle is real. The other is exactly the magical world Harari studies: it is over-fascinated with the unseen realm, forever busy warding off and controlling spirits with charms and spells — Scripture would call this another bondage, eyes moved from God onto the demons. Scripture walks a third road: soberly acknowledging the reality of dark powers, yet fixing all trust and gaze on the Lord who has already triumphed. We do not fight darkness with sorcery, but are “strong in the Lord and in his mighty power,” putting on “the full armor of God” (Eph 6:10-11).")),
                step(S5, S5E,
                    ul(
                        ("我更靠近哪种极端：否认看不见的争战（世俗主义），还是过度迷恋、惧怕属灵权势（魔法心态）？",
                         "Which extreme am I closer to: denying the unseen struggle (secularism), or being over-fascinated with and fearful of spiritual powers (a magical mindset)?"),
                        ("圣经承认鬼魔真实，却教人『投靠』神而非『对付』鬼魔。这如何改变我面对属灵黑暗时的反应？",
                         "Scripture grants demons are real yet teaches us to “take refuge” in God rather than “handle” demons. How does that change my response to spiritual darkness?"),
                        ("面对惧怕，我是去寻找『更强的方法』，还是去『投靠至高者的隐密处』？",
                         "Facing fear, do I look for “a stronger method,” or take “refuge in the shelter of the Most High”?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "言语能成事——咒语与「话语的能力」",
            "title_en": "Words That Do Things — Spells and the Power of Speech",
            "steps": [
                step(S1, S1E,
                    p("哈拉里有一章专门借用语言哲学家奥斯汀的「言语行为理论」(speech act theory) 来分析咒语——书的标题灵感正来自奥斯汀的名作《如何以言行事》。核心洞见是：有些话语不只是「描述」世界，而是试图<em>促成</em>某事发生。咒语正是如此：它不是在「陈述」，而是在「施行」——说出（或写下）正确的字句，被认为本身就能<em>改变现实</em>。哈拉里指出，魔法对「话语」抱有一种极强的信念：被恰当地说出或写下的词，具有客观的、近乎自动的效力。这是整个魔法世界观的引擎。",
                      "Harari devotes a chapter to analyzing spells through the philosopher J. L. Austin's “speech act theory” — the book's title nods to Austin's famous <em>How to Do Things with Words</em>. The core insight: some utterances do not merely “describe” the world but attempt to <em>bring something about</em>. A spell is just so: not a “statement” but a “performance” — speaking (or writing) the right words is thought to itself <em>change reality</em>. Harari notes that magic holds an intense belief about “words”: a term, properly spoken or written, has an objective, almost automatic efficacy. This is the engine of the whole magical worldview.")),
                step(S2, S2E,
                    bq("「神说：要有光，就有了光……诸天藉耶和华的命而造；万象藉祂口中的气而成。」",
                       "“And God said, ‘Let there be light,’ and there was light... By the word of the LORD the heavens were made, their starry host by the breath of his mouth.”",
                       "《创世记》1:3 · 《诗篇》33:6 · Genesis 1:3; Psalm 33:6")),
                step(S3, S3E,
                    p("<strong>דָּבָר · davar</strong>——同时意为「话语」与「事物」。希伯来语用同一个词指「言」与「实」，本身就道出一个深刻的真理：在神那里，说话与成事是合一的。「神说：要有光，就有了光。」这是宇宙间最有能力的「言语行为」——而它正属于神。魔法对「话语能成事」的直觉，并非全然错谬；错的是它<em>把这能力的源头错置了</em>：以为能力在于「正确的字句与公式」本身，仿佛话语是一台只要按对按钮就会运转的机器。圣经的真理是：唯有<em>神</em>的话 (devar Adonai) 带着创造与成就的大能；人的话之所以有分量，是因为它回应、传递、顺服神的话，而非因为它本身是一道可被操控的咒。",
                      "<strong>דָּבָר · davar</strong> — meaning both “word” and “thing.” That Hebrew uses one word for “speech” and “reality” itself voices a deep truth: in God, to speak and to accomplish are one. “God said, ‘Let there be light,’ and there was light.” This is the most powerful “speech act” in the universe — and it belongs to God. Magic's intuition that “words do things” is not wholly wrong; what is wrong is that it <em>misplaces the source</em> of that power: imagining the power lies in “the right words and formulas” themselves, as if speech were a machine that runs once the right button is pressed. Scripture's truth is that only <em>God's</em> word (<em>devar Adonai</em>) carries the power to create and accomplish; human words have weight insofar as they answer, carry, and obey God's word — not because they are a controllable spell in themselves.")),
                step(S4, S4E,
                    p("这一课邀请我们重新省察自己「使用话语」的方式。基督徒的祷告，绝不是基督教版本的咒语——它的能力<em>从不</em>在于「念对了某个公式、某句话、某个次数」。把祷告变成「只要这样说、说够遍数，神就必须照办」的技术，正是悄悄滑向魔法的逻辑：把信靠的祈求，扭曲成了对神的操控。圣经里真正有能力的话语，是<em>神</em>的话，以及人对神的话语<em>谦卑的回应与宣告</em>。我们宣讲、祷告、宣告神的应许，能力不在我们的措辞，而在那位说话的神。我们说话，是因信靠祂；不是为了驱使祂。",
                      "This lesson invites us to re-examine how we “use words.” Christian prayer is never a Christian version of a spell — its power lies <em>never</em> in “reciting the right formula, the right phrase, the right number of times.” Turning prayer into a technique of “say it this way, enough times, and God must comply” is exactly the quiet slide into magic's logic: twisting a trusting petition into a manipulation of God. The truly powerful words in Scripture are <em>God's</em> words, and a person's <em>humble response and proclamation</em> of God's word. When we preach, pray, and proclaim God's promises, the power is not in our phrasing but in the God who speaks. We speak because we trust him; not to compel him.")),
                step(S5, S5E,
                    ul(
                        ("我的祷告里，是否藏着一种『只要念对了、念够了，神就必须照办』的咒语式逻辑？",
                         "Is there a spell-like logic hidden in my prayers — “if I say it right, enough times, God must comply”?"),
                        ("『神说，就有了』——宇宙中最有能力的话语属于神。这如何让我对自己话语的能力保持谦卑？",
                         "“God said, and it was” — the most powerful words in the universe belong to God. How does that keep me humble about the power of my own words?"),
                        ("我宣告神的应许时，把能力寄托在我的『措辞技巧』上，还是寄托在那位说话的神身上？",
                         "When I proclaim God's promises, do I rest the power on my “wording technique,” or on the God who speaks?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "妥拉划下的那条线——为什么神禁止邪术",
            "title_en": "The Line the Torah Draws — Why God Forbids Sorcery",
            "steps": [
                step(S1, S1E,
                    p("哈拉里诚实地指出一个张力：他所研究的这些「魔法」，是由<em>犹太人</em>、用<em>犹太</em>的圣名与传统、在<em>犹太</em>群体中流传的——然而妥拉本身却极其严厉地禁止邪术。这意味着：圣经的禁令，针对的从来不是某个外邦的、遥远的现象，而恰恰是会在神自己子民中间滋生的真实试探。哈拉里也敏锐地观察到，古代犹太社会内部一直存在一场关于「界线」的争论：哪些做法是被许可的「妙方」(segulah)、是敬虔，哪些是被禁止的「邪术」(kishuf)。这条线，社会争论不休——但妥拉早已郑重地划下。",
                      "Harari honestly notes a tension: the “magic” he studies was practiced by <em>Jews</em>, using <em>Jewish</em> holy names and traditions, circulating within <em>Jewish</em> communities — yet the Torah itself forbids sorcery in the strongest terms. This means Scripture's prohibition was never aimed at some foreign, distant phenomenon, but precisely at a real temptation that would arise among God's own people. Harari also keenly observes that ancient Jewish society carried an ongoing argument about the “line”: which practices were permitted <em>segulah</em> (remedy) and devotion, and which were forbidden <em>kishuf</em> (sorcery). Society argued the line endlessly — but the Torah had already drawn it solemnly.")),
                step(S2, S2E,
                    bq("「你要在耶和华你的神面前作完全人。你所要赶出的那些国民，都听信观兆的和占卜的;至于你，耶和华你的神从来不许你这样行。」",
                       "“You must be blameless before the LORD your God. The nations you will dispossess listen to those who practice sorcery or divination. But as for you, the LORD your God has not permitted you to do so.”",
                       "《申命记》18:13-14 · Deuteronomy 18:13-14")),
                step(S3, S3E,
                    p("<strong>תָּמִים · tamim</strong>——「完全、纯全、毫无保留地属于神」。这是《申命记》18 章在列举一长串被禁的邪术之后，给以色列的总命令：「你要在耶和华你的神面前作 <em>tamim</em>（完全人）。」这个词是理解整条禁令的钥匙。神禁止占卜邪术，核心不在于「祂小气地不让人接触某些有趣的能力」，而在于：邪术的本质是<em>分心二意</em>——是在神之外，另寻一个可供操控的能力来源，为自己的未来与安危「上一道额外的保险」。而 <em>tamim</em> 要求的，是<em>毫无保留、不留后门</em>地单单信靠神。占卜问的是「我能否操控未来」；<em>tamim</em> 说的是「我把未来全然交在祂手中」。这条线，分别了操控与信靠、二心与专一。",
                      "<strong>תָּמִים · tamim</strong> — “blameless, whole, belonging to God without reserve.” This is the summary command Deuteronomy 18 gives Israel after listing a long catalog of forbidden sorceries: “You must be <em>tamim</em> (blameless) before the LORD your God.” This word is the key to the whole prohibition. God forbids divination and sorcery not because “he stingily withholds access to some interesting powers,” but because the essence of sorcery is a <em>divided heart</em> — seeking, outside of God, another controllable source of power to take out “extra insurance” for one's future and safety. <em>Tamim</em> demands a trust in God that is <em>without reserve, with no back door</em>. Divination asks, “can I control the future?”; <em>tamim</em> says, “I place the future wholly in his hands.” This line divides control from trust, a divided heart from an undivided one.")),
                step(S4, S4E,
                    p("现在我们能看清，为什么妥拉对邪术的禁令如此严厉，而它对今天的我们又如此切身。神禁止邪术，是出于爱与忌邪的合一——祂不愿祂所爱的子民，把信靠分给一个虚假、且最终会捆绑人的能力来源。这条线今天依然锋利。我们或许不碰咒语碗，但「邪术之心」会以现代的形式回来：求签问卜、星座占星、为「掌控命运」而追逐的种种灵异技术，乃至把信仰本身降格为「让神听我的、按我意思办事」的工具。妥拉的呼召始终如一：<em>tamim</em>——完全地、不留后门地，单单信靠那位独一的真神。这不是剥夺，而是自由：从「必须自己操控一切」的重担里被释放出来。",
                      "Now we can see why the Torah's prohibition of sorcery is so severe — and why it is so personal for us today. God forbids sorcery out of a union of love and jealousy — he will not have his beloved people divide their trust toward a false power-source that ultimately enslaves. This line is still sharp today. We may not touch incantation bowls, but the “heart of sorcery” returns in modern forms: fortune-telling, horoscopes and astrology, the various occult techniques chased in order to “control fate,” even reducing faith itself into a tool to “make God listen to me and do things my way.” The Torah's call is constant: <em>tamim</em> — wholly, with no back door, trusting the one true God alone. This is not deprivation but freedom: release from the burden of “having to control everything myself.”")),
                step(S5, S5E,
                    ul(
                        ("邪术的本质是『二心』——在神之外另寻一个可操控的保险。我生命里有没有这样的『额外保险』？",
                         "The essence of sorcery is a “divided heart” — seeking a controllable insurance outside of God. Is there such “extra insurance” in my life?"),
                        ("『tamim(完全人)』要求不留后门地单单信靠神。我对神的信靠，有没有留着某扇『后门』？",
                         "<em>Tamim</em> (blameless) demands trust in God with no back door. Does my trust in God keep some “back door” open?"),
                        ("今天『邪术之心』的现代形式可能是什么（占星、求签、操控命运的技术）？它如何悄悄分走我的信靠？",
                         "What are the modern forms of the “heart of sorcery” today (astrology, fortune-telling, techniques to control fate)? How do they quietly divide my trust?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "一个更大的名——以弗所的火与得胜的主",
            "title_en": "A Greater Name — The Fire at Ephesus and the Lord Who Triumphs",
            "steps": [
                step(S1, S1E,
                    p("哈拉里所描绘的那个充满护符与咒语的世界，并非一个遥远抽象的过去——它正是新约信仰诞生时所处的真实环境。使徒行传记载了福音与这个魔法世界的几次正面相遇：行邪术的西门想用钱买使徒的能力，被严厉斥责（徒 8）；术士以吕马（巴耶稣）抵挡福音，被击打眼瞎（徒 13）；在以弗所——古代魔法的重镇——士基瓦的七个儿子想盗用「耶稣」的名去赶鬼，反被恶鬼制伏、赤身逃走（徒 19）。而那一切的高潮是：以弗所许多行邪术的信了主，把价值连城的魔法书卷公开堆起来焚烧。福音来到，魔法的世界在那一位的名前崩塌了。",
                      "The world of charms and spells Harari paints is not a distant abstraction — it is the very environment in which the New Testament faith was born. Acts records several head-on encounters between the Gospel and this magical world: Simon the sorcerer tries to buy the apostles' power with money and is sternly rebuked (Acts 8); the magician Elymas (Bar-Jesus) opposes the Gospel and is struck blind (Acts 13); at Ephesus — a great center of ancient magic — the seven sons of Sceva try to misuse the name “Jesus” to drive out a demon and are instead overpowered and flee naked (Acts 19). And the climax: many sorcerers at Ephesus came to faith and publicly burned their priceless magic scrolls in a heap. The Gospel arrived, and the world of magic collapsed before that one Name.")),
                step(S2, S2E,
                    bq("「平素行邪术的，也有许多人把书拿来，堆积在众人面前焚烧……主的道大大兴旺,而且得胜，就是这样。」",
                       "“A number who had practiced sorcery brought their scrolls together and burned them publicly... In this way the word of the Lord spread widely and grew in power.”",
                       "《使徒行传》19:19-20 · Acts 19:19-20")),
                step(S3, S3E,
                    p("<strong>שֵׁם יֵשׁוּעַ · Shem Yeshua</strong>——「耶书亚的名」。士基瓦众子的故事，是整份指南最锋利的对照。他们想把「耶稣的名」当成一道<em>更强的咒语</em>——一个可以盗用、可以驱动的能力公式。结果恶鬼回答：「耶稣我认识，保罗我也知道，你们却是谁呢？」(徒 19:15) 这句话道破了魔法与信仰的全部分野：在耶书亚的名里真正的能力，<em>从不</em>属于那些想<em>操控</em>这名的人，<em>只</em>属于那些<em>降服</em>于这名所代表的主、与祂有真实关系的人。同一个名，对术士是空洞的咒语，对门徒是又真又活的主。能力从不在「名的发音」，而在「与那名的主人的关系」。",
                      "<strong>שֵׁם יֵשׁוּעַ · Shem Yeshua</strong> — “the name of Yeshua.” The story of Sceva's sons is the sharpest contrast in the whole guide. They tried to use “the name of Jesus” as a <em>stronger spell</em> — a power-formula to be borrowed and driven. The demon answered: “Jesus I know, and Paul I know about, but who are you?” (Acts 19:15). That line lays bare the entire divide between magic and faith: the real power in the name of Yeshua belongs <em>never</em> to those who would <em>control</em> the name, but <em>only</em> to those who <em>surrender</em> to the Lord it represents and have a real relationship with him. The same name is an empty spell to the sorcerer and a living Lord to the disciple. The power was never in “the pronunciation of the name,” but in “relationship with the One who bears it.”")),
                step(S4, S4E,
                    p("这是整份指南的终点，也是它的整个目的。我们透过哈拉里的学术之窗，看见了一个充满护符、咒语、召唤与惧怕的真实世界——并且一次次地，圣经把我们引向一条截然不同的路：不是用更强的咒术去操控属灵的力量，而是降服于那位早已得胜的主。以弗所信徒焚书的那堆火，是这一切最美的图画：当人真正认识了那位至高的主，他便不再需要一切属灵的「额外保险」——他可以把它们全都烧掉，因为他寻见了那位他在咒语里一直徒劳寻找的、又真又活的神。愿这八堂课，使你在一个仍旧充满惧怕与操控的世代里，作一个 <em>tamim</em>（完全人）：不靠咒术，单靠那位名字超乎万名之上的主——耶书亚。",
                      "This is the end of the whole guide, and its entire purpose. Through Harari's scholarly window we have seen a real world full of charms, spells, invocations, and fear — and again and again, Scripture leads us to a wholly different road: not controlling spiritual powers with a stronger sorcery, but surrendering to the Lord who has already triumphed. The bonfire of the Ephesian believers' scrolls is the most beautiful picture of it all: when a person truly knows the Most High Lord, he no longer needs any spiritual “extra insurance” — he can burn it all, because he has found the living God he was vainly seeking in the spells. May these eight lessons make you, in an age still full of fear and control, a <em>tamim</em> — one made whole: not trusting in sorcery, but in the Lord whose name is above every name — Yeshua.")),
                step(S5, S5E,
                    ul(
                        ("士基瓦众子想盗用『耶稣的名』当咒语，恶鬼却说『你们是谁?』。我与那名的主人，有真实的关系吗？",
                         "Sceva's sons tried to misuse “the name of Jesus” as a spell, but the demon asked “who are you?” Do I have a real relationship with the One who bears that name?"),
                        ("以弗所的信徒把魔法书卷烧掉。我生命里，有哪些属灵的『额外保险』需要被烧掉？",
                         "The Ephesian believers burned their magic scrolls. What spiritual “extra insurance” in my life needs to be burned?"),
                        ("在一个充满惧怕与操控的世代，『作完全人(tamim)、单靠耶书亚』对我具体意味着什么？",
                         "In an age full of fear and control, what does “being <em>tamim</em>, trusting Yeshua alone” concretely mean for me?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "向那名超乎万名之主的祝祷",
    "closing_title_en": "A Blessing to the Lord Whose Name Is Above Every Name",
    "closing_zh": "「愿耶和华向你仰脸，赐你平安。」<br/><br/>愿你看过那个充满护符与咒语的古代世界，<br/>就更深地领受圣经所划的那条线：<br/>不是操控，乃是信靠；<br/>不是咒术，乃是敬拜；<br/>不是差遣神，乃是事奉神。<br/><br/>愿你在一个仍旧惧怕、仍旧想掌控命运的世代里，<br/>作一个完全人 (tamim)——<br/>把一切属灵的『额外保险』都付之一炬，<br/>单单投靠那位至高者的隐密处，<br/>单单倚靠那名超乎万名之上的主——耶书亚。",
    "closing_en": "“The LORD lift up his countenance upon you, and give you peace.”<br/><br/>Having seen that ancient world full of charms and spells,<br/>may you receive more deeply the line Scripture draws:<br/>not control, but trust;<br/>not sorcery, but worship;<br/>not dispatching God, but serving him.<br/><br/>May you, in an age that still fears and still grasps to control its fate,<br/>be one made whole (tamim) —<br/>setting every spiritual “extra insurance” to the fire,<br/>taking refuge in the shelter of the Most High alone,<br/>trusting the Lord whose name is above every name — Yeshua.",
}

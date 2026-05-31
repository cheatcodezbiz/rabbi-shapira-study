# -*- coding: utf-8 -*-
"""Content module for study-divided-lives.html.

Cynthia Crane, *Divided Lives: The Untold Stories of Jewish-Christian Women
in Nazi Germany* (St. Martin's Press, 2000 / 2006).
"""

RHYTHM_ZH = """        <strong>① 作者说什么</strong>—— 用克兰自己的笔触概述这一章的见证；<br/>
        <strong>② 关键经文</strong>—— 一处与之共鸣的圣经；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，照亮这段历史；<br/>
        <strong>④ 基督徒视角</strong>—— 教会该如何聆听、如何悔改、如何记念；<br/>
        <strong>⑤ 诚实的提问</strong>—— 留给你与小组继续追问的问题。"""

RHYTHM_EN = """        <strong>① What the Author Says</strong> — the chapter's testimony in Crane's own frame;<br/>
        <strong>② Key Scripture</strong> — one biblical text that resonates with it;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that lights up the history;<br/>
        <strong>④ A Christian Lens</strong> — how the Church should listen, repent, and remember;<br/>
        <strong>⑤ Honest Questions</strong> — questions to keep asking, alone or in a group."""


def step(label_zh, label_en, *body):
    return {"label_zh": label_zh, "label_en": label_en, "body": list(body)}

def p(zh, en):
    return {"type": "p", "zh": zh, "en": en}

def bq(zh, en, cite=None):
    return {"type": "blockquote", "zh": zh, "en": en, "cite": cite}

def ul(*items):
    return {"type": "ul", "items": [{"zh": z, "en": e} for z, e in items]}

S1 = "① 作者说什么"
S1E = "① What the Author Says"
S2 = "② 关键经文"
S2E = "② Key Scripture"
S3 = "③ 希伯来语之眼"
S3E = "③ Through Hebrew Eyes"
S4 = "④ 基督徒视角"
S4E = "④ A Christian Lens"
S5 = "⑤ 诚实的提问"
S5E = "⑤ Honest Questions"


study = {
    "title_tag": "《分裂的人生》研习指南 · Divided Lives — Study Guide · 妥拉之光",
    "meta_desc": "A Christian study guide to Cynthia Crane's Divided Lives — eight bilingual lessons on the Jewish-Christian “Mischlinge” women of Nazi Germany, on divided identity, the law of blood, baptism that could not protect, faith under fire, and the duty to remember.",
    "og_title": "Divided Lives — A Christian Study Guide",
    "og_desc": "Eight bilingual lessons walking through Cynthia Crane's Divided Lives: the untold stories of Jewish-Christian women in Nazi Germany, read with Hebrew eyes.",
    "cover_alt": "Divided Lives — The Untold Stories of Jewish-Christian Women — Study Guide",
    "tagline_zh": "研习指南 · 见证与记念 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · Testimony &amp; Remembrance · 2026 · 5 · 31",
    "headline_zh": "《分裂的人生》<br/>研习指南",
    "headline_en": "Divided Lives<br/>A Christian Study Guide",
    "deck_zh": "八堂课程，倾听十位「混血儿」(Mischlinge) 女性的口述——她们受洗为基督徒，却被纳粹按血统判为犹太人。在被撕裂的身份里，我们听见一个关于余民、苦难与记念的故事。",
    "deck_en": "Eight lessons listening to ten “Mischlinge” women — baptized as Christians, yet branded Jews by Nazi blood-law. In their torn identities we hear a story about the remnant, about suffering, and about the duty to remember.",
    "byline_zh": "基于辛西娅·克兰 (Cynthia Crane)《分裂的人生——纳粹德国犹太裔基督徒女性不为人知的故事》(St. Martin's Press, 2000)",
    "byline_en": "Based on Divided Lives: The Untold Stories of Jewish-Christian Women in Nazi Germany by Cynthia Crane (St. Martin's Press, 2000)",
    "readtime_zh": "约 50 分钟通读",
    "readtime_en": "~50 min read-through",
    "book_url": "https://us.macmillan.com/books/9780312219536/dividedlives",
    "book_link_zh": "购买原书",
    "book_link_en": "Get the Book",
    "cta_url": "https://us.macmillan.com/books/9780312219536/dividedlives",
    "cta_zh": "购买《分裂的人生》原书 · St. Martin's Press",
    "cta_en": "Get the Book — Divided Lives · St. Martin's Press",

    "lead_zh": "这份指南不是要替你「读完」辛西娅·克兰 (Cynthia Crane) 的《分裂的人生》，而是陪你慢慢地、带着敬畏地读它。克兰是一位美国学者，她的祖父费利克斯·科恩 (Felix Cohn) 是汉堡的监狱医生，因「犹太血统」在 1938 年被吊销行医执照、逃往美国。多年后，克兰带着富布赖特奖学金回到汉堡，在档案馆里翻出祖母为了保住祖父的听诊器而写给盖世太保的信——那一刻，她意识到自己身份里「缺失的那一块」。于是她访谈了十位「混血儿」(Mischlinge) 女性：她们大多在路德宗或天主教里长大、受过洗，却在某一天被告知自己「是犹太人」。这本书写的，是那些「夹在所有椅子之间 (zwischen allen Stühlen)」的人。",
    "lead_en": "This guide is not a shortcut around Cynthia Crane's <em>Divided Lives</em> — it is a companion for reading it slowly, with reverence. Crane is an American scholar whose grandfather, Felix Cohn, was a prison doctor in Hamburg until his medical license was revoked in 1938 for “Jewish blood” and he fled to the United States. Years later, on a Fulbright in Hamburg, Crane sat in the state archives reading the letters her grandmother had to write to the Gestapo just to keep her husband's stethoscope — and felt the size of what had been missing from her own identity. So she interviewed ten <em>Mischlinge</em> women: most raised and baptized Lutheran or Catholic, who one day were told they “were Jewish.” This is a book about people left <em>zwischen allen Stühlen</em> — straddling every chair, belonging to none.",

    "intro": [
        p("克兰用「混血儿」(Mischlinge)——希特勒用来称呼「半犹太人」的贬义词，意为「杂种」「混种」——来命名这群人。在纳粹的种族法里，一个人若有三位犹太祖父母便是「完全的犹太人」；有两位是「一级混血」，一位是「二级混血」。历史学家估计，除犹太人本身之外，约有近四十万人因为是犹太人的配偶、子女或孙辈而受迫害。这本书，就是写给这群「被遗忘的受害者」的。",
          "Crane uses Hitler's own derogatory word — <em>Mischlinge</em>, “half-breeds,” “hybrids” — to name these people. Under the racial laws, a person with three Jewish grandparents was a “full Jew”; two made you a “first-degree” Mischling, one a “second-degree.” Historians estimate that, apart from Jews themselves, nearly 400,000 people were persecuted simply for being the spouses, children, or grandchildren of Jews. This is a book for those forgotten victims."),
        p("本指南共 <strong>八堂课</strong>，沿着书的两篇导论（「灵」与「法」）和女性们的故事推进。每一堂都包含五个部分：",
          "The guide is structured as <strong>eight lessons</strong>, following the book's two framing essays (“The Spirit” and “The Law”) and the women's stories. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句提醒：这是一本关于大屠杀 (Shoah) 边缘地带的书。请慢慢读，常常停下来祷告。聆听本身，就是一种敬意。",
          "A word of caution: this is a book about the edges of the Shoah. Read slowly, and stop often to pray. To listen carefully is itself an act of honor."),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "局外人——一段缺失的身份",
            "title_en": "The Outsider — A Missing Identity",
            "steps": [
                step(S1, S1E,
                    p("克兰以自己开篇。她说：「我不记得自己曾经感觉像别的、而不是一个『局外人』。」她的姓氏与祖母不同，父亲一被问起家族就脸色发白。直到祖母终于从地下室取出那本藏起来的回忆录，克兰才开始把自己「原本的针脚重新缝回去」。她的祖父科恩在一战中是战壕里的军医，得过两枚铁十字勋章，自认是德国人、是汉堡财政参议员的儿子——「他不认为自己是犹太人」。然而希特勒的法律不在乎他怎么认为。身份，被别人从外面强行接管了。",
                      "Crane opens with herself: “I do not remember ever feeling like anything but an outsider.” Her surname differed from her grandmother's; her father's face paled whenever the family was mentioned. Only when her grandmother finally retrieved a hidden memoir from the basement did Crane begin to “put back the original stitches” of her life. Her grandfather Cohn had been a front-line army doctor in WWI, decorated with two Iron Crosses, the son of a Hamburg finance senator — “he did not think of himself as a Jew.” But Hitler's law did not care what he thought. Identity was taken over from the outside.")),
                step(S2, S2E,
                    bq("「我在母腹中，你已认识我……我未成形的体质，你的眼早已看见了。」",
                       "“Your eyes saw my unformed body; all the days ordained for me were written in your book before one of them came to be.”",
                       "《诗篇》139:15-16 · Psalm 139:15-16")),
                step(S3, S3E,
                    p("<strong>גֵּר · ger</strong>——「寄居者」「外人」。《妥拉》三十六次命令以色列要爱<em>ger</em>，理由总是同一个：「因为你们在埃及地也作过寄居的」(《利未记》19:34)。圣经里的「局外人」从来不是一个要被消灭的范畴，而是一个要被<em>记念、被款待、被爱</em>的人。希特勒制造「局外人」是为了铲除他们；耶和华谈论「局外人」是为了保护他们。这两种「外人观」的距离，正是这本书全部的张力所在。",
                      "<strong>גֵּר · ger</strong> — “sojourner,” “stranger.” Thirty-six times the Torah commands Israel to love the <em>ger</em>, always with the same reason: “for you were strangers in the land of Egypt” (Leviticus 19:34). In Scripture the outsider is never a category to be eliminated but a person to be <em>remembered, welcomed, loved</em>. Hitler manufactured outsiders in order to erase them; the LORD speaks of the outsider in order to protect him. The distance between those two visions of the stranger is the whole tension of this book.")),
                step(S4, S4E,
                    p("基督徒读到这里应当心头一震：教会自己的历史里，也曾把犹太人当作「神学上的局外人」。克兰的家族受洗、上主日学、自认基督徒——可这一切都未能改变别人给他们贴的标签。当一个社会能够单凭「血统」就重写一个人的身份，我们看见的不只是政治之恶，更是一种属灵的僭越：人篡夺了唯有神才有的权柄——命名、认识、定义一个灵魂。",
                      "A Christian should feel a jolt here: the Church's own history once cast Jews as “theological outsiders.” Crane's family was baptized, attended Sunday school, considered themselves Christian — and none of it changed the label others fixed on them. When a society can rewrite a person's identity by “blood” alone, we are watching more than political evil; we are watching a spiritual usurpation — humans seizing a prerogative that belongs to God alone: to name, to know, and to define a soul.")),
                step(S5, S5E,
                    ul(
                        ("我的身份感，建立在什么之上？是别人的目光，还是神在我母腹中对我的认识？",
                         "On what is my sense of identity built — on the gaze of others, or on the God who knew me in the womb?"),
                        ("我所在的群体里，谁是『局外人』？我对待他们的方式，更像希特勒的法律，还是更像《利未记》的命令？",
                         "Who is the “outsider” in my community? Do I treat them more like Hitler's law, or more like the command of Leviticus?"),
                        ("克兰说她身份里『缺了一块』。我的属灵身份里，是否也有一块——犹太根源——长久缺失而我未曾察觉？",
                         "Crane felt a “missing piece” in her identity. Is there a piece — the Jewish root of my faith — long missing from mine, that I never noticed?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "那条把你判成犹太人的法律",
            "title_en": "The Law That Named You a Jew",
            "steps": [
                step(S1, S1E,
                    p("在题为「法」(The Law) 的第二篇导论里，克兰讲述 1935 年 9 月 15 日的《纽伦堡法》：它剥夺了「非德意志或亲缘血统」者的公民权，禁止犹太人与「纯种德国人」通婚或有性关系——违者即犯「种族玷污罪 (Rassenschande)」。一个人是「完全犹太人」若有三位犹太祖父母；「一级混血」有两位，「二级混血」有一位。被洗礼为基督徒的混血儿，数量是「自认犹太人 (Geltungsjuden)」的九倍。克兰写道，对这些女性而言，最深的创伤是「身份被接管」：突然被告知自己属于一个「犹太种族」，却「几乎不知道做犹太人意味着什么」。这是一场背叛。",
                      "In the second framing essay, “The Law,” Crane recounts the Nuremberg Laws of 15 September 1935: they stripped citizenship from anyone not of “German or related blood” and forbade Jews to marry or have relations with “pure Germans” — a crime of <em>Rassenschande</em>, “racial defilement.” Three Jewish grandparents made you a “full Jew”; two a “first-degree,” one a “second-degree” Mischling. Baptized-Christian Mischlinge outnumbered self-declared Jews nine to one. The deepest wound, Crane writes, was the <em>takeover of identity</em>: suddenly told they belonged to a “Jewish race” while having “little or no idea what being Jewish meant.” It was a betrayal.")),
                step(S2, S2E,
                    bq("「人是看外貌；耶和华是看内心。」",
                       "“The LORD does not look at the things people look at. People look at the outward appearance, but the LORD looks at the heart.”",
                       "《撒母耳记上》16:7 · 1 Samuel 16:7")),
                step(S3, S3E,
                    p("<strong>זֶרַע · zera</strong>——「种子」「后裔」「血脉」。纳粹用「血」(Blut) 来定义人，制造了一套伪科学的「种族」。圣经也常说「亚伯拉罕的<em>后裔 (zera)</em>」，但那是一条<em>应许</em>的血脉，不是一条<em>仇恨</em>的血脉。保罗甚至说：「那从肉身生的儿女不算神的儿女，惟独那应许的儿女才算是后裔 (zera)」(《罗马书》9:8)。纳粹把『血统』变成死刑判决；神却用『后裔』指向那位要赐福万族的弥赛亚。同一个概念，一个用来咒诅，一个用来祝福。",
                      "<strong>זֶרַע · zera</strong> — “seed,” “offspring,” “bloodline.” The Nazis defined people by <em>Blut</em>, inventing a pseudo-scientific “race.” Scripture, too, speaks often of “the <em>seed (zera)</em> of Abraham” — but it is a line of <em>promise</em>, not of hatred. Paul even says, “it is not the children by physical descent who are God's children, but the children of the promise who are regarded as the seed” (Romans 9:8). The Nazis turned bloodline into a death sentence; God uses “seed” to point to the Messiah who blesses all nations. The same idea — wielded by one to curse, by the other to bless.")),
                step(S4, S4E,
                    p("教会不能假装这套「血统神学」与自己无关。几个世纪以来，基督教世界用「该隐的记号」「神弃绝的民族」等说法，为「血」的偏见铺了路；西班牙的「血统纯净 (limpieza de sangre)」法令，甚至追查皈依者祖上是否有犹太血——这是纳粹种族法的中世纪先声。当我们读《纽伦堡法》，我们不是在读一段「别人的」历史；我们是在读一棵毒树结出的果子，而那棵树的根，有一部分扎在教会的土壤里。承认这一点，是悔改的开始。",
                      "The Church cannot pretend this “theology of blood” had nothing to do with it. For centuries Christendom paved the way for blood-prejudice with talk of “the mark of Cain” and “a people rejected by God”; Spain's <em>limpieza de sangre</em> statutes even hunted for Jewish ancestry among converts — a medieval forerunner of the Nazi race laws. Reading the Nuremberg Laws is not reading someone else's history; it is reading the fruit of a poisoned tree whose roots reach, in part, into Church soil. To admit this is where repentance begins.")),
                step(S5, S5E,
                    ul(
                        ("我是否曾不假思索地以『血统』『民族』来评断一个人的价值或属灵地位？",
                         "Have I ever, without thinking, judged a person's worth or spiritual standing by “blood” or “ethnicity”?"),
                        ("『神看内心』——如果这是真的，那么任何以外在身份给人定罪的体系，从根上就是反对神的。我所默许的体系里，有这样的成分吗？",
                         "If “God looks at the heart” is true, then any system that condemns by outward identity is, at its root, against God. Are there such elements in systems I quietly accept?"),
                        ("从亚伯拉罕的『后裔』到弥赛亚——我能否把『血脉』重新理解为应许与祝福，而不是排斥与恐惧？",
                         "From the “seed” of Abraham to the Messiah — can I relearn “bloodline” as promise and blessing rather than exclusion and fear?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "受了洗，却被烙印",
            "title_en": "Baptized, and Branded",
            "steps": [
                step(S1, S1E,
                    p("克兰的祖父在离开德国前，坚持立刻为孩子施洗「以保护他们」——他们本已在路德宗教会上主日学。书中大多数女性也是如此：父母虔诚地把她们养成基督徒。然而洗礼救不了她们。在纳粹眼中，水洗改变不了「血」。这是「混血儿」处境最尖锐的悖论：在教会里，她们是基督徒；在街上、在学校、在政府档案里，她们是犹太人。她们「同时是受害者与（被指为）加害者，是犹太人又是基督徒，是局外人又是局内人」。她们的人生，从此被劈成两半。",
                      "Before leaving Germany, Crane's grandfather insisted the children be baptized at once “to protect them” — they were already in Lutheran Sunday school. So with most of the women in the book: devout parents raised them as Christians. Yet baptism could not save them. In Nazi eyes, water could not wash away “blood.” This is the sharpest paradox of the Mischling condition: in church, Christians; on the street, in school, in the state files, Jews. They were at once “victim and (accused) victimizer, Jew and Christian, outsider and insider.” Their lives were split in two.")),
                step(S2, S2E,
                    bq("「他们逼迫了我，也要逼迫你们……只因我的名。」",
                       "“If they persecuted me, they will persecute you also... they will treat you this way because of my name.”",
                       "《约翰福音》15:20-21 · John 15:20-21")),
                step(S3, S3E,
                    p("<strong>מָשִׁיחַ · Mashiach</strong>——「受膏者」「弥赛亚」。这些女性受洗归入的那一位，本身就是一个犹太人，一个在罗马权势下被自己的世界判为「外人」的拿撒勒人。基督教若忘记自己的主是犹太人，就会荒谬地用「基督」的名去逼迫祂骨肉之亲的同胞。受洗的混血儿正活在这荒谬的夹缝中：她们被领进一位犹太弥赛亚的羊圈，却因为与这位弥赛亚同族的血，而被世界追杀。她们的苦难，奇异地贴近了她们所信之主的苦难。",
                      "<strong>מָשִׁיחַ · Mashiach</strong> — “the Anointed One,” the Messiah. The One into whom these women were baptized was himself a Jew, a Nazarene declared an “outsider” by his own world under Roman power. When Christianity forgets that its Lord is Jewish, it absurdly uses the name of “Christ” to persecute his own flesh and blood. The baptized Mischlinge lived in exactly that absurd gap: led into the fold of a Jewish Messiah, yet hunted by the world for sharing that Messiah's blood. Their suffering came strangely close to the suffering of the Lord they believed in.")),
                step(S4, S4E,
                    p("这一课向教会提出一个灼人的问题：洗礼到底意味着什么？对纳粹来说，洗礼是一张作废的票。但对神来说，洗礼从不是为了「洗去犹太性」、把人变成「安全的外邦人」。早期教会的许多殉道者正是犹太信徒。当教会把『成为基督徒』暗暗等同于『不再是犹太人』，它就背叛了自己最初的样子——那个由犹太门徒组成、敬拜一位犹太弥赛亚的教会。这些受洗却被烙印的女性，无声地见证：在基督里，犹太人不必停止做犹太人。",
                      "This lesson puts a burning question to the Church: what does baptism actually mean? To the Nazis it was a voided ticket. But to God, baptism was never meant to “wash away Jewishness” and turn a person into a “safe Gentile.” Many of the early Church's martyrs were Jewish believers. When the Church quietly equates “becoming Christian” with “no longer being Jewish,” it betrays its own beginning — a Church of Jewish disciples worshiping a Jewish Messiah. These baptized-yet-branded women bear silent witness: in the Messiah, a Jew need not stop being a Jew.")),
                step(S5, S5E,
                    ul(
                        ("我心里是否暗暗觉得，一个犹太人信了耶稣，就该『不再像犹太人』？这个想法从何而来？",
                         "Do I secretly feel that a Jew who believes in Jesus should “stop being so Jewish”? Where did that feeling come from?"),
                        ("如果我的信仰使我与基督的苦难相连，我准备好像这些女性一样,『因祂的名』被人误解、被边缘化吗？",
                         "If my faith joins me to the Messiah's suffering, am I ready, as these women were, to be misread and marginalized “because of his name”?"),
                        ("洗礼把我领进的，是一个怎样的家?——是一个抹去差异的家，还是一个让犹太人与外邦人都做回真正自己的家？",
                         "What kind of family did baptism bring me into — one that erases difference, or one where Jew and Gentile both become truly themselves?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "「德国人和纳粹，于我不是同义词」——英格博格·赫希特",
            "title_en": "“The Germans and the Nazis Were Not Synonyms” — Ingeborg Hecht",
            "steps": [
                step(S1, S1E,
                    p("第一位女性英格博格·赫希特 (Ingeborg Hecht) 的故事，标题是她的一句话：「德国人和纳粹，于我从来不是同义词。」她的父亲是犹太人，被剥夺一切、最终遇害；她自己作为「一级混血」在恐惧中长大。但她拒绝用对纳粹的恨，去恨整个德意志民族——她记得那些冒险帮助过她的普通德国人。这是一种艰难的、刀刃上的恩典：在自己受害最深的地方，仍坚持区分『一个民族』与『一种意识形态』，拒绝以暴制暴的简化。",
                      "The first woman, Ingeborg Hecht, gives the book one of its titles: “The Germans and the Nazis were never synonyms for me.” Her father was Jewish, stripped of everything and ultimately killed; she grew up a terrified “first-degree” Mischling. Yet she refused to let her hatred of the Nazis become hatred of the German people — she remembered the ordinary Germans who risked themselves to help her. It is a hard, knife-edge grace: at the very place of her deepest wound, she insists on distinguishing <em>a people</em> from <em>an ideology</em>, refusing the easy arithmetic of returning evil for evil.")),
                step(S2, S2E,
                    bq("「不要为恶所胜，反要以善胜恶。」",
                       "“Do not be overcome by evil, but overcome evil with good.”",
                       "《罗马书》12:21 · Romans 12:21")),
                step(S3, S3E,
                    p("<strong>סְלִיחָה · slichah</strong>——「赦免」，是赎罪日 (Yom Kippur) 的核心词之一。犹太传统里的赦免不是廉价的遗忘，而是一种清醒的拒绝——拒绝让仇恨拥有最后的话语权。赫希特不是说『纳粹无罪』；她是说『罪不该被株连到全族』。这正合乎先知的心肠：以西结说，「儿子必不担当父亲的罪孽」(《以西结书》18:20)。把一个人的恶扩大成一整个民族的本质——纳粹对犹太人这样做，而赫希特拒绝对德国人这样做。",
                      "<strong>סְלִיחָה · slichah</strong> — “forgiveness,” a central word of Yom Kippur. In Jewish tradition forgiveness is not cheap forgetting but a clear-eyed refusal — a refusal to give hatred the last word. Hecht is not saying “the Nazis were innocent”; she is saying “guilt must not be charged to a whole people.” That is the heart of the prophets: “the son shall not bear the iniquity of the father” (Ezekiel 18:20). To inflate one person's evil into the essence of an entire people — the Nazis did this to the Jews, and Hecht refuses to do it to the Germans.")),
                step(S4, S4E,
                    p("赫希特的拒绝，对今天的教会是一面镜子。基督徒在面对反犹历史时，容易掉进两个陷阱：要么否认（『那不是真正的基督教』），要么用集体的羞耻把今天的某一群人重新妖魔化。赫希特指出第三条路：诚实地说出恶，却拒绝株连。我们可以、也应当为基督教世界两千年的『轻蔑的教导』(teaching of contempt) 悔改，同时不把任何一个今天活着的人，简化成他祖先之恶的化身。爱，既要看清真相，又要拒绝仇恨。",
                      "Hecht's refusal is a mirror for the Church today. Facing the history of antisemitism, Christians fall into two traps: denial (“that wasn't real Christianity”) or a collective shame that re-demonizes some group in the present. Hecht points to a third road: name the evil honestly, yet refuse collective guilt. We can and should repent of Christendom's two-thousand-year “teaching of contempt,” while refusing to reduce any living person to the embodiment of an ancestor's sin. Love both sees the truth and refuses hatred."),),
                step(S5, S5E,
                    ul(
                        ("在我受过最深伤害的地方，我能否仍然区分『伤我的那个人』与『他所属的群体』？",
                         "At the place of my deepest wound, can I still distinguish “the person who hurt me” from “the group he belonged to”?"),
                        ("『以善胜恶』在赫希特身上是什么样子？在我身上，它会要求我放下什么？",
                         "What did “overcoming evil with good” look like in Hecht? What would it require me to lay down?"),
                        ("我是否曾把一整个民族、宗派或国家，简化为它最坏成员的样子？",
                         "Have I ever reduced a whole people, denomination, or nation to the image of its worst members?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "「我是浪与浪之间的漂泊者」——英格丽德·韦克尔",
            "title_en": "“A Wanderer Between the Waves” — Ingrid Wecker",
            "steps": [
                step(S1, S1E,
                    p("英格丽德·韦克尔 (Ingrid Wecker) 用一句诗概括了混血儿的存在：「我是浪与浪之间的漂泊者，不属于任何人。」对德国人而言她太『犹太』，对犹太人而言她太『德国』；战后，那段身份要么成了耻辱，要么成了护身符。克兰反复用一个德语短语形容她们：<em>zwischen allen Stühlen</em>——『夹在所有椅子之间』，哪一把都坐不下。这是一种没有归属的孤独：不是被某一个群体放逐，而是被所有群体同时悬置。",
                      "Ingrid Wecker captured the Mischling existence in a single line: “I was a wanderer between the waves, belonging to no one.” Too “Jewish” for the Germans, too “German” for the Jews; after the war that identity became either a shame or a shield. Crane keeps reaching for one German phrase to describe these women: <em>zwischen allen Stühlen</em> — “between all the chairs,” unable to sit on any. It is a loneliness without belonging: not exiled by one group, but suspended by all of them at once.")),
                step(S2, S2E,
                    bq("「我作了寄居的，在外邦……我成了我弟兄的外人，是我母亲儿女眼中的外邦人。」",
                       "“I am a foreigner to my own family, a stranger to my own mother's children... I dwell as an alien.”",
                       "《诗篇》69:8 · Psalm 69:8")),
                step(S3, S3E,
                    p("<strong>גָּלוּת · galut</strong>——「流亡」「离散」。这是犹太历史最深的词之一：不只是地理上的离开故土，更是一种『身在此处、心无归处』的生存状态。韦克尔的漂泊，正是 galut 的一个微缩版本。然而犹太信仰从未让流亡成为终点——它总是与『回归 (shuv)』、与弥赛亚的盼望连在一起。诗篇 69 篇这位『成了弟兄外人』的诗人，传统上被基督徒读作指向受苦的弥赛亚：那位连自己的同胞都不接纳的『漂泊者』。",
                      "<strong>גָּלוּת · galut</strong> — “exile,” “diaspora.” It is one of the deepest words in Jewish history: not merely geographic displacement, but a way of being “here in body, homeless in heart.” Wecker's wandering is galut in miniature. Yet Jewish faith never lets exile be the end — it is always bound up with <em>shuv</em>, “return,” and with messianic hope. The psalmist of Psalm 69, “a stranger to his own brothers,” has long been read by Christians as pointing to the suffering Messiah: the very Wanderer his own people would not receive."),),
                step(S4, S4E,
                    p("教会本该是那张『为漂泊者预留的椅子』。新约说基督徒『在世为客旅、是寄居的』(《彼得前书》2:11)——我们本就该懂得无家可归的滋味，因此理应特别善待真正无处归属的人。可悲的是，历史上教会常常成了又一张把人推开的椅子。这一课邀请我们悔改并转向：让我们的群体成为一处真正的款待之地，让每一个『浪与浪之间的漂泊者』，能在弥赛亚里找到一个家——不是被抹去差异的家，而是连差异也被珍惜的家。",
                      "The Church was meant to be the one chair kept open for the wanderer. The New Testament calls believers “foreigners and exiles” in this world (1 Peter 2:11) — we, of all people, should know what homelessness tastes like, and so should be tender toward those who truly belong nowhere. Tragically, the Church has often been just one more chair that pushes people away. This lesson calls us to repent and turn: to make our communities a place of real hospitality, where every “wanderer between the waves” can find a home in the Messiah — not a home that erases difference, but one where even the differences are cherished."),),
                step(S5, S5E,
                    ul(
                        ("『夹在所有椅子之间』——我生命中有没有这样无处归属的经历？它教了我什么？",
                         "“Between all the chairs” — have I ever known that homelessness? What did it teach me?"),
                        ("我所在的教会或群体，是『又一把推开人的椅子』，还是『为漂泊者预留的椅子』？",
                         "Is my church or community “one more chair that pushes people away,” or “a chair kept open for the wanderer”?"),
                        ("如果基督徒本是『客旅与寄居的』，这身份该如何改变我对待陌生人、移民、边缘人的方式？",
                         "If believers are “foreigners and exiles,” how should that identity change the way I treat strangers, immigrants, the marginalized?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "「神把我的生命握在祂手中」——信心与「神在哪里」",
            "title_en": "“God Took My Life Into His Hands” — Faith and “Where Was God?”",
            "steps": [
                step(S1, S1E,
                    p("书中并存着两种声音，克兰都忠实地记录下来。一边是格蕾特尔·洛伦岑 (Gretel Lorenzen)：「神把我的生命握在祂手中，我永远为此感恩。」另一边，是克兰在「法」一章里转述的另一位女性的低语：「神在哪里？」(Where was God?) 这不是一本给出廉价答案的书。它把『坚定的感恩』与『撕裂的质问』放在同一张桌上，不调和、不评判——因为真实的苦难里，信心与控诉常常住在同一颗心里。",
                      "Two voices live side by side in this book, and Crane records both faithfully. On one side, Gretel Lorenzen: “God took my life into his hands, and I am forever grateful for that.” On the other, the whispered question Crane relays in “The Law” from another woman: “Where was God?” This is not a book that hands out cheap answers. It sets steadfast gratitude and torn protest on the same table, unreconciled and unjudged — because in real suffering, faith and accusation often live in the same heart.")),
                step(S2, S2E,
                    bq("「我的神，我的神！为什么离弃我?……但你是圣洁的，是用以色列的赞美为宝座的。」",
                       "“My God, my God, why have you forsaken me?... Yet you are enthroned as the Holy One; you are the one Israel praises.”",
                       "《诗篇》22:1-3 · Psalm 22:1-3")),
                step(S3, S3E,
                    p("<strong>אֵיכָה · Eichah</strong>——「怎会如此？」这是《耶利米哀歌》的开篇词，也是希伯来圣经为大灾难保留的发问方式。圣经从不禁止人向神发出『神在哪里』的呼喊；恰恰相反，它把这呼喊收进了正典——《诗篇》《约伯记》《哀歌》里满是这样的声音。犹太传统甚至有一个惊人的观念：<em>Shekhinah</em>（神的临在）与祂的子民一同流亡，一同受苦。神不在苦难『之外』冷眼旁观；按这一传统，祂在苦难『之中』与受苦者同在。",
                      "<strong>אֵיכָה · Eichah</strong> — “How can this be?” It is the opening word of the book of Lamentations, the way the Hebrew Bible holds space for catastrophe. Scripture never forbids the cry “Where is God?”; on the contrary, it canonizes it — the Psalms, Job, and Lamentations are full of that voice. Jewish tradition even holds a staggering idea: the <em>Shekhinah</em>, God's Presence, goes into exile with his people and suffers alongside them. God does not watch suffering coldly from outside; in this tradition, he is <em>within</em> it, with those who suffer."),),
                step(S4, S4E,
                    p("基督徒在十字架上看见这个奥秘的顶点。耶稣在十字架上喊出的，正是《诗篇》22 篇——『我的神，我的神，为什么离弃我？』神并没有回避『神在哪里』的问题；在弥赛亚里，神亲自走进了那个问题的中心。这并不『解释』了大屠杀的恶——没有任何神学能轻巧地解释它。但它意味着：当那些女性低声问『神在哪里』时，基督徒至少不能用居高临下的答案打发她们。我们只能与哀哭的人同哭，并指向那位同样被弃绝、同样呼喊过的受苦弥赛亚。",
                      "Christians see the summit of this mystery at the cross. The cry Jesus utters there is Psalm 22 — “My God, my God, why have you forsaken me?” God did not dodge the question “Where is God?”; in the Messiah, God walked into the center of it. This does not “explain” the evil of the Shoah — no theology explains it lightly. But it means that when these women whisper “Where was God?” a Christian cannot answer from above. We can only weep with those who weep, and point to the suffering Messiah who was likewise forsaken, who likewise cried out."),),
                step(S5, S5E,
                    ul(
                        ("我能否同时容纳『感恩』与『质问』，像这本书那样，不急着把它们调和？",
                         "Can I hold both gratitude and protest at once, as this book does, without rushing to reconcile them?"),
                        ("面对别人深重的苦难,我是更倾向于给『答案』，还是愿意先安静地同哭？",
                         "Facing another's deep suffering, do I reach for “answers,” or am I willing first to weep in silence alongside them?"),
                        ("『神与受苦者同在』——这对我祷告、读经、安慰人的方式,意味着什么？",
                         "“God is present within the suffering” — what does that mean for how I pray, read Scripture, and comfort others?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "「大象皮」与余民的坚韧——露丝·维尔姆申",
            "title_en": "“Elephant Skin” and the Endurance of the Remnant — Ruth Wilmschen",
            "steps": [
                step(S1, S1E,
                    p("露丝·维尔姆申 (Ruth Wilmschen) 说：「在纳粹岁月里，我练就了一身大象皮，什么样的对待都能扛得住。」这句话里有创伤，也有惊人的生命力。这些女性活了下来——不是因为她们『更坚强所以活该受苦』（克兰明确驳斥这种说法），而是因为人的灵魂在被碾压时，会长出意想不到的韧性。克兰注意到一个细节：在『混合婚姻』里，犹太一方往往比『雅利安』配偶活得更久。仿佛那承受最多的人，反而被苦难磨出了某种不肯熄灭的生命。",
                      "Ruth Wilmschen said: “In the Nazi years, I acquired an elephant skin and could handle any kind of treatment.” There is trauma in that line, and astonishing vitality. These women survived — not because they were “stronger and therefore deserved the suffering” (Crane flatly rejects that logic) — but because the human soul, when crushed, grows unexpected resilience. Crane notes a striking detail: in “mixed marriages,” the Jewish partner often outlived the “Aryan” spouse. As if the one who bore the most was ground by suffering into a life that would not go out.")),
                step(S2, S2E,
                    bq("「我们四面受敌，却不被困住；心里作难，却不至失望……身上常带着耶稣的死，使耶稣的生也显明在我们身上。」",
                       "“We are hard pressed on every side, but not crushed; perplexed, but not in despair... always carrying in the body the death of Jesus, so that the life of Jesus may also be revealed in our body.”",
                       "《哥林多后书》4:8-10 · 2 Corinthians 4:8-10")),
                step(S3, S3E,
                    p("<strong>שְׁאֵרִית · she'erit</strong>——「余民」「剩下的人」。这是先知书反复出现的盼望：审判与灾难过后，神总会保守『一小群剩下的』，从他们重新开始。以赛亚给儿子起名『施亚雅述』(Shear-jashub)，意思就是『余民必归回』(《以赛亚书》7:3)。这些幸存的女性，正是二十世纪的一支『余民』——不是因为她们伟大，而是因为她们『剩下了』，并且开口说话了。余民的意义从不在数量，而在于：只要还有一个人活着作见证，那段历史就没有被彻底抹去。",
                      "<strong>שְׁאֵרִית · she'erit</strong> — “remnant,” “those who remain.” It is the recurring hope of the prophets: after judgment and catastrophe, God always preserves “a small number left,” and begins again from them. Isaiah named his son Shear-jashub, “a remnant shall return” (Isaiah 7:3). These surviving women are a twentieth-century remnant — not because they were great, but because they <em>remained</em>, and spoke. The meaning of the remnant is never in numbers; it is this: as long as one survivor lives to testify, that history has not been wholly erased."),),
                step(S4, S4E,
                    p("『大象皮』提醒基督徒不要浪漫化苦难。圣经从不歌颂痛苦本身——它歌颂的是那位在痛苦中托住人的神。保罗说『四面受敌却不被困住』，关键不在于他的坚强，而在于那托住他的『莫大的能力是出于神，不是出于我们』(《哥林多后书》4:7)。当我们聆听余民的见证，我们的任务不是赞叹他们的坚韧、然后翻篇；而是接过他们的见证，成为『记念的人』，让他们承受的一切，结出悔改与守护的果子。",
                      "The “elephant skin” warns Christians not to romanticize suffering. Scripture never praises pain itself — it praises the God who upholds people within pain. Paul says he is “hard pressed but not crushed,” and the point is not his strength but that “this all-surpassing power is from God and not from us” (2 Cor 4:7). When we listen to the remnant's testimony, our task is not to admire their resilience and move on; it is to receive their witness, become people who remember, and let all they endured bear fruit in repentance and in vigilant protection of others."),),
                step(S5, S5E,
                    ul(
                        ("我是否曾把别人的『幸存』当作『他们本来就够坚强』的证据，从而免去自己的责任？",
                         "Have I ever treated another's survival as proof that “they were strong enough,” quietly excusing myself from responsibility?"),
                        ("『余民必归回』——在我自己的灰烬里，神是否也保守了某些『剩下的』，等我从那里重新开始？",
                         "“A remnant shall return” — in my own ashes, has God preserved something “left over” from which to begin again?"),
                        ("听完幸存者的故事，我会做什么？只是感动，还是成为一个『记念的人』？",
                         "After hearing a survivor's story, what will I do — merely be moved, or become someone who remembers?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "记念——把不为人知的故事讲出来",
            "title_en": "Remembrance — Telling the Untold Story",
            "steps": [
                step(S1, S1E,
                    p("克兰花了近十年完成这本书，因为这些故事差点就永远沉默了。许多女性战后重获了德国身份与匿名，她们害怕『再次引人注目、再去翻动过去』。这本书的存在本身，就是一场与遗忘的搏斗。克兰引用一句话：『你播下种子，然后等待。常常你以为种子坏了，因为它们毫无动静……然后突然，子叶冒了出来。』讲述，就是播种；记念，就是不让那片土壤被永远封死。书名《分裂的人生》，最终指向一个合一的盼望：被讲出来的故事，能让分裂的人重新被缝合。",
                      "Crane spent nearly a decade on this book, because these stories nearly fell silent forever. Many of the women had regained German identity and anonymity after the war, and feared “drawing attention to themselves again, dabbling in the past.” The book's very existence is a struggle against forgetting. Crane quotes a friend: “you plant seeds and wait. Often you think the seeds are no good because they do nothing... then suddenly the cotyledons appear.” To tell is to sow; to remember is to refuse to let that soil be sealed forever. The title <em>Divided Lives</em> finally points toward a hope of wholeness: a story told can re-stitch a divided life.")),
                step(S2, S2E,
                    bq("「你要记念你在埃及地作过奴仆……所以耶和华你的神吩咐你守这日。」",
                       "“Remember that you were slaves in Egypt... therefore the LORD your God has commanded you to keep this day.”",
                       "《申命记》5:15 · Deuteronomy 5:15")),
                step(S3, S3E,
                    p("<strong>זָכוֹר · zachor</strong>——「记念!」这是整本希伯来圣经最重的命令之一。对犹太信仰而言，记念不是怀旧，而是一种道德行动：逾越节的家宴 (Seder) 要让每一代人『仿佛自己亲身从埃及出来』。忘记，等于让压迫者第二次得胜。这正是克兰所做的：她把口述变成文字，让这些『不为人知的故事』进入集体的记忆，成为后人无法绕过的见证。<em>Zachor</em> 与它的反面 <em>shikchah</em>（遗忘）之间，隔着整个民族的命运。",
                      "<strong>זָכוֹר · zachor</strong> — “Remember!” It is among the weightiest commands in the whole Hebrew Bible. For Jewish faith, remembering is not nostalgia but a moral act: the Passover Seder makes every generation recount the Exodus “as if they themselves came out of Egypt.” To forget is to let the oppressor win a second time. This is exactly what Crane does: she turns oral testimony into text, so these “untold stories” enter collective memory as a witness no one can bypass. Between <em>zachor</em> and its opposite, <em>shikchah</em> (forgetting), hangs the fate of a whole people."),),
                step(S4, S4E,
                    p("教会的圣餐，本身就是一场『记念 (anamnesis)』——『你们应当如此行,为的是记念我』(《路加福音》22:19)。基督徒是被『记念』塑造的子民。那么，记念主的我们，岂能对祂骨肉之亲所受的苦视而不见、听而不闻？读《分裂的人生》，是一种属灵的操练：练习记念那些差点被历史遗忘的人，练习哀哭，练习悔改，练习守望——好让『永不重演』不只是口号，而是一个记念之民用生命守护的承诺。愿这八堂课，使我们成为这样的人。",
                      "The Church's Communion is itself an act of remembrance — <em>anamnesis</em>: “do this in remembrance of me” (Luke 22:19). Christians are a people shaped by remembering. How then can we, who remember the Lord, be blind and deaf to the suffering of his own flesh and blood? Reading <em>Divided Lives</em> is a spiritual discipline: practicing remembrance of those history nearly forgot, practicing lament, repentance, and watchfulness — so that “never again” is not a slogan but a promise a remembering people guards with their lives. May these eight lessons make us such people."),),
                step(S5, S5E,
                    ul(
                        ("『忘记等于让压迫者第二次得胜』——我生活中有哪些『不为人知的故事』，是我有责任记住、并说出来的？",
                         "“To forget is to let the oppressor win twice” — what “untold stories” in my world am I responsible to remember and to tell?"),
                        ("作为一个被『记念』塑造的子民（圣餐），我对犹太民族的历史苦难，负有怎样的记念责任？",
                         "As a people shaped by remembrance (Communion), what duty of memory do I bear toward the historic suffering of the Jewish people?"),
                        ("读完这份指南，我会以什么具体的行动，去『记念』而不是『翻篇』？",
                         "Having finished this guide, what concrete action will I take to <em>remember</em> rather than simply move on?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "记念之民的祝祷",
    "closing_title_en": "A Blessing for a People Who Remember",
    "closing_zh": "「愿耶和华赐福给你，保护你；愿耶和华使祂的脸光照你，赐恩给你。」<br/><br/>愿你听见了那十个声音，也记住了她们；<br/>愿你不再把『犹太人』与『基督徒』当作彼此对立的两半——<br/>而看见在弥赛亚里，那道被历史劈开的裂缝，正在被缝合。<br/><br/>愿你成为一个记念的人：<br/>为轻蔑的教导悔改，<br/>与哀哭的人同哭，<br/>并守望，使那暗夜永不重临。",
    "closing_en": "“The LORD bless you and keep you; the LORD make his face shine upon you and be gracious to you.”<br/><br/>May you have heard those ten voices, and may you remember them.<br/>May you no longer hold “Jew” and “Christian” as two opposing halves —<br/>but see, in the Messiah, the seam that history tore open being stitched whole again.<br/><br/>May you become a person who remembers:<br/>repenting of the teaching of contempt,<br/>weeping with those who weep,<br/>and keeping watch, that the long night never come again.",
}

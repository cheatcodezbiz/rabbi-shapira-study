# -*- coding: utf-8 -*-
"""Content module for study-historian-exile.html.

Jeremy Cohen, *A Historian in Exile: Solomon ibn Verga, Shevet Yehudah, and
the Jewish-Christian Encounter* (University of Pennsylvania Press, 2017).
"""

RHYTHM_ZH = """        <strong>① 学者说什么</strong>—— 用科恩的研究，呈现伊本·维尔加这部书的世界；<br/>
        <strong>② 关键经文</strong>—— 一处与之相关、需重新聆听的圣经；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，照亮这段苦难史；<br/>
        <strong>④ 基督徒视角</strong>—— 我们该如何聆听、悔改、记念、盼望；<br/>
        <strong>⑤ 诚实的提问</strong>—— 留给你与小组省察的问题。"""

RHYTHM_EN = """        <strong>① What the Scholar Says</strong> — the world of ibn Verga's book, in Cohen's research;<br/>
        <strong>② Key Scripture</strong> — a related text we must hear again;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that lights up this history of suffering;<br/>
        <strong>④ A Christian Lens</strong> — how we should listen, repent, remember, and hope;<br/>
        <strong>⑤ Honest Questions</strong> — questions for you and your group to examine."""


def step(label_zh, label_en, *body):
    return {"label_zh": label_zh, "label_en": label_en, "body": list(body)}

def p(zh, en):
    return {"type": "p", "zh": zh, "en": en}

def bq(zh, en, cite=None):
    return {"type": "blockquote", "zh": zh, "en": en, "cite": cite}

def ul(*items):
    return {"type": "ul", "items": [{"zh": z, "en": e} for z, e in items]}

S1, S1E = "① 学者说什么", "① What the Scholar Says"
S2, S2E = "② 关键经文", "② Key Scripture"
S3, S3E = "③ 希伯来语之眼", "③ Through Hebrew Eyes"
S4, S4E = "④ 基督徒视角", "④ A Christian Lens"
S5, S5E = "⑤ 诚实的提问", "⑤ Honest Questions"


study = {
    "title_tag": "《流亡中的史家》研习指南 · A Historian in Exile — Study Guide · 妥拉之光",
    "meta_desc": "A study guide to Jeremy Cohen's A Historian in Exile — eight bilingual lessons on Solomon ibn Verga's Shevet Yehudah, the disputations, libels, martyrs, and conversos of Jewish suffering under Christendom, read with repentance and messianic hope.",
    "og_title": "A Historian in Exile — A Study Guide",
    "og_desc": "Eight bilingual lessons through Jeremy Cohen's study of Solomon ibn Verga's Shevet Yehudah — the Jewish-Christian encounter in an age of expulsion, read with repentance and Hebrew eyes.",
    "cover_alt": "A Historian in Exile: Solomon ibn Verga, Shevet Yehudah — Study Guide",
    "tagline_zh": "研习指南 · 流亡、记念与盼望 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · Exile, Remembrance &amp; Hope · 2026 · 5 · 31",
    "headline_zh": "流亡中的史家<br/>研习指南",
    "headline_en": "A Historian in Exile<br/>A Study Guide",
    "deck_zh": "八堂课程，跟随杰里米·科恩 (Jeremy Cohen)，进入十六世纪犹太史家所罗门·伊本·维尔加 (Solomon ibn Verga) 的《犹大之杖》(Shevet Yehudah)——一部从西班牙驱逐与被迫受洗的创伤中写成的书，记下了犹太民族在基督教世界中所受的辩论、诬告、殉道与被迫归信。带着悔改与盼望，直面这段沉重的历史。",
    "deck_en": "Eight lessons following Jeremy Cohen into the sixteenth-century Jewish historian Solomon ibn Verga's Shevet Yehudah (The Scepter of Judah) — a book written out of the trauma of the Spanish expulsion and forced baptism, recording the disputations, libels, martyrdoms, and forced conversions the Jewish people endured under Christendom. Facing this heavy history with repentance and hope.",
    "byline_zh": "基于杰里米·科恩 (Jeremy Cohen)《流亡中的史家——所罗门·伊本·维尔加、《犹大之杖》与犹太-基督相遇》(University of Pennsylvania Press, 2017)",
    "byline_en": "Based on A Historian in Exile: Solomon ibn Verga, Shevet Yehudah, and the Jewish-Christian Encounter by Jeremy Cohen (University of Pennsylvania Press, 2017)",
    "readtime_zh": "约 55 分钟通读",
    "readtime_en": "~55 min read-through",
    "book_url": "https://www.pennpress.org/9780812248586/a-historian-in-exile/",
    "book_link_zh": "购买原书 · Penn Press",
    "book_link_en": "Get the Book · Penn Press",
    "cta_url": "https://www.pennpress.org/9780812248586/a-historian-in-exile/",
    "cta_zh": "购买《流亡中的史家》原书 · University of Pennsylvania Press",
    "cta_en": "Get the Book — A Historian in Exile · University of Pennsylvania Press",

    "lead_zh": "为什么爱犹太民族的我们,要读一本关于犹太人在基督教世界中受苦的书?因为爱必须从真相开始,「爱我民」(Ahavat Ammi) 不能建立在遗忘之上。科恩 (Jeremy Cohen) 这部研究,带我们走近所罗门·伊本·维尔加——一位卡斯蒂利亚的犹太医师、贵族、犹太社群在当局前的代言人。1492 年,他随着整个西班牙犹太族群被逐;逃到葡萄牙后,极可能被强迫受洗。正是从这样的创伤里,他写下(或编纂)了《犹大之杖》(Shevet Yehudah):六十多个关于犹太人「在外邦人之地」所受苦难的故事——血祭诬告、强制辩论、阴谋、恶法、驱逐。这本书四百年来一版再版,因为它不只是史料,更是一个受伤民族的灵魂自述。",
    "lead_en": "Why should we who love the Jewish people read a book about Jewish suffering under Christendom? Because love must begin with truth, and <em>Ahavat Ammi</em> cannot be built on forgetting. Jeremy Cohen's study brings us close to Solomon ibn Verga — a Castilian Jewish physician, nobleman, and spokesman for his community before the authorities. In 1492 he was expelled with the whole of Spanish Jewry; fleeing to Portugal, he was most likely baptized against his will. Out of exactly such trauma he wrote (or compiled) <em>Shevet Yehudah</em> (The Scepter of Judah): more than sixty stories of Jewish suffering “in the lands of non-Jewish peoples” — blood libels, forced disputations, conspiracies, evil decrees, expulsions. The book has been reprinted for four centuries, because it is not merely a record but the soul's self-account of a wounded people.",

    "intro": [
        p("科恩指出,《犹大之杖》既是历史,也是神学:伊本·维尔加不只记录灾难,他在苦苦追问——为什么?神在哪里?他甚至大胆地借书中人物之口,反省犹太人自身、也批判基督徒的逼迫。对今天读这本书的基督徒而言,这是一面镜子:它逼我们看见,我们的信仰传统在历史上,曾如何成为别人苦难的来源。读它,不是为了自责瘫痪,而是为了悔改、记念,并带着盼望,学习以全新的方式去爱这个民族。",
          "Cohen shows that <em>Shevet Yehudah</em> is both history and theology: ibn Verga not only records catastrophe but agonizes over it — why? Where is God? He even dares, through his characters, both to examine the Jews themselves and to indict Christian persecution. For a Christian reading this book today, it is a mirror: it forces us to see how our own faith tradition was, in history, a source of others' suffering. We read it not for paralyzed self-reproach, but for repentance, remembrance, and learning — with hope — to love this people in a wholly new way."),
        p("本指南共 <strong>八堂课</strong>，循着书与科恩研究的主要主题展开。每一堂遵循同样的五部分节奏：",
          "The guide is structured as <strong>eight lessons</strong>, following the major themes of the book and Cohen's study. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句郑重的提醒:这堂课会让人不舒服。请不要带着自义去读「中世纪的他们」,而要带着省察去读「今天的我们」。同样的逼迫之灵,今天仍可能以新的形式回来。",
          "A solemn caution: this study will be uncomfortable. Do not read it with self-righteousness about “those medievals,” but with self-examination about “us, today.” The same spirit of persecution can return in new forms."),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "《犹大之杖》——从伤口里写成的历史",
            "title_en": "The Scepter of Judah — History Written from the Wound",
            "steps": [
                step(S1, S1E,
                    p("科恩首先让我们认识这本书与它的作者。伊本·维尔加不是一位安坐书斋的旁观者;他是 1492 年大驱逐的<em>亲历者与受害者</em>,书写的是自己民族、也是自己的伤口。《犹大之杖》收录了从晚期古代直到伊比利亚犹太人毁灭的六十多个苦难故事,但它绝非冷冰冰的编年。科恩强调,这是一部带着强烈个人视角与神学焦虑的作品:作者一面记下灾难,一面苦苦追问灾难的意义。这本书之所以四百年间深深打动一代代犹太读者(甚至有拉比禁止在安息日读它,因为太催人泪下),正因为它是从一个民族最深的伤口里流出来的。",
                      "Cohen first introduces the book and its author. Ibn Verga is no detached observer in a study; he is a <em>survivor and victim</em> of the great expulsion of 1492, writing the wound of his own people and his own. <em>Shevet Yehudah</em> gathers more than sixty stories of suffering from late antiquity to the destruction of Iberian Jewry — yet it is no cold chronicle. Cohen stresses it is a work of intense personal perspective and theological anxiety: the author records catastrophe while agonizing over its meaning. The book moved generations of Jewish readers so deeply for four centuries (some rabbis forbade reading it on the Sabbath because it was too tear-inducing) precisely because it flows from the deepest wound of a people.")),
                step(S2, S2E,
                    bq("「我们的竖琴挂在那里的柳树上……我们怎能在外邦唱耶和华的歌呢?耶路撒冷啊,我若忘记你,情愿我的右手忘记技巧。」",
                       "“There on the poplars we hung our harps... How can we sing the songs of the LORD while in a foreign land? If I forget you, Jerusalem, may my right hand forget its skill.”",
                       "《诗篇》137:2, 4-5 · Psalm 137:2, 4-5")),
                step(S3, S3E,
                    p("<strong>שֵׁבֶט · shevet</strong>——这个书名里的词,一身三义,意味深长:它既是「权杖、君王的权柄」,又是「支派、宗族」(如「犹大支派」),还是「击打的棍杖」。伊本·维尔加选这个词作书名,几乎是一首浓缩的诗:它同时诉说着犹大民族(shevet)所承受的击打(shevet),以及那从未真正失落的君王盼望(shevet)。一个被驱逐、被鞭打的民族,却给自己受苦的记录,起了一个带着「王权」的名字。这本身就是信心的宣告:鞭杖之下,犹大的杖——那应许的王权——并未折断。",
                      "<strong>שֵׁבֶט · shevet</strong> — the word in the title carries three meanings at once, full of significance: “scepter, royal authority”; “tribe, clan” (as in “the tribe of Judah”); and “the rod that strikes.” Ibn Verga's choice of this word as his title is almost a compressed poem: it speaks at once of the blows (<em>shevet</em>) the people of Judah (<em>shevet</em>) endured, and of the kingly hope (<em>shevet</em>) never truly lost. A people expelled and beaten gave its record of suffering a name carrying “kingship.” That itself is a confession of faith: under the rod, the scepter of Judah — the promised royal authority — was not broken.")),
                step(S4, S4E,
                    p("对基督徒而言,翻开这本书的第一课,是学会<em>聆听</em>。太久以来,「犹太人的历史」在基督教的叙事里被消音、被简化、甚至被扭曲。伊本·维尔加的书逼我们坐下来,听一个受害的民族,用自己的声音,讲自己的苦难——而其中许多苦难,正是以「基督」之名加给他们的。聆听本身,就是一种悔改的开始;它把我们从「历史的旁观者」,变成「邻舍的痛苦的见证人」。诗篇 137 那挂起的竖琴、那「怎能在外邦唱歌」的哀号,值得我们安静地、久久地聆听。",
                      "For Christians, the first lesson of opening this book is to learn to <em>listen</em>. For far too long, “Jewish history” was silenced, simplified, even distorted within the Christian narrative. Ibn Verga's book forces us to sit down and hear a victimized people tell their own suffering in their own voice — much of it inflicted in the name of “Christ.” Listening itself is a beginning of repentance; it turns us from “spectators of history” into “witnesses of a neighbor's pain.” The hung-up harps of Psalm 137, the cry “how can we sing in a foreign land,” deserve our quiet and long attention.")),
                step(S5, S5E,
                    ul(
                        ("『聆听本身就是悔改的开始』。我是否真的听过犹太民族用自己的声音讲述他们的苦难？",
                         "“Listening itself is a beginning of repentance.” Have I truly heard the Jewish people tell their own suffering in their own voice?"),
                        ("书名 shevet 同时意味着『鞭杖、支派、权杖』。一个受苦的民族给苦难记录起了『王权』之名——这是怎样的信心？",
                         "The title <em>shevet</em> means “rod, tribe, scepter” at once. A suffering people named their record of suffering with “kingship” — what kind of faith is that?"),
                        ("诗篇137的挂起竖琴,描绘流亡中的哀恸。我能否安静下来,真正与哀哭的人同哭？",
                         "The hung harps of Psalm 137 depict grief in exile. Can I be still and truly weep with those who weep?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "强制的辩论——托尔托萨与「被安排好的失败」",
            "title_en": "The Forced Disputation — Tortosa and a “Rigged Defeat”",
            "steps": [
                step(S1, S1E,
                    p("科恩用专章讨论书中反复出现的「宗教辩论」(disputation),尤其是 1413–1414 年的托尔托萨大辩论——中世纪规模最大、最具毁灭性的强制性犹太-基督辩论。表面上,这是「学术对话」;实质上,它是由教廷主导、结局早已注定的政治施压:拉比们被强迫出席,在敌对的环境中为自己的信仰辩护,而辩论的真正目的,是迫使犹太人归信、瓦解他们的士气。伊本·维尔加记下这类场景,既是控诉这种「被安排好的失败」,也借笔下人物之口,呈现犹太人在巨大压力下的智慧、尊严与挣扎。",
                      "Cohen devotes a chapter to the recurring “disputation” in the book, especially the great Disputation of Tortosa (1413–1414) — the largest and most devastating forced Jewish-Christian debate of the Middle Ages. On the surface, “scholarly dialogue”; in substance, political pressure orchestrated by the papacy with a foregone conclusion: rabbis compelled to attend, defending their faith in a hostile setting, the real aim being to force Jewish conversion and break their morale. Ibn Verga records such scenes both to indict this “rigged defeat” and, through his characters, to portray the wisdom, dignity, and struggle of Jews under immense pressure.")),
                step(S2, S2E,
                    bq("「先听的似乎有理;但邻舍来到,就察出实情。」",
                       "“In a lawsuit the first to speak seems right, until someone comes forward and cross-examines.”",
                       "《箴言》18:17 · Proverbs 18:17")),
                step(S3, S3E,
                    p("<strong>וִכּוּחַ · vikuach</strong>——「辩论、争辩」。这是希伯来传统里指称这类「宗教论战」的词。但《箴言》提醒我们,一场公正的辩论,必须让「另一方到场对质」。托尔托萨辩论之所以是不义的,恰恰因为它从根本上违背了这一点:它不是一场两方平等、真诚求真的 <em>vikuach</em>,而是一方手握权力、刀架在脖子上的施压。当『辩论』的一方可以决定另一方的生死、财产与去留,真理便无从产生——产生的只有恐惧与屈服。圣经所爱的 <em>emet</em>(真理),只能在自由与平等中生长,绝不能从强迫中长出。",
                      "<strong>וִכּוּחַ · vikuach</strong> — “disputation, debate.” This is the Hebrew tradition's word for such “religious polemics.” But Proverbs reminds us that a just debate must let “the other party come and be cross-examined.” The Tortosa disputation was unjust precisely because it violated this at the root: it was not a <em>vikuach</em> of two equal parties sincerely seeking truth, but pressure from one side holding power, a blade at the throat. When one “debating” party can decide the other's life, property, and place, truth cannot be born — only fear and submission. The <em>emet</em> (truth) Scripture loves can grow only in freedom and equality, never out of coercion.")),
                step(S4, S4E,
                    p("这一课对基督徒是一记沉重的提醒:用权力施压所「赢」来的,从来不是真信仰。耶书亚从不强迫人;祂总是邀请——「你们愿意也走吗?」(约 6:67) 当中世纪的教会用国家的权力,把犹太人逼上辩论的舞台、再逼他们「认输归信」,它彻底背离了它所传之主的样式。真正的见证,如彼得前书所说,是「有人问你们……就以温柔敬畏的心回答」——是回应真诚的发问,而非赢得一场对方无法退场的辩论。这一课呼召我们悔改,并立志:我们绝不用任何形式的强迫,去「赢得」一个灵魂。",
                      "This lesson is a heavy reminder for Christians: what is “won” by the pressure of power is never true faith. Yeshua never coerced; he always invited — “You do not want to leave too, do you?” (John 6:67). When the medieval Church used the power of the state to drag Jews onto the stage of debate and then force them to “concede and convert,” it utterly betrayed the pattern of the Lord it preached. True witness, as 1 Peter says, is “answering... with gentleness and respect” those who ask — responding to a sincere question, not winning a debate the other cannot walk out of. This lesson calls us to repent and resolve: we will never use any form of coercion to “win” a soul.")),
                step(S5, S5E,
                    ul(
                        ("『用权力施压赢来的,从来不是真信仰』。我分享信仰时,有没有不自觉地用关系、地位或情绪去施压？",
                         "“What is won by the pressure of power is never true faith.” When I share my faith, do I unconsciously pressure others through relationship, status, or emotion?"),
                        ("耶书亚总是邀请,从不强迫(『你们愿意也走吗?』)。我的见证,更像邀请,还是更像强迫的辩论？",
                         "Yeshua always invited, never coerced (“Do you also want to leave?”). Is my witness more like invitation, or like a coerced debate?"),
                        ("真理只能在自由与平等中生长。这如何重塑我对『成功传福音』的理解？",
                         "Truth can grow only in freedom and equality. How does that reshape what I count as “successful” evangelism?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "受审的塔木德——当一个民族的灵魂被定罪",
            "title_en": "The Talmud on Trial — When a People's Soul Is Condemned",
            "steps": [
                step(S1, S1E,
                    p("科恩讨论书中关于「塔木德与塔木德学者」的主题。中世纪基督教世界对犹太人的攻击,在十三世纪发生了一个危险的转向:从「指控犹太人拒绝圣经里的弥赛亚」,变为「指控犹太人离弃了真正的(圣经的)犹太教,转而信奉拉比所编造的、亵渎的塔木德」。塔木德本身于 1240 年在巴黎被「审判」、被定罪、被公开焚烧。这意味着:被攻击的,不再只是犹太人的「错误」,而是他们整个赖以为生、世代相传的信仰生命与学术传统。伊本·维尔加的书,见证了一个民族眼睁睁看着自己的灵魂被架在火上的痛。",
                      "Cohen discusses the book's theme of “the Talmud and Talmudists.” The medieval Christian attack on the Jews took a dangerous turn in the thirteenth century: from “charging the Jews with rejecting the Messiah of Scripture” to “charging them with abandoning true (biblical) Judaism for the rabbis' fabricated, blasphemous Talmud.” The Talmud itself was “put on trial,” condemned, and publicly burned in Paris in 1240. This meant that what was attacked was no longer merely the Jews' “error,” but the whole faith-life and scholarly tradition by which they lived and which they handed down across generations. Ibn Verga's book witnesses the agony of a people watching its very soul set ablaze.")),
                step(S2, S2E,
                    bq("「这些话……你也要殷勤教训你的儿女。无论你坐在家里,行在路上,躺下,起来,都要谈论。」",
                       "“These commandments... Impress them on your children. Talk about them when you sit at home and when you walk along the road, when you lie down and when you get up.”",
                       "《申命记》6:6-7 · Deuteronomy 6:6-7")),
                step(S3, S3E,
                    p("<strong>תַּלְמוּד · talmud</strong>——「学习、研读」。这个被审判、被焚烧的庞大文本,它的名字本身就是「学习」。它是犹太民族两千年来「殷勤教训儿女」(申 6:7) 的果实——一代代拉比围绕神的话语,日夜「谈论、研读」所积累的浩瀚对话。焚烧塔木德,在象征意义上,是想焚烧一个民族「学习神话语」这一行为本身。然而圣经早已应许,神的话「必不徒然返回」(赛 55:11);而事实证明,塔木德烧不尽——因为「学习」深植在这个民族的骨血里。一个把「研读」奉为至高敬拜的民族,是无法靠火被消灭的。",
                      "<strong>תַּלְמוּד · talmud</strong> — “study, learning.” The vast text put on trial and burned bears, as its name, the word “learning.” It is the fruit of the Jewish people's two-thousand-year practice of “impressing God's words on their children” (Deut 6:7) — the immense conversation accumulated by generation after generation of rabbis “discussing and studying” God's word day and night. To burn the Talmud was, symbolically, an attempt to burn the very act of a people “studying God's word.” Yet Scripture long promised that God's word “will not return empty” (Isa 55:11); and the fact is, the Talmud could not be burned away — because “study” is woven into this people's very blood. A people that holds “study” as its highest worship cannot be destroyed by fire.")),
                step(S4, S4E,
                    p("基督徒读这一课,当心生敬畏与惭愧。敬畏,是因为犹太民族对神话语那种刻骨的爱——「殷勤教训儿女」「昼夜思想」——本是我们当效法的;惭愧,是因为我们的传统曾试图把这份对学习的热爱付之一炬。这一课也邀请我们以谦卑的「学习者」姿态,重新看待犹太的解经传统:其中有许多智慧、深度与对每一个字的认真,能丰富、校正我们读经的方式。「爱我民」,不只是为过去的焚烧悔改,更是带着尊重,向这个仍在 talmud(研读) 神话语的民族,谦卑领受。",
                      "Reading this lesson, Christians should feel awe and shame. Awe, because the Jewish people's bone-deep love for God's word — “impress it on your children,” “meditate on it day and night” — is exactly what we should imitate; shame, because our tradition once tried to set that love of study to the flames. This lesson also invites us into the humble posture of a “learner,” to reconsider the Jewish interpretive tradition: it holds much wisdom, depth, and seriousness about every word that can enrich and correct how we read Scripture. <em>Ahavat Ammi</em> is not only repenting of past burnings, but humbly receiving, with respect, from a people still engaged in <em>talmud</em> — the study of God's word.")),
                step(S5, S5E,
                    ul(
                        ("焚烧塔木德,象征着要焚烧一个民族『学习神话语』的行为本身。这让我对犹太人对神话语的爱,生出怎样的敬畏？",
                         "Burning the Talmud symbolized burning a people's very act of “studying God's word.” What awe does that stir in me toward the Jewish love of Scripture?"),
                        ("犹太传统把『研读』奉为至高敬拜。我对神的话,有这样昼夜思想、殷勤教训儿女的热爱吗？",
                         "The Jewish tradition holds “study” as the highest worship. Do I have that day-and-night love for God's word, impressing it on my children?"),
                        ("以『学习者』的谦卑看待犹太解经传统——其中有哪些能丰富、校正我读经的方式？",
                         "Approaching the Jewish interpretive tradition as a humble “learner” — what in it might enrich and correct how I read Scripture?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "诬告——当谎言点燃火刑",
            "title_en": "The Libels — When Lies Light the Pyre",
            "steps": [
                step(S1, S1E,
                    p("《犹大之杖》里反复出现的,是「反犹诬告」(anti-Jewish libels)——尤其是「血祭诬告」:诬告犹太人为宗教仪式而杀害基督徒儿童取血,以及「亵渎圣体」「投毒水井」等。科恩指出,伊本·维尔加对这些诬告有着痛切的关注,因为正是这些凭空捏造的谎言,一次次点燃了对整个犹太社群的屠杀与驱逐。书中既呈现这些诬告的荒谬与残酷,有时也透过笔下较为「开明」的君王或学者之口,揭穿它们的虚假——仿佛在废墟之上,微弱地呼求一点理性与公义。",
                      "Recurring throughout <em>Shevet Yehudah</em> are the “anti-Jewish libels” — above all the “blood libel”: the false charge that Jews murdered Christian children for blood in their rituals, along with “host desecration” and “well-poisoning.” Cohen notes ibn Verga's anguished attention to these libels, because it was precisely these fabricated lies that again and again ignited massacres and expulsions of whole Jewish communities. The book both portrays the absurdity and cruelty of these libels and, at times through its more “enlightened” kings or scholars, exposes their falsehood — as if, amid the ruins, faintly pleading for a little reason and justice.")),
                step(S2, S2E,
                    bq("「这些事都为耶和华所恨恶……就是吐谎言的假见证,并弟兄中布散纷争的人。」",
                       "“There are things the LORD hates... a false witness who pours out lies and a person who stirs up conflict in the community.”",
                       "《箴言》6:16-19 · Proverbs 6:16-19")),
                step(S3, S3E,
                    p("<strong>דַּם · dam</strong>——「血」。「血祭诬告」是何等黑暗的讽刺:它诬告犹太人取血,而希伯来圣经恰恰最严厉地禁止「吃血」、禁止流无辜人的血——「流人血的,他的血也必被人所流」(创 9:6)。把一项犹太律法本身最严禁的罪,反过来栽赃给守这律法的民族,是「假见证」(<em>edut sheker</em>) 的极致。圣经说,无辜者的 <em>dam</em>(血) 会「从地里向我哀告」(创 4:10)。从中世纪的火刑到后世的大屠杀,那从地里发出的、犹太人无辜的血的哀声,至今仍在向教会的良心发问。",
                      "<strong>דַּם · dam</strong> — “blood.” The “blood libel” is the darkest irony: it accuses Jews of taking blood, while the Hebrew Bible most strictly forbids “eating blood” and shedding innocent blood — “whoever sheds human blood, by humans shall their blood be shed” (Gen 9:6). To pin onto a people the very sin their own Law most forbids is false witness (<em>edut sheker</em>) at its extreme. Scripture says the <em>dam</em> (blood) of the innocent “cries out from the ground” (Gen 4:10). From the medieval pyres to the later Shoah, the cry of innocent Jewish blood rising from the ground still questions the conscience of the Church.")),
                step(S4, S4E,
                    p("这一课不容许任何「话语是无害的」的幻想。《箴言》把神所恨恶的并列:「吐谎言的假见证」与「布散纷争的人」——因为前者必然导向后者。讲台上、谣言里的诬告,从不会停在耳朵里;它会走到街上,拿起石头与火把。对今天的我们,这是一记重锤:我们任凭在心里、教会里、网络上流传的关于犹太人(或任何群体)的「故事」,绝不是中立的。每一个未经查证就接受、转述的偏见,都是在为某一处的暴力添柴。悔改,从拒绝传播谎言、从拒绝相信关于邻舍的虚构版本开始。",
                      "This lesson permits no illusion that “words are harmless.” Proverbs lists side by side what God hates: “a false witness who pours out lies” and “one who stirs up conflict” — because the first inevitably leads to the second. Libel on the pulpit and in rumor never stops in the ear; it walks into the street and takes up stones and torches. For us today this is a hammer blow: the “stories” about Jews (or any group) we allow to circulate in our hearts, churches, and feeds are never neutral. Every prejudice accepted and passed on unverified adds fuel to violence somewhere. Repentance begins with refusing to spread lies — refusing to believe the fictional version of one's neighbor.")),
                step(S5, S5E,
                    ul(
                        ("我是否曾在未经查证的情况下,相信并转述关于某个群体的负面『故事』？",
                         "Have I ever believed and passed on a negative “story” about a group without verifying it?"),
                        ("血祭诬告把犹太律法最严禁的罪,栽赃给守这律法的民族。这种『假见证』的荒谬,如何警醒我？",
                         "The blood libel pinned the sin Jewish law most forbids onto the people who keep that law. How does the absurdity of such “false witness” warn me?"),
                        ("无辜者的血『从地里哀告』。教会该如何面对从中世纪火刑到大屠杀所流的犹太人的血？",
                         "Innocent blood “cries out from the ground.” How should the Church face the Jewish blood shed from medieval pyres to the Shoah?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "殉道者——为神的名而死",
            "title_en": "The Martyrs — Dying for the Name of God",
            "steps": [
                step(S1, S1E,
                    p("科恩讨论书中「殉道与殉道者」的主题。在《犹大之杖》里,一次次出现这样的场景:面对「归信或赴死」的逼迫,无数犹太人选择了死——他们宁可在火中、在刀下失去生命,也不肯否认自己的信仰与他们的神。中世纪犹太传统把这种为信仰而死的行为,称为 <em>Kiddush HaShem</em>(「使神的名成圣」)。伊本·维尔加既以敬畏之心记下这些殉道者的坚贞,有时也透过书中人物,流露出对如此惨烈之苦难的困惑与哀痛。这是全书最沉重、也最圣洁的一页。",
                      "Cohen discusses the book's theme of “martyrdom and martyrs.” Again and again in <em>Shevet Yehudah</em>, the scene recurs: facing the demand to “convert or die,” countless Jews chose death — losing their lives in fire and by the sword rather than deny their faith and their God. The medieval Jewish tradition called this dying for one's faith <em>Kiddush HaShem</em> (“the sanctification of the Name”). Ibn Verga records the steadfastness of these martyrs with reverence, and at times, through his characters, lets show his bewilderment and grief at such terrible suffering. This is the book's heaviest and most holy page.")),
                step(S2, S2E,
                    bq("「我们为你的缘故终日被杀;人看我们如将宰的羊……求你兴起帮助我们,凭你的慈爱救赎我们。」",
                       "“Yet for your sake we face death all day long; we are considered as sheep to be slaughtered... Rise up and help us; rescue us because of your unfailing love.”",
                       "《诗篇》44:22, 26 · Psalm 44:22, 26")),
                step(S3, S3E,
                    p("<strong>קִדּוּשׁ הַשֵּׁם · Kiddush HaShem</strong>——「使神的名成圣」。这个词出自《利未记》22:32:「我在以色列人中,要被尊为圣 (v'nikdashti)。」对犹太传统而言,宁死不否认神,是对神之名最高的尊荣。耐人寻味的是,新约也用了完全相同的逻辑:主祷文第一句就是「愿人都尊你的名为圣」(太 6:9);而耶书亚自己,正是那位以顺服至死、来「荣耀父的名」的那一位(约 12:28; 17:1)。这些为不肯否认神而死的犹太殉道者,以他们的血,活出了犹太与基督信仰共有的、最深的渴望:神的名,在万有之上被尊为圣。",
                      "<strong>קִדּוּשׁ הַשֵּׁם · Kiddush HaShem</strong> — “the sanctification of the Name.” The phrase comes from Leviticus 22:32: “I will be hallowed (<em>v'nikdashti</em>) among the children of Israel.” For the Jewish tradition, to die rather than deny God is the highest honor given to God's name. Strikingly, the New Testament uses exactly the same logic: the first line of the Lord's Prayer is “hallowed be your name” (Matt 6:9); and Yeshua himself is the One who “glorified the Father's name” by obedience unto death (John 12:28; 17:1). These Jewish martyrs who died rather than deny God lived out, in their blood, the deepest longing shared by Jewish and Christian faith: that God's name be hallowed above all things.")),
                step(S4, S4E,
                    p("基督徒站在这些犹太殉道者面前,当俯首。我们必须诚实地承认那令人战栗的事实:许多时候,逼他们「归信或赴死」的,正是举着十字架的人。这是历史最深的悖论与罪:以那位为爱舍命的弥赛亚之名,去逼祂的骨肉之亲为不肯背教而死。这一课呼召我们为这血债深深悔改。同时,它也让我们以全新的敬意,看待犹太人对神之名的忠贞——那份「宁死不否认神」的信,与初代教会众多犹太殉道者的信,本是同一道火。愿我们既为过去哀恸,也被这份至死忠诚的信所激励。",
                      "Before these Jewish martyrs, Christians must bow their heads. We must honestly admit the shuddering fact: many times, those who forced them to “convert or die” were the very people holding up the cross. This is history's deepest paradox and sin: in the name of the Messiah who gave his life for love, to force his own flesh and blood to die rather than apostatize. This lesson calls us to deep repentance for this debt of blood. At the same time, it lets us look with new reverence at the Jewish people's faithfulness to God's name — that faith of “dying rather than denying God” is the same fire as that of the many Jewish martyrs of the early Church. May we both grieve the past and be stirred by this faith, faithful unto death.")),
                step(S5, S5E,
                    ul(
                        ("犹太殉道者宁死不否认神。我的信仰,经得起『归信或赴死』这样的考验吗？",
                         "The Jewish martyrs died rather than deny God. Would my faith withstand a test of “convert or die”?"),
                        ("逼他们赴死的,常是举着十字架的人。这历史最深的悖论,要求我作出怎样的悔改？",
                         "Those who forced them to die often held up the cross. What repentance does this deepest paradox of history require of me?"),
                        ("『使神的名成圣』是犹太与基督信仰共有的渴望。我的生命,是在使神的名成圣,还是使它蒙羞？",
                         "“Sanctifying the Name” is a longing shared by Jewish and Christian faith. Does my life hallow God's name, or profane it?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "被迫归信者——藏在面具下的信",
            "title_en": "The Conversos — Faith Hidden Behind a Mask",
            "steps": [
                step(S1, S1E,
                    p("科恩用专章讨论「被迫归信者与归信」(conversos and conversion)——这也是伊本·维尔加自己最切身的伤口:他极可能就是一位被强迫受洗的犹太人。在西班牙与葡萄牙,成千上万的犹太人在「受洗或被逐/被杀」的逼迫下,表面成了基督徒(conversos / New Christians),许多人却在暗中坚守犹太信仰(被称为 anusim「被强迫者」,或贬称 marranos)。他们活在一个撕裂的处境里:在教堂里画十字,回家却点安息日的灯;永远活在宗教裁判所的猜疑之下,既不被基督徒真正接纳,又与犹太群体被迫分离。伊本·维尔加的书,正是从这个「夹在两个世界之间」的破碎身份里写成的。",
                      "Cohen devotes a chapter to “conversos and conversion” — also ibn Verga's most personal wound, for he was most likely a forcibly baptized Jew himself. In Spain and Portugal, tens of thousands of Jews, under the demand “be baptized or be expelled/killed,” outwardly became Christians (<em>conversos</em> / New Christians), while many secretly kept the Jewish faith (called <em>anusim</em>, “the coerced,” or the slur <em>marranos</em>). They lived torn: crossing themselves in church, lighting Sabbath lamps at home; forever under the suspicion of the Inquisition, never truly accepted by Christians, yet forcibly cut off from the Jewish community. Ibn Verga's book is written precisely out of this broken identity, “caught between two worlds.”")),
                step(S2, S2E,
                    bq("「人是看外貌;耶和华是看内心。」",
                       "“The LORD does not look at the things people look at. People look at the outward appearance, but the LORD looks at the heart.”",
                       "《撒母耳记上》16:7 · 1 Samuel 16:7")),
                step(S3, S3E,
                    p("<strong>אֲנוּסִים · anusim</strong>——「被强迫者」。犹太传统用这个充满怜悯的词,称呼那些<em>在强迫之下</em>外表归信、内心仍忠于神的人——刻意与「自愿背教者」区分开来。这个词背后,是一种深刻而温柔的属灵分辨:神看的不是被刀架在脖子上时口里说了什么,而是内心向谁。《撒母耳记上》16:7「耶和华是看内心」,正是 anusim 全部的盼望所在。当一个体制只凭外在的「受洗记录」就给人贴上「基督徒」的标签,圣经却宣告:那位看透人心的神,认得每一盏在暗中点燃的安息日的灯。",
                      "<strong>אֲנוּסִים · anusim</strong> — “the coerced.” The Jewish tradition uses this compassion-filled word for those who, <em>under coercion</em>, converted outwardly while remaining inwardly faithful to God — deliberately distinguished from “willing apostates.” Behind the word is a deep, tender spiritual discernment: God looks not at what the mouth says with a blade at the throat, but at where the heart turns. 1 Samuel 16:7, “the LORD looks at the heart,” is the entire hope of the <em>anusim</em>. When a system labels a person “Christian” by an outward “baptismal record” alone, Scripture proclaims that the God who sees through the heart recognizes every Sabbath lamp lit in secret.")),
                step(S4, S4E,
                    p("被迫归信者的悲剧,向基督徒提出一个直击核心的问题:信仰,到底是什么?对宗教裁判所而言,「成为基督徒」是一纸受洗证明、一套外在合规。但圣经清楚地宣告,真信仰是「内心」的归向,绝不能被强迫,也无法被强迫——一颗被刀逼出来的「信」,根本不是信。这一课呼召我们悔改:为教会曾把『得人归主』变成『强迫受洗』而悔改。它也提醒我们,真正的福音,永远尊重人心的自由,永远等候那出于自愿的回应。神不要面具下勉强的口头承认;祂要的,是一颗自由地、真实地爱祂的心。",
                      "The tragedy of the conversos puts a question to Christians that strikes the core: what, in fact, is faith? To the Inquisition, “becoming a Christian” was a baptismal certificate, an outward compliance. But Scripture plainly declares that true faith is the “heart's” turning, which cannot be — and must not be — coerced; a “faith” forced out at knifepoint is no faith at all. This lesson calls us to repent: for the Church's turning of “winning people to the Lord” into “forced baptism.” It also reminds us that the true Gospel always honors the freedom of the heart and always waits for a freely given response. God does not want a reluctant verbal confession behind a mask; he wants a heart that freely and truly loves him.")),
                step(S5, S5E,
                    ul(
                        ("对宗教裁判所,信仰是『一纸证明』;对圣经,信仰是『内心的归向』。我心中的『信』,更接近哪一个？",
                         "To the Inquisition, faith was “a certificate”; to Scripture, faith is “the heart's turning.” Which is my own “faith” closer to?"),
                        ("『耶和华是看内心』是 anusim 全部的盼望。神看得见每一盏暗中点燃的灯——这给我怎样的安慰与提醒？",
                         "“The LORD looks at the heart” was the whole hope of the <em>anusim</em>. God sees every lamp lit in secret — what comfort and warning does that give me?"),
                        ("真信仰永远尊重人心的自由。教会把『得人归主』变成『强迫受洗』,我该为此作怎样的悔改？",
                         "True faith always honors the heart's freedom. How should I repent of the Church's turning “winning people” into “forced baptism”?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "神在哪里?——流亡中的信",
            "title_en": "Where Is God? — Faith in Exile",
            "steps": [
                step(S1, S1E,
                    p("科恩强调,《犹大之杖》最深之处,是一部苦难的神学。伊本·维尔加不满足于记录灾难,他像约伯一样,把灾难举到神面前发问:为什么?你的选民,为何承受这无尽的鞭打?他借书中人物之口,探索各种可能的答案——是因以色列自己的罪?是神隐藏的护理?是基督教世界的残暴?他没有给出一个整齐的答案,但他拒绝放弃两样东西:既不放弃对神的信,也不放弃那灼人的发问。这种「在伤口中仍紧抓着神」的信,正是希伯来信仰最深、最诚实的传统。",
                      "Cohen stresses that at its deepest, <em>Shevet Yehudah</em> is a theology of suffering. Ibn Verga is not content to record catastrophe; like Job, he lifts it before God and asks: why? Your chosen people — why do they bear this endless beating? Through his characters he explores various possible answers — is it Israel's own sin? God's hidden providence? the cruelty of Christendom? He gives no tidy answer, but refuses to give up two things: neither his faith in God nor his burning question. This faith that “still clutches God within the wound” is the deepest and most honest tradition of Hebrew faith.")),
                step(S2, S2E,
                    bq("「耶和华啊,你为什么站在远处?在患难的时候为什么隐藏?……耶和华啊,求你起来!神啊,求你举手,不要忘记困苦人。」",
                       "“Why, LORD, do you stand far off? Why do you hide yourself in times of trouble?... Arise, LORD! Lift up your hand, O God. Do not forget the helpless.”",
                       "《诗篇》10:1, 12 · Psalm 10:1, 12")),
                step(S3, S3E,
                    p("<strong>הֶסְתֵּר פָּנִים · hester panim</strong>——「神的隐藏之面」。这是犹太传统用来理解苦难的核心概念之一,出自《申命记》31:17-18:「我必……掩面不顾他们。」它指神在苦难中暂时「隐藏祂的脸」——神并未离开,但祂似乎沉默、似乎遥远。伊本·维尔加的整本书,都活在 <em>hester panim</em> 的张力里:神在哪里?然而,希伯来信仰从不让「隐藏」成为终局。它总与盼望相连:那隐藏的脸,终必再次「向你仰脸」。诗篇里一次次的「你为什么隐藏?」,从来不是无神论的控诉,而是有信者向他确信仍在的神所发的、撕心裂肺的呼求。",
                      "<strong>הֶסְתֵּר פָּנִים · hester panim</strong> — “the hiding of God's face.” One of the Jewish tradition's core concepts for understanding suffering, from Deuteronomy 31:17-18: “I will hide my face from them.” It names God's temporary “hiding of his face” in suffering — God has not left, but he seems silent, seems far. Ibn Verga's whole book lives in the tension of <em>hester panim</em>: where is God? Yet Hebrew faith never lets “hiding” be the end. It is always bound to hope: that hidden face will surely “turn toward you” again. The Psalms' repeated “why do you hide?” is never an atheist's accusation but the heart-rending cry of a believer to the God he is sure is still there.")),
                step(S4, S4E,
                    p("基督徒在十字架上看见这个奥秘的顶点。耶书亚在十字架上喊出的,正是一句希伯来的哀歌——「我的神,我的神,为什么离弃我?」(太 27:46; 诗 22:1) 神并没有回避「神在哪里」的问题;在弥赛亚里,神<em>亲自走进了</em>那「隐藏之面」的黑暗中心。这并不「解释」掉犹太民族所受的苦难——没有任何神学能轻巧地解释它。但它意味着:当伊本·维尔加和无数受苦的犹太人低声问「神在哪里」时,基督徒至少不能用居高临下的答案打发他们。我们只能与哀哭的人同哭,并指向那位同样被弃绝、同样在黑暗中呼喊、却最终带来复活之光的弥赛亚。",
                      "Christians see the summit of this mystery at the cross. The cry Yeshua utters there is a Hebrew lament — “My God, my God, why have you forsaken me?” (Matt 27:46; Ps 22:1). God did not dodge the question “where is God?”; in the Messiah, God <em>walked himself</em> into the dark center of that “hidden face.” This does not “explain away” the suffering of the Jewish people — no theology explains it lightly. But it means that when ibn Verga and countless suffering Jews whisper “where is God?” a Christian cannot answer from above. We can only weep with those who weep, and point to the Messiah who was likewise forsaken, who likewise cried in the darkness, and who finally brought the light of resurrection.")),
                step(S5, S5E,
                    ul(
                        ("伊本·维尔加在伤口中『既不放弃信,也不放弃发问』。我能否同时容纳坚定的信与撕心的质问？",
                         "In his wound, ibn Verga “gave up neither faith nor question.” Can I hold both steadfast faith and heart-rending protest at once?"),
                        ("『神的隐藏之面』不是终局,总与盼望相连。当神似乎沉默时,我如何持守这份盼望？",
                         "The “hiding of God's face” is not the end; it is always bound to hope. When God seems silent, how do I hold that hope?"),
                        ("耶书亚在十字架上也喊出『为什么离弃我』。这如何改变我安慰受苦者的方式——从给答案,到同哭？",
                         "Yeshua too cried “why have you forsaken me?” on the cross. How does that change how I comfort the suffering — from giving answers to weeping with them?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "圭必不离犹大——那未曾折断的杖",
            "title_en": "The Scepter Shall Not Depart — The Rod That Was Not Broken",
            "steps": [
                step(S1, S1E,
                    p("走到全书的尽头,我们终于可以回到那个意味深长的书名:《犹大之杖》(Shevet Yehudah)。科恩指出,这书名几乎必然在向《创世记》49:10 致意——雅各对犹大的祝福:「<em>圭必不离犹大</em>,杖必不离他两脚之间,直等细罗 (Shiloh) 来到,万民都必归顺。」一个被驱逐、被鞭打、被迫受洗的民族,给自己满载苦难的书,起了一个出自弥赛亚应许的名字。这是何等的信心:即使在 1492 年最深的黑暗里,这个民族仍在宣告——犹大的「杖」(那应许的王权与弥赛亚)没有、也绝不会折断。",
                      "Reaching the book's end, we can finally return to its significant title: <em>Shevet Yehudah</em> (The Scepter of Judah). Cohen notes the title almost surely alludes to Genesis 49:10 — Jacob's blessing of Judah: “<em>The scepter shall not depart from Judah</em>, nor the ruler's staff from between his feet, until Shiloh comes, and the obedience of the nations shall be his.” A people expelled, beaten, and forcibly baptized gave their book laden with suffering a name drawn from the messianic promise. What faith: even in the deepest darkness of 1492, this people still proclaimed that the “scepter” of Judah — the promised royal authority and the Messiah — had not, and never would, depart.")),
                step(S2, S2E,
                    bq("「圭必不离犹大,杖必不离他两脚之间,直等细罗(Shiloh)来到,万民都必归顺。」",
                       "“The scepter will not depart from Judah, nor the ruler's staff from between his feet, until he to whom it belongs shall come and the obedience of the nations shall be his.”",
                       "《创世记》49:10 · Genesis 49:10")),
                step(S3, S3E,
                    p("<strong>שִׁילֹה · Shiloh</strong>——「细罗」「那应许归属之人」。这个古老而神秘的词,历世历代的犹太与基督教解经者,都把它读作对<em>弥赛亚</em>的指称——那位犹大支派要兴起的、万民要归顺的王。《犹大之杖》的全部张力,都收束在这一个词的盼望里:无论流亡多么漫长、鞭杖多么沉重,犹大的杖之所以「必不离」,是因为它在等候 <em>Shiloh</em> 的来到。对相信耶书亚的我们而言,这正是那从马槽、十字架、空坟墓里向全地敞开的好消息:那位「万民要归顺」的细罗,已经来了;而祂还要再来,使犹大的杖,在荣耀中永不折断。",
                      "<strong>שִׁילֹה · Shiloh</strong> — “Shiloh,” “the one to whom it belongs.” This ancient, mysterious word, Jewish and Christian interpreters across the ages have read as a reference to the <em>Messiah</em> — the king to rise from the tribe of Judah, to whom the nations will turn. The whole tension of <em>Shevet Yehudah</em> gathers into the hope of this one word: however long the exile, however heavy the rod, the scepter of Judah “shall not depart” because it awaits the coming of <em>Shiloh</em>. For those of us who believe in Yeshua, this is the very good news opened to all the earth from the manger, the cross, the empty tomb: the Shiloh “to whom the nations will turn” has come; and he will come again, that the scepter of Judah may, in glory, never be broken.")),
                step(S4, S4E,
                    p("这是整份指南的终点,也是它出人意料的盼望。我们走过了驱逐、辩论、焚书、诬告、火刑、被迫归信、与「神在哪里」的呼号——这一切的重量,几乎要把人压垮。然而,这一切苦难的记录,竟以一个弥赛亚的盼望为名。愿这八堂课塑造我们:成为既深深为教会的过去悔改、又满怀「爱我民」之心的人;与那受苦却不折断的犹太民族同站,既诚实地哀恸历史的血债,又满怀盼望地与他们一同等候——等候那一日,犹大的「杖」所盼望的细罗,向以色列全家显明祂自己,万民都在祂里面,弟兄和睦同居,蒙耶和华命定永远的福。",
                      "This is the end of the whole guide, and its unexpected hope. We have journeyed through expulsion, disputation, the burning of books, libel, the pyre, forced conversion, and the cry “where is God?” — a weight that nearly crushes. And yet this whole record of suffering bears the name of a messianic hope. May these eight lessons shape us into people who deeply repent of the Church's past and are full of <em>Ahavat Ammi</em>; who stand with the Jewish people, beaten yet unbroken, honestly grieving history's debt of blood while waiting in hope alongside them — for the day when the Shiloh whom the scepter of Judah awaited reveals himself to all Israel, and the nations are gathered in him, living together in unity, and the LORD bestows his blessing forevermore."),),
                step(S5, S5E,
                    ul(
                        ("一个被驱逐的民族,给苦难之书起了一个出自弥赛亚应许的名字。这是怎样不可摧毁的盼望？",
                         "An expelled people named their book of suffering after a messianic promise. What kind of unbreakable hope is that?"),
                        ("『圭必不离犹大,直等细罗来到』。对相信耶书亚的我,这节经文如何成为向以色列述说的好消息？",
                         "“The scepter shall not depart from Judah, until Shiloh comes.” For me who believes in Yeshua, how is this verse good news to tell Israel?"),
                        ("走完这段沉重的历史,我会以什么具体的行动,去『记念』、悔改,并带着盼望去爱犹太民族？",
                         "Having finished this heavy history, what concrete action will I take to remember, repent, and love the Jewish people in hope?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "为那未曾折断的杖、为合一的盼望祝祷",
    "closing_title_en": "A Blessing for the Unbroken Scepter, and the Hope of Unity",
    "closing_zh": "「愿耶和华使祂的脸光照你,赐恩给你。」<br/><br/>愿你听见了《犹大之杖》里那些受苦的声音,也记住了他们;<br/>愿你为那以『基督』之名所流的无辜之血,哀恸、悔改;<br/>愿你与那受苦却不折断的犹太民族同站,<br/>既诚实地记念,又满怀盼望。<br/><br/>因为圭必不离犹大,<br/>直等那位细罗(Shiloh)来到——<br/>愿你认得祂:就是那位为以色列、也为万民,<br/>使犹大的杖在荣耀中永不折断的弥赛亚,耶书亚。",
    "closing_en": "“The LORD make his face shine upon you and be gracious to you.”<br/><br/>May you have heard the suffering voices in the Scepter of Judah, and may you remember them.<br/>May you grieve and repent of the innocent blood shed in the name of “Christ.”<br/>May you stand with the Jewish people, beaten yet unbroken,<br/>remembering honestly, and full of hope.<br/><br/>For the scepter shall not depart from Judah,<br/>until Shiloh comes —<br/>may you know him: the Messiah who, for Israel and for all nations,<br/>keeps the scepter of Judah unbroken in glory: Yeshua.",
}

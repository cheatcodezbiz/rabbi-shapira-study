# -*- coding: utf-8 -*-
"""Content module for study-charity-traditions.html.

Julia R. Lieberman, Michal Jan Rozbicki, and Thomas Adam (eds.), *Charity in
Jewish, Christian, and Islamic Traditions* (Lexington / Rowman & Littlefield).
"""

RHYTHM_ZH = """        <strong>① 学者说什么</strong>—— 用书中学者的研究，呈现某一传统的施予；<br/>
        <strong>② 关键经文</strong>—— 与之相关的圣经；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，照亮「施予」的真义；<br/>
        <strong>④ 基督徒视角</strong>—— 这如何指向那位先施予我们的神；<br/>
        <strong>⑤ 诚实的提问</strong>—— 留给你与小组省察的问题。"""

RHYTHM_EN = """        <strong>① What the Scholars Say</strong> — a tradition's giving, in the book's research;<br/>
        <strong>② Key Scripture</strong> — the related biblical text;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that lights up the true sense of “giving”;<br/>
        <strong>④ A Christian Lens</strong> — how this points to the God who gave to us first;<br/>
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
    "title_tag": "《犹太、基督与伊斯兰传统中的慈善》研习指南 · Charity in the Abrahamic Traditions — Study Guide · 妥拉之光",
    "meta_desc": "A study guide to Charity in Jewish, Christian, and Islamic Traditions — eight bilingual lessons on tzedakah, caritas, and sadaqa, on giving as justice and as worship, read with Hebrew eyes and a Christian lens.",
    "og_title": "Charity in Jewish, Christian, and Islamic Traditions — A Study Guide",
    "og_desc": "Eight bilingual lessons on charity across the Abrahamic faiths — tzedakah as justice, caritas as love, sadaqa as sincerity — and the God who gave to us first.",
    "cover_alt": "Charity in Jewish, Christian, and Islamic Traditions — Study Guide",
    "tagline_zh": "研习指南 · 施予的灵性 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · The Spirituality of Giving · 2026 · 5 · 31",
    "headline_zh": "犹太、基督与伊斯兰<br/>传统中的慈善",
    "headline_en": "Charity in the<br/>Abrahamic Traditions",
    "deck_zh": "八堂课程，跟随一部跨学科文集，比较慈善（施予）在犹太、基督、伊斯兰三大传统中的根基与实践——犹太的「公义之施」(tzedakah)、基督的「爱」(caritas)、伊斯兰的「真诚之施」(sadaqa)。透过「施予」这扇窗，我们窥见每一个民族最深的价值，也看见那位先把万有白白赐给我们的神。",
    "deck_en": "Eight lessons following an interdisciplinary volume comparing charity (giving) across the Jewish, Christian, and Islamic traditions — Jewish <em>tzedakah</em> (giving as justice), Christian <em>caritas</em> (love), and Islamic <em>sadaqa</em> (giving as sincerity). Through the window of “giving,” we glimpse a people's deepest values — and see the God who first gave us all things freely.",
    "byline_zh": "基于茱莉亚·利伯曼 (Julia R. Lieberman) 等编《犹太、基督与伊斯兰传统中的慈善》(Lexington / Rowman & Littlefield)",
    "byline_en": "Based on Charity in Jewish, Christian, and Islamic Traditions, edited by Julia R. Lieberman, Michal Jan Rozbicki, and Thomas Adam (Lexington / Rowman & Littlefield)",
    "readtime_zh": "约 55 分钟通读",
    "readtime_en": "~55 min read-through",
    "book_url": "https://rowman.com/ISBN/9781498560856",
    "book_link_zh": "购买原书 · Rowman & Littlefield",
    "book_link_en": "Get the Book · Rowman &amp; Littlefield",
    "cta_url": "https://rowman.com/ISBN/9781498560856",
    "cta_zh": "购买《犹太、基督与伊斯兰传统中的慈善》原书",
    "cta_en": "Get the Book — Charity in Jewish, Christian, and Islamic Traditions",

    "lead_zh": "这份指南陪你读一部跨学科的学术文集,它把「慈善」(charity / 施予) 当作一面棱镜,折射出犹太、基督、伊斯兰三大传统最深的价值。编者指出,慈善是一扇罕有的窗:一个民族<em>如何施予、为何施予、施予给谁</em>,几乎透露出它对神、对人、对正义的全部信念。这本书既探讨慈善背后的「理论难题」(施予真的纯粹吗?还是隐藏着权力与「区隔他者」?),也细致地呈现三大传统在历史中真实的施予实践。对相信耶书亚的我们而言,这是一次宝贵的机会:重新发现,「施予」在圣经里,从来不是「行有余力的善举」,而是信仰的心跳本身。",
    "lead_en": "This guide walks you through an interdisciplinary scholarly volume that treats “charity” (giving) as a prism, refracting the deepest values of the Jewish, Christian, and Islamic traditions. The editors note that charity is a rare window: <em>how a people gives, why it gives, and to whom</em> reveals almost the whole of its convictions about God, humanity, and justice. The book explores both the “theoretical puzzles” behind charity (is giving ever pure? or does it hide power and the “othering” of the recipient?) and the real historical practices of giving across the three traditions. For those of us who believe in Yeshua, this is a precious chance to rediscover that “giving,” in Scripture, was never an “optional good deed for the well-off,” but the very heartbeat of faith.",

    "intro": [
        p("这本书有一个对基督徒尤其宝贵的发现:在希伯来语里,「慈善」这个词是 <em>tzedakah</em>——而它的字根意思是「公义、公正」。也就是说,在犹太传统里,接济穷人根本不是「可做可不做的好心」,而是「公义的本分」——是把<em>本就属于穷人的</em>那一份还给他们。这个洞见,会彻底改变我们对「施予」的理解。更奇妙的是:阿拉伯语的「施予」<em>sadaqa</em>,与希伯来语的 <em>tzedakah</em>,来自同一个闪族语字根。三大信仰对「施予」的理解,在最深处,共享着同一条「公义」的根。",
          "This book holds a discovery especially precious for Christians: in Hebrew, the word for “charity” is <em>tzedakah</em> — and its root means “righteousness, justice.” That is, in the Jewish tradition, helping the poor is not “optional kindness” but “an obligation of justice” — returning to the poor the portion that <em>already belongs</em> to them. This insight transforms our whole understanding of “giving.” More remarkably still: the Arabic word for giving, <em>sadaqa</em>, comes from the same Semitic root as Hebrew <em>tzedakah</em>. At their deepest, the three faiths' understanding of “giving” shares one and the same root of “justice.”"),
        p("本指南共 <strong>八堂课</strong>，循着书中的理论与实践展开。每一堂遵循同样的五部分节奏：",
          "The guide is structured as <strong>eight lessons</strong>, following the book's theory and practice. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句提醒:这本书会挑战我们,把「慈善」从「有余力时的施舍」,重新理解为「信仰的核心要求」。愿这八堂课不只更新你的头脑,更松开你的手与心。",
          "A word of note: this book will challenge us to relearn “charity” from “almsgiving when we have a surplus” into “a central demand of faith.” May these eight lessons renew not only your mind but loosen your hands and heart."),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "施予——窥见一个民族灵魂的窗",
            "title_en": "Giving — A Window into a People's Soul",
            "steps": [
                step(S1, S1E,
                    p("编者在导论中提出本书的核心方法:把「慈善」当作一面棱镜。他们写道,慈善的种种观念,「是窥见一个民族共有价值模型的窗口」;一个社会<em>如何</em>对待它最软弱的成员,几乎暴露出它关于神、人、正义的全部信念。比较三大传统的施予,不是为了评判高下,而是为了在彼此的映照中,更深地理解每一个传统——以及理解「施予」这一人类行为本身,何以承载着如此沉重的神圣意义。",
                      "In the introduction, the editors propose the book's core method: treating “charity” as a prism. They write that concepts of charity “serve as a window into a people's shared models of cultural value”; how a society treats its weakest members lays bare almost the whole of its convictions about God, humanity, and justice. Comparing the giving of the three traditions is not to rank them but, in mutual reflection, to understand each more deeply — and to grasp why the human act of “giving” itself carries such weighty sacred meaning.")),
                step(S2, S2E,
                    bq("「在神我们的父面前,那清洁没有玷污的虔诚,就是看顾在患难中的孤儿寡妇。」",
                       "“Religion that God our Father accepts as pure and faultless is this: to look after orphans and widows in their distress.”",
                       "《雅各书》1:27 · James 1:27")),
                step(S3, S3E,
                    p("<strong>צְדָקָה · tzedakah</strong>——「公义 / 慈善」。这是整本书、也是整个犹太施予观的钥匙词。同一个 <em>tzedakah</em>,既指「公义、公正」,又指「接济穷人」。这绝非巧合:在希伯来思想里,帮助穷人<em>就是</em>行公义。把多余的施舍给人,不是慷慨的恩赐,而是归还公义的亏欠——因为大地与其上的丰盛本属于神,而神早已命定其中有一份是留给穷人的。当「慈善」与「公义」共用一个词,整个施予的逻辑就被翻转了:施予不是「我大方」,而是「我守义」。",
                      "<strong>צְדָקָה · tzedakah</strong> — “righteousness / charity.” This is the key word of the whole book and of the entire Jewish view of giving. The one word <em>tzedakah</em> means both “righteousness, justice” and “helping the poor.” This is no coincidence: in Hebrew thought, to help the poor <em>is</em> to do justice. Giving away one's surplus is not a generous gift but the repayment of a debt of justice — for the earth and its fullness belong to God, who long ago decreed that a portion within it is set aside for the poor. When “charity” and “justice” share one word, the whole logic of giving is overturned: giving is not “I am generous,” but “I am keeping justice.”")),
                step(S4, S4E,
                    p("这个犹太式的洞见,深深扎根于整本圣经,也直接塑造了新约的信仰。雅各书说,「清洁没有玷污的虔诚」不是某种属灵的高言大智,而是「看顾在患难中的孤儿寡妇」——这正是先知阿摩司、以赛亚的一贯呼声:神厌恶那有敬拜之名、却无公义之实的宗教。耶书亚也宣告,末日万民受审,凭据竟是「我饿了,你们给我吃……这些事你们既作在我这弟兄中一个最小的身上,就是作在我身上了」(太 25:35-40)。对神而言,我们如何对待最软弱的人,就是我们如何对待祂。",
                      "This Jewish insight is rooted deep in all of Scripture and directly shaped the faith of the New Testament. James says that “pure and faultless religion” is not some lofty spiritual wisdom but “looking after orphans and widows in their distress” — the constant cry of the prophets Amos and Isaiah: God loathes a religion that bears the name of worship but lacks the substance of justice. Yeshua declares that at the final judgment of all nations, the evidence is “I was hungry and you gave me something to eat... whatever you did for one of the least of these brothers of mine, you did for me” (Matt 25:35-40). To God, how we treat the weakest is how we treat him.")),
                step(S5, S5E,
                    ul(
                        ("『慈善』与『公义』共用一个词。这如何翻转我对施予的理解——从『我大方』到『我守义』？",
                         "“Charity” and “justice” share one word. How does that overturn my view of giving — from “I am generous” to “I am keeping justice”?"),
                        ("雅各说『清洁的虔诚』就是看顾孤儿寡妇。我的『虔诚』,有没有这清洁的实质？",
                         "James says “pure religion” is caring for orphans and widows. Does my “devotion” have that pure substance?"),
                        ("『作在最小的身上,就是作在我身上』。这如何改变我看待身边最软弱之人的眼光？",
                         "“Whatever you did for the least, you did for me.” How does that change how I see the weakest people around me?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "公义之施——犹太传统的 Tzedakah",
            "title_en": "Giving as Justice — The Jewish Tzedakah",
            "steps": [
                step(S1, S1E,
                    p("书中关于犹太慈善的篇章（如论伦敦的西班牙葡萄牙犹太社群的 sedaca,以及从「慈善」到「慈善事业」的转变）展现了一个高度发达、组织严密的施予体系。犹太社群把 <em>tzedakah</em> 制度化为一种集体责任:有专门的基金、专职的管理者、细致的分配规则。迈蒙尼德更列出著名的「施予的八个层级」,从最低的「不情愿地给」,到最高的「帮一个穷人自立、使他不再需要施予」。这套体系背后的信念是:接济穷人不是个人随心的善举,而是整个信仰群体必须共同承担的、神圣的义务。",
                      "The book's chapters on Jewish charity (such as the <em>sedaca</em> of London's Spanish-Portuguese Jewish community, and the shift “from charity to philanthropy”) reveal a highly developed, tightly organized system of giving. Jewish communities institutionalized <em>tzedakah</em> as a collective responsibility: dedicated funds, professional administrators, detailed rules of distribution. Maimonides famously listed the “eight levels of giving,” from the lowest — “giving grudgingly” — to the highest — “helping a poor person become self-sufficient so that he no longer needs charity.” The conviction behind this system: helping the poor is not an individual's whim of kindness, but a sacred obligation the whole community of faith must bear together.")),
                step(S2, S2E,
                    bq("「在你弟兄中,若有一个穷人……你总要向他松开手,照他所缺乏的借给他。」",
                       "“If anyone is poor among your fellow Israelites... do not be hardhearted or tightfisted toward them. Rather, be openhanded and freely lend them whatever they need.”",
                       "《申命记》15:7-8 · Deuteronomy 15:7-8")),
                step(S3, S3E,
                    p("<strong>מַעֲשֵׂר · ma'aser</strong>——「十分之一、什一奉献」。妥拉规定以色列要拿出土产的十分之一,其中特别有一份是给「寄居的、孤儿、寡妇」的(申 14:28-29)。此外还有「拾遗」的律法:收割时不可割尽田角,掉落的不可拾取,要留给穷人(利 19:9-10)。这些律法启示出一个深刻的经济神学:在神的世界里,穷人对你的产业,拥有一种<em>合法的份额</em>。施予,因此是把神早已留给他们的那一份,亲手送达。<em>ma'aser</em> 不是「我的钱我捐出去」,而是「神的钱,我转交」。",
                      "<strong>מַעֲשֵׂר · ma'aser</strong> — “a tenth, the tithe.” The Torah requires Israel to set aside a tenth of the produce, with a portion specifically for “the foreigner, the fatherless, and the widow” (Deut 14:28-29). There are also the gleaning laws: at harvest, do not reap the corners of the field or pick up what falls — leave it for the poor (Lev 19:9-10). These laws reveal a profound economic theology: in God's world, the poor hold a <em>lawful share</em> in your produce. Giving, therefore, is the hand-delivery of the portion God already set aside for them. <em>Ma'aser</em> is not “my money, which I donate,” but “God's money, which I pass along.”")),
                step(S4, S4E,
                    p("犹太传统这种「制度化、共同承担」的施予,对今天的教会是一面校正的镜子。我们容易把奉献理解为「个人的、情绪驱动的、临时起意的」——心情好就多给,手头紧就少给。但圣经的视野更宏大:神要建立一个<em>整全的怜悯的群体</em>,在其中,照顾软弱者是有结构、有规律、有委身的集体生命。初代教会正是如此——「凡物公用」,「照各人所需用的分给各人」,以致「内中没有一个缺乏的」(徒 4:32-35)。这不是乌托邦,而是一个把 <em>tzedakah</em> 活出来的群体的样式。",
                      "The Jewish tradition's “institutionalized, shared” giving is a corrective mirror for the Church today. We easily understand giving as “individual, emotion-driven, and impulsive” — give more in a good mood, less when money is tight. But Scripture's vision is grander: God means to build a <em>whole community of mercy</em>, in which caring for the weak is a structured, regular, committed collective life. The early Church was just so — “they shared everything,” “distributed to anyone who had need,” so that “there were no needy persons among them” (Acts 4:32-35). This is no utopia but the pattern of a community living out <em>tzedakah</em>.")),
                step(S5, S5E,
                    ul(
                        ("迈蒙尼德的最高施予,是帮穷人自立。我的施予,是让人更有尊严、更能自立,还是只让人更依赖？",
                         "Maimonides' highest giving helps the poor become self-sufficient. Does my giving restore dignity and independence, or only deepen dependence?"),
                        ("『穷人对你的产业拥有合法的份额』。这如何改变我对『我的钱』的认识？",
                         "“The poor hold a lawful share in your produce.” How does that change how I think about “my money”?"),
                        ("圣经要建立的是『整全的怜悯群体』,而非『个人临时的善举』。我的群体,在结构上关心软弱者吗？",
                         "Scripture builds “a whole community of mercy,” not “individual impulse.” Does my community care for the weak structurally?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "爱——基督传统的 Caritas",
            "title_en": "Love — The Christian Caritas",
            "steps": [
                step(S1, S1E,
                    p("书中关于基督教慈善的篇章（如论意大利慈善、罗马天主教的「领受性」）追溯了「caritas」——这个拉丁词,既是「慈善」,也是「爱」。在基督教传统里,施予的根基不是律法的义务,而是<em>爱</em>:因着神先在基督里爱了我们,我们便以爱回流向人。早期教会和中世纪修道院发展出医院、济贫院、收容所等大量的慈善机构;「七项慈悲的善工」(给饥饿者食物、给口渴者水、收留客旅、给赤身者衣裳、探望病人与监犯、埋葬死者) 成为信徒效法基督的具体操练。caritas 把「施予」从一种交易,提升为一种与神之爱相联的属灵生命。",
                      "The book's chapters on Christian charity (such as Italian charity and Roman Catholic “receptivity”) trace <em>caritas</em> — the Latin word that means both “charity” and “love.” In the Christian tradition, the ground of giving is not legal obligation but <em>love</em>: because God first loved us in the Messiah, we let love flow back out to people. The early Church and medieval monasteries developed a vast array of charitable institutions — hospitals, almshouses, shelters; the “seven works of mercy” (feed the hungry, give drink to the thirsty, shelter the stranger, clothe the naked, visit the sick and the imprisoned, bury the dead) became a concrete discipline of imitating Christ. <em>Caritas</em> lifts “giving” from a transaction into a spiritual life joined to the love of God.")),
                step(S2, S2E,
                    bq("「我们爱,因为神先爱我们……人若说我爱神,却恨他的弟兄,就是说谎话的。」",
                       "“We love because he first loved us... Whoever claims to love God yet hates a brother or sister is a liar.”",
                       "《约翰一书》4:19-20 · 1 John 4:19-20")),
                step(S3, S3E,
                    p("<strong>אַהֲבָה · ahavah</strong>——「爱」。拉丁的 caritas、希腊的 agape,在希伯来圣经里的根,是 <em>ahavah</em>。妥拉早已把这爱的命令并立为两条:「你要尽心、尽性、尽力<em>爱</em>耶和华你的神」(申 6:5),与「要<em>爱</em>人如己」(利 19:18)。耶书亚把这两条并为「律法和先知一切道理的总纲」(太 22:40)。基督教的 caritas 因此不是凭空的发明,而是这条古老 <em>ahavah</em> 命令的延续与成全:对神的爱,必然外溢为对人的爱;爱神而不爱弟兄,约翰说,是「说谎话的」。施予,是 <em>ahavah</em> 看得见的身体。",
                      "<strong>אַהֲבָה · ahavah</strong> — “love.” The root of Latin <em>caritas</em> and Greek <em>agape</em> in the Hebrew Bible is <em>ahavah</em>. The Torah already set the command of love as two: “<em>Love</em> the LORD your God with all your heart, soul, and strength” (Deut 6:5), and “<em>Love</em> your neighbor as yourself” (Lev 19:18). Yeshua joined these two as the summary on which “all the Law and the Prophets hang” (Matt 22:40). Christian <em>caritas</em> is thus no invention from nowhere but the continuation and fulfillment of this ancient command of <em>ahavah</em>: love for God necessarily overflows into love for people; to love God and not one's brother, John says, is to be “a liar.” Giving is the visible body of <em>ahavah</em>.")),
                step(S4, S4E,
                    p("这一课把基督徒的施予,带回它真正的源头与动力。我们施予,不是为了「赚取」神的喜悦或自己的功德(那会让施予沦为另一种交易),而是因为我们自己<em>先被白白地爱了、白白地施予了</em>。「你们白白地得来,也要白白地舍去」(太 10:8)。十字架是史上最伟大的施予——「神爱世人,甚至将他的独生子赐给他们」(约 3:16)。当我们真的领受了这份白白的爱,施予就不再是勉强的责任,而成了一种<em>满溢</em>:被爱充满的器皿,自然地向外倾倒。caritas 的奥秘是:我们最先,是领受者。",
                      "This lesson carries Christian giving back to its true source and power. We give not to “earn” God's favor or our own merit (which would make giving just another transaction), but because we ourselves were <em>first freely loved and freely given to</em>. “Freely you have received; freely give” (Matt 10:8). The cross is the greatest gift in history — “For God so loved the world that he gave his one and only Son” (John 3:16). When we truly receive this free love, giving is no longer a reluctant duty but an <em>overflow</em>: a vessel filled with love pours out naturally. The mystery of <em>caritas</em>: we are, first of all, receivers.")),
                step(S5, S5E,
                    ul(
                        ("我施予,是为了『赚取』神的喜悦或功德,还是因为我『先被白白地爱了』？",
                         "Do I give to “earn” God's favor or merit, or because I was “first freely loved”?"),
                        ("『爱神却恨弟兄,就是说谎话的』。我对神的爱,是否真的外溢为对身边人具体的施予？",
                         "“To love God yet hate a brother is to be a liar.” Does my love for God truly overflow into concrete giving to those around me?"),
                        ("caritas 的奥秘是『我们最先是领受者』。我是否常常忘了自己先领受了多少,以致施予时心生勉强？",
                         "The mystery of <em>caritas</em> is “we are first receivers.” Do I forget how much I first received, so that giving feels reluctant?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "真诚之施——伊斯兰传统的 Sadaqa 与 Zakat",
            "title_en": "Giving as Sincerity — The Islamic Sadaqa and Zakat",
            "steps": [
                step(S1, S1E,
                    p("书中关于伊斯兰慈善的篇章（如「sadaqa 作为真诚的标记」、奥斯曼帝国的犹太与穆斯林慈善）介绍了伊斯兰施予的两大支柱:<em>zakat</em>(天课)——一种规定比例、带有义务性质的济贫税,是伊斯兰「五功」之一;以及 <em>sadaqa</em>——更广义的、自愿的善行施予。学者指出,在伊斯兰传统里,施予被理解为一种「净化」:既净化财富,也净化施予者的心;<em>sadaqa</em>(其字面与「真诚 sidq」相关)更被视为信仰真诚的外在标志——一个人是否真信,看他是否愿意为神而施予。",
                      "The book's chapters on Islamic charity (such as “<em>sadaqa</em> as a sign of sincerity” and Jewish and Muslim charity in the Ottoman Empire) introduce the two pillars of Islamic giving: <em>zakat</em> (the obligatory alms) — a fixed-proportion, obligatory levy for the poor, one of Islam's “five pillars”; and <em>sadaqa</em> — the broader, voluntary giving of good works. Scholars note that in the Islamic tradition, giving is understood as a “purification”: purifying both wealth and the giver's heart; <em>sadaqa</em> (whose word is related to <em>sidq</em>, “sincerity”) is seen as the outward sign of true faith — whether a person truly believes is shown by whether they are willing to give for God's sake.")),
                step(S2, S2E,
                    bq("「你手若有行善的力量,不可推辞,就当向那应得的人施行。」",
                       "“Do not withhold good from those to whom it is due, when it is in your power to act.”",
                       "《箴言》3:27 · Proverbs 3:27")),
                step(S3, S3E,
                    p("<strong>צֶדֶק · tzedek</strong>——「公义」。这里藏着一个令人惊叹的事实:阿拉伯语的 <em>sadaqa</em>(施予) 与希伯来语的 <em>tzedakah</em>(慈善/公义),来自<em>同一个</em>闪族语字根 ṣ-d-q,本义都是「公义、真实、可靠」。换言之,在希伯来与阿拉伯这两种姊妹语言里,「施予穷人」与「公义、真诚」共享着同一条最深的语言之根。这绝非偶然,它指向一个三大亚伯拉罕信仰所共有的、深植的直觉:对穷人的施予,本质上是一件关乎<em>公义与真诚</em>的事——它是真信仰的试金石,是把内心对神的敬畏,翻译成对人具体的善行。",
                      "<strong>צֶדֶק · tzedek</strong> — “righteousness, justice.” Here lies an astonishing fact: the Arabic <em>sadaqa</em> (giving) and the Hebrew <em>tzedakah</em> (charity/justice) come from the <em>same</em> Semitic root ṣ-d-q, both originally meaning “righteousness, truth, reliability.” In other words, in these two sister languages, Hebrew and Arabic, “giving to the poor” and “justice, sincerity” share the same deepest linguistic root. This is no accident; it points to a deep-seated intuition shared by all three Abrahamic faiths: that giving to the poor is essentially a matter of <em>justice and sincerity</em> — the touchstone of true faith, translating the heart's reverence for God into concrete good toward people.")),
                step(S4, S4E,
                    p("这一课邀请基督徒在「施予是信仰真诚的标记」这一点上,与犹太、穆斯林邻舍一同站立——并把它推向新约的深度。雅各书几乎说了与「sadaqa 是信仰真诚之标志」一模一样的话:「信心若没有行为就是死的……若是弟兄或姐妹赤身露体,又缺了日用的饮食,你们中间有人……不给他们身体所需用的,这有什么益处呢?」(雅 2:14-17) 真信心,从来不是嘴上的承认,而是会动手、会松手的爱。施予,因此是检验我们信仰之真伪的、最诚实的一面镜子。一个不肯施予的「信」,圣经说,是死的。",
                      "This lesson invites Christians to stand with their Jewish and Muslim neighbors on the point that “giving is a sign of sincere faith” — and to press it to New Testament depth. James says almost exactly what “<em>sadaqa</em> is the mark of sincere faith” says: “Faith without deeds is dead... Suppose a brother or sister is without clothes and daily food. If one of you... does nothing about their physical needs, what good is it?” (James 2:14-17). True faith is never a verbal confession but a love that acts and lets go. Giving is therefore the most honest mirror testing whether our faith is real or false. A “faith” unwilling to give, Scripture says, is dead.")),
                step(S5, S5E,
                    ul(
                        ("阿拉伯语 sadaqa 与希伯来语 tzedakah 同根。三大信仰共享『施予 = 公义与真诚』的直觉——这给我怎样的启发？",
                         "Arabic <em>sadaqa</em> and Hebrew <em>tzedakah</em> share a root. The three faiths share the intuition “giving = justice and sincerity” — what does that teach me?"),
                        ("施予被视为信仰真诚的标志。如果有人凭我的施予来判断我信仰的真伪,他会看见什么？",
                         "Giving is seen as a sign of sincere faith. If someone judged the reality of my faith by my giving, what would they see?"),
                        ("雅各说『信心没有行为就是死的』。我的信心,是会动手、会松手的爱,还是只停在口里的承认？",
                         "James says “faith without deeds is dead.” Is my faith a love that acts and lets go, or only a verbal confession?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "礼物的两张脸——施予会「区隔」他者吗?",
            "title_en": "The Two Faces of the Gift — Does Giving “Other” the Receiver?",
            "steps": [
                step(S1, S1E,
                    p("本书理论部分提出一个尖锐的问题:慈善是不是一个「两面神」(Janus)?学者们(借用人类学对「礼物」的研究)指出,施予从来不是纯粹的:它在帮助人的同时,也可能在<em>制造等级</em>——把人区分为「施予者」(高、有能力、慷慨) 与「领受者」(低、有缺乏、亏欠)。一份带着优越感的施舍,可能羞辱了它本想帮助的人,把对方「区隔」为低人一等的「他者」。这是对一切行善者的一记警钟:施予若不伴随尊重,就可能在给出面包的同时,夺走尊严。",
                      "The book's theoretical section raises a sharp question: is charity a two-faced “Janus”? Drawing on anthropological studies of “the gift,” scholars note that giving is never pure: while helping, it can also <em>create hierarchy</em> — dividing people into “givers” (high, capable, generous) and “receivers” (low, lacking, indebted). A handout carrying superiority can humiliate the very person it means to help, “othering” them as inferior. This is an alarm bell for every doer of good: giving without respect may, in handing over bread, rob a person of dignity.")),
                step(S2, S2E,
                    bq("「怜悯贫穷的,就是借给耶和华;他的善行,耶和华必偿还。」",
                       "“Whoever is kind to the poor lends to the LORD, and he will reward them for what they have done.”",
                       "《箴言》19:17 · Proverbs 19:17")),
                step(S3, S3E,
                    p("<strong>גֵּר · ger</strong>——「寄居者、外人」。圣经处理「他者」的方式,恰恰是这个问题的解药。妥拉三十六次命令以色列要爱 <em>ger</em>(外人),理由总是同一句:「<em>因为你们在埃及地也作过寄居的</em>」(利 19:34)。这句话拆掉了施予者的优越感:你今天能施予,只因神先怜悯了曾经一无所有、为奴为客的你。在神面前,施予者与领受者,本是同一类人——都是蒙了怜悯的乞丐。记住「你也曾作过寄居的」,就再不能居高临下地施舍,只能带着同理与尊重,彼此守望。",
                      "<strong>גֵּר · ger</strong> — “sojourner, stranger.” Scripture's way of handling “the other” is precisely the antidote to this problem. The Torah commands Israel thirty-six times to love the <em>ger</em> (stranger), always with the same reason: “<em>for you were strangers in the land of Egypt</em>” (Lev 19:34). That sentence dismantles the giver's superiority: you can give today only because God first had mercy on you, who were once with nothing, a slave and a sojourner. Before God, giver and receiver are the same kind — both beggars who have received mercy. To remember “you too were a sojourner” is to be unable to give from above, but only to watch over one another with empathy and respect.")),
                step(S4, S4E,
                    p("这一课为基督徒的善行注入了至关重要的谦卑。福音彻底瓦解了「施予者高、领受者低」的等级,因为它宣告:在神面前,我们<em>所有人</em>都是赤贫的领受者。我们手里能给出去的一切,没有一样不是先白白领受来的(林前 4:7:「你有什么不是领受的呢?」)。因此,基督徒的施予,绝不能带着「我比你高」的姿态;它必须带着「我们都是同样蒙恩的乞丐,我只是把白白得来的,分给你」的弟兄之情。《箴言》说得最美:怜悯穷人,是「借给耶和华」——领受我们施予的,首先是那位与穷人认同的主自己。这哪里还有半点优越的余地?",
                      "This lesson injects vital humility into Christian good works. The Gospel utterly dismantles the hierarchy of “high giver, low receiver,” because it proclaims that before God, <em>all</em> of us are destitute receivers. Everything we can give was first freely received (1 Cor 4:7: “What do you have that you did not receive?”). So Christian giving must never carry the posture of “I am above you”; it must carry the brotherhood of “we are all beggars under the same grace, and I am simply sharing with you what I freely received.” Proverbs says it most beautifully: to be kind to the poor is to “lend to the LORD” — the One who receives our giving is, first of all, the Lord himself, who identifies with the poor. Where is there any room left for superiority?")),
                step(S5, S5E,
                    ul(
                        ("我的施予,有没有带着优越感,在给出帮助的同时,夺走了对方的尊严？",
                         "Does my giving carry superiority, robbing the receiver of dignity even as it offers help?"),
                        ("『因为你也曾作过寄居的』。记住自己曾经的缺乏与蒙恩,如何拆掉我的优越感？",
                         "“For you too were a sojourner.” How does remembering my own former lack and mercy dismantle my superiority?"),
                        ("『在神面前我们都是领受者』。这如何把我的施予,从『施舍』变成『弟兄间的分享』？",
                         "“Before God we are all receivers.” How does that turn my giving from a “handout” into “sharing among kin”?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "从慈善到慈善事业——制度、动机与权力",
            "title_en": "From Charity to Philanthropy — Institution, Motive, and Power",
            "steps": [
                step(S1, S1E,
                    p("书中的历史篇章追踪了一个重要的转变:从中世纪以救灵、尽义务为核心的「慈善」(charity),到近代以社会改良、文化资本为特征的「慈善事业」(philanthropy)。学者们诚实地揭示,施予从来不只是「纯粹的善」:富裕的犹太精英、基督教的兄弟会、穆斯林的宗教基金 (waqf),它们的施予往往也夹杂着社会地位的彰显、群体认同的维系、乃至权力的运作。这并非要否定施予的价值,而是提醒我们:人心是复杂的,即使是最高尚的善行,也总掺杂着不纯的动机。诚实地面对这一点,是迈向更纯粹之爱的第一步。",
                      "The book's historical chapters trace an important shift: from medieval “charity,” centered on saving souls and fulfilling obligation, to modern “philanthropy,” marked by social reform and cultural capital. Scholars honestly reveal that giving was never merely “pure good”: the giving of wealthy Jewish elites, Christian confraternities, and Muslim religious endowments (<em>waqf</em>) was often mixed with the display of social standing, the maintenance of group identity, even the workings of power. This is not to deny the value of giving but to remind us that the human heart is complex; even the noblest good works are always laced with impure motives. To face this honestly is the first step toward a purer love.")),
                step(S2, S2E,
                    bq("「你施舍的时候,不要在你前面吹号……要叫你施舍的事行在暗中;你父在暗中察看,必然报答你。」",
                       "“When you give to the needy, do not announce it with trumpets... so that your giving may be in secret. Then your Father, who sees what is done in secret, will reward you.”",
                       "《马太福音》6:2-4 · Matthew 6:2-4")),
                step(S3, S3E,
                    p("<strong>בַּסֵּתֶר · ba-seter</strong>——「在隐密中」。犹太传统极其推崇「隐密的施予」(<em>matan ba-seter</em>)——迈蒙尼德甚至把「施予者与领受者彼此都不知道对方是谁」列为极高的层级,因为这样最能保全领受者的尊严,也最能除去施予者求名的私心。耶书亚的教导与此完全一致:「要叫你施舍的事行在暗中」(太 6:4)。<em>ba-seter</em> 这个属灵操练,直击上一课所揭示的两个危险:它既防止施予沦为彰显地位的表演,又保护了领受者不被「区隔」为低人一等。在隐密中施予,是让施予回归它纯粹本质的良方。",
                      "<strong>בַּסֵּתֶר · ba-seter</strong> — “in secret.” The Jewish tradition highly prizes “secret giving” (<em>matan ba-seter</em>) — Maimonides even ranks “the giver and receiver not knowing each other's identity” as a very high level, because it best preserves the receiver's dignity and best removes the giver's craving for recognition. Yeshua's teaching is exactly aligned: “so that your giving may be in secret” (Matt 6:4). This spiritual discipline of <em>ba-seter</em> strikes directly at the two dangers of the previous lesson: it keeps giving from becoming a performance of status, and protects the receiver from being “othered” as inferior. To give in secret is the remedy that returns giving to its pure essence.")),
                step(S4, S4E,
                    p("这一课呼召基督徒诚实地省察自己施予的动机。耶书亚毫不留情地点破那种「在前面吹号」的施予——为要「得人的荣耀」。祂的诊断极深:同一个善行,可以出于纯粹的爱,也可以出于隐秘的骄傲;而真正蒙神悦纳的,是那「行在暗中」、不为人知、不求回报的施予。这不是要我们因动机不纯就停止行善(若等动机全然纯洁才施予,我们将永不施予);而是邀请我们,一边施予,一边求神洁净我们的心——让左手不知道右手所做的,让施予越来越少是为了「我」,越来越多是单单为了神和那需要的人。",
                      "This lesson calls Christians to honestly examine the motives of their giving. Yeshua mercilessly exposes the giving that “announces it with trumpets” — in order to be “honored by others.” His diagnosis is deep: the same good deed can flow from pure love or from secret pride; and what God truly accepts is the giving “done in secret,” unknown and unrewarded. This is not to make us stop doing good because our motives are impure (if we waited for wholly pure motives, we would never give); it is to invite us, while giving, to ask God to cleanse our hearts — to let the left hand not know what the right is doing, so that giving is less and less for “me,” and more and more for God and the one in need alone.")),
                step(S5, S5E,
                    ul(
                        ("『同一个善行,可以出于纯粹的爱,也可以出于隐秘的骄傲』。我施予时,内心真实的动机是什么？",
                         "“The same good deed can flow from pure love or from secret pride.” What is the true motive of my heart when I give?"),
                        ("犹太传统推崇『隐密的施予』。我愿意行多少不为人知、不求回报、不被点赞的善吗？",
                         "The Jewish tradition prizes “secret giving.” How much good am I willing to do unseen, unrewarded, un-liked?"),
                        ("耶稣说『不要在前面吹号』。在一个鼓励『晒善行』的时代,这如何挑战我？",
                         "Jesus says “do not announce it with trumpets.” In an age that rewards “displaying good deeds,” how does that challenge me?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "穷人坐在中央——神隐藏的所在",
            "title_en": "The Poor at the Center — Where God Is Hidden",
            "steps": [
                step(S1, S1E,
                    p("把全书汇拢,一个共同的、深刻的主题浮现出来:在三大亚伯拉罕信仰里,穷人都不是处在社会的边缘,而是被置于<em>属灵的中央</em>。施予穷人之所以被赋予如此崇高的地位,是因为三家都相信,在那有缺乏的人身上,神以某种特殊的方式临在、受感动、并垂顾。无论是犹太的「神听见穷人的哀声」,基督教的「我饿了,你们给我吃」,还是伊斯兰的「为神而施予」,它们都指向同一个颠覆性的真理:你怎样对待那最微小、最软弱、最被忽视的人,你就怎样对待神自己。",
                      "Gathering the whole book, a shared and profound theme emerges: in all three Abrahamic faiths, the poor are not at the margins of society but placed at the <em>spiritual center</em>. Giving to the poor is granted such exalted standing because all three believe that in the person who lacks, God is present, moved, and attentive in some special way. Whether the Jewish “God hears the cry of the poor,” the Christian “I was hungry and you gave me food,” or the Islamic “giving for God's sake,” they point to the same subversive truth: how you treat the smallest, weakest, most overlooked person is how you treat God himself.")),
                step(S2, S2E,
                    bq("「他为困苦人伸冤,为穷乏人辨屈,这不是认识我吗?这是耶和华说的。」",
                       "“He defended the cause of the poor and needy, and so all went well. Is that not what it means to know me? declares the LORD.”",
                       "《耶利米书》22:16 · Jeremiah 22:16")),
                step(S3, S3E,
                    p("<strong>אֶבְיוֹן · evyon</strong>(穷乏人) 与 <strong>עָנִי · ani</strong>(困苦人)。希伯来圣经反复用这两个词,而且每一次都把神放在他们这一边:「神是<em>穷人 (ani)</em> 的避难所」(诗 14:6);压制 <em>evyon</em> 的,就是「辱没造他的主」(箴 14:31)。最震撼的是《耶利米书》22:16 那句:「为穷乏人辨屈,这不是<em>认识我</em>吗?」——神竟把「认识祂」与「为穷人伸冤」等同起来!在圣经里,你无法绕过穷人去单独地「认识神」;关心 <em>evyon</em> 与 <em>ani</em>,不是认识神之后的副产品,而是认识神本身的一部分。",
                      "<strong>אֶבְיוֹן · evyon</strong> (the needy) and <strong>עָנִי · ani</strong> (the afflicted). The Hebrew Bible uses these two words again and again, and every time puts God on their side: “God is the refuge of the <em>poor (ani)</em>” (Ps 14:6); whoever oppresses the <em>evyon</em> “shows contempt for their Maker” (Prov 14:31). Most striking is Jeremiah 22:16: “He defended the cause of the needy — is that not what it means to <em>know me</em>?” God equates “knowing him” with “defending the poor”! In Scripture, you cannot bypass the poor to “know God” in isolation; caring for the <em>evyon</em> and the <em>ani</em> is not a by-product of knowing God but part of knowing God himself.")),
                step(S4, S4E,
                    p("这一课触及福音的一个奥秘的核心:那位创造宇宙的神,选择把自己<em>藏在穷人里</em>。耶书亚的话语惊心动魄——「这些事你们既作在我这弟兄中一个最小的身上,就是作在我身上了」(太 25:40)。这意味着,每一次我们向饥饿者递上食物、向孤独者送去探望、向赤身者披上衣裳,我们都在不知不觉中,服侍了那位道成肉身、与最小者认同的主。施予因此被提升为一种<em>圣事</em>:在那需要帮助的脸上,我们与基督相遇。一个忽视穷人的信仰,无论多么属灵、多么火热,圣经说,根本还没有真正「认识」神。",
                      "This lesson touches a mysterious core of the Gospel: the God who created the universe chose to hide himself <em>in the poor</em>. Yeshua's words are staggering — “whatever you did for one of the least of these brothers of mine, you did for me” (Matt 25:40). This means that every time we hand food to the hungry, visit the lonely, clothe the naked, we are, unawares, serving the incarnate Lord who identifies with the least. Giving is thereby lifted into a kind of <em>sacrament</em>: in the face of the one who needs help, we meet Christ. A faith that ignores the poor, however spiritual or fervent, Scripture says, has not yet truly “known” God.")),
                step(S5, S5E,
                    ul(
                        ("神把『认识祂』与『为穷人伸冤』等同。我『认识神』的功课里,有这一部分吗？",
                         "God equates “knowing him” with “defending the poor.” Does my pursuit of “knowing God” include this part?"),
                        ("神选择把自己藏在穷人里。我上一次在一个有需要的人脸上,与基督相遇,是什么时候？",
                         "God chose to hide himself in the poor. When did I last meet Christ in the face of someone in need?"),
                        ("『一个忽视穷人的信仰,还没真正认识神』。这句话,如何审视我自己的信仰？",
                         "“A faith that ignores the poor has not truly known God.” How does that sentence examine my own faith?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "其中最大的是爱——施予的成全",
            "title_en": "The Greatest of These Is Love — The Fulfillment of Giving",
            "steps": [
                step(S1, S1E,
                    p("走到全书的尽头,我们看见三大传统对「施予」的理解,在最深处奇妙地交汇,又各有其独特。犹太的 <em>tzedakah</em> 教我们:施予是公义的本分;伊斯兰的 <em>sadaqa</em> 教我们:施予是信仰真诚的标记;基督的 <em>caritas</em> 则把这一切的根基,指向<em>爱</em>——一种因「神先爱了我们」而生的、白白倾倒的爱。这本比较之书的最大馈赠,是让我们既看见与邻舍共有的、深植的施予之根(公义、真诚、怜悯),又更清楚地认出,基督信仰把施予最终安放在何处:不是律法,不是回报,而是那位在十字架上把自己完全舍出的、爱的神。",
                      "Reaching the book's end, we see the three traditions' understanding of “giving” converge wondrously at the deepest level, each with its own distinctiveness. Jewish <em>tzedakah</em> teaches us that giving is an obligation of justice; Islamic <em>sadaqa</em> teaches that giving is the mark of sincere faith; and Christian <em>caritas</em> points the ground of it all to <em>love</em> — a freely poured-out love born because “God first loved us.” The great gift of this comparative book is to let us see both the deep-rooted ground of giving we share with our neighbors (justice, sincerity, mercy) and, more clearly, where the Christian faith finally rests giving: not on law, not on reward, but on the God of love who gave himself completely on the cross.")),
                step(S2, S2E,
                    bq("「如今常存的有信,有望,有爱这三样,其中最大的是爱……我若将所有的周济穷人……却没有爱,仍然与我无益。」",
                       "“And now these three remain: faith, hope and love. But the greatest of these is love... If I give all I possess to the poor... but do not have love, I gain nothing.”",
                       "《哥林多前书》13:13, 3 · 1 Corinthians 13:13, 3")),
                step(S3, S3E,
                    p("<strong>אַהֲבָה · ahavah</strong>——「爱」。我们的旅程,从「公义之施」(tzedakah) 出发,如今回到了「爱」(ahavah)——而这两者,在圣经里从不矛盾。保罗在哥林多前书 13 章说出那句最令人战栗的话:「我若将所有的周济穷人……却没有爱,仍然与我无益。」原来,施予可以没有爱;最慷慨的善行,也可能空有其表。施予的<em>形式</em>(公义、真诚)固然不可或缺,但它的<em>灵魂</em>,是 <em>ahavah</em>。最高的施予,不是给出最多的钱,而是连同那笔钱,给出一颗真正爱人的心——一颗因被神白白地爱、便也学会白白地爱的心。",
                      "<strong>אַהֲבָה · ahavah</strong> — “love.” Our journey set out from “giving as justice” (<em>tzedakah</em>), and now returns to “love” (<em>ahavah</em>) — and the two never contradict in Scripture. Paul says the most arresting thing in 1 Corinthians 13: “If I give all I possess to the poor... but do not have love, I gain nothing.” So it turns out giving can be without love; the most generous good deed can be empty within. The <em>form</em> of giving (justice, sincerity) is indispensable, but its <em>soul</em> is <em>ahavah</em>. The highest giving is not handing over the most money, but giving, along with the money, a heart that truly loves — a heart that, having been freely loved by God, has learned to love freely.")),
                step(S4, S4E,
                    p("这是整份指南的终点,也是一个邀请。我们透过「施予」这扇窗,望见了犹太、基督、伊斯兰三大传统最深的价值,也更清楚地认出基督信仰的心跳:我们爱,因为神先爱了我们;我们施予,因为我们先白白领受。愿这八堂课塑造我们:成为既松开手、又敞开心的人;以 <em>tzedakah</em> 的公义、<em>sadaqa</em> 的真诚、<em>caritas</em> 的爱,去服侍那藏在穷人里的主;并带着「爱我民」之心,与每一位亚伯拉罕的后裔为邻、为友、彼此守望。因为到了末了,信、望、爱常存,而其中最大的,是爱——那把万有白白赐给我们、又呼召我们白白施予的神,祂自己就是爱。",
                      "This is the end of the whole guide, and an invitation. Through the window of “giving” we have glimpsed the deepest values of the Jewish, Christian, and Islamic traditions, and seen more clearly the heartbeat of the Christian faith: we love because God first loved us; we give because we first freely received. May these eight lessons shape us into people both open-handed and open-hearted; serving, with the justice of <em>tzedakah</em>, the sincerity of <em>sadaqa</em>, and the love of <em>caritas</em>, the Lord hidden in the poor; and, with a heart of <em>Ahavat Ammi</em>, being neighbor, friend, and keeper to every child of Abraham. For in the end, faith, hope, and love remain — and the greatest of these is love; for the God who freely gave us all things and calls us to give freely is himself love."),),
                step(S5, S5E,
                    ul(
                        ("『我若将所有的周济穷人,却没有爱,仍然与我无益』。我的施予,有爱作它的灵魂吗？",
                         "“If I give all I possess to the poor but have not love, I gain nothing.” Does my giving have love as its soul?"),
                        ("tzedakah(公义)、sadaqa(真诚)、caritas(爱)——这三样如何在我的施予中合一？",
                         "<em>Tzedakah</em> (justice), <em>sadaqa</em> (sincerity), <em>caritas</em> (love) — how do these three unite in my giving?"),
                        ("走完全书,我会以什么具体的一步,松开我的手,也敞开我的心？",
                         "Having finished the book, what one concrete step will I take to open my hand, and open my heart?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "为一双松开的手、一颗敞开的心祝祷",
    "closing_title_en": "A Blessing for an Open Hand and an Open Heart",
    "closing_zh": "「愿耶和华赐福给你,保护你。」<br/><br/>愿你看过三大传统里施予的根,<br/>就更深地领受那共有的真理:<br/>施予是公义 (tzedakah),是真诚 (sadaqa),是爱 (caritas)。<br/><br/>愿你记得,你手里能给的一切,<br/>没有一样不是先白白领受来的;<br/>愿你在那藏于穷人里的主面前,<br/>松开你的手,也敞开你的心——<br/>因为信、望、爱常存,<br/>其中最大的,是爱。",
    "closing_en": "“The LORD bless you and keep you.”<br/><br/>Having seen the root of giving in the three traditions,<br/>may you receive more deeply the truth they share:<br/>that giving is justice (tzedakah), sincerity (sadaqa), and love (caritas).<br/><br/>May you remember that all you can give<br/>was first freely received;<br/>and before the Lord hidden in the poor,<br/>may you open your hand, and open your heart —<br/>for faith, hope, and love remain,<br/>and the greatest of these is love.",
}

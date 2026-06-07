# -*- coding: utf-8 -*-
"""Content module for study-abrahamic-theology.html.

David B. Burrell, C.S.C., *Towards a Jewish-Christian-Muslim Theology*
(Wiley-Blackwell, Malden MA, 2011).
"""

RHYTHM_ZH = """        <strong>① 作者说什么</strong>—— 用伯勒尔自己的语境概述他的论点；<br/>
        <strong>② 关键经文</strong>—— 与之相关的圣经；<br/>
        <strong>③ 希伯来语之眼</strong>—— 一个关键的希伯来词，照亮这场对话；<br/>
        <strong>④ 基督徒视角</strong>—— 在敬重中持守、并见证那独一的中保；<br/>
        <strong>⑤ 诚实的提问</strong>—— 留给你与小组省察的问题。"""

RHYTHM_EN = """        <strong>① What the Author Says</strong> — Burrell's argument in his own frame;<br/>
        <strong>② Key Scripture</strong> — the related biblical text;<br/>
        <strong>③ Through Hebrew Eyes</strong> — one Hebrew word that lights up the conversation;<br/>
        <strong>④ A Christian Lens</strong> — holding fast in respect, and witnessing to the one mediator;<br/>
        <strong>⑤ Honest Questions</strong> — questions for you and your group to examine."""


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
    "title_tag": "《迈向犹太-基督-穆斯林神学》研习指南 · Towards a Jewish-Christian-Muslim Theology — Study Guide · 妥拉之光",
    "meta_desc": "A discerning Christian study guide to David Burrell's Towards a Jewish-Christian-Muslim Theology — eight bilingual lessons on creation, grace, trust in providence, and judgment across the Abrahamic faiths, held with respect and a clear witness to the one Mediator.",
    "og_title": "Towards a Jewish-Christian-Muslim Theology — A Study Guide",
    "og_desc": "Eight bilingual lessons through David Burrell's comparative Abrahamic theology — free creation, grace, trust, and consummation — read with respect, discernment, and Hebrew eyes.",
    "cover_alt": "Towards a Jewish-Christian-Muslim Theology — Study Guide",
    "tagline_zh": "研习指南 · 亚伯拉罕信仰的对话 · 2026 · 5 · 31",
    "tagline_en": "Study Guide · The Abrahamic Conversation · 2026 · 5 · 31",
    "headline_zh": "迈向犹太-基督-<br/>穆斯林神学",
    "headline_en": "Towards a Jewish-<br/>Christian-Muslim Theology",
    "deck_zh": "八堂课程，跟随天主教哲学神学家伯勒尔 (David Burrell)，进入犹太教、基督教、伊斯兰教三大「亚伯拉罕信仰」之间一场严肃而敬重的对话——围绕创造、自由、恩典、信靠与终末。本指南以圣经为分辨之尺，既在共通处彼此聆听，又清楚见证那位独一的中保。",
    "deck_en": "Eight lessons following Catholic philosophical theologian David Burrell into a serious, respectful conversation among the three “Abrahamic faiths” — Jewish, Christian, and Muslim — around creation, freedom, grace, trust, and the last things. This guide reads with Scripture as the measure of discernment: listening at the points held in common, while bearing clear witness to the one Mediator.",
    "byline_zh": "基于大卫·伯勒尔 (David B. Burrell, C.S.C.)《迈向犹太-基督-穆斯林神学》(Wiley-Blackwell, 2011)",
    "byline_en": "Based on Towards a Jewish-Christian-Muslim Theology by David B. Burrell, C.S.C. (Wiley-Blackwell, 2011)",
    "readtime_zh": "约 55 分钟通读",
    "readtime_en": "~55 min read-through",
    "book_url": "https://www.wiley.com/en-us/Towards+a+Jewish+Christian+Muslim+Theology-p-9780470657553",
    "book_link_zh": "购买原书 · Wiley",
    "book_link_en": "Get the Book · Wiley",
    "cta_url": "https://www.wiley.com/en-us/Towards+a+Jewish+Christian+Muslim+Theology-p-9780470657553",
    "cta_zh": "购买《迈向犹太-基督-穆斯林神学》原书 · Wiley-Blackwell",
    "cta_en": "Get the Book — Towards a Jewish-Christian-Muslim Theology · Wiley-Blackwell",

    "lead_zh": "先说清楚这份指南的立场：我们读伯勒尔 (David Burrell) 这部比较神学,是为了在敬重中<em>聆听与分辨</em>,而不是要抹平三大信仰之间真实而深刻的差异。伯勒尔是圣十字会的天主教神父、哲学神学家,毕生致力于探究犹太教、基督教与伊斯兰教在哲学神学上的「家族相似」。他的方法不是把三者搅成一锅,而是借着彼此的提问,让每一个传统都更深地思想自己所信。对相信耶书亚的我们而言,这本书既是一面镜子——照见我们与犹太、穆斯林邻舍共同的根基,也是一块试金石——逼我们更清楚地说出,为什么基督是独一的。",
    "lead_en": "Let this guide's stance be clear from the start: we read David Burrell's comparative theology to <em>listen and discern</em> with respect — not to flatten the real and deep differences among the three faiths. Burrell is a Holy Cross Catholic priest and philosophical theologian who spent his life exploring the philosophical-theological “family resemblance” among Judaism, Christianity, and Islam. His method is not to blend the three into one pot, but to let each tradition think more deeply about its own faith through the others' questions. For those of us who believe in Yeshua, this book is both a mirror — showing the ground we share with our Jewish and Muslim neighbors — and a touchstone — pressing us to say more clearly why the Messiah is unique.",

    "intro": [
        p("伯勒尔借用奥古斯丁的名言「信心寻求理解 (faith seeking understanding)」来描述这场对话的精神:三大信仰都相信独一的造物主,都把世界领受为「自由创造」的恩赐,都在「神的自由与人的自由」「恩典与人的努力」「信靠与审判」这些「经典议题」上反复思想。把它们并排放在一起,不是要分高下,而是让每一个传统的提问,都成为照亮另一个传统的光。",
          "Burrell uses Augustine's phrase “faith seeking understanding” to describe the spirit of this conversation: all three faiths believe in one Creator, receive the world as the gift of a “free creation,” and ponder again and again the “classical loci” — divine freedom and human freedom, grace and human effort, trust and judgment. Setting them side by side is not to rank them but to let each tradition's questions become light that illumines the others."),
        p("本指南共 <strong>八堂课</strong>，循着书中的主要议题展开。每一堂遵循同样的五部分节奏：",
          "The guide is structured as <strong>eight lessons</strong>, following the book's major themes. Every lesson follows the same five-part rhythm:"),
        bq(RHYTHM_ZH, RHYTHM_EN),
        p("一句提醒:健康的对话,不是含糊其辞,而是「在爱中说诚实话」。本指南既鼓励我们以谦卑和敬重聆听邻舍,也鼓励我们不回避那最核心的分别——耶书亚是谁。爱邻舍与忠于真理,从不彼此矛盾。",
          "A word of caution: healthy dialogue is not vagueness but “speaking the truth in love.” This guide encourages us both to listen to our neighbors with humility and respect, and not to dodge the most central difference — who Yeshua is. To love one's neighbor and to be faithful to the truth never contradict each other."),
    ],

    "lessons": [
        {
            "heb": "א", "num": "01",
            "title_zh": "信心寻求理解——一场对话的精神",
            "title_en": "Faith Seeking Understanding — The Spirit of a Conversation",
            "steps": [
                step(S1, S1E,
                    p("伯勒尔在导论中,把整场对话安放在奥古斯丁的格言之上:「信心寻求理解。」他主张,真正的跨信仰交流,不是各自把信仰「悬置」起来、退到一个所谓「中立」的地带;恰恰相反,正是因为我们<em>站在</em>自己信仰的根基上、并真诚地寻求理解,我们才有可能真正聆听彼此。伯勒尔毕生与犹太、穆斯林学者深交,他发现:正是在一同摔跤于「自由的创造」「恩典与努力」这些共同的难题时,各自的信仰反而被照得更亮、更深。",
                      "In the introduction, Burrell sets the whole conversation on Augustine's maxim: “faith seeking understanding.” He argues that true interfaith exchange is not each party “suspending” their faith to retreat into some supposedly “neutral” ground; on the contrary, precisely because we <em>stand</em> on the ground of our own faith and sincerely seek understanding, we become able to truly listen to one another. Burrell spent his life in deep friendship with Jewish and Muslim scholars, and found that exactly when wrestling together with shared puzzles — “free creation,” “grace and effort” — each one's faith was lit up brighter and deeper.")),
                step(S2, S2E,
                    bq("「只要心里尊主基督为圣。有人问你们心中盼望的缘由,就要常作准备,以温柔、敬畏的心回答各人。」",
                       "“In your hearts revere Christ as Lord. Always be prepared to give an answer to everyone who asks you for the reason for the hope that you have. But do this with gentleness and respect.”",
                       "《彼得前书》3:15 · 1 Peter 3:15")),
                step(S3, S3E,
                    p("<strong>אֱמוּנָה · emunah</strong>——「信、信实、坚定的信靠」。希伯来的 <em>emunah</em> 不是「闭着眼睛的盲信」,它的字根含有「稳固、可靠、立得住」的意味(同根于「亚们 Amen」)。这正是伯勒尔所说的「信心寻求理解」的根基:真信心不怕提问,因为它立在一位可靠的神身上。摩西的手在战场上「<em>稳住 (emunah)</em>,直到日落」(出 17:12)——同一个词。带着 <em>emunah</em> 进入对话,意味着我们既稳稳站在自己所信之上,又敞开心去理解、去聆听。",
                      "<strong>אֱמוּנָה · emunah</strong> — “faith, faithfulness, steadfast trust.” Hebrew <em>emunah</em> is not “blind belief with closed eyes”; its root carries the sense of “firm, reliable, able to stand” (the same root as “Amen”). This is the ground of Burrell's “faith seeking understanding”: true faith does not fear questions, because it stands on a reliable God. Moses' hands “remained <em>steady (emunah)</em> till sunset” on the battlefield (Exod 17:12) — the same word. To enter dialogue with <em>emunah</em> means standing firmly on what we believe while opening our hearts to understand and to listen.")),
                step(S4, S4E,
                    p("彼得前书 3:15 为基督徒的对话立下了完美的平衡。一方面,它要求我们「心里尊主基督为圣」——绝不为了「友好」而稀释我们对基督的忠诚;另一方面,它要求我们「以温柔、敬畏的心回答各人」——绝不以骄傲或轻蔑去对待提问的人。这正是这本书所示范的:稳稳地是基督徒,同时真诚地聆听犹太与穆斯林的邻舍。我们不必在「忠于真理」与「尊重他人」之间二选一;成熟的信心,两样都要。",
                      "1 Peter 3:15 sets a perfect balance for Christian dialogue. On one hand, it asks us to “revere Christ as Lord in our hearts” — never diluting our loyalty to the Messiah for the sake of being “friendly”; on the other, it asks us to answer “with gentleness and respect” — never treating the questioner with pride or contempt. This is exactly what the book models: being firmly Christian while sincerely listening to Jewish and Muslim neighbors. We need not choose between “faithful to truth” and “respectful of others”; mature faith holds both.")),
                step(S5, S5E,
                    ul(
                        ("真信心『不怕提问,因为它立在可靠的神身上』。我面对别人的疑问时,是恐惧防卫,还是稳稳聆听？",
                         "True faith “does not fear questions because it stands on a reliable God.” When others question, do I grow defensive and fearful, or listen from a steady place?"),
                        ("彼得前书要求『尊主为圣』又『温柔敬畏』。我在哪一边更容易失衡——稀释真理,还是失去温柔？",
                         "1 Peter asks both “revere Christ” and “gentleness and respect.” Which side do I more easily lose — diluting truth, or losing gentleness?"),
                        ("我能否带着 emunah(稳固的信),既不退到『中立地带』,又不轻看与我不同信仰的人？",
                         "Can I, with <em>emunah</em> (steady faith), neither retreat to “neutral ground” nor look down on those of another faith?"),
                    )),
            ],
        },
        {
            "heb": "ב", "num": "02",
            "title_zh": "自由的创造——共有的根基",
            "title_en": "Free Creation — The Shared Foundation",
            "steps": [
                step(S1, S1E,
                    p("伯勒尔认为,三大亚伯拉罕信仰最深的共同根基,是「自由的创造」(free creation)——即:宇宙不是必然流溢出来的,也不是神「不得不」造的;它是独一的神,出于完全的自由与爱,从无中创造 (creatio ex nihilo) 的恩赐。这一信念,把犹太教、基督教、伊斯兰教,与古代的多神论、流溢论、以及现代的唯物论,都划清了界限。世界因此不是偶然,也不是必然,而是<em>礼物</em>——而礼物,意味着一位赐礼的主,和一群当存感恩的领受者。伯勒尔说,这是三家「共有的功课」。",
                      "Burrell holds that the deepest shared foundation of the three Abrahamic faiths is “free creation” — that the universe is not a necessary emanation, nor something God “had to” make; it is the gift of the one God, who creates from nothing (<em>creatio ex nihilo</em>) out of complete freedom and love. This conviction sets Judaism, Christianity, and Islam apart from ancient polytheism, emanationism, and modern materialism alike. The world is therefore neither accident nor necessity but <em>gift</em> — and a gift implies a Giver, and recipients who owe gratitude. Burrell calls this the three faiths' “shared task.”")),
                step(S2, S2E,
                    bq("「起初,神创造天地……神看着一切所造的都甚好。」",
                       "“In the beginning God created the heavens and the earth... God saw all that he had made, and it was very good.”",
                       "《创世记》1:1, 31 · Genesis 1:1, 31")),
                step(S3, S3E,
                    p("<strong>בָּרָא · bara</strong>——「创造」。在希伯来圣经里,这个动词的主语<em>永远</em>是神;它表达的是一种唯独属于神的、从无到有的创造。《创世记》1:1 用 <em>bara</em> 开篇,一锤定音:万有都出于神自由的话语。三大信仰都从这个词出发,共享一个深刻的世界观:受造界是美善的(「神看着甚好」),是有秩序、有目的的,是当被感恩与看顾、而非被敬拜或被掠夺的。从 <em>bara</em> 出发,我们与犹太、穆斯林邻舍,确实站在同一片受造的土地上,同样仰望那位创造主。",
                      "<strong>בָּרָא · bara</strong> — “to create.” In the Hebrew Bible, the subject of this verb is <em>always</em> God; it expresses a creation from nothing that belongs to God alone. Genesis 1:1 opens with <em>bara</em>, settling it: all things come from God's free word. The three faiths set out from this word, sharing a profound worldview: the created order is good (“God saw that it was good”), ordered and purposeful, to be received with gratitude and stewarded — not worshiped or plundered. From <em>bara</em>, we truly stand with our Jewish and Muslim neighbors on the same created ground, looking up to the same Creator.")),
                step(S4, S4E,
                    p("「自由的创造」是真实而宝贵的共同点,值得我们珍惜,也为对话提供了真诚的起点。但基督信仰在这里也加上了一个独特而决定性的音符:那位「从无中创造」的话语,新约说,就是那位「太初有道」的<em>道 (Logos)</em>——「万物是藉着他造的」(约 1:3),而这道「成了肉身」。换言之,对基督徒而言,创造与救赎出于同一位:创造万有的那一位,亲自进入受造界,为要救赎它。我们与邻舍同认一位创造主——这是恩典;而我们更要见证,这位创造主已在耶书亚里向我们显明了祂的面。",
                      "“Free creation” is a real and precious common ground, worth treasuring and a sincere starting point for dialogue. But the Christian faith adds here a distinctive and decisive note: the Word that “creates from nothing,” the New Testament says, is the <em>Logos</em> who was “in the beginning” — “through him all things were made” (John 1:3) — and this Word “became flesh.” In other words, for Christians, creation and redemption flow from the same One: the One who made all things entered the created order himself to redeem it. That we share one Creator with our neighbors is grace; and we are to witness further that this Creator has shown us his face in Yeshua.")),
                step(S5, S5E,
                    ul(
                        ("世界是『礼物』而非偶然或必然。这如何改变我对受造界、对每一天生命的态度？",
                         "The world is “gift,” not accident or necessity. How does that change my posture toward creation and toward each day of life?"),
                        ("与犹太、穆斯林邻舍同认一位创造主——这份共同点,如何成为真诚对话的起点？",
                         "Sharing one Creator with Jewish and Muslim neighbors — how can that common ground be a sincere starting point for dialogue?"),
                        ("创造与救赎出于同一位『道』。这如何加深我对『创造主亲自进入受造界』的惊叹？",
                         "Creation and redemption flow from the same “Word.” How does that deepen my wonder at “the Creator entering creation himself”?"),
                    )),
            ],
        },
        {
            "heb": "ג", "num": "03",
            "title_zh": "神的自由与人的自由",
            "title_en": "Divine Freedom and Human Freedom",
            "steps": [
                step(S1, S1E,
                    p("既然万有都倚靠那位自由的创造主,一个古老的难题便随之而来,三大信仰都为之苦思:如果神是全能、全知、全权的,那么人还有真正的自由吗?伯勒尔指出,三家都拒绝两个极端——既不愿说「人完全自主、神被架空」,也不愿说「人只是被神操控的木偶」。它们都在摸索一种更深的图景:人的自由不是与神的主权<em>竞争</em>的,而恰恰是神主权的<em>恩赐</em>;正因为神是自由的创造主,祂才能创造出真正自由的受造者。神的自由不压垮人的自由,反而成全它。",
                      "Since all things depend on the free Creator, an ancient puzzle follows, over which all three faiths have labored: if God is all-powerful, all-knowing, all-sovereign, do humans have any real freedom? Burrell notes that all three reject two extremes — neither “humans fully autonomous, God sidelined,” nor “humans mere puppets God controls.” All three grope for a deeper picture: human freedom does not <em>compete</em> with God's sovereignty but is its very <em>gift</em>; precisely because God is the free Creator, he can create genuinely free creatures. God's freedom does not crush human freedom but fulfills it.")),
                step(S2, S2E,
                    bq("「我今日呼天唤地向你作见证;我将生死祸福陈明在你面前,所以你要拣选生命,使你和你的后裔都得存活。」",
                       "“This day I call the heavens and the earth as witnesses against you that I have set before you life and death, blessings and curses. Now choose life, so that you and your children may live.”",
                       "《申命记》30:19 · Deuteronomy 30:19")),
                step(S3, S3E,
                    p("<strong>בְּחִירָה · bechirah</strong>——「拣选、自由意志」。犹太传统用 <em>bechirah chofshit</em>(自由的拣选)来表达人真实的道德自由。《申命记》30 章那句「<em>你要拣选 (u-vacharta)</em> 生命」,正是这自由的庄严宣告——神郑重地把选择交在人手中,这本身就证明祂看重、并真实地赐下了人的自由。然而,圣经里的自由从不是「自主自足」的现代式自由;它是「被造的自由」——一种唯有在转向、信靠、顺服那赐自由的主时,才得以圆满的自由。最深的自由,不是「随心所欲」,而是「拣选生命」。",
                      "<strong>בְּחִירָה · bechirah</strong> — “choice, free will.” The Jewish tradition uses <em>bechirah chofshit</em> (free choice) for humanity's real moral freedom. The “<em>choose (u-vacharta)</em> life” of Deuteronomy 30 is the solemn declaration of that freedom — God genuinely places the choice in human hands, which itself proves he values and truly grants human freedom. Yet biblical freedom is never the modern “autonomous self-sufficiency”; it is “created freedom” — a freedom made whole only in turning to, trusting, and obeying the God who gives it. The deepest freedom is not “doing as I please,” but “choosing life.”")),
                step(S4, S4E,
                    p("这一课触及一个让无数信徒挣扎的问题,而基督信仰给出一个独特的、以基督为中心的答案。保罗写道:「基督释放了我们,叫我们得以自由。」(加 5:1) 真自由不是脱离神的「独立」,而是脱离罪与死的「释放」;不是「无人辖制我」,而是「真理使你们得以自由」(约 8:32)。在耶书亚里,神的主权与人的自由最深地相遇:祂以全然的自由顺服了父,「不要照我的意思,只要照你的意思」——而正是这完美的顺服,成就了我们的得释放。我们效法祂,便发现:把自由交还给神,反而第一次寻见了真正的自由。",
                      "This lesson touches a question over which countless believers struggle, and the Christian faith gives a distinctive, Christ-centered answer. Paul writes, “It is for freedom that Christ has set us free” (Gal 5:1). True freedom is not “independence” from God but “liberation” from sin and death; not “no one rules me” but “the truth will set you free” (John 8:32). In Yeshua, God's sovereignty and human freedom meet most deeply: he obeyed the Father in perfect freedom — “not my will, but yours be done” — and that very obedience won our liberation. Imitating him, we discover that handing our freedom back to God is where we first find true freedom.")),
                step(S5, S5E,
                    ul(
                        ("『人的自由不是与神主权竞争,而是它的恩赐。』这如何化解我心里『神主权 vs 我的自由』的张力？",
                         "“Human freedom does not compete with God's sovereignty but is its gift.” How does that ease the tension I feel between God's sovereignty and my freedom?"),
                        ("最深的自由不是『随心所欲』,而是『拣选生命』。我对『自由』的定义,需要被怎样更新？",
                         "The deepest freedom is not “doing as I please” but “choosing life.” How does my definition of “freedom” need renewing?"),
                        ("耶书亚以完全的自由顺服父。把自由交还给神,如何反而成了真自由的入口？",
                         "Yeshua obeyed the Father in perfect freedom. How is handing freedom back to God the very entrance to true freedom?"),
                    )),
            ],
        },
        {
            "heb": "ד", "num": "04",
            "title_zh": "人的努力与神的恩典",
            "title_en": "Human Effort and Divine Grace",
            "steps": [
                step(S1, S1E,
                    p("紧接着自由的问题,是恩典与努力的问题:在神面前,得救与成圣,究竟靠神白白的恩典,还是靠人的善行?伯勒尔指出,这是三大信仰各自内部、以及彼此之间,最激烈也最富成果的辩论之一。每个传统里都有「更强调恩典」与「更强调人的责任」的张力(在基督教里是奥古斯丁与佩拉纠之争,在伊斯兰里是不同学派之争,在犹太教里是律法与神之怜悯的张力)。伯勒尔的比较神学帮我们看见:三家其实都在拒绝两个极端——既不愿把人变成纯粹被动的,也不愿让人骄傲地以为可以「赚得」神。",
                      "Following the question of freedom comes the question of grace and effort: before God, do salvation and sanctification rest on God's free grace, or on human good works? Burrell notes this is one of the fiercest and most fruitful debates both within and among the three faiths. Each tradition holds a tension between “emphasizing grace more” and “emphasizing human responsibility” (in Christianity, the Augustine-Pelagius controversy; in Islam, debates among schools; in Judaism, the tension between law and God's mercy). Burrell's comparative theology helps us see that all three actually reject two extremes — neither making humans purely passive, nor letting humans proudly imagine they can “earn” God.")),
                step(S2, S2E,
                    bq("「你们得救是本乎恩,也因着信;这并不是出于自己,乃是神所赐的;也不是出于行为,免得有人自夸。」",
                       "“For it is by grace you have been saved, through faith — and this is not from yourselves, it is the gift of God — not by works, so that no one can boast.”",
                       "《以弗所书》2:8-9 · Ephesians 2:8-9")),
                step(S3, S3E,
                    p("<strong>חֵן / חֶסֶד · chen / chesed</strong>——「恩惠 / 慈爱、信实的爱」。希伯来圣经满了这两个词:挪亚「在耶和华眼前蒙恩 (chen)」(创 6:8);神「有丰盛的慈爱 (chesed)」(出 34:6)。值得注意的是:连在「律法」的核心,恩典也始终是根基——出埃及(救赎的恩典)<em>在前</em>,西奈颁律(蒙恩之民的回应)<em>在后</em>。神先白白地拯救,然后才呼召人回应。这个次序至关重要:在圣经里,恩典从不是对善行的报酬,善行乃是对恩典的回应。",
                      "<strong>חֵן / חֶסֶד · chen / chesed</strong> — “grace / steadfast, faithful love.” The Hebrew Bible is full of both words: Noah “found favor (chen) in the eyes of the LORD” (Gen 6:8); God is “abounding in love (chesed)” (Exod 34:6). Notably, even at the heart of “the law,” grace is always the foundation — the Exodus (the grace of redemption) comes <em>first</em>, the giving of the law at Sinai (the response of an already-redeemed people) comes <em>after</em>. God freely saves first, then calls for response. This order is vital: in Scripture, grace is never the reward for good works; good works are the response to grace.")),
                step(S4, S4E,
                    p("这一课让基督徒更清楚地说出自己信仰的心跳。以弗所书 2 章把它定了音:「你们得救是本乎恩……不是出于行为,免得有人自夸。」在与其他信仰的对话中,基督信仰带来的那份独特,正在这里:不是「神帮助那些自助的人」,而是「神在我们还作罪人的时候,为我们死」(罗 5:8)。这并不轻看人对神的真诚追求(每个传统里都有圣洁而美好的追求),而是把一切追求的根基,重新指向那位先爱我们、白白施恩的神。我们带进对话的,不是「我们更努力」,而是「我们被更白白地爱了」——而这份白白的爱,有一个名字:耶书亚。",
                      "This lesson helps Christians articulate the heartbeat of their faith more clearly. Ephesians 2 sets the tone: “by grace you have been saved... not by works, so that no one can boast.” In dialogue with other faiths, the distinctive thing the Christian faith brings is exactly here: not “God helps those who help themselves,” but “while we were still sinners, Christ died for us” (Rom 5:8). This does not belittle the sincere pursuit of God in others (every tradition holds holy and beautiful pursuit), but redirects the ground of all pursuit back to the God who loved us first and gives freely. What we bring to the conversation is not “we try harder,” but “we have been more freely loved” — and that free love has a name: Yeshua.")),
                step(S5, S5E,
                    ul(
                        ("在圣经里,恩典在前,回应在后(出埃及在前,西奈颁律在后)。我是否把这个次序颠倒了,想用善行去『赚得』神？",
                         "In Scripture, grace comes first, response after (Exodus before Sinai's law). Have I reversed the order, trying to “earn” God by good works?"),
                        ("『神在我们还作罪人的时候为我们死』。这份白白的爱,如何区别于『神帮助自助者』的逻辑？",
                         "“While we were still sinners, Christ died for us.” How does this free love differ from the logic of “God helps those who help themselves”?"),
                        ("我带进与人对话的,是『我们更努力』,还是『我们被更白白地爱了』？",
                         "What do I bring into conversation with others — “we try harder,” or “we have been more freely loved”?"),
                    )),
            ],
        },
        {
            "heb": "ה", "num": "05",
            "title_zh": "信靠神的看顾——Tawakkul 与 Bittachon",
            "title_en": "Trust in Providence — Tawakkul and Bittachon",
            "steps": [
                step(S1, S1E,
                    p("伯勒尔特别用一章谈伊斯兰传统里的 <em>tawakkul</em>——「全然信靠、把自己交托给神的看顾」。这是伊斯兰灵修的核心德性之一:在尽了本分之后,把结果完全交在神手中,带着深深的安息。伯勒尔指出,这一德性在三大信仰里都有它的对应:犹太教里的 <em>bittachon</em>(信靠),基督教里的「凡事交托、不要忧虑」。把它们并读,我们看见一个共同的、却常被现代人遗忘的真理:成熟的信心,最终都通向一种「松开掌控、安息在神看顾里」的自由。这不是消极,而是一种最深的勇气。",
                      "Burrell devotes a chapter to the Islamic tradition's <em>tawakkul</em> — “complete trust, entrusting oneself to God's providence.” It is one of the central virtues of Islamic spirituality: having done one's part, to place the outcome entirely in God's hands, resting deeply. Burrell notes this virtue has its counterpart in all three faiths: <em>bittachon</em> (trust) in Judaism, “cast all your cares, do not be anxious” in Christianity. Reading them together, we see a shared truth often forgotten by the modern mind: mature faith leads, in the end, to a freedom of “loosening control and resting in God's providence.” This is not passivity but the deepest courage.")),
                step(S2, S2E,
                    bq("「你要专心仰赖耶和华,不可倚靠自己的聪明,在你一切所行的事上都要认定他,他必指引你的路。」",
                       "“Trust in the LORD with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.”",
                       "《箴言》3:5-6 · Proverbs 3:5-6")),
                step(S3, S3E,
                    p("<strong>בִּטָּחוֹן · bittachon</strong>——「信靠、笃定的依靠」。它的字根 <em>batach</em> 含有「安然躺卧、毫无惧怕地倚靠」的意味。《箴言》3:5「你要<em>专心仰赖 (betach)</em> 耶和华」,描绘的正是这种把全身的重量,毫无保留地交托给一位可靠之主的姿态。<em>bittachon</em> 与伊斯兰的 <em>tawakkul</em> 是惊人地相近的灵修语言——两者都在说:真正的平安,不来自掌控一切,而来自信靠那位掌管一切的主。在一个被焦虑与「掌控欲」捆绑的时代,这是亚伯拉罕诸信仰共同的、宝贵的礼物。",
                      "<strong>בִּטָּחוֹן · bittachon</strong> — “trust, confident reliance.” Its root <em>batach</em> carries the sense of “lying down securely, leaning without fear.” Proverbs 3:5, “<em>trust (betach)</em> in the LORD with all your heart,” depicts exactly this posture of placing one's whole weight, without reserve, on a reliable Lord. <em>Bittachon</em> and the Islamic <em>tawakkul</em> are strikingly close as spiritual language — both say that real peace comes not from controlling everything but from trusting the One who governs everything. In an age bound by anxiety and the lust for control, this is a precious shared gift of the Abrahamic faiths.")),
                step(S4, S4E,
                    p("这一课邀请基督徒把信靠,推到它最个人、最具体的地步——而基督信仰为这信靠,赐下了一个独一的根据:那位呼召我们「不要忧虑」的,是一位曾亲自走过十字架、又从死里复活的主。我们的信靠,不是「信靠一个抽象的命运或力量」,而是信靠一位「连一只麻雀掉在地上,你们的父也都知道」(太 10:29)、并且「为我们舍了自己儿子」的天父。保罗的逻辑很美:「神既不爱惜自己的儿子,为我们众人舍了,岂不也把万物和他一同白白地赐给我们吗?」(罗 8:32) 最深的信靠,立在十字架所证明的、那已被验证的爱之上。",
                      "This lesson invites Christians to press trust to its most personal, concrete point — and the Christian faith gives that trust a unique ground: the One who calls us “do not be anxious” is a Lord who walked the cross himself and rose from the dead. Our trust is not “trust in an abstract fate or force,” but trust in a Father who knows when “even a sparrow falls to the ground” (Matt 10:29) and who “gave up his own Son for us all.” Paul's logic is beautiful: “He who did not spare his own Son, but gave him up for us all — how will he not also, along with him, graciously give us all things?” (Rom 8:32). The deepest trust rests on the already-proven love demonstrated by the cross.")),
                step(S5, S5E,
                    ul(
                        ("在尽了本分后,我能否真正『松开掌控,安息在神的看顾里』?还是焦虑仍紧紧抓着我？",
                         "Having done my part, can I truly “loosen control and rest in God's providence”? Or does anxiety still grip me tightly?"),
                        ("Bittachon 与 tawakkul 都说『平安来自信靠,而非掌控』。这份跨信仰共有的智慧,如何挑战我的生活方式？",
                         "Both <em>bittachon</em> and <em>tawakkul</em> say “peace comes from trust, not control.” How does that shared cross-faith wisdom challenge my way of life?"),
                        ("我的信靠,立在『一位为我舍了儿子的父』之上。这个根据,如何让我的信靠比泛泛的『相信命运』更稳固？",
                         "My trust rests on “a Father who gave up his Son for me.” How does that ground make my trust more solid than a vague “belief in fate”?"),
                    )),
            ],
        },
        {
            "heb": "ו", "num": "06",
            "title_zh": "归回、审判与万有的终局",
            "title_en": "Return, Judgment, and the End of All Things",
            "steps": [
                step(S1, S1E,
                    p("伯勒尔用「『归回』、审判与『第二次来临』——从创造到成全」为题,探讨三大信仰共有的「终末」维度。三家都相信:历史不是无尽的循环,也不是走向虚无,而是<em>有方向</em>的——它从神自由的创造出发,朝着神的审判与成全行进。三家都郑重地宣告:每一个人、整个受造界,都要向那位创造主交账;善恶并非毫无后果;历史终将「归回」到它的源头与目的——那位又是开始、又是终结的神。这一共同的终末盼望,赋予了人的每一个抉择,以永恒的分量。",
                      "Burrell takes up the title “‘Return,’ Judgment, and ‘Second Coming’ — Creation to Consummation,” exploring the “eschatological” dimension shared by the three faiths. All three believe history is not an endless cycle nor a march into nothingness, but <em>directional</em> — setting out from God's free creation and moving toward God's judgment and consummation. All three solemnly proclaim that every person and the whole created order will give account to the Creator; that good and evil are not without consequence; that history will at last “return” to its source and goal — the God who is both Beginning and End. This shared eschatological hope gives every human choice an eternal weight.")),
                step(S2, S2E,
                    bq("「你们要归向我,我就归向你们。这是万军之耶和华说的。」",
                       "“‘Return to me,’ declares the LORD Almighty, ‘and I will return to you.’”",
                       "《撒迦利亚书》1:3 · Zechariah 1:3")),
                step(S3, S3E,
                    p("<strong>תְּשׁוּבָה · teshuvah</strong>——「归回、悔改」。这是希伯来信仰中最有能力的词之一:不是「内疚」,而是「转身归回」——离开歧路,转回到神面前。值得注意的是,圣经里的 <em>teshuvah</em> 是双向的:「你们要<em>归向 (shuvu)</em> 我,我就<em>归向</em> 你们」(亚 1:3)。人的归回,总是回应着神先伸出的、邀请的手。三大信仰共有的「审判」维度,从不只是冷峻的清算;它的核心其实是这双向的归回——神切切地呼唤祂的受造者转身回家。终末的审判,背后是一位渴望与人和好的神。",
                      "<strong>תְּשׁוּבָה · teshuvah</strong> — “return, repentance.” It is one of the most powerful words in Hebrew faith: not “guilt” but “turning back” — leaving the wrong path, turning back to God's presence. Notably, biblical <em>teshuvah</em> is two-way: “<em>Return (shuvu)</em> to me, and I will <em>return</em> to you” (Zech 1:3). Human return always answers a hand God first extends in invitation. The “judgment” dimension shared by the three faiths is never merely a cold reckoning; at its heart is this two-way return — God earnestly calling his creatures to turn and come home. Behind the final judgment stands a God longing to be reconciled with people.")),
                step(S4, S4E,
                    p("在这「终末」的共同盼望里,基督信仰带来一个独特而具体的内容:那位要来审判的,与那位曾为我们死的,是<em>同一位</em>。基督徒所说的「第二次来临」,意味着历史的审判者不是一个陌生的、冷漠的权能,而是那位带着钉痕、认识我们、爱我们的弥赛亚。这既是无比的安慰,也是严肃的呼召:那位将要审判万有的,正向今天的我们伸出归回的手。「现在正是悦纳的时候,现在正是拯救的日子」(林后 6:2)。我们带进对话的盼望,不是模糊的「善有善报」,而是一位有名有姓、又真又活、必要再来的救主。",
                      "Within this shared eschatological hope, the Christian faith brings a distinctive, concrete content: the One who will come to judge and the One who died for us are <em>the same person</em>. The “Second Coming” Christians speak of means that history's Judge is not a strange, cold power but the Messiah who bears the nail-marks, knows us, and loves us. This is at once an immense comfort and a sober call: the One who will judge all things is even now extending the hand of return to us today. “Now is the time of God's favor, now is the day of salvation” (2 Cor 6:2). The hope we bring to dialogue is not a vague “good will be rewarded,” but a Savior with a name, living and true, who will surely come again.")),
                step(S5, S5E,
                    ul(
                        ("Teshuvah 是双向的:神先伸手,人才归回。这如何改变我对『悔改』的理解——从内疚,到回家？",
                         "<em>Teshuvah</em> is two-way: God reaches first, then we return. How does that change my view of “repentance” — from guilt to coming home?"),
                        ("那位要来审判的,与那位曾为我死的,是同一位。这对我面对『审判』的心态,是安慰还是惧怕？",
                         "The One who will judge and the One who died for me are the same. Facing “judgment,” is that comfort or fear to me?"),
                        ("『现在正是拯救的日子』——历史是有方向、有终局的。这如何赋予我今天的抉择以永恒的分量？",
                         "“Now is the day of salvation” — history is directional, with an end. How does that give my choices today eternal weight?"),
                    )),
            ],
        },
        {
            "heb": "ז", "num": "07",
            "title_zh": "诚实面对那些真实的分歧",
            "title_en": "Facing the Real Differences Honestly",
            "steps": [
                step(S1, S1E,
                    p("伯勒尔没有回避难题。他有一章专门「敬重地协商那些尚未解决的、令人神经紧绷的议题」(neuralgic issues),并以一篇关于「亚伯拉罕传统之被滥用与误用」的结语作结。他清醒地承认:三大信仰之间,存在着真实、深刻、不可轻易抹平的分歧——尤其是关于「耶稣是谁」的核心分歧。健康的对话,不是假装这些分歧不存在,而是有勇气把它们摆上桌面,在彼此敬重中诚实地谈论。伯勒尔也警告:这些信仰传统,历史上一再被人扭曲、利用,沦为仇恨与暴力的工具——而真正的对话,正是抵御这种滥用的良药。",
                      "Burrell does not dodge the hard things. He devotes a chapter to “respectfully negotiating outstanding neuralgic issues” and closes with an epilogue on “the misuses and abuses of the Abrahamic traditions.” He soberly acknowledges that real, deep differences exist among the three faiths — not least the central difference over “who Jesus is” — differences that cannot be easily smoothed away. Healthy dialogue does not pretend these differences are absent, but has the courage to put them on the table and speak of them honestly, in mutual respect. Burrell also warns that these faith traditions have, throughout history, been twisted and weaponized into instruments of hatred and violence — and that genuine dialogue is the very remedy against such abuse.")),
                step(S2, S2E,
                    bq("「惟用爱心说诚实话,凡事长进,连于元首基督。」",
                       "“Speaking the truth in love, we will grow to become in every respect the mature body of him who is the head, that is, Christ.”",
                       "《以弗所书》4:15 · Ephesians 4:15")),
                step(S3, S3E,
                    p("<strong>אֱמֶת · emet</strong>——「真理、真实、可靠」。它的字根含有「稳固、立得住、经得起对质」的意味。健康的对话需要 <em>emet</em>:不为了「友好」而粉饰分歧,也不为了「赢」而扭曲对方。但希伯来圣经常把 <em>emet</em> 与 <em>chesed</em>(慈爱)成对使用——「<em>慈爱与诚实 (chesed ve'emet)</em>」(出 34:6),因为在神那里,真理与爱本是一体。诚实地说出分歧,与温柔地敬重邻舍,从不彼此矛盾;最深的真理,总是以爱的方式被说出;最真诚的爱,也从不回避真相。",
                      "<strong>אֱמֶת · emet</strong> — “truth, reality, reliability.” Its root carries the sense of “firm, able to stand, able to withstand cross-examination.” Healthy dialogue needs <em>emet</em>: not whitewashing differences for the sake of being “nice,” nor distorting the other in order to “win.” But the Hebrew Bible often pairs <em>emet</em> with <em>chesed</em> (lovingkindness) — “<em>love and truth (chesed ve'emet)</em>” (Exod 34:6), because in God, truth and love are one. To name differences honestly and to tenderly respect a neighbor never contradict each other; the deepest truth is always spoken in love, and the most sincere love never evades the truth.")),
                step(S4, S4E,
                    p("这一课为基督徒的对话立下成熟的标准。我们既不该是「为了避免冲突而什么都同意」的人,也不该是「为了证明自己对而轻看别人」的人。「用爱心说诚实话」要求我们两样都做到:诚实地见证「在神和人中间只有一位中保,乃是降世为人的基督耶稣」(提前 2:5)——这是我们不能、也不愿放弃的真理;同时,以基督般的温柔与敬重,去爱每一位犹太、穆斯林的邻舍,把他们当作神按自己形象所造、并深爱的人。忠于真理,与深爱邻舍——这正是耶书亚自己的样式。",
                      "This lesson sets a mature standard for Christian dialogue. We should be neither those who “agree to everything to avoid conflict,” nor those who “belittle others to prove ourselves right.” “Speaking the truth in love” requires both: to witness honestly that “there is one mediator between God and mankind, the man Christ Jesus” (1 Tim 2:5) — a truth we cannot and will not surrender; and at the same time, with Christ-like gentleness and respect, to love every Jewish and Muslim neighbor as one made in God's image and dearly loved by him. Faithful to the truth, and deeply loving the neighbor — this is the very pattern of Yeshua himself.")),
                step(S5, S5E,
                    ul(
                        ("我更容易掉进哪个陷阱:为避免冲突而什么都同意,还是为证明自己对而轻看别人？",
                         "Which trap do I fall into more easily: agreeing to everything to avoid conflict, or belittling others to prove myself right?"),
                        ("真理与爱在神那里本是一体(chesed ve'emet)。我能否同时坚守『独一的中保』又深爱不同信仰的邻舍？",
                         "Truth and love are one in God (<em>chesed ve'emet</em>). Can I hold fast to “the one mediator” and at the same time deeply love neighbors of other faiths?"),
                        ("信仰传统曾被扭曲为仇恨的工具。真诚的对话如何成为抵御这种滥用的良药？",
                         "Faith traditions have been twisted into tools of hatred. How can sincere dialogue be a remedy against such abuse?"),
                    )),
            ],
        },
        {
            "heb": "ח", "num": "08",
            "title_zh": "亚伯拉罕的众子——以及那独一的中保",
            "title_en": "The Children of Abraham — and the One Mediator",
            "steps": [
                step(S1, S1E,
                    p("伯勒尔全书的盼望,是让三大信仰重新认识到彼此那「家族的相似」——它们都自称是「亚伯拉罕的后裔」,都仰望那位独一的造物主,都在创造、自由、恩典、信靠、审判这些最深的问题上,作着同源的思想。这份「家族」的认识,不是要消解差异,而是要把对话从「敌人之间的攻防」,重置为「亲属之间的诚实交谈」。对基督徒而言,这份认识既宝贵,又必须与一个清醒的见证并行:我们与犹太、穆斯林邻舍同称亚伯拉罕为父——但保罗说,亚伯拉罕真正的「后裔」,最终指向那一位「后裔」,就是基督(加 3:16)。",
                      "Burrell's hope across the book is to help the three faiths rediscover their “family resemblance” — all claiming to be “children of Abraham,” all looking to the one Creator, all thinking from a common source about the deepest questions: creation, freedom, grace, trust, judgment. This “family” recognition does not dissolve differences but resets the conversation from “the attack and defense of enemies” to “the honest talk of kin.” For Christians this recognition is precious, and must walk alongside a clear-eyed witness: we share Abraham as father with our Jewish and Muslim neighbors — but Paul says Abraham's true “seed” finally points to the one “seed,” who is the Messiah (Gal 3:16).")),
                step(S2, S2E,
                    bq("「所应许的原是向亚伯拉罕和他子孙说的……乃是说『你那一个子孙』,指着一个人,就是基督。」",
                       "“The promises were spoken to Abraham and to his seed. Scripture does not say ‘and to seeds,’ meaning many people, but ‘and to your seed,’ meaning one person, who is Christ.”",
                       "《加拉太书》3:16 · Galatians 3:16")),
                step(S3, S3E,
                    p("<strong>אַבְרָהָם · Avraham</strong>——「多国的父」(创 17:5)。神给亚伯拉罕改的这个名字,本身就含着一个普世的应许:「地上的万族都要因你得福」(创 12:3)。三大亚伯拉罕信仰,从某种意义上,都是这应许在历史中投下的影子——万族确实因亚伯拉罕的神而被搅动、被吸引。但圣经清楚地指明这祝福临到万族的<em>渠道</em>:藉着亚伯拉罕那「一个子孙」——弥赛亚。我们珍视与「亚伯拉罕众子」的亲缘,也满怀盼望地见证:那应许给万族的福,已经在亚伯拉罕的子孙耶书亚里,向全地敞开了。",
                      "<strong>אַבְרָהָם · Avraham</strong> — “father of many nations” (Gen 17:5). The name God gave Abraham itself holds a universal promise: “all peoples on earth will be blessed through you” (Gen 12:3). The three Abrahamic faiths are, in a sense, shadows that promise casts across history — the nations truly have been stirred and drawn by the God of Abraham. But Scripture names clearly the <em>channel</em> by which this blessing reaches all peoples: through Abraham's “one seed” — the Messiah. We cherish our kinship with the “children of Abraham,” and witness in hope that the blessing promised to all nations has, in Abraham's offspring Yeshua, been opened to all the earth.")),
                step(S4, S4E,
                    p("这是整份指南的终点,也是一个平衡的呼召。我们走过了创造、自由、恩典、信靠、审判与分歧——在每一站,我们既看见与犹太、穆斯林邻舍真实的共同根基,也更清楚地认出基督那不可替代的独特。愿这八堂课塑造我们:成为既谦卑敬重、又坚定见证的人;以彼得前书的样式,「心里尊主基督为圣」,又「以温柔敬畏回答各人」;爱每一位亚伯拉罕的后裔为邻舍,尤其带着「爱我民」之心,为以色列认识她自己的弥赛亚祷告;并满怀盼望地传扬那应许给万族的福——它有一个名字,就是亚伯拉罕的子孙、独一的中保:耶书亚。",
                      "This is the end of the whole guide, and a call to balance. We have journeyed through creation, freedom, grace, trust, judgment, and difference — and at every station we have seen both real common ground with our Jewish and Muslim neighbors and, more clearly, the irreplaceable uniqueness of the Messiah. May these eight lessons shape us to be both humbly respectful and firmly witnessing; in the pattern of 1 Peter, to “revere Christ as Lord in our hearts” and “answer everyone with gentleness and respect”; to love every child of Abraham as a neighbor, and especially, with a heart of <em>Ahavat Ammi</em>, to pray that Israel will know her own Messiah; and to proclaim in hope the blessing promised to all nations — which has a name: Abraham's offspring, the one Mediator, Yeshua."),),
                step(S5, S5E,
                    ul(
                        ("把对话从『敌人的攻防』重置为『亲属的诚实交谈』,会如何改变我对待不同信仰邻舍的方式？",
                         "Resetting conversation from “the attack and defense of enemies” to “the honest talk of kin” — how would that change how I treat neighbors of other faiths?"),
                        ("我能否同时珍视与『亚伯拉罕众子』的亲缘,又清楚见证基督那不可替代的独特？",
                         "Can I both cherish kinship with the “children of Abraham” and clearly witness to the irreplaceable uniqueness of the Messiah?"),
                        ("应许给万族的福,藉亚伯拉罕的『一个子孙』临到。我如何带着盼望,把这福分传给我的邻舍？",
                         "The blessing for all nations comes through Abraham's “one seed.” How do I carry that blessing, in hope, to my neighbors?"),
                    )),
            ],
        },
    ],

    "closing_title_zh": "为亚伯拉罕的众子、为独一中保祝祷",
    "closing_title_en": "A Blessing for the Children of Abraham, and the One Mediator",
    "closing_zh": "「愿耶和华赐福给你,保护你。」<br/><br/>愿你在创造、恩典、信靠的共同根基上,<br/>谦卑地聆听你犹太、穆斯林的邻舍;<br/>又在那最核心的真理上,坚定而温柔地见证——<br/>在神和人中间,只有一位中保,<br/>就是亚伯拉罕的子孙、独一的救主:耶书亚。<br/><br/>愿你既忠于真理,又满有爱;<br/>愿那应许给万族的福,藉着你,<br/>临到每一位亚伯拉罕的后裔。",
    "closing_en": "“The LORD bless you and keep you.”<br/><br/>On the shared ground of creation, grace, and trust,<br/>may you humbly listen to your Jewish and Muslim neighbors;<br/>and on the most central truth, witness firmly and tenderly —<br/>that between God and mankind there is one mediator,<br/>Abraham's offspring, the one Savior: Yeshua.<br/><br/>May you be both faithful to the truth and full of love;<br/>and may the blessing promised to all nations,<br/>through you, reach every child of Abraham.",
}

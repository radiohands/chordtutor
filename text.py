# 40 characters per line (just so it looks nicer / fills in the screen)
#
# S T R A      A R T S
# O I Y E      E Y I O

topRow = [
    "a r t s ta rat sas star art tras tart ta",
    "arts tar stats ar srat rats as trat rats",
    "as ta stars tar art strar satar as strat",
    "stars art rar tar strats as ararat sa ar"
]

bottomRow = [
    "e y i o yo ioi yeoi oy yeey eiei oo yoii",
    "eoiyy iyeo yee iooe iy oe eo iey oieey o",
    "eoiiy ioy eyyi eoeoy eoeoi yiyoe oiey iy",
    "iyoe eoyi yiyeoi eiyo oeiy oyie eoyi iei"
]

bothRows = [
    "rats are toys or ears yet yetis arts are",
    "a ratio says a sassy irate oyster toy yo",
    "i rot as yeast stores teary oats or stir",
    "air as satire orates years to rise tears",
    "riots are as rare as a ear stye troy say",
    "try star air it is a artsy tier to tries",
    "toe sores at tyros is a easy tier yet so",
    "rise or yeet sea oars or stir ye airs yo"
]

# add CFJN
chords1 = [
    "cf jn cc jfn cjfj ncnj fc njnjcf fcf jnj",
    "no certification if jon rejoins janitors",
    "factory certificate injectors can create",
    "fractions of cryons for cafe joints jars",
    "fancy janet in action enjoys jfnc fiance",
    "nonsense sentence sorry for it i fanfare",
    "crafty joiners in an insect craft jfcnjf"
]

# add BWHKV
chords2 = [
    "b w h k v vwhk bkvh kh bv hk kw hvbkbwvb",
    "the network views hokey bikeways who ban",
    "babies every beaky white hawks who bakes",
    "whey when bikes hike bow weak why obey k",
    "the web was written very hot wave vibers",
    "a wave hive has taken woven wives viewer",
    "okay he votes when wavy hair knives bake"
]

# add GUQP
chords3 = [
    "g u q p puq pgpg pupgq guppu quup puq gg",
    "wakeup peeps quahog gives wipes pique up",
    "whip up opaque grainy gak bug hoagies yo",
    "your phobia outweighs boogers wave bubye",
    "ginger beer wakeups are in vogue quaints",
    "vague wagyu argue queries i give up page"
]

# add DLMXZ
chords4 = [
    "d l m x z dmlmdl zlzmdx xlmd dxml xzlmdm",
    "did you know gazumped is real word mazed",
    "xerox maxed mod gizmo lumped magic diode",
    "my diploma got damaged in the mail today",
    "the plagued melody galoped over the lazy",
    "dog god zilla lives in a duplex you know"
]

punctuation = [
    "hey! this, is. going to be annoying!,!.",
    ", . ' / ! !,. '/... ,/./! ''., ,, .!.',!",
    "how, much. more can i/you take! ... well",
    "i, think. that's enough! can, i stop!/!."
]

# Stories
story1 = [
    "call me ishmael! some years ago, never",
    "mind how long precisely, having little",
    "or no money in my purse, and nothing in",
    "particular to interest me onshore, i",
    "thought i would sail about a little and",
    "see the watery part of the world. it is",
    "a way i have of driving off the spleen,",
    "and regulating the circulation. whenever",
    "i find myself growing grim about the",
    "mouth, whenever it is a damp, drizzly",
    "november in my soul, whenever i find",
    "myself involuntarily pausing before coffin",
    "warehouses, and bringing up the rear of",
    "every funeral i meet, and especially",
    "whenever my hypos get such an upper hand",
    "of me, that it requires a strong moral",
    "principle to prevent me from deliberately",
    "stepping into the street, and methodically",
    "knocking people's hats off, then, i",
    "account it high time to get to sea as soon",
    "as i can. this is my substitute for pistol",
    "and ball. whith a philosophical flourish",
    "cato throws himself upon his sword, i",
    "quietly take to the ship. there is nothing",
    "suprising in this. if they but knew it,",
    "almost all men in their degree, some time",
    "or other, cherish very nearly the same",
    "feelings towards the ocean with me."
]

story2 = [
    "it was the very witching time of night",
    "that ichabod, heavy hearted and crestfallen",
    "pursued his travels homewards, along the",
    "sides of the lofty hills which rise above",
    "tarry town, and which he had traversed",
    "so cheerily in the afternoon. the hour",
    "was as dismal as himself. far below him",
    "the tappan zee spread its dusky and",
    "indistinct waste of waters, with here and",
    "there the tall mast of a sloop, riding",
    "quietly at anchor under the land. in the",
    "dead hush of midnight, he could even hear",
    "the barking of the watchdog from the",
    "opposite shore of the hudson but it was",
    "so vague and faint as only to give an idea",
    "of his distance from this faithful companion",
    "of man. now and then, too, the long drawn",
    "crowing of a cock, accidentally awakened",
    "would sound far, far off, from some",
    "farmhouse away among the hills but it was",
    "like a dreaming sound in his ear. no signs",
    "of life occurred near him, but",
    "occasionally the melancholy chirp of a",
    "cricket, or perhaps the guttural twang",
    "of a bullfrog from a neighboring marsh",
    "as if sleeping uncomfortably and turning",
    "suddenly in his bed."
    ]

# Chord list used to draw the proper chord layout
chord = {}

chord["a"] = "a"
chord["b"] = "oe"
chord["c"] = "ye"
chord["d"] = "tra"
chord["e"] = "e"
chord["f"] = "ra"
chord["g"] = "tr"
chord["h"] = "ie"
chord["i"] = "i"
chord["j"] = "st"
chord["k"] = "oy"
chord["l"] = "iye"
chord["m"] = "oiy"
chord["n"] = "oi"
chord["o"] = "o"
chord["p"] = "oie"
chord["q"] = "sta"
chord["r"] = "r"
chord["s"] = "s"
chord["t"] = "t"
chord["u"] = "iy"
chord["v"] = "sr"
chord["w"] = "sa"
chord["x"] = "str"
chord["y"] = "y"
chord["z"] = "stra"
chord[" "] = "eyio"
chord['\''] = "aiy"
chord['.'] = "ai"
chord[','] = "ay"
chord["/"] = "ao"


chord["!"] = "ti"

# [Characters that are not yet implemented]

# z means hold or toggle shift
# n = num pad (tap s before the letter)
# b = bracket menu (tap a before the letter)
# p = punctuation menu (tab e before the letter)
#chord["\""] = "zaiy"
chord[">"] = "zai"
chord["<"] = "zay"
chord["@"] = "znsr"
chord["#"] = "znst"
chord["$"] = "znse"
chord["%"] = "znsy"
chord["["] = "bi"
chord["]"] = "by"
chord["("] = "bt"
chord[")"] = "br"
chord["{"] = "bo"
chord["}"] = "bs"
chord["?"] = "zao"
chord["`"] = "ps"
chord["~"] = "zps"
chord[";"] = "pt"
chord[":"] = "pzt"
chord["\\"] = "pr"
chord["|"] = "zpr"

#chord[""] = ""

# remaining symbols to add
# ^ & * _ + - =



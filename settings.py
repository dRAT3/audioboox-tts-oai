### SETTINGS
FILE_PATH_PDF = '../abecker10.pdf'
START_PAGE = 7
END_PAGE = 10 

OUT_FILE_PATH = "output"

# See https://platform.openai.com/account/limits for your personal rate limit
YOUR_RATE_LIMIT_TTS1 = '50'

# Set this to False if you don't want to clean up text using gpt-3.5-turbo
USE_GPT_3_5_TO_CLEAN = True 

#AUDIO SETTINGS
MUX_AUDIO_INTO_ONE_FILE = True

# If you've set to True adapt the prompts below
SYSTEM_PROMPT = """
You are the assistant.
### MISSION:
You are given a page extracted from a pdf, sometimes words are broken, you will fix them.

### CONDITIONS:
*If you find broken words, i.e. words with newlines inside the word: fix them and
return the whole text in good formatting.
*If you don't find broken words: return OK
"""
CLEANER_PROMPT = """Clean up broken words in the page.

Page:

"""
EXAMPLE_PROMPT_TO_FIX = """
Clean up broken words in the page.

Page:

2. I
NFO
 M
ARKETING
Info marketing is exactly what it sounds like: the selling of information. Go and
visit sites like JVZoo.com or ClickBank.com and you will see people making
millions of dollars selling products that teach people about any topic under the
sun. Dating, getting rid of acne, getting a six-pack, how to make money, how to
revive dead plants, it’s all there. The reason why I suggest this is because info
products:
Take no money to create.
Are the easiest types of product to create.
Can be sold instantly via online download.
On top of this, I am going to assume that you are really, really good at
something. Maybe it’s knitting or how to stand up to bullies or how to keep
goldfish alive for more than a week. Whatever that something is, there are
probably other people who want to learn about it. All you really have to do is
pick a topic, write a course or eBook explaining all you know about that topic,
and sell it on a site like JVZoo or ClickBank.
Info marketing is a topic that I could talk about for days on end, but I can’t
explain everything that I know in this little chapter. If this seems like something
you’d enjoy doing, I’d highly suggest checking out
The Official Get Rich Guide To
Info Marketing
by Dan Kennedy.
3. M
ARKETING
, C
ONSULTING
,
AND
 D
IRECT
-S
ELLING
 B
ASED
 S
ERVICES
Out of the three suggestions for CF businesses, I recommend this one the most
often. Why? The above two suggestions require you to learn quite a bit about
how the Internet works, and obtaining true wealth from them will take a while.
But I consistently see people get rich quickly using this third method based
around direct selling. This is because the only thing separating you from a
payday is convincing someone to give you a check. Once you get good a
convincing/selling to people, you can accumulate large checks very quickly.
There is no investment to picking up the phone and selling, and there can be an
almost instant reward in doing so.
"""
EXAMPLE_RESPONSE_FIXED = """
2. INFO MARKETING
Info marketing is exactly what it sounds like: the selling of information. Go and
visit sites like JVZoo.com or ClickBank.com and you will see people making
millions of dollars selling products that teach people about any topic under the
sun. Dating, getting rid of acne, getting a six-pack, how to make money, how to
revive dead plants, it’s all there. The reason why I suggest this is because info
products:
Take no money to create.
Are the easiest types of product to create.
Can be sold instantly via online download.
On top of this, I am going to assume that you are really, really good at
something. Maybe it’s knitting or how to stand up to bullies or how to keep
goldfish alive for more than a week. Whatever that something is, there are
probably other people who want to learn about it. All you really have to do is
pick a topic, write a course or eBook explaining all you know about that topic,
and sell it on a site like JVZoo or ClickBank.
Info marketing is a topic that I could talk about for days on end, but I can’t
explain everything that I know in this little chapter. If this seems like something
you’d enjoy doing, I’d highly suggest checking out
The Official Get Rich Guide To
Info Marketing
by Dan Kennedy.
3. MARKETING, CONSULTING,AND DIRECT SELLING BASED SERVICES
Out of the three suggestions for CF businesses, I recommend this one the most
often. Why? The above two suggestions require you to learn quite a bit about
how the Internet works, and obtaining true wealth from them will take a while.
But I consistently see people get rich quickly using this third method based
around direct selling. This is because the only thing separating you from a
payday is convincing someone to give you a check. Once you get good a
convincing/selling to people, you can accumulate large checks very quickly.
There is no investment to picking up the phone and selling, and there can be an
almost instant reward in doing so.
"""


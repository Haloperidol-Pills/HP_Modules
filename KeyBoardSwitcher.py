# name: KeyBoardSwitcher
# meta developer: @hp_modules
# author: @HaloperidolPills
# requires: pymorphy3 pymorphy3-dicts-ru
# meta banner: https://raw.githubusercontent.com/Haloperidol-Pills/metaassets/refs/heads/main/Keyboardswitcher.jpg
# meta pic: https://raw.githubusercontent.com/Haloperidol-Pills/metaassets/refs/heads/main/Keyboardswitcher.jpg

__version__ = 2,0,0
import re
import pymorphy3
from .. import loader, utils

EN_COMMON_WORDS = frozenset({
    "a", "about", "above", "add", "added", "adding", "adds", "after", "again", "against",
    "all", "allow", "allowed", "allowing", "allows", "already", "also", "although",
    "always", "am", "an", "and", "another", "any", "appear", "appeared", "appearing",
    "appears", "are", "aren", "as", "ask", "asked", "asking", "asks", "at", "back", "bad",
    "be", "because", "been", "before", "began", "begin", "beginning", "begins", "begun",
    "being", "believe", "believed", "believes", "believing", "below", "best", "better",
    "between", "big", "both", "bought", "bring", "bringing", "brings", "brought", "build",
    "building", "builds", "built", "but", "buy", "buying", "buys", "by", "bye", "call",
    "called", "calling", "calls", "came", "can", "change", "changed", "changes",
    "changing", "come", "comes", "coming", "consider", "considered", "considering",
    "considers", "continue", "continued", "continues", "continuing", "cool", "could",
    "couldn", "create", "created", "creates", "creating", "cut", "cuts", "cutting", "d",
    "did", "didn", "die", "died", "dies", "different", "do", "does", "doesn", "doing",
    "don", "down", "during", "dying", "each", "easy", "even", "every", "expect",
    "expected", "expecting", "expects", "fall", "fallen", "falling", "falls", "false",
    "feel", "feeling", "feels", "fell", "felt", "few", "find", "finding", "finds", "first",
    "follow", "followed", "following", "follows", "for", "found", "from", "further",
    "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "go", "goes",
    "going", "gone", "good", "goodbye", "got", "great", "grew", "grow", "growing", "grown",
    "grows", "had", "hadn", "happen", "happened", "happening", "happens", "happy", "hard",
    "has", "hasn", "hate", "have", "haven", "having", "he", "hear", "heard", "hearing",
    "hears", "hello", "help", "helped", "helping", "helps", "her", "here", "hers",
    "herself", "hey", "hi", "high", "him", "himself", "his", "how", "i", "if", "in",
    "include", "included", "includes", "including", "into", "is", "isn", "it", "its",
    "itself", "just", "keep", "keeping", "keeps", "kept", "kill", "killed", "killing",
    "kills", "knew", "know", "knowing", "known", "knows", "last", "lead", "leading",
    "leads", "learn", "learned", "learning", "learns", "least", "leave", "leaves",
    "leaving", "led", "left", "less", "let", "lets", "letting", "like", "live", "lived",
    "lives", "living", "ll", "long", "look", "looked", "looking", "looks", "lose", "loses",
    "losing", "lost", "love", "low", "m", "made", "make", "makes", "making", "many", "may",
    "maybe", "me", "mean", "meaning", "means", "meant", "meet", "meeting", "meets", "met",
    "might", "mine", "more", "most", "move", "moved", "moves", "moving", "much", "must",
    "my", "myself", "near", "need", "needed", "needing", "needs", "never", "new", "next",
    "nice", "no", "nor", "not", "now", "of", "off", "offer", "offered", "offering",
    "offers", "often", "ok", "okay", "old", "on", "only", "open", "opened", "opening",
    "opens", "or", "other", "our", "ours", "ourselves", "out", "over", "paid", "pay",
    "paying", "pays", "play", "played", "playing", "plays", "please", "ran", "re", "reach",
    "reached", "reaches", "reaching", "read", "reading", "reads", "ready", "remain",
    "remained", "remaining", "remains", "remember", "remembered", "remembering",
    "remembers", "right", "run", "running", "runs", "s", "same", "sat", "saw", "see",
    "seeing", "seem", "seemed", "seeming", "seems", "seen", "sees", "send", "sending",
    "sends", "sent", "serve", "served", "serves", "serving", "set", "sets", "setting",
    "shall", "she", "short", "should", "shouldn", "show", "showed", "showing", "shown",
    "shows", "since", "sit", "sits", "sitting", "small", "so", "some", "sometimes", "soon",
    "sorry", "speak", "speaking", "speaks", "spend", "spending", "spends", "spent",
    "spoke", "spoken", "stand", "standing", "stands", "start", "started", "starting",
    "starts", "stay", "stayed", "staying", "stays", "still", "stood", "stop", "stopped",
    "stopping", "stops", "such", "sure", "t", "take", "taken", "takes", "taking", "talk",
    "talked", "talking", "talks", "tell", "telling", "tells", "thank", "thanks", "that",
    "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they",
    "think", "thinking", "thinks", "this", "those", "though", "thought", "through", "to",
    "today", "told", "tomorrow", "too", "took", "tried", "tries", "true", "try", "trying",
    "turn", "turned", "turning", "turns", "under", "understand", "understanding",
    "understands", "understood", "unless", "up", "us", "use", "used", "uses", "using",
    "usually", "ve", "very", "wait", "waited", "waiting", "waits", "walk", "walked",
    "walking", "walks", "want", "wanted", "wanting", "wants", "was", "wasn", "watch",
    "watched", "watches", "watching", "we", "welcome", "well", "went", "were", "weren",
    "what", "when", "where", "which", "while", "who", "whom", "whose", "why", "will",
    "win", "winning", "wins", "with", "won", "work", "worked", "working", "works", "worse",
    "worst", "would", "wouldn", "write", "writes", "writing", "written", "wrong", "wrote",
    "yes", "yesterday", "yet", "you", "your", "yours", "yourself", "yourselves",
})

class KeyBoardSwitcher(loader.Module):
'''Модуль для смены раскладки клавиатуры'''
    strings = {"name": "KeyBoardSwitcher"}

    en_layout = "`~qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?@#$^&"
    ru_layout = "ёЁйцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,\"№;:?"
    word_re = re.compile(r"[^\W\d_]+", re.UNICODE)
    protected_re = re.compile(
        r"(@[A-Za-z0-9_]+|https?://\S+|&(?:[a-zA-Z]+|#\d+|#x[0-9a-fA-F]+);|\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/\S*)?\b)",
        re.IGNORECASE,
    )
    min_words = 2
    score_low = 0.34
    score_high = 0.6
    history_scan_limit = 50

    async def client_ready(self, client, db):
        self.morph = pymorphy3.MorphAnalyzer()
        self.en_to_ru = str.maketrans(self.en_layout, self.ru_layout)
        self.ru_to_en = str.maketrans(self.ru_layout, self.en_layout)

    def _swap_chars(self, text):
        en_letters = sum(1 for c in text if c.isalpha() and c in self.en_layout)
        ru_letters = sum(1 for c in text if c.isalpha() and c in self.ru_layout)
        table = self.en_to_ru if en_letters >= ru_letters else self.ru_to_en
        return text.translate(table)

    def _swap_layout(self, text):
        parts = self.protected_re.split(text)
        return "".join(
            part if i % 2 == 1 else self._swap_chars(part)
            for i, part in enumerate(parts)
        )

    def _words(self, text):
        return self.word_re.findall(text)

    def _ru_score(self, text):
        tokens = self._words(text)
        if not tokens:
            return 0.0
        known = sum(1 for word in tokens if self.morph.word_is_known(word))
        return known / len(tokens)

    def _en_score(self, text):
        tokens = self._words(text)
        if not tokens:
            return 0.0
        known = sum(1 for word in tokens if word.lower() in EN_COMMON_WORDS)
        return known / len(tokens)

    async def _find_last_own_message(self, message, me):
        async for msg in message.client.iter_messages(message.chat_id, offset_id=message.id, limit=self.history_scan_limit):
            if msg.sender_id == me.id and msg.text:
                return msg
        return None

    async def kbscmd(self, message):
        """Используй .kbs (реплай, текст или без аргументов — последнее твоё сообщение), чтобы сменить раскладку"""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        client = message.client
        me = await client.get_me()

        if args:
            target_text = args
            target_msg = message
        elif reply:
            target_text = reply.raw_text
            if reply.sender_id == me.id:
                target_msg = reply
                await message.delete()
            else:
                target_msg = message
        else:
            target_msg = await self._find_last_own_message(message, me)
            if target_msg is None:
                await utils.answer(message, "<tg-emoji emoji-id=5456307331644037599>🌘</tg-emoji> Не нашёл твоего последнего сообщения для исправления")
                return
            target_text = target_msg.raw_text
            await message.delete()

        converted_text = self._swap_layout(target_text)

        if target_msg.id == message.id:
            await message.edit(converted_text)
        else:
            await target_msg.edit(converted_text)

    async def kbsautocmd(self, message):
        """<on/off> — вкл/выкл автоисправление раскладки в своих сообщениях (без аргумента — переключает)"""
        args = utils.get_args_raw(message).strip().lower()
        if args in ("on", "вкл", "1", "true"):
            enabled = True
        elif args in ("off", "выкл", "0", "false"):
            enabled = False
        else:
            enabled = not self.get("kbs_auto", True)
        self.set("kbs_auto", enabled)
        await utils.answer(
            message,
            "Автоисправление раскладки: "
            + ("включено <tg-emoji emoji-id=5458805056990119991>🌘</tg-emoji>" if enabled else "выключено <tg-emoji emoji-id=5456307331644037599>🌘</tg-emoji>"),
        )

    @loader.watcher(out=True, only_messages=True, no_commands=True, no_media=True)
    async def watcher(self, message):
        if not self.get("kbs_auto", True):
            return

        text = message.text
        if not text:
            return

        check_text = self.protected_re.sub(" ", text)
        if len(self._words(check_text)) < self.min_words:
            return

        is_latin = all(not ch.isalpha() or ch in self.en_layout for ch in check_text)
        is_cyrillic = all(not ch.isalpha() or ch in self.ru_layout for ch in check_text)

        if is_latin and not is_cyrillic:
            if self._en_score(check_text) < self.score_low and self._ru_score(self._swap_chars(check_text)) >= self.score_high:
                await message.edit(self._swap_layout(text))
        elif is_cyrillic and not is_latin:
            if self._ru_score(check_text) < self.score_low and self._en_score(self._swap_chars(check_text)) >= self.score_high:
                await message.edit(self._swap_layout(text))

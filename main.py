from rtmbot import RtmBot
from rtmbot.core import Plugin

import secret
# from secret import SLACK_TOKEN

class HelloPlugin(Plugin):
    def process_message(self, data):
        if "세영" in data["text"]:
            self.outputs.append([data["channel"], "안녕하세영?"])
        elif "배로선생님" in data["text"]:
            self.outputs.append([data["channel"], "지은: 근데 배로쌤 저 질문있어여-"])
        elif "애란선생님" in data["text"]:
            self.outputs.append([data["channel"], "지은: 근데 애란쌤 저 질문있어여-"])
        elif "가빈" in data["text"]:
            self.outputs.append([data["channel"], "가빈: 수업에 안나옴)"])
        elif "피곤해" in data["text"]:
            self.outputs.append([data["channel"], "소현:(오로나민씨 들고 입장) 1+1 이에요 :)"])
        elif "문희" in data["text"]:
            self.outputs.append([data["channel"], "문희: 잠은 죽어서 자요."])
        elif "예인" in data["text"]:
            self.outputs.append([data["channel"], "예인: (별안간 열정적인 탱고를 춘다:dancer:)"])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()

print("seyoung nim, please be strong")
print("점심10분남았다!히히!")
print("마이쮸 포도보다는 사과가 더 맛있다")

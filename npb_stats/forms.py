from django import forms

PLAYERCHOICES = (
    ("1", "野手 一軍"),
    ("2", "野手 二軍"),
    ("3", "投手 一軍"),
    ("4", "投手 二軍"),
)

TEAMCHOICES = (
    ("all", "全球団"),
    ("ce", "セ・リーグ"),
    ("pa", "パ・リーグ"),
    ("g", "巨人"),
    ("yb", "DeNA"),
    ("t", "阪神"),
    ("c", "広島"),
    ("d", "中日"),
    ("s", "ヤクルト"),
    ("l", "西武"),
    ("h", "ソフトバンク"),
    ("e", "楽天"),
    ("m", "ロッテ"),
    ("f", "日本ハム"),
    ("bs", "オリックス"),
    ("es", "イースタン・リーグ"),
    ("ws", "ウェスタン・リーグ"),
)

HITTERTARGETCHOICES = (
    ("1", "全て"),
    ("2", "上位50人"),
    ("3", "規定打席以上"),
    ("4", "規定打席の1/2以上"),
    ("5", "規定打席の1/3以上"),
    ("6", "ルーキー"),
    ("7", "新人王有資格者"),
)

PITCHERTARGETCHOICES = (
    ("1", "全て"),
    ("2", "上位50人"),
    ("3", "規定投球回以上以上"),
    ("4", "規定投球回以上の1/2以上"),
    ("5", "規定投球回以上の1/3以上"),
    ("6", "ルーキー"),
    ("7", "新人王有資格者"),
)

HITTERDATACHOICES = (
    ("打率", "打率"),
    ("試合", "出場試合数"),
    ("打席数", "打席数"),
    ("打数", "打数"),
    ("安打", "安打"),
    ("本塁打", "本塁打"),
    ("打点", "打点"),
    ("盗塁", "盗塁"),
    ("四球", "四球"),
    ("死球", "死球"),
    ("三振", "三振"),
    ("犠打", "犠打"),
    ("併殺打", "併殺打"),
    ("出塁率", "出塁率"),
    ("長打率", "長打率"),
    ("OPS", "OPS"),
)

PITCHERDATACHOICES = (
    ("防御率", "防御率"),
    ("試合", "出場試合数"),
    ("勝利", "勝利"),
    ("敗北", "敗北"),
    ("セーブ", "セーブ"),
    ("ホールド", "ホールド"),
    ("勝率", "勝率"),
    ("打者", "打者"),
    ("投球回", "投球回"),
    ("被安打", "被安打"),
    ("被本塁打", "被本塁打"),
    ("与四球", "与四球"),
    ("与死球", "与死球"),
    ("奪三振", "奪三振"),
    ("失点", "失点"),
    ("自責点", "自責点"),
    ("WHIP", "WHIP"),
)

class SelectForm(forms.Form):
    playerChoice = forms.ChoiceField(widget=forms.Select, choices=PLAYERCHOICES, label="どの成績を見ますか？")
    teamChoice = forms.ChoiceField(widget=forms.Select, choices=TEAMCHOICES, label="対象を選択してください")
    hitterTargetChoice = forms.ChoiceField(widget=forms.Select, choices=HITTERTARGETCHOICES, label="対象者を選択してください ※打者のみ")
    pitcherTargetChoice = forms.ChoiceField(widget=forms.Select, choices=PITCHERTARGETCHOICES, label="対象者を選択してください ※投手のみ")
    hitterDataChoice = forms.ChoiceField(widget=forms.Select, choices=HITTERDATACHOICES, label="表示する項目を選択してください ※打者のみ")
    pitcherDataChoice = forms.ChoiceField(widget=forms.Select, choices=PITCHERDATACHOICES, label="表示する項目を選択してください ※投手のみ")
    number = forms.IntegerField(initial=20, label="表示件数を入力してください")

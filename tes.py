from gt import GT

tes = GT()
print(tes.t("selamat pagi", "auto", "ja"))

#another example
text = tes.text("good morning", "en", "ko")
print(text["translate"])

text = tes.text("좋은 아침", "auto", "en")
print(text["translate"])

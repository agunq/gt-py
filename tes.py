from gt import GT

tes = GT()
print(tes.t("selamat pagi", "ja", "auto"))

#another example
text = tes.text("good morning", "ko", "en")
print(text["translate"])

text = tes.text("좋은 아침", "en")
print(text["translate"])

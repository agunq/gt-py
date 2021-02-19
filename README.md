# gt-py
google translate free API

## Usage

simply run 
python tes.py

``` py
from gt import GT

tes = GT()
print(tes.t("selamat pagi", "id", "ja"))
```

will make dict() output
``` py
{'translate': 'おはようございます', 'pronunciation': 'Ohayōgozaimasu', 'text': 'selamat pagi', 'pronunciation_text': None, 'lang_from': 'id', 'lang_to': 'ja'}
```

another example
``` py
tes = GT()
text = tes.text("good morning", "en", "ko")
print(text["translate"])
```
output
```
좋은 아침
```

and another one :v
``` py
tes = GT()
text = tes.text("좋은 아침", "auto", "en")
print(text["translate"])
```
output
``` py
Good morning
```


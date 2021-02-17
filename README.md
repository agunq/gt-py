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

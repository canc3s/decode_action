#2025-03-10 07:15:37
#//Base:https://github.com/echo094/decode-js
#//Modify:https://github.com/canc3s/decode_action


import bz2
import base64
import lzma
exec(bz2.decompress(base64.b64decode('' + b'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'.decode() + '')))
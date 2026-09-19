import tiktoken

zh = "数学是人类最伟大的成就。它不依赖语言，不依赖国界，一个证明在任何地方都同样成立。物理、工程、经济、计算机，全都建立在它之上。更难得的是，它常常在几百年后才被用上。"
en = "Math is humanity's greatest achievement. It doesn't depend on language or on borders — a proof holds equally well anywhere. Physics, engineering, economics, computing all rest on top of it. And the rarest part is that it often isn't put to use until centuries later."

try:
    enc = tiktoken.encoding_for_model("gpt-5.6-luna")
    which = "gpt-5.6-luna"
except KeyError:
    enc = tiktoken.get_encoding("o200k_base")
    which = "o200k_base (fallback — luna not in this tiktoken version)"

zh_tokens = len(enc.encode(zh))
en_tokens = len(enc.encode(en))

print(f"encoding: {which}")
print(f"EN: {en_tokens} tokens, {len(en)} characters")
print(f"ZH: {zh_tokens} tokens, {len(zh)} characters")
print(f"ratio ZH:EN = {zh_tokens / en_tokens:.2f}")
from transformers import AutoTokenizer

zh = "数学是人类最伟大的成就。它不依赖语言，不依赖国界，一个证明在任何地方都同样成立。物理、工程、经济、计算机，全都建立在它之上。更难得的是，它常常在几百年后才被用上。"
en = "Math is humanity's greatest achievement. It doesn't depend on language or on borders — a proof holds equally well anywhere. Physics, engineering, economics, computing all rest on top of it. And the rarest part is that it often isn't put to use until centuries later."

tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B")

zh_tokens = len(tok.encode(zh))
en_tokens = len(tok.encode(en))

print(f"EN: {en_tokens} tokens")
print(f"ZH: {zh_tokens} tokens")
print(f"ratio ZH:EN = {zh_tokens / en_tokens:.2f}")

# Tokens, context, attention and caching

The statistics exercise prints numbers reported by the service. To read them, start with what was sent: a rule, a question and a note. A tokenizer splits that text into units called tokens. A token is sometimes a whole word, sometimes part of one; the split depends on the model, so the number of characters in a question does not tell you the number of tokens.

**Input tokens** are the request as the service counts it, including some formatting the model adds around messages. **Output tokens** are the generated answer under the service's rules; some models also count their internal reasoning there. Two services do not necessarily count the same things, so read each provider's definitions.

The **context window** is how much text the model can handle in one request: history, instructions, sources and the answer it is generating all take up room. In the local request we set `num_ctx=4096`, which is why the output says "requested": it is our setting, not a measurement of how full the window is. Context also does not grow because another file sits on the disk; only what the program sends is in the request.

**Attention** is the mechanism inside the model that lets it relate each part of the text to the others, for example the question about Python lists to the note about item order. Our counters show how much text was processed, not which sentences the model actually relied on. A whole document can fit into the request and the model can still miss the one paragraph that matters, which is why we compare the answer with the source.

**Caching** comes in two forms. While generating, a model keeps intermediate results for the part of the request it has already processed (the KV cache), so it does not recompute them for every new token. Some services also support prompt caching: when several requests start with the same long instruction and document, the repeated beginning is not processed again. Conditions and prices differ between providers, and it is usually not a cache of finished answers. `cached_tokens=None` means the service reported nothing; zero means it reported zero.

Elapsed time and generation speed are different measures too. Elapsed time includes waiting, possibly loading the model, the calculation and the network exchange. Ollama reports generation duration separately, so its speed can be calculated from the answer alone.

Back to [the statistics exercise](extra-usage.md). When you compare runs, change one thing at a time and keep the same model, and treat the numbers as measurements of your computer, not a promise for another one.

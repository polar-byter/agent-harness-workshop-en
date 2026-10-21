# Tokens, context, attention and caching

In the statistics exercise we display values reported by a provider. To interpret them, start with what was sent: an instruction, a question and source notes. A tokenizer splits their text into units called tokens. A token is not reliably a whole word; the division depends on the model's tokenizer and the text.

**Input tokens** represent the request as counted by the service. **Output tokens** represent generated output under its accounting rules. Extra reasoning or protocol fields may be counted separately or included differently. Use the provider's definitions rather than assuming two services measure identical things.

The **context window** is the model's bounded capacity for the token sequence processed in a request. History, instructions, source text and generated output consume capacity under the model's particular limits. Raising a configured limit does not give the computer infinite memory or make missing evidence appear.

**Attention** is a mechanism that combines information from token representations as the model processes a sequence. It is not a guarantee that every sentence in a long document will influence the answer equally well. For our application, the practical question remains: did we send the relevant note, and did the answer use it correctly? Our token counters do not measure how much attention a particular sentence received.

**Prompt caching** can reuse computation for repeated input when a provider supports it. It does not necessarily mean a previously generated answer is simply returned. Cache eligibility, expiration and pricing vary. `cached_tokens=None` means the adapter has no reported value; zero means a reported zero. Preserve that difference in `format_usage`.

Elapsed request time also differs from generation throughput. Loading, waiting and network exchange contribute to elapsed time. Ollama may expose generation duration and token counts from which an output-token rate can be calculated; other services may not provide the same values.

Return to [the statistics exercise](extra-usage.md). Change one factor, such as the number of source notes, and compare recorded values with the same model. Label the result as your measurement rather than a speed promise for other computers.

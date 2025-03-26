from openai import OpenAI
# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:17600/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

stream = client.chat.completions.create(
    model="DeepSeek-R1-Distill-Qwen-7B",
    messages=[
        {"role": "assistant", "content": ""},
    ],
    temperature=0.1,
    top_p=0.8,
    max_tokens=16384,
    extra_body={
        "repetition_penalty": 1.05,
    },
    stream=True
)

# 实时流式输出
print("Chat response stream:")
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content is not None:
        print(content, end="", flush=True)

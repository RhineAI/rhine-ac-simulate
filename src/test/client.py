from openai import OpenAI
# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://10.176.56.244:17600/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

stream = client.chat.completions.create(
    model="DeepSeek-R1-Distill-Llama-70B",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "分析 Transformer 中的 QKV 矩阵的作用，并详细列出完整的数学原理，及运算和梯度下降等相关过程的代码和数学公式。"},
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

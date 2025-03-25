from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

MODEL_PATH = "/data/disk1/guohaoran/model/DeepSeek-R1"
SAMPLING_PARAMS = SamplingParams(
    temperature=0.1,
    top_p=0.5,
    frequency_penalty=0.2,
    repetition_penalty=1.05,
    max_tokens=16384,
    top_k=30,
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)


llm = LLM(model=MODEL_PATH, trust_remote_code=True)


prompt = "Tell me something about large language models."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)


outputs = llm.generate([text], SAMPLING_PARAMS)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt:\n{prompt!r}\nGenerated text:\n{generated_text!r}")

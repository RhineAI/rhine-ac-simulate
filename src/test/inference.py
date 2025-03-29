import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer


system_prompt = '''You are a helpful assistant.'''
user_prompt = '''请详细说明 Transformer 中的 QKV 矩阵分别具有什么作用？'''

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# 初始化计时
start_time = time.time()
print(f'[Init] Start at: {time.strftime("%H:%M:%S", time.localtime())}')

# 模型加载
model_path = "/data/disk1/guohaoran/model/DeepSeek-R1-Distill-Qwen-7B"
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    device_map='cuda:0',
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 输入预处理
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# 流式输出配置
streamer = TextStreamer(
    tokenizer,
    skip_prompt=True,
    skip_special_tokens=True,
)

# 生成参数
print("\n[Generation Start]")
generate_start = time.time()

# 执行生成（关键修改点）
generated = model.generate(
    **model_inputs,
    max_new_tokens=512,
    streamer=streamer,
    pad_token_id=tokenizer.eos_token_id,
    return_dict_in_generate=True,
    output_scores=True,
    return_legacy_cache=True,
)

# 性能统计
generate_duration = time.time() - generate_start
total_new_tokens = generated.sequences[0].size(0) - model_inputs.input_ids.size(1)
tpm = total_new_tokens / (generate_duration / 60)

# 最终输出
print(f"\n[Status] Generation completed in {generate_duration:.2f}s")
print(f"[Metric] TPM: {tpm:.0f} | Tokens: {total_new_tokens}")
print(f"[Total] Duration: {time.time() - start_time:.2f}s")


./llama.cpp/build/bin/llama-cli \
  -m /data/disk1/guohaoran/model/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf \
  -c 8192 \
  --chat-template deepseek3 \
  --n-gpu-layers 8 \
  --cache-type-k f32 \
  --prio 2 \
  --temp 0 \
  --no-mmap

sudo ./llama.cpp/build/bin/llama-server \
  -m /data/disk1/guohaoran/model/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf \
  -c 8192 \
  --chat-template deepseek3 \
  --n-gpu-layers 8 \
  --cache-type-k f32 \
  --prio 2 \
  --temp 0 \
  --host 0.0.0.0 \
  --port 9090 \
  --no-mmap

用 Python 写一个 LLM 的 Transformer 层


sudo ./llama.cpp/build/bin/llama-server \
  -m /data/disk1/guohaoran/model/DeepSeek-R1-GGUF-Q8/DeepSeek-R1-Q8_0/DeepSeek-R1.Q8_0-00001-of-00015.gguf \
  -c 4096 \
  --threads 48 \
  --chat-template deepseek3 \
  --n-gpu-layers 32 \
  --cache-type-k f16 \
  --host 0.0.0.0 \
  --port 9090 \
  --prio 2 \
  --temp 0 \
  --no-mmap

用 Python 写一个 LLM 的 Transformer 层

Rust写冒泡排序

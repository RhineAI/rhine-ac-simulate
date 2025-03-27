
CUDA_VISIBLE_DEVICES=0,1 ./llama.cpp/build/bin/llama-server \
  -m /data/disk1/guohaoran/model/DeepSeek-R1-Distill-Qwen-32B-GGUF/DeepSeek-R1-Distill-Qwen-32B-F16/DeepSeek-R1-Distill-Qwen-32B-F16-00001-of-00002.gguf \
  -c 4096 \
  --threads 48 \
  --chat-template deepseek3 \
  --n-gpu-layers 65 \
  --cache-type-k f16 \
  --host 0.0.0.0 \
  --port 9090 \
  --prio 2 \
  --temp 0 \
  --no-mmap

Rust写冒泡排序

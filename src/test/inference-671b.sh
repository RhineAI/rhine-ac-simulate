
./llama.cpp/build/bin/llama-cli \
  --model models/DeepSeek-R1-Q4_K_M/DeepSeek-R1-Q4_K_M-00001-of-00009.gguf \
  --n-gpu-layers 24 \
  --cache-type-k q4_0 \
  --threads 15 --prio 2 \
  --temp 0.6 \
  --ctx-size 8192 \
  --seed 3407

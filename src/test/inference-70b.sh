vllm serve /data/disk1/guohaoran/model/DeepSeek-R1-Distill-Llama-70B \
  --served-model-name DeepSeek-R1-Distill-Llama-70B \
  --port 17600 \
  --dtype bfloat16 \
  --tensor_parallel_size 8 \
  --gpu-memory-utilization 0.95
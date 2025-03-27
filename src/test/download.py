from modelscope import snapshot_download

snapshot_download(
  "unsloth/DeepSeek-R1-Distill-Qwen-32B-GGUF",
  local_dir="/data/disk1/guohaoran/model/DeepSeek-R1-Distill-Qwen-32B-GGUF",
  allow_patterns=["*32B-F16*"],
)

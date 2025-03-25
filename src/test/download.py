from modelscope import snapshot_download

snapshot_download(
  "unsloth/DeepSeek-R1-GGUF",
  local_dir="/data/disk1/guohaoran/model/DeepSeek-R1-GGUF",
  allow_patterns=["DeepSeek-R1-Q4_K_M*"],
)

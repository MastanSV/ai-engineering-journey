import torch

print(f"pyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")

if torch.cuda.is_available():
    print(f"GPU:                 {torch.cuda.get_device_name(0)}")
    vram_gb = torch.cuda.get_device_properties(0).total_memory / 1e9
    print(f"VRAM:    {vram_gb:.2f} GB")

    #real GPU sanity check - actually do compute     on the GPU
    x = torch.randn(1000, 1000, device="cuda")
    y = x @ x.T
    torch.cuda.synchronize()
    print(f"Matmul on GPU: OK (result shape: {tuple(y.shape)})")
    print("\n✅ GPU READY. Green light to proceed.")
else:
    print("\n CUDA NOT AVAILABLE - STOP AND DEBUG.")
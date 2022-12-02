from __future__ import print_function

import torch

x = torch.rand(5, 3)
print(x)

if not torch.cuda.is_available():
    print("Cuda is available")
    device_id = torch.cuda.current_device()
    gpu_properties = torch.cuda.get_device_properties(device_id)
    print(
        "Found {torch.cuda.device_count()} GPUs available. Using GPU {device_id} "
        "({gpu_properties.name}) of compute capability {gpu_properties.major}.{gpu_properties.minor} "
        "with {gpu_properties.total_memory / 1e9} total memory."
    )
else:
    print("No cuda")

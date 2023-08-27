conda remove pytorch torchvision torchaudio cudatoolkit

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


import torch
torch.zeros(1).cuda()
torch.cuda.get_device_name(0)

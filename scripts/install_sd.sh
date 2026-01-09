#!/bin/bash

# Clone Automatic1111 Stable Diffusion WebUI
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui

# Patch repo URLs for Kaggle compatibility
sed -i 's@https://github.com/Stability-AI/stablediffusion.git@https://github.com/w-e-w/stablediffusion.git@g' stable-diffusion-webui/modules/launch_utils.py
sed -i 's@https://github.com/Stability-AI/stablediffusion@https://github.com/w-e-w/stablediffusion@g' stable-diffusion-webui/modules/launch_utils.py

# Update transformers version
sed -i 's/transformers==4.30.2/transformers==4.38.2/g' stable-diffusion-webui/requirements_versions.txt

# Install dependencies
pip install -r stable-diffusion-webui/requirements_versions.txt

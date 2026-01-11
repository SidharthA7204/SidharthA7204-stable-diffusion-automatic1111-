# Stable Diffusion with Automatic1111 on Kaggle GPU

## Overview
This project demonstrates how to run Stable Diffusion using Automatic1111 WebUI on a free Kaggle GPU and access it remotely via Ngrok. It allows unlimited AI image generation with full control over prompts, samplers, CFG scale, seeds, and image resolution without using paid APIs.

This setup is designed for learning diffusion models, prompt engineering, and real-world AI deployment workflows.

---

## Key Features
- Free GPU-powered image generation using Kaggle
- Automatic1111 WebUI for easy control
- Text-to-Image (txt2img) and Image-to-Image (img2img)
- Full parameter control (CFG, Sampler, Steps, Seed, Batch)
- Remote browser access via Ngrok
- Open-source and customizable
- No daily limits or subscriptions

---

## Technologies Used
- Stable Diffusion
- Automatic1111 WebUI
- Kaggle Notebook (GPU Runtime)
- Ngrok
- Python
- PyTorch

---

## Capabilities
- Text-to-Image generation
- Image-to-Image transformation
- Style-based image generation
- Batch image creation
- Reproducible outputs using seeds
- Multiple sampling methods (Euler, DPM++, DDIM)

---

## Architecture
User Browser
   |
   | (Ngrok Secure Tunnel)
   |
Kaggle Cloud GPU
   |
   ├── Automatic1111 WebUI
   └── Stable Diffusion Model

---

## Setup Instructions

### Step 1: Kaggle Notebook
1. Create a new Kaggle Notebook
2. Enable GPU from notebook settings
3. Paste or upload the provided notebook code

### Step 2: Install Stable Diffusion
- Clone Automatic1111 repository
- Install required dependencies
- Download Stable Diffusion model files

### Step 3: Ngrok Configuration
1. Create a free Ngrok account
2. Copy your Ngrok Auth Token
3. Add the token inside the notebook
4. Run Ngrok to generate a public URL

### Step 4: Access WebUI
- Open the Ngrok URL in your browser
- Automatic1111 WebUI will load
- Start generating images

---

## Core Controls Explained
Prompt: Describes what you want the AI to generate  
Negative Prompt: Specifies what the AI should avoid  
CFG Scale: Controls how closely the AI follows the prompt  
Sampling Steps: Higher steps give better refinement  
Sampler: Controls speed vs quality  
Seed: Reproduce the same image again  

---

## Example Prompt
Prompt:
A cinematic portrait of a futuristic cyberpunk warrior, ultra realistic, sharp focus, dramatic lighting, 8k

Negative Prompt:
blurry, low quality, extra fingers, deformed face, watermark

---

## Notes and Limitations
- Kaggle sessions are temporary
- Ngrok URLs change every session
- Model files are not stored in this repository
- Intended for educational and portfolio use

---

## Repository Structure
stable-diffusion-automatic1111/
│
├── README.md
├── kaggle_notebook.ipynb
├── setup/
│   ├── install.sh
│   └── ngrok_setup.sh
├── prompts/
│   └── sample_prompts.txt
└── screenshots/
    └── ui_preview.png

---

## License
This project is licensed under the MIT License.

---


## 👤 Author

Sidharth A  
- GitHub: https://github.com/SidharthA7204  
- LinkedIn: : www.linkedin.com/in/sidhartha742003 

Open to opportunities

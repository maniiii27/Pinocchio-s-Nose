# Pinocchio's Nose: Digital Wellbeing Solution
## Overview
Pinocchio's Nose is a comprehensive online wellbeing platform designed to detect various forms of manipulated or inappropriate content. Named after the famous character whose nose grew when he lied, this project aims to identify "digital lies" in the form of deepfakes, AI-generated images, and inappropriate audio content.
## 🚀 Key Features
### 1. Pinocchio's Nose: Deepfake Image Detection
> [!NOTE]
> The Resnet50 Model is hosted on **Hugging Face🤗** for easy loading and deployment. [**View**](https://huggingface.co/krimson1/Resnet50_deepfake_detection)

- 🔍 **Advanced Neural Architecture:** Leverages a calibrated **ResNet50** architecture to identify manipulated facial imagery
- 🗂️ **Comprehensive Dataset:** Trained on the **DeepFakeFace** dataset containing **30,000 real** and **90,000 deepfake** images
- 📈 **High Performance:** Achieves **98.1% accuracy** on detection tasks
- 🛡️ **Misinformation Shield:** Flags deepfake images to prevent the spread of **false information**
- 📚 **Dataset Link:** [**DeepFakeFace**](https://huggingface.co/datasets/OpenRL/DeepFakeFace)


### 2. Pinocchio's Nose: AI-Generated Image Detection

- 🔍 **Advanced AI-Powered Detection:** Leverages a Convolutional Neural Network (CNN) trained on extensive AI and real image datasets
- 🗂️ **Misinformation Combat:** Identifies and flags AI-generated and deepfake images
- 🛡️ **Cyber Crime Reporting:** Provides direct reporting mechanism to Indian cyber crime portal when deepfakes are detected
- 📈 **Robust Training Dataset:** Trained over a dataset of 100,000 images, consisting of 50,000 fake and 50,000 real images. 
- 📚 Dataset Link: [**CIFAKE**](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images)


<p>
  <img src="https://github.com/Visheshh21/Pinocchio-s-Nose/blob/main/misc/pinocchio's_nose_md1.png" width="300">
  <img src="https://github.com/Visheshh21/Pinocchio-s-Nose/blob/main/misc/pinocchio's_nose_md2.png" width="300">
</p>

### 3. VulgarVeto: Audio Profanity Filter

- 🗣️ **Automated Profanity Detection:** Uses Google Speech Recognition for precise audio analysis
- 🚫 **Comprehensive Filtering:** Identifies and censors explicit language in real-time
- 🎛️ **Customizable Controls:** User-friendly interface for personalized content moderation
<img src="https://github.com/Visheshh21/Pinocchio-s-Nose/blob/main/misc/image%20(1).png" width="500">

## 🧾 Project Structure:
- **[ResNet50_Training.ipynb](https://github.com/Visheshh21/Pinocchio-s-Nose/blob/main/ResNet50_Training.ipynb)**  
  Trains a ResNet50 model on an image dataset to detect deepfake content.
- **[Resnet50_Usage.ipynb](https://github.com/Visheshh21/Pinocchio-s-Nose/blob/main/Resnet50_Usage.ipynb)**  
  Demonstrates how to load and use the trained ResNet50 model for inference on new images.
- **[CNN_Training.ipynb](https://github.com/Visheshh21/Pinocchio-s-Nose/blob/main/CNN_Training.ipynb)**  
  Builds and trains a custom Convolutional Neural Network (CNN) for binary classification of AI-generated vs. real images.
- **[CNN_Usage_ui.py](https://github.com/Visheshh21/Pinocchio-s-Nose/blob/main/CNN_Usage_ui.py)**  
  Implements a simple UI to upload images and get predictions from the trained CNN model.
- **[VulgarVeto.py](https://github.com/Visheshh21/Pinocchio-s-Nose/blob/main/VulgarVeto.PY)**  
  Filters and flags profane language in audio content using speech recognition and text analysis.


#### 🖋️ **Key Capabilities**
- Image preprocessing and data augmentation techniques
- Comprehensive model performance monitoring
- Cutting-edge machine learning approaches to combat digital manipulation
- Supports audio file input
- Converts speech to text
- Maintains extensive profanity database
- Replaces offensive content with "beep" sounds or custom censoring.

## 🔮 Future Scope

#### **For Pinocchio’s Nose:**
- Implement **EfficientNetB7, or Vision Transformer** as the classifier for better detection performance.
#### **For VulgarVeto:**
- Integrate speech recognition models like **Wav2Vec2 or Whisper (OpenAI)** for advanced speech-to-text capabilities.
- Use **SpeechT5 (Microsoft) or F5** as a text-to-speech tool for improved translation of machine language to audio.

## 🎯 Mission
Promoting responsible technology use and creating safer digital communities by providing intelligent, user-centric content moderation tools.

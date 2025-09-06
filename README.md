# 🖼️ Image Caption Generator 🤖

## Project Overview  
The Image Caption Generator is an AI-powered system that automatically generates descriptive captions for images.  
It combines computer vision (**CNNs**) with natural language processing (**LSTMs**) to produce human-like image descriptions.  
The project is implemented with **Flask** for the web interface and leverages pre-trained models for accuracy.  

## Key Features  
1. 📷 **Image Upload & Processing**  
   - Upload images via the web interface.  
   - Extracts features using the **Xception** model (pre-trained on ImageNet).  

2. 📝 **Automatic Caption Generation**  
   - Generates descriptive captions word by word.  
   - Uses an **LSTM (Long Short-Term Memory)** network for sequence modeling.  

3. 🔬 **Deep Learning Architecture**  
   - **CNN (Xception)** for feature extraction.  
   - **LSTM** for natural language text generation.  

4. 🎨 **User-Friendly Interface**  
   - Built with **Flask, HTML, and CSS**.  
   - Simple and interactive GUI to test the model.  

## Tech Stack  

- **Keras** → High-level deep learning API.  
- **TensorFlow** → Backend ML framework.  
- **Xception Model** → Pre-trained CNN for feature extraction.  
- **LSTM** → Generates captions word by word.  
- **Flask, HTML, CSS** → Interactive web application.  
- **Kaggle (Flickr8K Dataset)** → Image-caption dataset.  

## Model Architecture  

![Image](https://github.com/user-attachments/assets/a0b8f108-ecb3-4eff-9d9b-f87420cad366) 

- **Vision Understanding:** CNN extracts features from the image and converts them into a feature vector.  
- **Text Generation:** LSTM generates captions sequentially, starting with a *start* token and ending with an *end* token.  

## Dataset Description  

- **Dataset:** Flickr8K  
- **Images:** 8091 total  
- **Captions:** 5 captions per image  
- **Structure:**  
  - `Flicker8k_Dataset` → Contains images  
  - `Flickr_8k_text` → Contains captions  

## Evaluation Metric  

📊 **BLEU Score** (Bilingual Evaluation Understudy) is used to evaluate captions.  
- Score close to **1** → Generated captions match human captions.  
- Score close to **0** → Captions differ significantly.  

## Interface Screenshots  

<img width="550" height="300" alt="Image" src="https://github.com/user-attachments/assets/5c4b7cf3-9501-45ab-9fbe-df39adcd7cf3" />  

<img width="550" height="300" alt="Image" src="https://github.com/user-attachments/assets/24781ef8-e322-449c-8577-0e09de09df41" />

## Getting Started  

### Prerequisites  
Make sure you have the following installed:  
- Python 3.8+  
- TensorFlow & Keras  

### Clone the Repository  
```sh
git clone <repository-url>
cd <project-directory>
```
## Run the App
```sh
python app.py
```

## Try the App 🚀

👉 Coming soon with a live Flask deployment!

## Contact

For questions or suggestions, feel free to reach out:

📩 elhadifi.soukaina@gmail.com

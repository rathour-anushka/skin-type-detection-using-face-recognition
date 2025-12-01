# Skin Type Detection Using Face Recognition

A deep-learning powered system that classifies a person's **skin type** (Dry, Oily, Normal, Combination, Sensitive) using facial analysis.  
The project integrates **computer vision** (OpenCV) for face detection and **MobileNetV2** (transfer learning) for classification, supporting both **image upload** and **real-time webcam input**.

---

## 📌 Features
- 🔍 **Face Detection** using OpenCV  
- 🧠 **Skin Type Classification** with MobileNetV2 (fine-tuned on custom dataset)  
- 📊 **Balanced Dataset** of 2250 labeled images across 5 categories  
- 🎛️ **Data Augmentation** (brightness, zoom, rotation, contrast) for generalization  
- ⚡ **Real-Time Prediction** via webcam stream  
- 🖥️ **Backend Integration** with modular API (controllers, services, utilities)  
- 📱 **Scalable Deployment** for skincare apps, dermatology tools, and recommendation systems  

---

## 🏗️ System Architecture
1. **Dataset Preparation** → Balanced Train/Validation/Test splits  
2. **Preprocessing** → Face detection, cropping, normalization  
3. **Model Training** → MobileNetV2 fine-tuned on skin-type dataset  
4. **Evaluation** → Accuracy, loss curves, generalization checks  
5. **Backend API** → FastAPI/Node.js endpoints for predictions  
6. **Prediction Workflow** → Supports both image upload & webcam input  

---

## ⚙️ Tech Stack
- **Languages:** Python, Node.js  
- **Libraries:** TensorFlow, Keras, OpenCV, Pandas, NumPy, Scikit-learn  
- **Backend:** FastAPI, REST APIs  
- **Tools:** Google Colab, Power BI (visualization), UML diagrams for design  
- **Databases:** MySQL, PostgreSQL  

---

## 🚀 Installation & Setup
```bash
# Clone the repository
git clone https://github.com/your-username/skin-type-detection.git
cd skin-type-detection

# Install dependencies
pip install -r requirements.txt

# Run training (Google Colab / local)
python train.py

# Start backend server
uvicorn app.main:app --reload

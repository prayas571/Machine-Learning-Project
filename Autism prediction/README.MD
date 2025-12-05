# 🧠 Autism Spectrum Disorder (ASD) Risk Prediction Using Machine Learning

Early identification of Autism Spectrum Disorder (ASD) is a major challenge because traditional diagnostic procedures are time-consuming, costly, and require trained medical specialists. This project aims to develop a reliable **machine learning–based classification system** to predict the **risk of Autism Spectrum Disorder (ASD)** using behavioral, demographic, medical, and contextual data. The system is intended as a **supportive early screening tool**, not as a medical diagnosis.

---

## 📌 Project Objective

To build a machine learning model that predicts the likelihood of Autism Spectrum Disorder (ASD) using:

* Behavioral screening scores (A1–A10)
* Demographic details (age, gender, ethnicity)
* Medical history (jaundice at birth, family history of autism)
* Contextual features (country of residence, prior screening app usage)

---

## 📊 Dataset Description

The dataset contains multiple features categorized as follows:

### ✅ Behavioral Screening Features

* `A1_Score` – Social interest / interaction
* `A2_Score` – Communication behavior
* `A3_Score` – Imagination behavior
* `A4_Score` – Attention behavior
* `A5_Score` – Emotional response
* `A6_Score` – Sensory behavior
* `A7_Score` – Routine behavior
* `A8_Score` – Eye contact
* `A9_Score` – Social comfort
* `A10_Score` – Repetitive behavior

### ✅ Demographic & Medical Features

* `age` – Age of the person
* `gender` – Male (m) / Female (f)
* `ethnicity` – Racial background
* `jaundice` – Jaundice at birth (yes/no)
* `austim` – Family history of autism (yes/no)

### ✅ Contextual Features

* `contry_of_res` – Country of residence
* `used_app_before` – Prior use of autism screening app

### ✅ Target Variable

* `Class/ASD` – Output label

  * `0` → No Autism
  * `1` → Autism

---

## ⚙️ Machine Learning Models Used

The following classification models were trained and evaluated:

* ✅ Decision Tree
* ✅ Random Forest
* ✅ XGBoost

---

## 📈 Model Performance (5-Fold Cross Validation)

| Model         | Mean Accuracy           |
| ------------- | ----------------------- |
| Decision Tree | ~85.6%                  |
| Random Forest | **~91.9% (Best Model)** |
| XGBoost       | ~90.4%                  |

✅ **Random Forest was selected as the final model** due to its highest accuracy and stable performance across all folds.

---

## 🏆 Key Features of the Project

* ✅ Real-world healthcare-based prediction system
* ✅ Multiple machine learning models tested
* ✅ Cross-validation for performance stability
* ✅ Proper model comparison and selection
* ✅ Suitable for academic and professional portfolios

---

## ⚠️ Medical Disclaimer

> This system is intended **only for early risk screening and educational purposes**.
> It does **not replace professional medical diagnosis**. Final diagnosis must always be done by a qualified healthcare professional.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib / Seaborn

---

## 🚀 How to Run the Project

1. Clone the repository:

   ```
   git clone https://github.com/your-username/your-repository-name.git
   ```
2. Install required libraries:

   ```
   pip install -r requirements.txt
   ```
3. Run the notebook:

   ```
   jupyter notebook Autism_Prediction.ipynb
   ```

---

## 📌 Future Enhancements

* ✅ Web application deployment using Streamlit or Flask
* ✅ ROC-AUC curve and feature importance visualization
* ✅ Cloud deployment
* ✅ Real-time user input interface

---

## 👨‍💻 Author

**Prayas Sahoo**
Aspiring AI Developer with a strong foundation in Data Analysis, Machine Learning, and Intelligent Applications.

---

## ⭐ If you like this project, don’t forget to give it a star on GitHub!


# 🎯 Customer Uplift Modeling for Targeted Marketing

## 📌 Overview

This project implements an **end-to-end causal machine learning system** to identify customers who are most likely to respond positively to marketing interventions. Instead of predicting churn or conversion probability alone, the model estimates the **incremental impact of marketing campaigns (uplift)** on individual customers.

The system helps businesses optimize marketing budgets by targeting only those customers whose behavior can be influenced by promotional campaigns.

The project includes data preprocessing, exploratory analysis, uplift model training, evaluation using uplift metrics, and an interactive dashboard for campaign insights.

---

# 💼 Business Problem

Traditional predictive models identify customers likely to convert. However, many of these customers would convert **even without marketing intervention**, which wastes marketing budget.

**Uplift modeling solves this by identifying:**

* 🎯 Customers who will respond **only if targeted**
* 🛒 Customers who will purchase **regardless of marketing**
* 🚫 Customers who **should not be targeted**

This enables **data-driven campaign optimization and ROI improvement.**

---

# 📊 Dataset

The project uses the **Kevin Hillstrom MineThatData Email Marketing Dataset**, a well-known dataset for uplift modeling research.

The dataset contains customer behavioral features including:

* Customer recency
* Purchase history
* Channel preference
* Previous campaign interactions
* Spending behavior

Target variables:

* 📧 **Treatment** → Whether a marketing email was sent
* 💰 **Conversion** → Whether the customer made a purchase

---

# 🏗 Project Architecture

```
churn_uplift_project
│
├── .ipynb_checkpoints
│   ├── EDA-checkpoint.ipynb
│   └── Untitled-checkpoint.ipynb
│
├── data
│   ├── raw
│   │   └── Kevin_Hillstrom_Email_Data.csv
│   │
│   └── processed
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_test.csv
│       ├── t_train.csv
│       └── t_test.csv
│
├── notebooks
│   └── EDA.ipynb
│
├── models
│   └── baseline_model.pkl
│
├── outputs
│
├── .gitignore
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Methodology

## 1️⃣ Data Preprocessing

* Data cleaning and feature engineering
* Handling categorical variables
* Train-test split with treatment indicators

## 2️⃣ Exploratory Data Analysis

EDA was performed to analyze:

* Customer purchase behavior
* Campaign response patterns
* Feature distributions
* Treatment vs control conversion differences

---

## 🤖 3️⃣ Uplift Modeling Approach

The project focuses on **causal machine learning techniques** rather than traditional predictive models.

Key idea:

```
Uplift = P(conversion | treatment) - P(conversion | control)
```

The model estimates the **incremental impact of marketing intervention**.

---

# 📈 Model Evaluation

Uplift models are evaluated using **ranking-based metrics** rather than traditional accuracy metrics.

Key evaluation methods:

* 📊 **Uplift Curve**
* 📉 **Qini Curve**
* 🔟 **Decile Analysis**
* 🔍 **Treatment vs Control response comparison**

These metrics measure how well the model identifies customers whose behavior is influenced by marketing.

---

# 🖥 Interactive Dashboard

The project includes a **Streamlit dashboard** to visualize campaign performance and uplift insights.

The dashboard allows users to:

* 📊 Explore customer segments
* 📈 Visualize uplift scores
* 🔍 Analyze treatment vs control conversions
* 🎯 Simulate marketing targeting strategies

---

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/CodingWithDevraj/churn-uplift-project.git
cd churn-uplift-project
```

---

## 2️⃣ Install Dependencies

Create a virtual environment and install requirements.

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

# 🧰 Tech Stack

**Programming**

* 🐍 Python

**Data Processing**

* Pandas
* NumPy

**Machine Learning**

* Scikit-learn
* XGBoost

**Visualization**

* Plotly
* Matplotlib
* Seaborn

**Dashboard**

* Streamlit

---

# 🎯 Key Outcomes

* Built an end-to-end **causal machine learning pipeline**
* Identified customers most likely to respond to marketing campaigns
* Implemented **uplift modeling techniques for targeted marketing**
* Developed an **interactive dashboard for campaign simulation and insights**
* Demonstrated how uplift modeling can significantly improve **marketing ROI**

---

# 🔮 Future Improvements

Possible extensions for the project:

* Implement **Meta-Learners (T-Learner, S-Learner, X-Learner)**
* Add **Causal Forest models**
* Build **real-time campaign optimization**
* Deploy the dashboard on **Streamlit Cloud**

---

# 👨‍💻 Author

**Devraj Choudhary**

🎓 B.Tech – Gurukul Kangri University
📍 Roorkee, Uttarakhand

📧 Email: [devrajror366@gmail.com](mailto:devrajror366@gmail.com)

🔗 LinkedIn:
[https://www.linkedin.com/in/devraj-choudhary-3889412bb/](https://www.linkedin.com/in/devraj-choudhary-3889412bb/)

💻 GitHub:
[https://github.com/CodingWithDevraj](https://github.com/CodingWithDevraj)

🌐 **Working Dashboard:**
[https://churn-uplift-project-ywtsbsygcbjklcrmuqubnm.streamlit.app/](https://churn-uplift-project-ywtsbsygcbjklcrmuqubnm.streamlit.app/)

---


If you want, I can also give you **3 small GitHub improvements that make your project look like a senior data scientist project (and impress recruiters)**.



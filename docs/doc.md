# Documentation: Forecasting Nepal’s Economic and Social Development  

## 📖 Project Description  
This project is developed as part of the internship requirement for the course **Python with Data Science**.  
The goal is to **forecast Nepal’s economic and social development** using time series forecasting models and deploy the results as an **interactive Streamlit web app**.  

We focus on four key indicators that represent Nepal’s progress from **1980 to 2024** and forecast for the next **10 years**:  

1. **GDP (Gross Domestic Product)** – Economic output of Nepal  
2. **Life Expectancy** – Average lifespan of people  
3. **Total Population** – Number of people living in Nepal  
4. **GDP per Capita** – Average income per person  

---

## 📊 Dataset Details  

- **Source:** World Bank API (via `pandas_datareader`)  
- **Years Covered:** 1980 – 2024 (45 years)  
- **Features:**
  - GDP (in billions, USD)  
  - Life Expectancy (in years)  
  - Population (in billions)  
  - GDP per Capita (calculated feature)  
- **Dropped:** Literacy Rate (84% missing values)  

---

## 🔄 Data Preprocessing  

1. **Drop Columns** – Removed Literacy Rate and Country  
2. **Handle Missing Values** – Forward-fill for Life Expectancy (2.22% missing)  
3. **Feature Engineering** – Created GDP per Capita = GDP ÷ Population  
4. **Indexing** – Converted Year column to datetime and set as index  

---

## 📈 Exploratory Data Analysis (EDA)  

- **GDP:** Sharp growth after 2003, rising from $1.94B to $42.9B  
- **Life Expectancy:** Increased steadily from 48 to 70 years  
- **Population:** Almost doubled (15.5M → 29.7M)  
- **GDP per Capita:** Increased significantly ($125 → $1,447)  

---

## 🤖 Model Building  

- **Algorithm Used:** Facebook Prophet  
- **Forecast Horizon:** 10 years into the future  
- **Train-Test Split:**  
  - Train: 1980–2015  
  - Test: 2016–2024  

### ✅ Model Performance  
- All models achieved **MAE and RMSE < 16**, indicating high accuracy  

---

## 📦 Deployment  

- **Models Saved:** Pickle files (`model_gdp.pkl`, `model_life.pkl`, `model_pop.pkl`, `model_gdp_cap.pkl`)  
- **App:** Deployed using **Streamlit** (`app.py`)  
- **Interaction:** Users can select an indicator and forecast future values  

---

## 🛠️ Tech Stack  

- **Programming:** Python  
- **Libraries:**  
  - `pandas`, `numpy` – Data handling  
  - `pandas_datareader` – Data collection from World Bank  
  - `prophet` – Forecasting  
  - `matplotlib`, `seaborn` – Visualization  
  - `scikit-learn` – Evaluation  
  - `streamlit` – Deployment  

---


---

## 🚀 How to Run  

1. Clone repository and navigate into project folder:  
   ```bash
   git clone <repo-link>
   cd Forecasting-Nepal-Development

2. Create virtual environment (Python 3.10+ recommended):
python -m venv myenv
myenv\Scripts\activate   # Windows
source myenv/bin/activate  # Linux/Mac

3. Install requirements:

pip install -r requirements.txt

4. Run the Streamlit app:

streamlit run app.py

✍️ Author: Dipen Sherpa
📖 Internship Project: Python with Data Science



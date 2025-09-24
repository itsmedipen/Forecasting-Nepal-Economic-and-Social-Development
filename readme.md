# Forecasting Nepal’s Economic and Social Development  

This project was developed as part of the internship requirement for the course **“Python with Data Science”**.  
The objective is to build a **Time Series Forecasting Model** to predict Nepal’s economic and social development indicators and deploy the results as an interactive **Streamlit web application**.  

The project uses data from the **World Bank API (via pandas_datareader)** and applies **Facebook Prophet** for time series forecasting.  

---

## 📌 Project Overview  

Nepal’s development progress is studied and forecasted using **four key indicators**:  

1. **Gross Domestic Product (GDP):**  
   Total monetary value of all goods and services produced within a country’s borders in one year.  
   - In Nepal, GDP increased from **1.94B USD (1980)** to **42.9B USD (2024)**.  

2. **Life Expectancy:**  
   Average number of years a person is expected to live.  
   - In Nepal, life expectancy rose from **48 years** to **70 years**.  

3. **Total Population:**  
   The total number of people living in Nepal.  
   - Grew from **15.5M** to **29.7M** over 45 years.  

4. **GDP per Capita:**  
   Average economic output per person, calculated as GDP ÷ Population.  
   - Increased from **$125** to **$1,447**.  

👉 Units: GDP and Total Population are expressed in **billions**, and currency is in **USD**.  
👉 Note: The **Literacy Rate** column was dropped due to **84% missing values**.  

---

## ⚙️ Steps in the Project  

### 1. **Data Collection**  
- Source: World Bank API (via `pandas_datareader`)  
- Time period: **1980 – 2024**  

### 2. **Data Cleaning & Transformation**  
- Dropped **Literacy Rate** (too many missing values)  
- Forward-filled missing values in **Life Expectancy** (2.22% missing)  
- Dropped **country** column  
- Converted **year** to datetime and set as index  

### 3. **Exploratory Data Analysis (EDA)**  
- Visualized each variable using **line and bar charts**  
- Observations:  
  - GDP growth accelerated after 2003  
  - Life Expectancy gradually improved year by year  
  - Population nearly doubled in 45 years  
  - GDP per capita followed GDP’s upward trend  

### 4. **Feature Engineering**  
- Created **GDP per Capita** = GDP ÷ Total Population  

### 5. **Model Building**  
- Used **Prophet** to build forecasting models for all four indicators  

### 6. **Train-Test Split & Evaluation**  
- Train set: **1980–2015**  
- Test set: **2016–2024**  
- Evaluated using **MAE** and **RMSE**  
- Results: **All models achieved MAE and RMSE < 16**, indicating strong accuracy  

### 7. **Model Optimization**  
- Since errors are already low, **cross-validation was not required**  

### 8. **Model Saving**  
- Models serialized with **Pickle** for deployment  

### 9. **Deployment**  
- Deployed as a **Streamlit Web App** for interactive forecasting  

---

## 📊 Key Insights  

- Nepal’s **GDP** shows strong upward growth after 2003  
- **Life Expectancy** steadily increased, reflecting healthcare and living improvements  
- **Population** nearly doubled in 45 years  
- **GDP per Capita** rose significantly, showing improved economic well-being  

---

## 🚀 Tech Stack  

- **Python**  
- **pandas**, **numpy**  
- **pandas_datareader** (World Bank API)  
- **Prophet** (time series forecasting)  
- **scikit-learn** (evaluation)  
- **seaborn**, **matplotlib** (visualization)  
- **Streamlit** (deployment)  

---

## 📂 Project Structure 

📁 FORECASTING NEPAL ECONOMIC AND SOCIAL DEVELOPMENT
│── 📁 docs
│   └── doc.md
    └── Forecasting Nepal’s Economic and Social Development.docx
│── 📄 app.py
│── 📄 model_gdp_cap.pkl
│── 📄 model_gdp.pkl
│── 📄 model_life.pkl
│── 📄 model_pop.pkl
│── 📄 readme.md
│── 📄 requirements.txt
│── 📁 myenv (virtual environment)
│── 📄 .gitignore

---

## 📈 Results  

- **MAE & RMSE < 16 for all models**  
- Reliable forecasts for next 10 years (2025–2035)  
- Interactive deployment allows prediction for any given future year  

---

## 🌐 Deployment  

The project is deployed using **Streamlit**.  
Users can interactively explore and forecast Nepal’s GDP, Life Expectancy, Total Population, and GDP per Capita.  

---

✍️ **Author:** *Dipen Sherpa*  
📖 **Course:** Python with Data Science (Internship Project)  

import streamlit as st
import pandas as pd
import joblib

# Fungsi untuk memuat model yang disimpan
def load_model(model_name):
    model = joblib.load(f"{model_name}.pkl")
    return model

# Tampilan awal aplikasi
st.title('Prediksi Harga Emas')

# Nama-nama model
model_names = {
    "Linear Regression": "lr_model",
    "Decision Tree": "dt_model",
    "Random Forest": "rf_model",
    "Gradient Boosting": "gb_model",
    "SVR": "svr_model",
    "AdaBoost": "abr_model"
}

# Dropdown untuk memilih model
model_choice = st.selectbox("Pilih Model", list(model_names.keys()))

# Input pengguna
close_price = st.number_input("Masukkan Harga Penutupan", value=0.0)
inflation_data = st.number_input("Masukkan Data Inflasi", value=0.0)
exchange_rate = st.number_input("Masukkan Nilai Tukar", value=0.0)

# Tombol prediksi
if st.button('Prediksi Harga Emas'):
    # Memuat model yang dipilih
    model = load_model(model_names[model_choice])
    
    # Membuat prediksi
    input_data = pd.DataFrame([[close_price, inflation_data, exchange_rate]], 
                              columns=['Close', 'Data Inflasi', 'Kurs Tengah'])
    prediction = model.predict(input_data)
    
    # Menampilkan hasil prediksi dengan maksimal empat angka di belakang koma
    st.write(f"Prediksi Harga Emas: {prediction[0]:.4f}")

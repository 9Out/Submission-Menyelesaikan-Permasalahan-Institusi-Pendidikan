import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --- LOAD MODELS ---
@st.cache_resource
def load_models():
    # Menggunakan Pathlib agar lebih robust terhadap OS
    base_path = Path(__file__).parent
    preprocessor_path = base_path / 'preprocessor_model.pkl'
    model_path = base_path / 'xgboost_model.pkl'

    if not preprocessor_path.exists() or not model_path.exists():
        st.error(f"File model tidak ditemukan! Pastikan file pkl ada di: {base_path}")
        st.stop()

    preprocessor = joblib.load(preprocessor_path)
    model = joblib.load(model_path)
    return preprocessor, model

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Prediksi Status Mahasiswa", layout="centered", page_icon="🎓")

# Load models
preprocessor, model = load_models()

# Custom CSS untuk tampilan lebih modern
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { 
        width: 100%; 
        background-color: #e76f51; 
        color: white; 
        border-radius: 10px; 
        height: 3em; 
        font-weight: bold; 
    }
    .stSuccess { background-color: #d4edda; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Sistem Prediksi Kelulusan Mahasiswa")
st.write("Masukkan data akademik dan profil mahasiswa untuk memprediksi status kelulusan.")

# --- FORM INPUT ---
with st.form("prediction_form"):
    
    st.subheader("👤 Profil Mahasiswa")
    cp1, cp2 = st.columns(2)
    with cp1:
        age = st.number_input("Usia saat Enrollment", 14, 60, 19)
    with cp2:
        admission_grade = st.number_input("Nilai Masuk (0-200)", 0.0, 200.0, 130.0)
    
    st.divider()
    
    st.subheader("💰 Status Finansial & Beasiswa")
    col_fin1, col_fin2, col_fin3 = st.columns(3)

    with col_fin1:
        tuition = st.selectbox("Pembayaran SPP", ["Tepat Waktu", "Menunggak"])
    with col_fin2:
        scholarship = st.selectbox("Status Beasiswa", ["Penerima", "Bukan Penerima"])
    with col_fin3:
        debtor = st.selectbox("Status Debitur", ["Tidak Berhutang", "Berhutang"])

    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📚 Semester 1")
        sks_1 = st.number_input("SKS Lulus (Sem 1)", 0, 40, 15)
        grade_1 = st.slider("Nilai Rata-rata (0-20) - S1", 0.0, 20.0, 12.0)

    with col2:
        st.subheader("📚 Semester 2")
        sks_2 = st.number_input("SKS Lulus (Sem 2)", 0, 40, 15)
        grade_2 = st.slider("Nilai Rata-rata (0-20) - S2", 0.0, 20.0, 12.0)

    submit_button = st.form_submit_button("🔍 Jalankan Prediksi")

# --- PREDICTION LOGIC ---
if submit_button:
    with st.spinner('Menganalisis data...'):
        # Membangun dictionary input
        input_dict = {
            'Tuition_fees_up_to_date': [1 if tuition == "Tepat Waktu" else 0],
            'Scholarship_holder': [1 if scholarship == "Penerima" else 0],
            'Debtor': [1 if debtor == "Berhutang" else 0],
            'Curricular_units_1st_sem_approved': [sks_1],
            'Curricular_units_1st_sem_grade': [grade_1],
            'Curricular_units_2nd_sem_approved': [sks_2],
            'Curricular_units_2nd_sem_grade': [grade_2],
            'Age_at_enrollment': [age],
            'Admission_grade': [admission_grade],
            
            # Nilai default untuk kolom yang tidak ada di UI
            'Previous_qualification_grade': [120.0],
            'Curricular_units_1st_sem_credited': [0],
            'Curricular_units_1st_sem_evaluations': [0],
            'Curricular_units_1st_sem_without_evaluations': [0],
            'Curricular_units_2nd_sem_without_evaluations': [0],
            'Unemployment_rate': [11.0],
            'Inflation_rate': [0.5],
            'GDP': [1.0],
            'Application_mode': [1],
            'Application_order': [1],
            'Course': [1],
            'Mothers_qualification': [1],
            'Fathers_qualification': [1],
            'Mothers_occupation': [1],
            'Fathers_occupation': [1],
            'Displaced': [1],
            'Gender': [1]
        }

        input_data = pd.DataFrame(input_dict)

        try:
            # 1. Transformasi data menggunakan preprocessor
            processed_data = preprocessor.transform(input_data)

            # 2. Prediksi menggunakan model
            prediction = model.predict(processed_data)

            # 3. Tampilkan Hasil
            st.markdown("---")
            if prediction[0] == 0:
                st.error("### ⚠️ Hasil Prediksi: **Dropout**")
                st.info("Rekomendasi: Lakukan konseling akademik untuk memantau perkembangan mahasiswa ini.")
            else:
                st.success("### ✅ Hasil Prediksi: **Graduate**")
                
                st.write("Mahasiswa diprediksi akan menyelesaikan pendidikan dengan baik.")

        except Exception as e:
            st.error(f"Terjadi kesalahan teknis: {e}")
            st.warning("Tips: Pastikan urutan dan nama kolom input_data sama dengan saat model dilatih.")
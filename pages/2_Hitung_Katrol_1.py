import streamlit as st
import math

st.image('gambar/katrol1.png', caption='Katrol 1', width=600)

def hitung_hasil(massa1, massa2, se):
    rad   = math.radians(se)
    gaya1 = round(massa1 * 9.8 * math.sin(rad), 3)
    gaya2 = round(massa2 * 9.8, 3)    
    a     = round((massa1 * math.sin(rad) - massa2) * 9.8  / (massa1 + massa2), 2)
    t     = round((massa2*a)+(massa2*9.8), 3)
    return (rad, gaya1, gaya2, a, t)


# Judul aplikasi
st.title('Menghitung katrol dengan salah satu massa di bidang miring')

# Input panjang dan lebar dari user
massa1 = st.number_input("Masukkan massa 1:", min_value=0.0)
massa2 = st.number_input("Masukkan massa 2:", min_value=0.0)
se = st.number_input("Masukkan sudut elevasi:", min_value=0.0)

# Tombol untuk menghitung luas
if st.button("Hitung Hasil"):
    rad, gaya1, gaya2, a, t = hitung_hasil(massa1, massa2, se)
    st.success(f'Gaya massa 1    :   {gaya1:.2f} Newton')
    st.success(f'Gaya massa 2    :   {gaya2:.2f} Newton')
    st.success(f'Tegangan        :   {t:.2f} Newton')
    if a > 0 :
        st.success(f'Percepatan      :   {a:.2f} m/s kuadrat, karena percepatan positif maka arah M1 ke bawah dan M2 ke atas')
        video = open('video/katrol1.1.mp4','rb')
        videotest = video.read()
        st.video(videotest)
    elif a < 0 :
        st.success(f'Percepatan      :   {a:.2f} m/s kuadrat, karena percepatan negatif maka arah M1 ke atas dan M2 ke bawah')
        video = open('video/katrol1.2.mp4','rb')
        videotest = video.read()
        st.video(videotest)
    else :
        st.success(f'Percepatan      :   {a:.2f} m/s kuadrat, karena percepatan 0, maka tidak ada pergerakan')

# Catatan tambahan
st.write("Catatan: Masukkan massa dalam satuan [Kg] dan Sudut Elevasi dalam derajat.")
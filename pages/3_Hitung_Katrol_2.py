import streamlit as st
import math

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image('gambar/katrol2.png', caption='Katrol 2', width=200)

with col3:
    st.write(' ')

def hitung_hasil(massaA, massaB):
    gayaA = round(massaA * 9.8, 3)
    gayaB = round(massaB * 9.8, 3)    
    a     = round(((massaB - massaA) * 9.8)  / (massaA + massaB), 2)
    t     = round((massaA* 9.8)+(massaA * a), 3)
    return (gayaA, gayaB, a, t)


# Judul aplikasi
st.title('Menghitung katrol tanpa bidang miring')

# Input panjang dan lebar dari user
massaA = st.number_input("Masukkan massa A:", min_value=0.0)
massaB = st.number_input("Masukkan massa B:", min_value=0.0)

# Tombol untuk menghitung luas
if st.button("Hitung Hasil"):
    gayaA, gayaB, a, t = hitung_hasil(massaA, massaB)
    st.success(f'Gaya massa A    :   {gayaA:.2f} Newton')
    st.success(f'Gaya massa B    :   {gayaB:.2f} Newton')
    st.success(f'Tegangan        :   {t:.2f} Newton')
    if a > 0 :
        st.image('video/katrol2.1.gif', caption='', width=600)
    elif a < 0:
        st.success(f'Percepatan      :   {a:.2f} m/s kuadrat, karena percepatan negatif maka arah MA ke bawah dan MB ke atas')
        video = open('video/katrol2.2.mp4','rb')
        videotest = video.read()
        st.video(videotest)
    else :
        st.success(f'Percepatan      :   {a:.2f} m/s kuadrat, karena percepatan 0, maka tidak ada pergerakan')

# Catatan tambahan
st.write("Catatan: Masukkan massa dalam satuan [Kg] dan Sudut Elevasi dalam derajat.")

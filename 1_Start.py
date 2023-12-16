import streamlit as st

st.set_page_config(page_title="Home",page_icon="⭐")
st.title("PERHITUNGAN HUKUM NEWTON II PADA KATROL")

st.markdown("""
## - Katrol
Katrol adalah salah satu jenis pesawat sederhana yang ada untuk mempermudah pekerjaan manusia,
Katrol ini biasanya digunakan untuk menarik atau mengangkat benda yang berukuran berat.
""")

st.markdown("""
## - Hukum Newton II
"Percepatan suatu benda yang disebabkan oleh perubahan kecepatan berbanding lurus dengan besarnya resultan gaya 
atau gaya yang bekerja pada benda tersebut dan berbanding terbalik dengan massa benda tersebut."
""")

st.markdown(""" 
## -Penggunaan Hukum Newton II Pada Katrol
Dengan rumus Hukum Newton II Yaitu :
""")

st.latex(r'''
\sum F = m.a
''')  

st.markdown("""
Kita bisa menghitung Gaya kedua massa, percepatan pergerakan dan tegangan tali pada katrol,
tetapi karena beragamnya jenis katrol maka penjabaran rumusnya pun akan berbeda beda,
maka dari itu disini disediakan 2 jenis katrol, yaitu :
""")

st.markdown("""
### 1. Katrol dengan salah satu massa berada di bidang miring
""")

st.image('gambar/katrol1.png', caption='Katrol 1', width=600)

st.markdown(""" 
Dengan penjabaran rumus :
""")

st.latex(r''' 
F1 = m1.g.sinθ
''')

st.latex(r''' 
F2 = m2.g
''')

st.latex(r''' 
a = \frac {(m1.sinθ-m2)g}{m1+m2}
''')

st.latex(r''' 
T = m2.a + m2.g
''')

st.text("""dimana
F1  = Gaya 1            (Newton)
F2  = Gaya 2            (Newton)
a   = percepatan        (m/s²)
m1  = massa 1           (Kg)
m2  = massa 2           (Kg)
T   = tegangan          (Newton) 
g   = gravitasi [9.8]   (m/s²)
θ   = sudut elevasi
""")
    
st.markdown("""
### 2. Katrol tanpa bidang miring
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image('gambar/katrol2.png', caption='Katrol 2', width=200)

with col3:
    st.write(' ')
    
st.markdown(""" 
Dengan penjabaran rumus :
""")

st.latex(r''' 
FA = mA.g
''')

st.latex(r''' 
FB = mB.g
''')

st.latex(r''' 
a = \frac {(mB-mA)g}{mA+mB}
''')

st.latex(r''' 
T = mA.g + mA.a
''')

st.text("""dimana
FA  = Gaya A            (Newton)
FB  = Gaya B            (Newton)
a   = percepatan        (m/s²)
mA  = massa A           (Kg)
mB  = massa B           (Kg)
g   = gravitasi [9.8]   (m/s²)
T   = tegangan          (Newton)
""")
import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px

# Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.radio("Pilih Halaman", ["Beranda", "Tentang", "Galeri", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Selamat datang di halaman beranda aplikasi ini.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Aplikasi ini dibuat untuk mendemonstrasikan fitur Streamlit.")
elif selection == "Galeri":
    st.title("Galeri")
    st.write("Ini adalah halaman galeri yang menampilkan berbagai konten visual.")
else:
    st.title("Kontak")
    st.write("Hubungi kami melalui email: fathii.athallah@gmail.com")
    
#1 Element Text
st.title("My First Streamlit App")
st.header("Nama : Muhammad Fathi Athallah Anantaasri")
st.subheader("NIM : 22181010165")
st.caption("Kelas : B")
st.caption("Mata Kuliah : Pemrograman Web")
st.caption("Prodi : Bisnis Digital")
st.code("import numpy as np")
st.text("Aplikasi Streamlit App - Ini Text")
st.latex(r'x^2 + y^2 = z^2')
st.divider()
st.markdown("Aplikasi Streamlit App - Ini Markdown")

#2 Dataframe Input
#2.1 API
st.subheader("Lembar Kerja API")
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.error("Error: Data gagal di fetch dari API (Status Code: {response.status_code})")

st.subheader("Lembar Kerja Upload CSV")

#2.2 CSV Upload File
st.subheader("Lembar Kerja upload CSV")
uploaded_file = st.file_uploader("Upload a CSV file", type=("csv"))
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else: 
    st.write("No file uploaded yet.")

#2.3 Menggunakan st.write()
st.subheader("Lembar Kerja Simple Data")
data = {
    'Nama': ['Fathi', 'Arun', 'Kemal', 'Alim'],
    'Umur': [20,20,19,20],
    'City': ['Jawa', 'Soppeng', 'Sidrap', 'Makassar']
}

df = pd.DataFrame(data)
st.dataframe(df)

#2.4 Menggunakan dataframe random NP
st.subheader("Lembar Kerja Dataframe Random")
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)
st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0))
st.dataframe(df.style.highlight_min(axis=0))
st.dataframe(df.style.highlight_max(axis=1))


st.subheader("Lembar Kerja Belajar Data 2")
#3 Metrix Streamlit
st.subheader("Lembar Kerja Metrix")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Penjualan", value="Rp. 1.000.000", delta="Rp. 100.000")

with col2:
    st.metric(label="Total Pengeluaran", value="Rp. 500.000", delta="Rp. 50.000")   

with col3:
    st.metric(label="Total Keuntungan", value="Rp. 500.000", delta="Rp. 50.000")    


#4 Chart
#4.2 Line Chart
st.subheader("Lembar Kerja Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

#4.3 Map Chart
st.subheader("Lembar Kerja Map Chart")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-6.2, 106.8],
    columns=['lat', 'lon']
)
st.map(df)

#4.4 Visualisasi st.plotly_chart()
st.title("Dashboard Penjualan")
st.subheader("Visualisasi Penjualan")
st.write("Visualisasi Penjualan menggunakan Plotly")
data = pd.DataFrame({
    'Tahun' : [2018, 2019, 2020, 2021, 2022],
    'Penjualan' : [100, 200, 300, 400, 500],
    'Pengeluaran' : [50, 100, 150, 200, 250],
    'Keuntungan' : [50, 100, 150, 200, 250]
})
fig_penjualan = px.line(data, x='Tahun', y='Penjualan', title='Grafik Penjualan')
data,
x= 'Tahun',
y= 'Pengeluaran',
markers=True,
text='Penjualan',
title='Grafik Penjualan'
labels={'Penjualan':'Jumlah Penjualan', 'Tahun':'Tahun'},
template= 'plotly_dark',
color_discrete_sequence=['#FF5733']

fig_pengeluaran = px.line(data, x='Tahun', y='Pengeluaran', title='Grafik Pengeluaran')
fig_pengeluaran.update_traces(mode='markers+lines', marker=dict(size=10, color='blue'))
fig_pengeluaran.update_layout(title_text='Grafik Pengeluaran', title_x=0.5)

fig_keuntungan = px.line(data, x='Tahun', y='Keuntungan', title='Grafik Keuntungan')
fig_keuntungan.update_traces(mode='markers+lines', marker=dict(size=10, color='green'))
fig_keuntungan.update_layout(title_text='Grafik Keuntungan', title_x=0.5)
st.plotly_chart(fig_penjualan, use_container_width=True)
st.plotly_chart(fig_pengeluaran, use_container_width=True)
st.plotly_chart(fig_keuntungan, use_container_width=True)

#5 Input Form
st.subheader("Lembar Kerja Input Form")
with st.form(key='my_form'):
    name = st.text_input("Nama")
    age = st.number_input("Umur", min_value=0, max_value=100, value=20)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    foto_kamera = st.camera_input("Foto Kamera")
    jenis_kelamin = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    hobi = st.multiselect("Hobi", ["Membaca", "Menulis", "Main Game", "Menari"])
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        st.write("Nama:", name)
        st.write("Umur:", age)
        st.write("Tanggal Lahir:", tanggal_lahir)
        st.write("Jenis Kelamin:", jenis_kelamin)
        st.write("Hobi:", hobi)
        if foto_kamera is not None:
            st.image(foto_kamera, caption='Foto Anda', use_column_width=True)
        st.success("Data berhasil disimpan!")

#6 Upload Media di Streamlit
st.subheader("Lembar Kerja Upload Media youtube")
st.video("https://youtu.be/CTbnT0t531s?si=whc-lB_XoyEdla5n")
st.subheader("Lembar Kerja Upload Media Audio")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")



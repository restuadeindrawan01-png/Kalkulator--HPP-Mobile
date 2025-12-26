import streamlit as st

def format_rp(angka):
    return f"Rp {angka:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

st.set_page_config(page_title="Accounting System 2025", layout="centered")
st.title("📊 SISTEM AKUNTANSI BIAYA")

tab1, tab2 = st.tabs(["Job Order Costing", "Process Costing"])

with tab1:
    st.subheader("📋 Detail Biaya Pesanan")
    nama = st.text_input("Nama Pesanan", placeholder="Contoh: Percetakan Buku X")
    bbb = st.number_input("Total Bahan Baku (BBB)", min_value=0.0, step=1000.0)
    jam = st.number_input("Jam Kerja Langsung", min_value=0.0)
    upah = st.number_input("Tarif Upah per Jam", min_value=0.0)
    bop_tarif = st.number_input("Tarif BOP per Jam", min_value=0.0)

    if st.button("HITUNG TOTAL HPP"):
        btkl = jam * upah
        bop_dibebankan = jam * bop_tarif
        total_hpp = bbb + btkl + bop_dibebankan
        st.metric("TOTAL HPP", format_rp(total_hpp))

with tab2:
    st.subheader("🏭 Produksi Massal")
    total_biaya = st.number_input("Total Biaya Produksi", min_value=0.0, step=1000.0)
    jadi = st.number_input("Produk Selesai (Unit)", min_value=0.0)
    pdp = st.number_input("Produk PDP (Unit)", min_value=0.0)
    tingkat = st.slider("Tingkat Penyelesaian (%)", 0, 100, 80) / 100

    if st.button("PROSES ALOKASI"):
        ue = jadi + (pdp * tingkat)
        biaya_satuan = total_biaya / ue if ue > 0 else 0
        st.info(f"Biaya per Unit: {format_rp(biaya_satuan)}")

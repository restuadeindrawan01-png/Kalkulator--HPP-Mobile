import streamlit as st

# --- FUNGSI FORMAT RUPIAH ---
def format_rp(angka):
    return f"Rp {angka:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="Accounting System 2025", layout="centered")

st.title("📊 SISTEM AKUNTANSI BIAYA")
st.write("Aplikasi Perhitungan HPP Versi Mobile")

# --- MENU TAB ---
tab1, tab2 = st.tabs(["Job Order Costing", "Process Costing"])

with tab1:
    st.subheader("📋 Detail Biaya Pesanan")
    with st.container():
        nama = st.text_input("Nama Pesanan", placeholder="Contoh: Percetakan Buku X")
        bbb = st.number_input("Total Bahan Baku (BBB)", min_value=0.0, step=1000.0)
        jam = st.number_input("Jam Kerja Langsung", min_value=0.0)
        upah = st.number_input("Tarif Upah per Jam", min_value=0.0)
        bop_tarif = st.number_input("Tarif BOP per Jam", min_value=0.0)

        if st.button("HITUNG TOTAL HPP"):
            btkl = jam * upah
            bop_dibebankan = jam * bop_tarif
            total_hpp = bbb + btkl + bop_dibebankan
            
            st.success(f"*Hasil Perhitungan: {nama.upper()}*")
            st.write(f"BBB: {format_rp(bbb)}")
            st.write(f"BTKL: {format_rp(btkl)}")
            st.write(f"BOP: {format_rp(bop_dibebankan)}")
            st.divider()
            st.metric("TOTAL HPP", format_rp(total_hpp))

with tab2:
    st.subheader("🏭 Produksi Massal (Dep. A)")
    total_biaya = st.number_input("Total Biaya Produksi", min_value=0.0, step=1000.0)
    jadi = st.number_input("Produk Selesai (Unit)", min_value=0.0)
    pdp = st.number_input("Produk Dalam Proses (Unit)", min_value=0.0)
    tingkat = st.slider("Tingkat Penyelesaian (0-100%)", 0, 100, 80) / 100

    if st.button("PROSES ALOKASI BIAYA"):
        ue = jadi + (pdp * tingkat)
        biaya_satuan = total_biaya / ue if ue > 0 else 0
        
        st.info("*Ringkasan Biaya Proses*")
        st.write(f"Unit Ekuivalen: {ue:,.0f} Unit")
        st.write(f"Biaya per Unit: {format_rp(biaya_satuan)}")
        st.divider()
        st.write(f"HP Produk Jadi: {format_rp(jadi * biaya_satuan)}")
        st.write(f"HP PDP Akhir: {format_rp((pdp * tingkat) * biaya_satuan)}")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

st.set_page_config(page_title="My Dashboard")

byweekday_df = pd.read_csv("byweekday.csv")
byseasons_df = pd.read_csv("byseasons.csv")
user_df = pd.read_csv("user_data.csv")


with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("sepeda.png")
    st.title('Bike Sharing User :sparkles:')
    col1, col2 = st.columns(2)
    with col1:
        casual = user_df .casual.sum()
        st.metric("Casual User", value=casual)
    with col2:
        registered = user_df .registered.sum()
        st.metric("Registered User", value=registered)

    total = user_df .cnt.sum()
    st.metric("Total User", value=total)
    



st.title('Bike Sharing Dashboard :sparkles:')
tab1, tab2 = st.tabs(["Analisis 1", "Analisis 2"])

with tab1:
    st.header("Number of Bicycle Rental Per Week in 2011-2012")

    fig, ax = plt.subplots(figsize=(20, 10))

    ax.plot(byweekday_df.index, byweekday_df["casual"], label="Casual", marker='o', linewidth=2)
    ax.plot(byweekday_df.index, byweekday_df["registered"], label="Registered", marker='o', linewidth=2)
    ax.plot(byweekday_df.index, byweekday_df["cnt"], label="Total", marker='o', linewidth=2)

    ax.set_xlabel("Weekday", fontsize=30)
    ax.set_ylabel("Number of Bicycle Rental Per Week", fontsize=30)
    ax.set_xticks(byweekday_df.index)
    ax.set_xticklabels(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], fontsize=35)
    ax.tick_params(axis='y', labelsize=30)
    ax.legend()

    st.pyplot(fig)

    with st.expander("Simpulan"):
        st.write(
        """Terlihat bahwa banyaknya penyewaan selama 2011-2012 dipengaruhi oleh weekday 
        dengan total penyewaan terbanyak terjadi pada hari Jumat. 
        Jika melihat dari karakteristek pelanggan, casual memiliki pelonjakan pada hari libur
        yaitu sabtu-minggu ini dikarenakan pengguna casual hanya menggunakan Bike Saring untuk rekreasi. 
        Sedangkan, pada karakteristik regitered, penurunan terjadi di hari libur yaitu
          sabtu-minggu yang dapat disimpulkan pelanggan registered adalah pekerja yang bekerja pada senin-jumat."""
        )

with tab2:
    st.header("Number of Bicycle Rental Per Season in 2011-2012")
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="hr", 
        x=[0,1,2,3],
        data=byseasons_df.sort_values(by="hr", ascending=False),
        palette=colors
    )
    plt.xlabel("Season", fontsize=30)
    plt.ylabel("Average Hourly Rentals", fontsize=30)
    plt.xticks([0, 1, 2,3], ['Spring', 'Summer', 'Fall', 'Winter'], fontsize=35)
    plt.yticks(fontsize=30)
    st.pyplot(fig)

    with st.expander("Simpulan"):
        st.write(
        """Terlihat bahwa lama penggunaan sepeda pada 4 season selama 2011-2012 memiliki 
        rata-rata yang hampir sama dengan rata-rata tertinggi diraih oleh musim spring. 
        Ini menunjukan pengaruh musim dalam lamanya penggunaan Bike Sharing sangatlah kecil 
        yang menyebabkan tidak ada kekhawatiran pada musim-musim tertentu."""
        )
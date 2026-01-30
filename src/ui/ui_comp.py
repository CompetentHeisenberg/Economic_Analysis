import streamlit as st

def render_sidebar():
    st.sidebar.header("Налаштування")
    source = st.sidebar.selectbox("Джерело даних", ["Завантажити файл", "Yahoo Finance", "FRED API"])
    
    st.sidebar.markdown("---")
    st.sidebar.info(
        """
        **Інструкція:**
        1. Оберіть джерело.
        2. Завантажте дані.
        3. Проведіть аналіз.
        """
    )
    return source

def display_stats(df):
    st.write(f"**Рядків:** {df.shape[0]} | **Колонок:** {df.shape[1]}")

def render_welcome_page():
    st.title("Система аналізу економічних даних")
    st.markdown("""
    <style>
    .big-font { font-size:20px !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Програмний комплекс для обробки масивів даних із використанням методів багатовимірної статистики.</p>', unsafe_allow_html=True)

    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Можливості")
        st.success("Імпорт даних (CSV, Excel, API)")
        st.success("Попередня обробка та очищення")
        st.success("Стандартизація показників")
        st.success("Багатовимірний аналіз (PCA, Кластеризація)")

    with col2:
        st.header("Про проект")
        st.info("""
        Ця система розроблена в рамках дипломної роботи. 
        Основна мета — автоматизація виявлення прихованих залежностей 
        в економічних часових рядах.
        """)

    st.warning("Щоб розпочати роботу, оберіть джерело даних у меню зліва.")
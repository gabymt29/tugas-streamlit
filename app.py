import streamlit as st
import numpy as np
import pandas as pd

st.title(' VECTOR MATRIX APPS')

with st.sidebar:
    tipe = st.radio('Pilih Tipe', ['single vector', 'double vector', 'single matrix', 'double matrix', 'invers matrix', 'SVD', 'Diagonalize'])

if tipe == 'single vector':
    with st.expander('Pilih Ukuran'):
        with st.form('Pilih Ukuran'):
            size = st.number_input('Ukuran vektor', min_value=2)
            submit = st.form_submit_button('Submit')

    if submit:
        df = pd.DataFrame(columns=range(1, size + 1), index=range(1, 2), dtype=float)
        st.write('Masukkan data untuk vektor')
        df_input = st.experimental_data_editor(df, use_container_width=True)
        vector = df_input.fillna(0).to_numpy()[0]
        st.write('Vektor:', vector)

elif tipe == 'double vector':
    with st.expander('Pilih Ukuran'):
        with st.form('Pilih Ukuran'):
            size = st.number_input('Ukuran vektor', min_value=2)
            submit = st.form_submit_button('Submit')

    if submit:
        df1 = pd.DataFrame(columns=range(1, size + 1), index=range(1, 2), dtype=float)
        df2 = pd.DataFrame(columns=range(1, size + 1), index=range(1, 2), dtype=float)
        st.write('Masukkan data untuk vektor pertama')
        df1_input = st.experimental_data_editor(df1, use_container_width=True)
        st.write('Masukkan data untuk vektor kedua')
        df2_input = st.experimental_data_editor(df2, use_container_width=True)
        vector1 = df1_input.fillna(0).to_numpy()[0]
        vector2 = df2_input.fillna(0).to_numpy()[0]
        st.write('Vektor Pertama:', vector1)
        st.write('Vektor Kedua:', vector2)
        # Lakukan operasi pada vektor

elif tipe == 'single matrix':
    with st.expander('Pilih Ukuran'):
        with st.form('Pilih Ukuran'):
            rows = st.number_input('Jumlah baris', min_value=2)
            cols = st.number_input('Jumlah kolom', min_value=2)
            submit = st.form_submit_button('Submit')

    if submit:
        df = pd.DataFrame(columns=range(1, cols + 1), index=range(1, rows + 1), dtype=float)
        st.write('Masukkan data untuk matriks')
        df_input = st.experimental_data_editor(df, use_container_width=True)
        matrix = df_input.fillna(0).to_numpy()
        st.write('Matriks:')
        st.write(matrix)
        # Lakukan operasi pada matriks

elif tipe == 'double matrix':
    with st.expander('Pilih Ukuran'):
        with st.form('Pilih Ukuran'):
            rows1 = st.number_input('Jumlah baris matriks pertama', min_value=2)
            cols1 = st.number_input('Jumlah kolom matriks pertama', min_value=2)
            rows2 = st.number_input('Jumlah baris matriks kedua', min_value=2)
            cols2 = st.number_input('Jumlah kolom matriks kedua', min_value=2)
            submit = st.form_submit_button('Submit')

    if submit:
        df1 = pd.DataFrame(columns=range(1, cols1 + 1), index=range(1, rows1 + 1), dtype=float)
        df2 = pd.DataFrame(columns=range(1, cols2 + 1), index=range(1, rows2 + 1), dtype=float)
        st.write('Masukkan data untuk matriks pertama')
        df1_input = st.experimental_data_editor(df1, use_container_width=True)
        st.write('Masukkan data untuk matriks kedua')
        df2_input = st.experimental_data_editor(df2, use_container_width=True)
        matrix1 = df1_input.fillna(0).to_numpy()
        matrix2 = df2_input.fillna(0).to_numpy()
        st.write('Matriks Pertama:')
        st.write(matrix1)
        st.write('Matriks Kedua:')
        st.write(matrix2)
        # Lakukan operasi pada matriks

elif tipe == 'invers matrix':
    with st.expander('Pilih Ukuran'):
        with st.form('Pilih Ukuran'):
            rows = st.number_input('Jumlah baris matriks', min_value=2)
            cols = st.number_input('Jumlah kolom matriks', min_value=2)
            submit = st.form_submit_button('Submit')

    if submit:
        df = pd.DataFrame(columns=range(1, cols + 1), index=range(1, rows + 1), dtype=float)
        st.write('Masukkan data untuk matriks')
        df_input = st.experimental_data_editor(df, use_container_width=True)
        matrix = df_input.fillna(0).to_numpy()
        st.write('Matriks:')
        st.write(matrix)
        # Lakukan operasi invers pada matriks

elif tipe == 'SVD':
    with st.expander('Pilih Ukuran'):
        with st.form('Pilih Ukuran'):
            rows = st.number_input('Jumlah baris matriks', min_value=2)
            cols = st.number_input('Jumlah kolom matriks', min_value=2)
            submit = st.form_submit_button('Submit')

    if submit:
        df = pd.DataFrame(columns=range(1, cols + 1), index=range(1, rows + 1), dtype=float)
        st.write('Masukkan data untuk matriks')
        df_input = st.experimental_data_editor(df, use_container_width=True)
        matrix = df_input.fillna(0).to_numpy()
        st.write('Matriks:')
        st.write(matrix)
        # Lakukan operasi SVD pada matriks

elif tipe == 'Diagonalize':
    with st.expander('Pilih Ukuran'):
        with st.form('Pilih Ukuran'):
            rows = st.number_input('Jumlah baris matriks', min_value=2)
            cols = st.number_input('Jumlah kolom matriks', min_value=2)
            submit = st.form_submit_button('Submit')

    if submit:
        df = pd.DataFrame(columns=range(1, cols + 1), index=range(1, rows + 1), dtype=float)
        st.write('Masukkan data untuk matriks')
        df_input = st.experimental_data_editor(df, use_container_width=True)
        matrix = df_input.fillna(0).to_numpy()
        st.write('Matriks:')
        st.write(matrix)
        # Lakukan operasi diagonalisasi pada matriks

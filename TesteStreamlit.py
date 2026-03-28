#Estudo de como funciona o streamlit

import streamlit as st
import time

def main():
    st.title("esse é meu titulo")
    st.write("esse e outro texto")

    st.header("input de texto")
    input_text = st.text_input("Digite um texto aqui: ")
    if input_text:
        st.write("Voce digitou",input_text)
    st.header("Seleção")
    selectd_options = st.selectbox("Selecione uma opção", ["Opção 1","Opção 2","Opção 3","Opção 4"])
    if selectd_options:
        st.write("Opção selecionada: ", selectd_options)

    st.header("Slider")
    slider_value = st.slider("Escolha um valor", 0,100,50)   
    st.write("Essa e a sua opçã",slider_value)

    st.header("Checkbox")
    check_state = st.checkbox("Marque para ativar")
    st.write("Cheackbox:", check_state)

    st.header("Botão")
    if st.button("Clique aqui"):
        st.write("Você apertou no botão!")
    
    st.header("Loading")
    with st.spinner("Aguarde..."):
        time.sleep(3)
    st.success("Carregando com sucesso")

    st.header("Upload")
    upload_file = st.file_uploader("Escolha um arquivo", type=["pdf","csv"])
    if upload_file:
        st.write("Nome do arquivo:", upload_file)

    st.header("Graficos")
    data = {'x':[1,2,3,4],'y':[10,20,30,40]}
    st.line_chart(data)

main()

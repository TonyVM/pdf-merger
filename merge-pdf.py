import streamlit as st
import PyPDF2

#Vars
output_pdf = "documents/pdf_final.pdf"

#FUNCION QUE COMBINA
def unirPdfs(output_path, documents):
    pdf_result = PyPDF2.PdfMerger() #crear objeto PdfMerger de PyPDF2 para combinar archivos

    for document in documents:
        pdf_result.append(document)  #ir adicionando los pdf para unirlos
    
    pdf_result.write(output_path)  #guardar el pdf unido en la ruta definida

#Frontend de la app
st.image("assets/combine-pdf.png")
st.header("Combinar PDFs")
st.subheader("Adjuntar documentos PDF para unirlos")

pdf_adjuntos = st.file_uploader(label = "", accept_multiple_files = True)

combinar = st.button("Unir PDFs")

if(combinar):
    if len(pdf_adjuntos) <= 1:
        st.warning("Debe adjuntar más de un documento")
    else:
        unirPdfs(output_pdf, pdf_adjuntos)
        st.success("Desde aquí puedes descargar el documento final")
        with open(output_pdf,'rb') as file:
            pdf_data = file.read()
        st.download_button(label = "Descargar PDF final", data = pdf_data, file_name = "pdf_final.pdf")
#Creator: Oziel Ramos
#Any questions, send me an email: prof.oziiel@gmail.com
#Envie um email: prof.oziiel@gmail.com
#Para Qualquer dúvida, feedback, orientações ou alguma mensagem que vise
# a colaboração e evolução deste trabalho


#Lib de reconhecimento de imagens
import pytesseract
#lib de conversão
import PyPDF2
#Lib suporte para conversão
import io
#Lib de acesso a diretorios direto no pc
import os

#As paginas estavam dispostas em jpg, com seus nomes dispostos em paginas. O que eu fiz, foi realizar a junção dessa páginas em um único pdf.
#Em seguida realizei o reconhecimento de cada pagina contida no pdf. No final salvei esse pdf no meu diretorio
#Como converti os nomes dos arquivos para inteiros, trabalhei com o comando while para conversão. 
#No entanto o comando for pode ser mais útil para reconhecimneto da lista de nomes
#Número dos arquivos
i = 0
while i <= 1435:
    #Começo da conversão, esse print mostra qual arquivo começou a ser convertido
    print(i)
    #array vazio para depois listar os arquivos contidos na pastas
    all_files = []
    #comando que realiza o reconhecimento das pastas, primeiro ele acessa as pastas que contem as paginas
    for (path, dirs, files) in os.walk('/trab0/' + str(i)):
        #segundo, ele realiza o reconhecimento de cada paginas e adiciona seu nome em uma lista para depois converter eles em pdf
        for file in files:
            if not file.endswith(".jpg"):
                continue
            file = os.path.join(path,file)
            all_files.append(file)
    #comando que realiza a conversão das imagens em pdf
    pdf_writer = PyPDF2.PdfFileWriter()
    #comando que organiza as paginas em ordem numerica
    all_files.sort()
    #comando que realiza reconhecimento dos caracteres contidos em cada pagina pdf
    for file in all_files:
        page = pytesseract.image_to_pdf_or_hocr(file, extension = 'pdf')
        pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
        pdf_writer.addPage(pdf.getPage(0))
    #comando que salva os pdf no diretorio da pasta que o script está salvi
    with open(str(i) + ".pdf", "wb") as f:
        pdf_writer.write(f)
    #comando que reconhece a conversão final
    print("Converteu"+str(i))
    #recomeço da contagem
    i = i + 1

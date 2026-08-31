from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# Criando o documento
pdf = SimpleDocTemplate(r"e:\Laboratório de Prática\Python\pratica\string_metodos_exercicios_estilizado.pdf",
    pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Título
titulo = Paragraph("Métodos úteis da classe String em Python", styles['Title'])
story.append(titulo)
story.append(Spacer(1, 20))

# Seção explicativa
subtitulo1 = Paragraph("Explicação", styles['Heading2'])
story.append(subtitulo1)
story.append(Spacer(1, 10))

# Criando tabela com métodos
data = [
    ["Método", "Descrição", "Exemplo"],
    [".upper()", "Transforma em maiúsculas", '"python".upper() → "PYTHON"'],
    [".lower()", "Transforma em minúsculas", '"PYTHON".lower() → "python"'],
    [".strip()", "Remove espaços extras", '"   nome   ".strip() → "nome"'],
    [".replace()", "Substitui partes da string", '"Eu gosto de Java".replace("Java","Python")'],
    [".split()", "Divide em lista", '"a b c".split() → ["a","b","c"]'],
    [".join()", "Junta lista em string", '"-".join(["a","b","c"]) → "a-b-c"'],
    [".startswith()", "Verifica início", '"texto".startswith("te") → True'],
    [".endswith()", "Verifica fim", '"arquivo.pdf".endswith(".pdf") → True'],
    [".find()", "Localiza trecho", '"Programar em Python".find("Python") → 12'],
    [".count()", "Conta ocorrências", '"banana".count("a") → 3'],
]

tabela = Table(data, colWidths=[100, 200, 200])
tabela.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
    ('TEXTCOLOR', (0,0), (-1,0), colors.black),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
]))
story.append(tabela)
story.append(Spacer(1, 20))

# Seção exercícios
subtitulo2 = Paragraph("Exercícios", styles['Heading2'])
story.append(subtitulo2)
story.append(Spacer(1, 10))

exercicios = """
1. Transforme "Python é divertido" em maiúsculas, minúsculas e capitalize.
2. Remova espaços extras de "   Alexandre   ".
3. Substitua "Java" por "Python" em "Eu gosto de Java".
4. Divida "Aprender Python é divertido" em palavras e depois junte com '-'.
5. Verifique se "relatorio.pdf" termina com .pdf e começa com "rela".
6. Encontre a posição de "Python" em "Programar em Python". O que acontece se procurar "Java"?
7. Conte quantas vezes aparece "a" em "banana".
"""
story.append(Paragraph(exercicios, styles['Normal']))

# Gerando o PDF
pdf.build(story)
print("PDF estilizado com tabela e cores gerado com sucesso!")

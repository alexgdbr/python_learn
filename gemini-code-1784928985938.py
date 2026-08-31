"""
gerar_pdf.py - Gera o relatório resumido em PDF da aula de Python e POO
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def criar_pdf_resumo(nome_arquivo="Resumo_Python_POO.pdf"):
    doc = SimpleDocTemplate(
        nome_arquivo,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Estilos customizados
    titulo_style = ParagraphStyle(
        'TituloPrincipal',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1A365D'),
        spaceAfter=15
    )
    
    subtitulo_style = ParagraphStyle(
        'SubtituloPrincipal',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#2B6CB0'),
        spaceBefore=12,
        spaceAfter=8
    )
    
    body_style = ParagraphStyle(
        'CorpoTexto',
        parent=styles['BodyText'],
        fontSize=10,
        leading=14,
        spaceAfter=6
    )

    code_style = ParagraphStyle(
        'CodigoTexto',
        parent=styles['Code'],
        fontSize=9,
        leading=12,
        fontName='Courier',
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=6
    )

    elements = []

    # --- CABEÇALHO / TÍTULO ---
    elements.append(Paragraph("Apostila do Dia: Python Avançado & POO", titulo_style))
    elements.append(Paragraph("<b>Tópicos abordados:</b> List Comprehension, Generators, f-strings, POO, Herança, Encapsulamento, Métodos Mágicos e Persistência JSON.", body_style))
    elements.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1A365D'), spaceBefore=10, spaceAfter=15))

    # --- ÍNDICE ---
    elements.append(Paragraph("📌 ÍNDICE DE CONTEÚDOS", subtitulo_style))
    
    indice_dados = [
        ["Módulo", "Conteúdo Principal", "Principais Sintaxes/Conceitos"],
        ["1", "List Comprehension vs Generator", "[x for x in list] vs (x for x in list) - Uso de memória"],
        ["2", "Formatação com f-strings", "Fatiamento de CPF [[:3]...] e formatação %d/%m/%Y para datas"],
        ["3", "Fundamentos de POO em Python", "Classes, Objetos, __init__ e o parâmetro self"],
        ["4", "Construtores e @classmethod", "Padrão Factory Method, parâmetro cls e do_dicionario()"],
        ["5", "Herança e Polimorfismo", "Classes filhas (Servidor/Terceirizado) e função super()"],
        ["6", "Desempacotamento de Dicionário", "O operador **dados para passar parâmetros dinâmicos"],
        ["7", "Métodos Mágicos (Dunders)", "__str__ para print(objeto) e __eq__ para comparação"],
        ["8", "Encapsulamento com @property", "Atributos privados (__cpf) com getters e setters"],
        ["9", "Arquitetura do Sistema Completo", "Divisão em validador, modelo, gerenciador e main"]
    ]
    
    tabela_indice = Table(indice_dados, colWidths=[50, 210, 270])
    tabela_indice.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2B6CB0')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F7FAFC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E0')),
        ('FONTSIZE', (0,1), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    
    elements.append(tabela_indice)
    elements.append(Spacer(1, 15))

    # --- SEÇÃO 1: LIST COMPREHENSION X GENERATORS ---
    elements.append(Paragraph("1. List Comprehension vs. Generator Expression", subtitulo_style))
    elements.append(Paragraph("<b>List Comprehension:</b> Aloca toda a lista na RAM instantaneamente. Ideal para reuso ou acesso por índice.", body_style))
    elements.append(Paragraph("<code>lista = [x * 2 for x in range(1000)]</code>", code_style))
    elements.append(Paragraph("<b>Generator Expression:</b> Avaliação preguiçosa ('lazy evaluation'). Gera um valor por vez na memória, ideal para funções como <code>sum()</code>.", body_style))
    elements.append(Paragraph("<code>gerador = (x * 2 for x in range(1000))</code>", code_style))
    elements.append(Spacer(1, 10))

    # --- SEÇÃO 2: F-STRINGS ---
    elements.append(Paragraph("2. Formatação com f-strings (CPF e Datas)", subtitulo_style))
    elements.append(Paragraph("• <b>Fatiamento de CPF:</b> <code>f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'</code>", body_style))
    elements.append(Paragraph("• <b>Data Datetime:</b> <code>f'{data:%d/%m/%Y}'</code>", body_style))
    elements.append(Paragraph("• <b>Preenchimento de zero à esquerda:</b> <code>f'{dia:02d}/{mes:02d}/{ano}'</code>", body_style))
    elements.append(Spacer(1, 10))

    # --- SEÇÃO 3: POO E ARQUITETURA ---
    elements.append(Paragraph("3. Programação Orientada a Objetos (POO)", subtitulo_style))
    elements.append(Paragraph("<b>4 Pilares Aplicados ao Sistema de Cadastro:</b>", body_style))
    elements.append(Paragraph("1. <b>Abstração/Classes:</b> Representação do modelo real com a classe <code>Pessoa</code>.", body_style))
    elements.append(Paragraph("2. <b>Herança:</b> Subclasses <code>Servidor</code> e <code>Terceirizado</code> herdando características de <code>Pessoa</code> via <code>super()</code>.", body_style))
    elements.append(Paragraph("3. <b>Encapsulamento:</b> Proteção do atributo privado <code>self.__cpf</code> utilizando decorators <code>@property</code> e <code>@cpf.setter</code> para validação automática.", body_style))
    elements.append(Paragraph("4. <b>Polimorfismo/Métodos Mágicos:</b> Implementação do método <code>__str__</code> para representação customizada de texto ao dar <code>print(objeto)</code>.", body_style))
    elements.append(Spacer(1, 10))

    # --- SEÇÃO 4: RESUMO DE CÓDIGO DA POO ---
    elements.append(Paragraph("4. Exemplo de Código do Modelo Encapsulado", subtitulo_style))
    exemplo_codigo = """class Pessoa:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;def __init__(self, nome, cpf):<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.nome = nome<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.__cpf = None<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.cpf = cpf  # Chama o @cpf.setter<br/><br/>
&nbsp;&nbsp;&nbsp;&nbsp;@property<br/>
&nbsp;&nbsp;&nbsp;&nbsp;def cpf(self):<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c = self.__cpf<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}" if c else ""<br/><br/>
&nbsp;&nbsp;&nbsp;&nbsp;@cpf.setter<br/>
&nbsp;&nbsp;&nbsp;&nbsp;def cpf(self, valor):<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if not validar_cpf(valor): raise ValueError("CPF Inválido")<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.__cpf = valor<br/><br/>
&nbsp;&nbsp;&nbsp;&nbsp;def __str__(self):<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return f"{self.nome} | CPF: {self.cpf}"
"""
    elements.append(Paragraph(exemplo_codigo, code_style))

    # Construção do documento
    doc.build(elements)
    print(f"✅ PDF gerado com sucesso: {nome_arquivo}")

if __name__ == "__main__":
    criar_pdf_resumo()
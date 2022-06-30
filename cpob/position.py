
class Position:
    def __init__(self) -> None:
        pass
def dados(self,data,etapa,ponto,telefone,rota,endereco,cidade,seq,inicio,final,qtd,distribuidor):
    # Data
    self.pdf.text(56,32,data)
    
    # Edição
    self.pdf.text(115,31,etapa)

    # Nome pv
    self.pdf.text(25,47,ponto)

    # Telefones
    self.pdf.text(25,53,telefone)

    # Rota
    self.pdf.text(45,62,rota)

    # Endereço
    self.pdf.text(31,74,endereco)

    # Distribuidor
    self.pdf.text(85,100,distribuidor)

    # Cidade
    self.pdf.text(38,82,cidade)

    # Orden Liberação
    self.pdf.set_font('helvetica','B',14)
    self.pdf.text(20,122,str(seq).zfill(3))

    # Título Início
    self.pdf.set_font('helvetica','B',14)
    self.pdf.text(50,122,inicio)

    # Título Fim
    self.pdf.set_font('helvetica','B',14)
    self.pdf.text(85,122,final)

    # Total Liberado
    self.pdf.set_font('helvetica','B',14)
    self.pdf.text(120,122,qtd)

    # Data Termo
    self.pdf.set_font('helvetica','',8)
    self.pdf.text(10,152,data)

    # Assinatura
    self.pdf.set_font('helvetica','',12)
    self.pdf.text(self.pdf.w/4,185,ponto)

    # Assinatura
    self.pdf.set_font('helvetica','',10)
    self.pdf.text(self.pdf.w/4,195,"Por favor mande uma mensagem via")
    self.pdf.text(self.pdf.w/5,200,"whatsapp para este número. (65) 99959-7408")

    if f'{distribuidor}.png' not in os.listdir('assets\\qrcode\\'):
    meuqr = Codigo(distribuidor,'https://api.whatsapp.com/send?phone=55659'+'99597408'+'&text=Ol%C3%A1%2C%20Pode%20me%20ajudar%3F')
    meuqr.codeqr()
    self.pdf.image(f'assets\\qrcode\\{distribuidor}.png',x=118,y=180,w=round(20),h=round(20))

    elif f'{distribuidor}.png' in os.listdir('assets\\qrcode\\'):
    self.pdf.image(f'assets\\qrcode\\{distribuidor}.png',x=118,y=180,w=round(20),h=round(20))

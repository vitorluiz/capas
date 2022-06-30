import locale
import csv
from datetime import date, timedelta
# from codqr import Codigo
from os import listdir
from fpdf import FPDF


locale.setlocale(locale.LC_ALL, '')

class Capas:
    """
    Programa para gerar capas de lote das distribuições feita pelos
    Regionais, lendo um arquivo csv das distribuições.

    """
    def __init__(self, arq_csv, valor, dia, mes):
        self.arq_csv = arq_csv
        self.valor = valor
        self.dia = dia
        self.mes = mes
        self.template = "/home/vitorluiz/Documentos/capas/assets/imagens/Template.jpg"
        self.output = "/home/vitorluiz/Documentos/capas/"

        # Create FPDF object
        # Layout ('P','L')
        # Unit('mm','cm','in')
        # format ('A3','A4',(default), 'A5', 'Letter', 'Legal',(100,150))
        self.pdf = FPDF('P', 'mm', 'A5')

        # Add a page
        self.pdf.add_page()

        # Add image no background
        self.pdf.image(self.template, x=0, y=0, w=round(self.pdf.w), h=round(self.pdf.h))

        # specify font
        # fonts ('times', 'courier', 'helvetica' , 'symbol', zpfdingbats')
        # 'B' (bold), 'U' (underline, 'I' (italics), ''(regular), combination (i.e., ('BU'))
        self.pdf.set_font('Times', 'BI', 11)

        # add text
        # w = width
        # h = height
        # txt = your text
        # ln (0 False; 1 True - move cursor down to next line)
        # border (0 False; 1 True - add border around cell)

        with open(self.arq_csv, encoding='UTF-8', errors='ignore') as csv_file:
            # Abrindo CSV
            _csv = csv.reader(csv_file, delimiter=';')
            # Pulando 1 lnh Cabeçalho
            _csv.__next__()
            _csv.__next__()
            x = 1
            for lnh in _csv:

                # Data Sorteio
                data = date(year=2022, month=self.mes, day=self.dia)
                sorteio = data.strftime('%d / %m / %Y')

                # Dia Entrega
                #data2 = date(year=2022, month=self.mes, day=self.dia)
                data2 = data - timedelta(days=8)
                entrega = data2.strftime('%d / %m / %Y')

                etapa = lnh[1]
                codPonto = lnh[2].zfill(3)
                ponto = lnh[3].strip()
                rota = lnh[4].strip()
                endereco = lnh[5].strip()
                cidade = lnh[6].strip()
                telefone = lnh[7].strip()
                seq = x
                inicio = lnh[9].strip()
                final = lnh[10].strip()
                qtd = lnh[11].strip()
                regional = lnh[12].strip()

                tel_distribuidor = lnh[13]

                observPonto = lnh[14].strip().replace('_x000D_', '')

                self.pdf.image(self.template,
                               x=0, y=0, w=round(self.pdf.w), h=round(self.pdf.h)
                               )
                self.dados(sorteio, etapa, codPonto, ponto, telefone, rota, endereco, cidade, seq,
                           inicio, final, qtd, regional, tel_distribuidor, observPonto,
                           entrega)

                self.pdf.add_page()
                x += 1
                print(seq)
            self.saida(regional)

    # Posição dos dados variaveis
    def dados(self, sorteio, codPonto, etapa, ponto, telefone, rota, endereco,
              cidade, seq, inicio, final, qtd, distribuidor,
              tel_distribuidor, observPonto, entrega):
        # Data Entrega
        self.pdf.set_text_color(255, 0, 0)
        self.pdf.text(32, 33.5, entrega)
        # Data Sorteio

        self.pdf.text(115, 33.5, sorteio)

        # Etapa/Edição
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.text(17.5, 42.5, etapa)

        # Código do PDV
        self.pdf.text(105, 42.5, codPonto)

        # Rota
        self.pdf.text(65, 42.5, rota)

        # Nome pv
        self.pdf.text(17.5, 49, ponto)

        # Telefones
        self.pdf.text(21, 79.5, telefone)

        # Endereço
        self.pdf.text(22, 56.5, endereco)

        # Observação dos PDV
        self.pdf.text(21, 64.5, observPonto)

        # Bairro/Cidade
        self.pdf.text(16.5, 72, cidade)

        # Distribuidor
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_font_size(10)
        self.pdf.text(29, 87.5, distribuidor)

        # Telefone Distribuidor
        self.pdf.set_font_size(10)
        self.pdf.text(80, 87.5, tel_distribuidor)

        # Orden Liberação
        self.pdf.set_font('times', 'B', 12)
        self.pdf.set_text_color(255, 0, 0)
        self.pdf.text(15, 156, str(seq).zfill(3))

        # Título Início
        self.pdf.set_font('helvetica', 'B', 12)
        self.pdf.text(42, 156, inicio)

        # Título Fim
        self.pdf.set_font('helvetica', 'B', 12)
        self.pdf.text(70, 156, final)

        # Quantidade
        self.pdf.set_font('helvetica', 'B', 12)
        self.pdf.text(100, 156, qtd)

        # Total Liberado
        total = int(qtd) * self.valor
        self.pdf.set_font('helvetica', 'B', 12)
        self.pdf.text(120, 156, f'R$ {total},00')

        # Data Termo
        # self.pdf.set_font('helvetica','',8)
        # self.pdf.text(10,152,data)

        # Assinatura
        self.pdf.set_font_size(12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.text(self.pdf.w / 3.5, 203, ponto)

        # Assinatura
        #     self.pdf.set_font('helvetica','',10)
        #     self.pdf.text(self.pdf.w/4,195,"Por favor mande uma mensagem via")
        #     self.pdf.text(self.pdf.w/5,200,"whatsapp para este número. (65) 99959-7408")

        #     if f'{distribuidor}.png' not in os.listdir('assets\\qrcode\\'):
        #         meuqr = Codigo(distribuidor,'https://api.whatsapp.com/send?phone=55659'+'99597408'+'&text=Ol%C3%A1%2C%20Pode%20me%20ajudar%3F')
        #         meuqr.codeqr()
        #         self.pdf.image(f'assets\\qrcode\\{distribuidor}.png',x=118,y=180,w=round(20),h=round(20))

        #     elif f'{distribuidor}.png' in os.listdir('assets\\qrcode\\'):
        #         self.pdf.image(f'assets\\qrcode\\{distribuidor}.png',x=118,y=180,w=round(20),h=round(20))

    def saida(self, nome):
        self.nome = nome
        self.pdf.output(self.output + '/pdf/' + self.nome + ".pdf")

    def version(self):
        print("Versão 1.0.0")
        print("Autor: Vitor Luiz Machado")
        print("Data: 04/01/2022")


if __name__ == '__main__':
    for f in listdir('/home/vitorluiz/Documentos/capas/csv'):
        print(f)
        Capas(f"/home/vitorluiz/Documentos/capas/csv/{f}",
              valor=15,
              dia=3,
              mes=7)

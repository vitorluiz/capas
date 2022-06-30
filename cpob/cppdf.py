from fpdf import FPDF
import csv,time,os


class Capas:
    def __init__(self,arquivo_csv):
        self.arquivo_csv = arquivo_csv

         #Create FPDF object
        #Layout ('P','L')
        # Unit('mm','cm','in')
        # format ('A3','A4',(default), 'A5', 'Letter', 'Legal',(100,150))
        self.pdf = FPDF('P','mm','A5')

        # Add a page
        self.pdf.add_page()

        # Add image no background
        self.pdf.image('assets\imagens\geral.jpg',x=0,y=0,w=round(self.pdf.w),h=round(self.pdf.h))

        # specify font
        # fonts ('times', 'courier', 'helvetica' , 'symbol', zpfdingbats')
        # 'B' (bold), 'U' (underline, 'I' (italics), ''(regular), combination (i.e., ('BU'))
        self.pdf.set_font('helvetica','',12)

        # add text
        # w = width
        # h = height
        # txt = your text
        # ln (0 False; 1 True - move cursor down to next line)
        # border (0 False; 1 True - add border around cell)

           
        with open(self.arquivo_csv,encoding='utf-8',errors='ignore') as csv_file:
            # Abrindo CSV
            ler_csv = csv.reader(csv_file, delimiter=';')
            # Pulando 1 lnh Cabeçalho
            ler_csv.__next__()
            x = 1
            for lnh in ler_csv:
                dataSorteio = str(lnh[0].zfill(3))
                data=f'{dataSorteio[:2]}/{dataSorteio[2:4]}/20{dataSorteio[4:]}'
                etapa = lnh[1].strip()
                ponto = lnh[2].strip()
                rota = lnh[3].strip()
                endereco = lnh[4].strip()
                cidade = lnh[5].strip()
                telefone = lnh[6].strip()
                seq = x
                #seq = str(lnh[7].strip())
                inicio = lnh[8].strip()
                final = lnh[9].strip()
                qtd = lnh[10].strip()
                distribuidor = lnh[11].strip()
                #print(lnh)
                print(seq)
                print(time.process_time())
                self.pdf.image('assets\imagens\geral.jpg',x=0,y=0,w=round(self.pdf.w),h=round(self.pdf.h))
                self.dados(data,etapa,ponto,telefone,rota,endereco,cidade,seq,inicio,final,qtd,distribuidor)
                self.pdf.add_page()
                x+=1
            self.saida(distribuidor)
import code
import qrcode
from PIL import Image
class Codigo:
    def __init__(self, nome, texto):
        self.nome = nome
        self.texto = texto
       
    def codeqr(self):

        center_img = Image.open('assets\imagens\whatsapp.png').resize((75,75))
        
        qr_big = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        qr_big.add_data(self.texto)
        qr_big.make()
        img_qr_big = qr_big.make_image().convert('RGB')
        
        pos = ((img_qr_big.size[0] - center_img.size[0]) // 2, (img_qr_big.size[1] - center_img.size[1]) // 2)


        img_qr_big.paste(center_img, pos)
        img_qr_big.save(f"assets\qrcode\{self.nome}.png")


if __name__ == "__main__":
    meuqr = Codigo("vitorluiz","https://www.google.com.br")
    meuqr.codeqr()
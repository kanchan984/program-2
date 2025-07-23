import qrcode 
qr = qrcode.QRCode(
    version = 8,
    box_size = 10,
    border = 5
)
data =" https://www.youtube.com/watch?v=Tx2uEx5yxx4&list=RDTx2uEx5yxx4&start_radio=1"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "red",back_color = "blue")
img.save("www.song.png")
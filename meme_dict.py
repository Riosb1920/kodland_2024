meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "AGGRO" : "untuk menjadi agresif/marah",
            "CREEPY" : "menakutkan, tidak menyenangkan",
            "ROFL" : "tanggapan terhadap lelucon"
            }

for i in range(5):
    word = input("\nKetik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ") 
    
    if word == "End":
        print("\nTerimakasih, telah menggunakan kamus ini!")
        break 

    if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
         print(meme_dict[word])
    
    else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?  
        print("Maat kata yang anda cari tidak ada")

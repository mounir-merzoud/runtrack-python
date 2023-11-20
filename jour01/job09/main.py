
nom_produit = 'shoes'
prix_du_produit = 10
quantite_en_stock = 200

print("Nom du produit:", nom_produit)
print("Prix unitaire:", prix_du_produit, "EURO")
print("Quantité en stock:", quantite_en_stock, "unité")

quantite_vendu = int(input("Entrez la quantité de produits vendu : "))
quantite_en_stock -= quantite_vendu

prix_du_produit *= 1.10

print("Prix unitaire après inflation :", prix_du_produit, "EURO")  
print("Quantité en stock apres la vente:", quantite_en_stock, "UNI")  



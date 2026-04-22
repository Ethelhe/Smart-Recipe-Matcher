class Recipe:  
    def __init__(self, name, ingredients): 
     self.name = name
     self.ingredients = set([i.strip().lower() for i in ingredients]) 
    
    def get_jaccard_score(self, user_inventory): 
     user_set = set([i.strip().lower() for i in user_inventory]) 
     intersection = self.ingredients.intersection(user_set) 
     union = self.ingredients.union(user_set) 
     return len(intersection) / len(union) if union else 0
print("Tarif Önericiye Hoş Geldiniz!")

menemen = Recipe("Menemen", ["yumurta", "domates", "biber", "siviyağ", "tuz"])
kullanici_malzemeleri = ["Yumurta", "domates", "Biber", "Siviyağ", "Tuz", "Soğan"]
skor = menemen.get_jaccard_score(kullanici_malzemeleri)

print(f"Menemen için Jaccard Eşleşme Skoru: {skor}")
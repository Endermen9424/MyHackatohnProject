import numpy as np
import matplotlib.pyplot as plt

average = 200

def calculates(todaylyWater: int = "0", PersonCount: int = "1", DaysCount: int = "1"):
    CalculateAverage = average * PersonCount * DaysCount
    FamilyWater = todaylyWater * PersonCount * DaysCount
    if FamilyWater > CalculateAverage + 50:
        return "Çok fazla su harcıyorsunuz!"
    elif FamilyWater < CalculateAverage -50:
        return "Su harcamanız Çok iyi."
    else:
        return "Su harcamanız normal."

def DrawGraph(todaylyWater: int = "0", PersonCount: int = "1", DaysCount: int = "1"):
    CalculateAverage = average * PersonCount * DaysCount
    FamilyWater = todaylyWater * PersonCount * DaysCount
    x = np.array([1, 2])
    y = np.array([CalculateAverage, FamilyWater])
    plt.bar(x, y)
    plt.xticks(x, ['Ortalama', 'Sizin'])
    plt.ylabel('Su Miktarı')
    plt.title('Su Harcama Grafiği')
    plt.savefig('static/picture/graph.png')
    
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# NLTK verilerini indiriyoruz (ilk kullanımda gerekebilir)
nltk.download('punkt_tab')
nltk.download('stopwords')

# Öneri fonksiyonu
def get_suggestions(user_input):
    # Küçük harfe dönüştürme
    user_input = user_input.lower()
    
    # Kelimeleri tokenize etme (cümleyi kelimelere ayırma)
    words = word_tokenize(user_input)
    
    # Stopwords (anlam taşımayan kelimeler) listesini al
    stop_words = set(stopwords.words('turkish'))
    
    # Stopwords hariç kelimeleri filtrele
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Kelimelerin sıklığını hesapla
    fdist = FreqDist(filtered_words)
    
    # En sık geçen 5 kelimeyi bulma
    most_common_words = fdist.most_common(5)
    
    # Kullanıcıya su tasarrufu önerileri oluşturma
    suggestions = []
    
    if 'su' in filtered_words:
        suggestions.append("Su tasarrufu sağlamak için duş sürenizi kısaltmayı deneyin.")
    if 'kullan' in filtered_words or 'harca' in filtered_words:
        suggestions.append("Su tasarrufu yapmak için muslukları kullanmadığınızda kapalı tutun.")
    if 'bahçe' in filtered_words:
        suggestions.append("Bahçenizi sularken suyunuzu israf etmeyin, sabah saatlerini tercih edin.")
    if 'çamaşır' in filtered_words:
        suggestions.append("Çamaşır makinelerini yalnızca tam dolu olduğunda çalıştırın.")
    
    # En sık kelimelere göre genel öneri
    if most_common_words:
        suggestions.append(f"En sık kullanılan kelimeler: {', '.join([word for word, _ in most_common_words])}")
    
    # Eğer su tasarrufu ile ilgili herhangi bir öneri bulunamadıysa, genel bir öneri
    if not suggestions:
        suggestions.append("Su tasarrufu sağlamak için bilinçli kullanım çok önemlidir. Unutmayın, her damla değerli!")
    
    return suggestions

print(get_suggestions("Su tasarrufu için neler yapabilirim?"))
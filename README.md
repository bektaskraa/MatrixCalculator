# Simple Matrix Calculator (Basit Matris Hesaplayıcı) 🐍🔢

Basit matris işlemleri için temel bir Python sınıfı ve fonksiyonları içeren bir kütüphane. Bu proje, matris tanımını, oluşturulmasını, görüntülenmesini ve toplama işlemlerini gerçekleştirmeyi amaçlar.

## 🌟 Özellikler

* **`Matrix` Sınıfı:** Matrisleri tutmak ve yönetmek için temel yapı.
* **Matris Oluşturma:** Belirtilen boyutlarda sıfır matrisi oluşturma (`create_matrix`).
* **Matris Görüntüleme:** Matrisi okunabilir formatta yazdırma (`print_matrix`).
* **Matris Toplama:** Aynı boyutlardaki iki matrisi toplama (`add` fonksiyonu).

## 🚀 Kurulum

Bu kütüphane harici bir bağımlılık gerektirmez. Kodu doğrudan projenize kopyalayıp kullanabilirsiniz.

### Kullanım

Kod dosyasını projenize dahil ettikten sonra, `Matrix` sınıfını ve `add` fonksiyonunu aşağıdaki gibi kullanabilirsiniz.

## 💻 Kullanım Örnekleri

İşte kütüphaneyi nasıl kullanacağınıza dair temel bir örnek:

```python
# Matrix sınıfı ve add fonksiyonunun olduğu dosyanızı import edin
# from matrix_calculator import Matrix, add 

# 1. Matris Tanımlama
# Not: Tanımlanan matrisler aynı boyutta olmalıdır.

A = Matrix([[1, 2, 3],
            [4, 5, 6]])

B = Matrix([[10, 20, 30],
            [40, 50, 60]])

# 2. Matrisleri Görüntüleme
print("--- A Matrisi ---")
A.print_matrix()
# Çıktı:
# [1, 2, 3]
# [4, 5, 6]

# 3. Matris Toplama
# C = A + B
C = add(A, B)

print("\n--- C = A + B Matrisi ---")
C.print_matrix()
# Çıktı:
# [11, 22, 33]
# [44, 55, 66]

# 4. Hata Yönetimi (Boyut Uyuşmazlığı)
D = Matrix([[1, 2], [3, 4]])
E = Matrix([[1, 2, 3], [4, 5, 6]])

print("\n--- Boyut Uyuşmazlığı Örneği (D + E) ---")
add(D, E)
# Çıktı:
# Error(add): Matris boyutları eşleşmiyor
```
## 🛠️ Kod Yapısı

### `Matrix` Sınıfı Metotları

| Metot Adı | Açıklama |
| :--- | :--- |
| `__init__(self, matrix: list=None)` | Matrisi verilen 2D liste ile başlatır ve `rows`/`cols` (satır/sütun) özelliklerini belirler. |
| `create_matrix(self, row, col)` | Belirtilen `row` ve `col` değerleriyle bir sıfır matrisi oluşturur. |
| `get_rows(self)` | Matrisin satırlarını döndürür (kendisini). |
| `get_columns(self)` | Matrisin **sütunlarını** liste olarak döndürür. |
| `print_matrix(self)` | Matrisi terminale yazdırır. |

### Fonksiyonlar

| Fonksiyon Adı | Açıklama |
| :--- | :--- |
| `add(Matrix1: Matrix, Matrix2: Matrix)` | Aynı boyuttaki iki matrisi toplar ve sonucu yeni bir `Matrix` nesnesi olarak döndürür. Boyutlar uyuşmazsa hata mesajı verir. |

---

## Geliştirici Notu

Lineer Cebir dersinde yeni öğrendiğim matrisler konusunu pekiştirmek amacıyla, tamamen kişisel emeğimle oluşturulmuştur.

Kütüphanenin tüm mantıksal kurgusunu, sınıf yapısını ve algoritmalarını hiçbir yapay zeka desteği almadan kendim tasarladım ve yazdım. Bu süreç, matris işlemlerinin teorisini pratiğe dökerek konuyu içselleştirmemi sağladı.

Yapay zekanın kullanıldığı tek yer README.md dosyasıdır; 
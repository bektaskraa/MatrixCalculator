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
# Matrix sınıfı ve fonksiyonları import edin
# from matrix_calculator import Matrix, add, sub, mul, transpose

# 1. Matris Tanımlama
A = Matrix([[1, 2, 3],
            [4, 5, 6]])

B = Matrix([[10, 20, 30],
            [40, 50, 60]])

# 2. Matrisleri Görüntüleme
print("--- A Matrisi ---")
A.print_matrix()

# 3. Matris Toplama
C = add(A, B)
print("\n--- C = A + B Matrisi ---")
C.print_matrix()

# 4. Matris Çıkarma
D = sub(A, B)
print("\n--- D = A - B Matrisi ---")
D.print_matrix()

# 5. Hata Yönetimi (Boyut Uyuşmazlığı)
D2 = Matrix([[1, 2], [3, 4]])
E2 = Matrix([[1, 2, 3], [4, 5, 6]])
print("\n--- Boyut Uyuşmazlığı Örneği (D2 + E2) ---")
add(D2, E2)  # Hata mesajı beklenir

# 6. Matris Çarpımı (mul)
M1 = Matrix([[1, 2],
             [3, 4],
             [5, 6]])

M2 = Matrix([[7, 8, 9],
             [10, 11, 12]])

print("\n--- Matris Çarpımı (M1 x M2) ---")
M3 = mul(M1, M2)
M3.print_matrix()
# Çıktı:
# [27, 30, 33]
# [61, 68, 75]
# [95, 106, 117]

# 7. Matris Transpozu (transpose)
print("\n--- A Matrisi Transpozu ---")
T = transpose(A)
T.print_matrix()
# Çıktı:
# [1, 4]
# [2, 5]
# [3, 6]

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

| Fonksiyon Adı                           | Açıklama                                                                                                                            |
|:----------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| `add(Matrix1: Matrix, Matrix2: Matrix)` | Aynı boyuttaki iki matrisi toplar ve sonucu yeni bir `Matrix` nesnesi olarak döndürür. Boyutlar uyuşmazsa hata mesajı verir.        |
| `sum(Matrix1: Matrix, Matrix2: Matrix)` | Aynı boyuttaki iki matrisi çıkartır ve sonucu yeni bir `Matrix` nesnesi olarak döndürür. Boyutlar uyuşmazsa hata mesajı verir.      |
| `mul(Matrix1: Matrix, Matrix2: Matrix)` | İlk matrisin sütun sayısı ikinci matrisin satır sayısına eşitse matris çarpımını yapar ve sonucu yeni bir `Matrix` olarak döndürür. |
| `transpose(Matrix1: Matrix)` | Verilen matrisi transpoze eder (satır ve sütunları yer değiştirir) ve sonucu yeni bir `Matrix` olarak döndürür.                                                                                       |

---

## Geliştirici Notu

Lineer Cebir dersinde yeni öğrendiğim matrisler konusunu pekiştirmek amacıyla, tamamen kişisel emeğimle oluşturulmuştur.

Kütüphanenin tüm mantıksal kurgusunu, sınıf yapısını ve algoritmalarını hiçbir yapay zeka desteği almadan kendim tasarladım ve yazdım. Bu süreç, matris işlemlerinin teorisini pratiğe dökerek konuyu içselleştirmemi sağladı.

Yapay zekanın kullanıldığı tek yer README.md dosyasıdır; 
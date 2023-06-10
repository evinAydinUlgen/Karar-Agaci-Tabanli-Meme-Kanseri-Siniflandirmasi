import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve, auc

# Veri setini yükleme
data = pd.read_csv(r'C:\Users\90546\OneDrive\Masaüstü\veriMadenciligi\breast-cancer.csv', header=0)
# Veri setinin boyutunu (satır, sütun)  görüntüleme
print("Veri setinin boyutu:", data.shape)
# Sütun adlarını görüntüleme
print("Sütun adları:", data.columns)
# Sütunların veri tiplerini göster
print("Veri tipleri:\n", data.dtypes)
# Her sütundaki eksik değer sayısını kontrol etme
print("Sütunlardaki eksik değer sayısı:\n", data.isnull().sum())
# Sütunlardaki benzersiz değerleri göster
for column in data.columns:
    unique_values = data[column].unique()
    print("Benzersiz değerler:\n", f"{column}: {unique_values}")

# String değerleri sayısal değerlere dönüştürme
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['Class'])
# Özniteliklerin dönüşümü
X_encoded = pd.get_dummies(data.drop('Class', axis=1))
print("Öznitelikler:\n", X_encoded)
print("Hedef değişken y:\n", y)
# Eğitim ve test verisi olarak böl
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=0)
# Decision Tree modelini oluştur ve eğit
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Decision Tree Çizimi
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(clf, max_depth = 2)
plt.savefig('decision_tree.png')

# Test veri kümesi üzerinde tahmin yap
y_pred = clf.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report, precision_score, recall_score, f1_score
# Metrikleri hesapla
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Metrikleri yazdır
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)
print("Classification Report:", report)

# Confusion matrix'i oluştur
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

#Confusion matrisini görselleştirme              
# Heatmap oluştur
sns.heatmap(cm, annot=True, cmap="Blues")
# Eksen etiketlerini ayarla
plt.xlabel("Tahmin Edilen Sınıflar")
plt.ylabel("Gerçek Sınıflar")
# Grafiği göster
plt.show()

#Roc-curve grafiğini kullanarak görselleştirme
y_pred_prob = clf.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label='ROC curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()
y_pred_prob = clf.predict_proba(X_test)[:, 1]

# precision-recall grafiğiyle görselleştirme
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_prob)
# Precision-Recall eğrisini çizmek için bir çizgi grafiği oluşturma
plt.plot(recall, precision, marker='.')
# Eksen ve başlık etiketlerini ayarlama
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
# Grafikleri göster
plt.show()














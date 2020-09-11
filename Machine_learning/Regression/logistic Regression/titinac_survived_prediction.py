##Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train=pd.read_csv('titanic_train.csv')

## Explorative Datenanalyse

#Fehlende Daten (en. missing data)
train.isnull() #Funktion zum erkennen aller fehlenden NaN
sns.heatmap(train.isnull())# Visualisierung der fehlenden Nullwerte

sns.countplot('Survived',data=train)

# Ungefähr 20 Prozent der Altersdaten (en. age data) fehlt. Der Anteil wahrscheinlich noch klein genug, um eine sinnvolle Ersetzung der fehlende Werte vorzunehmen.
# Wenn wir auf die Kabinenspalte (en. cabin column) schauen stellen wir etwas anderes fest. Es scheint als würden wir hier zu viele Datenpunkte auslassen, um eine vernünftige Ersetzung vorzunehmen

sns.countplot('Survived',data=train) # Anzahl aller survived bzw. not-survived
sns.countplot('Survived',hue='Sex',data=train) # Anzahl aller survived bzw. not-survived nach Geschlecht
sns.countplot('Survived',hue='Pclass',data=train) # Anzahl aller survived bzw. not-survived nach Ticketklasse
plt.hist(x=train['Age'],bins=30,color='darkred',alpha=0.7) #Verteilung aller Personen nach Alter via Histogramm
sns.countplot('SibSp',data=train) #Anzahl von Personen mit Familienmtiglieder
train['Fare'].hist(color='green',bins=40,figsize=(8,4)) # #Verteilung aller Personen nach Ticketpreis via Histogramm

## Datenbereinigung
# Wir wollen die fehlenden Altersdaten ersetzen anstatt die Zeilen mit fehlenden Werten einfach zu löschen.
# Eine Möglichkeit dies zu tun wäre das durchschnittliche Alter aller Passagiere einzufügen (Imputation).
# Wir können allerdings noch einen Schritt genauer vorgehen und das durchschnittliche Alter der entsprechenden Klasse einfügen.

train.groupby('Pclass')['Age'].mean()
sns.boxplot(x='Pclass',y='Age',data=train)

# Mit Hilfe der Impute Funktion können wir das Durchsnittsalter in das Datenset übergeben
from sklearn.impute import SimpleImputer
impute=SimpleImputer()

train_new=train

#Erstellung eines DF für jede Ticketklasse. Im nächsten Schritt DF auf die zu manipulierende Spalte begrenzen

#Ticketklasse 1
train_class1= train_new[train_new['Pclass']==1]
train_class1_age=train_class1[['Age']]
#Ticketklasse 2
train_class2= train_new[train_new['Pclass']==2]
train_class2_age=train_class2[['Age']]
#Ticketklasse 3
train_class3= train_new[train_new['Pclass']==3]
train_class3_age=train_class3[['Age']]

#Berechnung das Durchschnitts-Alter für jede Klasse
new_class1_age=impute.fit_transform(train_class1_age)
new_class2_age=impute.fit_transform(train_class2_age)
new_class3_age=impute.fit_transform(train_class3_age)

#Überschreiben der Manipulierten Spalte auf das DF je Ticketklasse
train_class1['Age']=new_class1_age
train_class2['Age']=new_class2_age
train_class3['Age']=new_class3_age

#Zusammenführen aller DF zu einem für die Prediction
df=pd.merge(train_class1,train_class2,how='outer')
df2=pd.merge(df,train_class3,how='outer')

#Löschen der Spalte Cabin (es fehlen zu viele Werte)
df2.drop('Cabin',axis=1,inplace=True)
#Löschen einzelner fehlender Einträge für ein sauberes durchgängiges DF
df2.dropna(inplace=True)

#Visualisierung des DF
sns.heatmap(df2),yticklabels=False,cbar=False,cmap='viridis')


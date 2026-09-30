# b4n1-boost

Moteur d'accélération de performance transparent pour **Django**, **FastAPI** et **Flask**.

`b4n1-boost` fournit un middleware Rust natif Plug-and-Play pour les frameworks web Python : chemin de réponse pass-through sans copie, compression native gzip/Brotli sans GIL et moteur JSON natif, sans modification du code de votre application.

---

> Mesurez l'accélération de bout en bout dans votre propre application — le gain réel dépend de votre charge de travail.

---

## 📦 Installation

Disponible sur les 4 registres (cœur natif + EULA inclus):

```bash
pip install b4n1-boost          # Python 3.10–3.13
npm install b4n1-boost          # Node.js
dotnet add package B4N1.Boost   # .NET
```
```xml
<dependency>
  <groupId>com.b4n1</groupId>
  <artifactId>boost</artifactId>
  <version>0.3.5</version>
</dependency>
```

---

## 🚀 Démarrage Rapide

```python
import b4n1_boost

# Activer pour Django
b4n1_boost.install_django()

# Activer pour FastAPI
b4n1_boost.install_fastapi()

# Activer pour Flask
b4n1_boost.install_flask()
```

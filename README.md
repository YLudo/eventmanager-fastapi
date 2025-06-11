
# 📆 EventManager API – FastAPI

Une API RESTful pour la gestion d'événements avec authentification JWT, envoi d'emails, géolocalisation, et structure modulaire en FastAPI.

## 🚀 Fonctionnalités principales

- 🔐 Authentification JWT (`/users/register`, `/users/login`)
- 📅 CRUD complet sur les événements (`/events`)
- 🌍 Intégration Nominatim API (géolocalisation des lieux)
- 📩 Envoi de mails de confirmation (Mailtrap SMTP)
- 🔄 CORS ouvert pour le client
- 🗃️ Cache mémoire sur les routes GET
- 🧩 Structure modulaire (models, schemas, services, crud)
- 🛡️ Sécurité par dépendance (`Depends`, JWT)
- 🗄️ PostgreSQL (NeonDB)
- ☁️ Déploiement Docker-ready (Render, Railway, etc.)

## 🔧 Technologies

- **FastAPI** (backend)
- **SQLAlchemy** (ORM)
- **Pydantic** (validation des schémas)
- **PostgreSQL** (NeonDB)
- **Mailtrap** (test d’e-mails SMTP)
- **Nominatim API** (géocodage)
- **Docker** (déploiement)
- **Uvicorn** (serveur ASGI)

## 📦 Installation locale

```bash
git clone https://github.com/votre-utilisateur/eventmanager-fastapi.git
cd eventmanager-fastapi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## ⚙️ Variables d'environnement (.env)

```env
# PostgreSQL NeonDB
DATABASE_URL=postgresql://...

# Auth
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
  
# Mail SMTP (Mailtrap)
SMTP_HOST=sandbox.smtp.mailtrap.io
SMTP_PORT=587
SMTP_USERNAME=...
SMTP_PASSWORD=...
SENDER_EMAIL=no-reply@eventmanager.com
```

## 🛠 Endpoints principaux

| Méthode | Route | Auth ? | Description |
| -- | -- | -- | -- |
| POST | /users/register | ❌ | Créer un nouvel utilisateur
| POST | /users/login | ❌ | Obtenir un token JWT
| GET | /events | ❌ | Liste des événements
| POST | /events | ✅ | Créer un événement
| PUT | /events/{id} | ✅ | Modifier un événement (propriétaire)
| DELETE | /events/{id} | ✅ | Supprimer un événement

## 📡 Déploiement

### 🔹 Render (Docker)

1. Connecter GitHub
2. Choisir Dockerfile comme runtime
3. Ajouter les variables d’environnement .env
4. Déploiement automatique

## ✅ Checklist M2 – Critères respectés

- ✅ Principes REST
- ✅ Authentification sécurisée
- ✅ Modèle modulaire clair
- ✅ Service externe (API & mail)
- ✅ Découplage & bonnes pratiques
- ❌ (optionnel) Microservices
- ✅ (bonus) Déploiement Dockerisé

## ✨ Auteur

Projet réalisé dans le cadre du module M2 Web Services
Développé avec ❤️ par Ludovic Roux – 2025
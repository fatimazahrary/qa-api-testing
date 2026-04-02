import pytest
import requests

# ─── Configuration ─────────────────────────────────────────────────────────────

BASE_URL = "https://jsonplaceholder.typicode.com"


# ─── Tests GET ─────────────────────────────────────────────────────────────────

class TestGetRequests:
    """Tests des requêtes GET sur l'API."""

    def test_get_all_posts(self):
        """TC-01 : Récupérer tous les posts — statut 200 et liste non vide."""
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200, f"Statut attendu 200, reçu {response.status_code}"
        data = response.json()
        assert isinstance(data, list), "La réponse doit être une liste."
        assert len(data) > 0, "La liste ne doit pas être vide."
        print(f"✅ TC-01 : {len(data)} posts récupérés.")

    def test_get_single_post(self):
        """TC-02 : Récupérer un post par ID — vérifier la structure JSON."""
        response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200
        data = response.json()
        assert "id" in data, "Le champ 'id' est manquant."
        assert "title" in data, "Le champ 'title' est manquant."
        assert "body" in data, "Le champ 'body' est manquant."
        assert "userId" in data, "Le champ 'userId' est manquant."
        assert data["id"] == 1
        print(f"✅ TC-02 : Post récupéré — titre : '{data['title'][:40]}...'")

    def test_get_post_not_found(self):
        """TC-03 : Récupérer un post inexistant — statut 404."""
        response = requests.get(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404, f"Statut attendu 404, reçu {response.status_code}"
        print("✅ TC-03 : Post inexistant — 404 retourné correctement.")

    def test_get_comments_by_post(self):
        """TC-04 : Récupérer les commentaires d'un post."""
        response = requests.get(f"{BASE_URL}/posts/1/comments")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        # Vérifier la structure d'un commentaire
        comment = data[0]
        assert "email" in comment
        assert "body" in comment
        print(f"✅ TC-04 : {len(data)} commentaires récupérés pour le post 1.")

    def test_response_time_acceptable(self):
        """TC-05 : Vérifier que le temps de réponse est inférieur à 3 secondes."""
        response = requests.get(f"{BASE_URL}/posts")
        assert response.elapsed.total_seconds() < 3, \
            f"Temps de réponse trop long : {response.elapsed.total_seconds():.2f}s"
        print(f"✅ TC-05 : Temps de réponse : {response.elapsed.total_seconds():.2f}s")


# ─── Tests POST ────────────────────────────────────────────────────────────────

class TestPostRequests:
    """Tests des requêtes POST (création de données)."""

    def test_create_post(self):
        """TC-06 : Créer un nouveau post — statut 201."""
        payload = {
            "title": "Test Automation Post",
            "body": "This post was created by an automated test.",
            "userId": 1
        }
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        assert response.status_code == 201, f"Statut attendu 201, reçu {response.status_code}"
        data = response.json()
        assert data["title"] == payload["title"]
        assert "id" in data
        print(f"✅ TC-06 : Post créé avec succès — ID : {data['id']}")

    def test_create_post_missing_field(self):
        """TC-07 : Créer un post sans titre — vérifier la réponse de l'API."""
        payload = {"body": "Post sans titre", "userId": 1}
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        # JSONPlaceholder accepte quand même (API de test), on vérifie juste que ça répond
        assert response.status_code in [200, 201]
        print("✅ TC-07 : Comportement API vérifié pour champ manquant.")


# ─── Tests PUT ─────────────────────────────────────────────────────────────────

class TestPutRequests:
    """Tests des requêtes PUT (mise à jour)."""

    def test_update_post(self):
        """TC-08 : Mettre à jour un post existant — statut 200."""
        payload = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated body content.",
            "userId": 1
        }
        response = requests.put(f"{BASE_URL}/posts/1", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        print("✅ TC-08 : Post mis à jour avec succès.")


# ─── Tests DELETE ──────────────────────────────────────────────────────────────

class TestDeleteRequests:
    """Tests des requêtes DELETE (suppression)."""

    def test_delete_post(self):
        """TC-09 : Supprimer un post — statut 200."""
        response = requests.delete(f"{BASE_URL}/posts/1")
        assert response.status_code == 200
        print("✅ TC-09 : Post supprimé avec succès.")


# ─── Tests Headers ─────────────────────────────────────────────────────────────

class TestHeaders:
    """Tests de validation des headers HTTP."""

    def test_content_type_is_json(self):
        """TC-10 : Vérifier que le Content-Type de la réponse est bien JSON."""
        response = requests.get(f"{BASE_URL}/posts/1")
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type, \
            f"Content-Type inattendu : {content_type}"
        print(f"✅ TC-10 : Content-Type correct : {content_type}")

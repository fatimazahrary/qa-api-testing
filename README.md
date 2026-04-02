# 🔌 REST API Testing Framework — Python + Pytest + Requests

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pytest](https://img.shields.io/badge/Pytest-7.x-orange)
![Requests](https://img.shields.io/badge/Requests-2.x-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📌 Description

A complete REST API testing framework built with **Python**, **Pytest**, and **Requests**.  
This project covers all HTTP methods (GET, POST, PUT, DELETE), response validation, JSON schema checks, and performance assertions on a real public API.

---

## 🎯 Test Cases Covered

| ID | Method | Test Case | Status |
|----|--------|-----------|--------|
| TC-01 | GET | Retrieve all posts — status 200, non-empty list | ✅ |
| TC-02 | GET | Retrieve single post — validate JSON structure | ✅ |
| TC-03 | GET | Non-existent resource returns 404 | ✅ |
| TC-04 | GET | Retrieve comments by post ID | ✅ |
| TC-05 | GET | Response time under 3 seconds | ✅ |
| TC-06 | POST | Create a new post — status 201 | ✅ |
| TC-07 | POST | Missing field behavior validation | ✅ |
| TC-08 | PUT | Update existing post — status 200 | ✅ |
| TC-09 | DELETE | Delete a post — status 200 | ✅ |
| TC-10 | GET | Content-Type header is application/json | ✅ |

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Requests** — HTTP calls
- **Pytest** — Test runner & assertions
- **pytest-html** — HTML test reports

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/fatimazahrary/qa-api-testing.git
cd qa-api-testing
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run all tests
```bash
pytest
```

### 4. View the HTML report
```bash
open reports/report.html
```

---

## 📁 Project Structure

```
qa-api-testing/
│
├── tests/
│   └── test_api.py         # All API test cases
│
├── reports/                # Auto-generated HTML reports
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
└── README.md
```

---

## 🌐 API Under Test

**JSONPlaceholder** — `https://jsonplaceholder.typicode.com`  
A free, public REST API used for testing and prototyping.  
Endpoints tested: `/posts`, `/posts/{id}`, `/posts/{id}/comments`

---

## 👩‍💻 Author

**[Ton Prénom Nom]**  
Junior QA Engineer | API Testing | Test Automation  
📧 [fatimazahrary.12@gmail.com]  
🔗 [linkedin.com/in/fatimazahrary]

---

## 📄 License

MIT License — free to use and modify.

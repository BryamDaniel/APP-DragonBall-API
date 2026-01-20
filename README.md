# DRAGON BALL API

App FullStack que consume la API de Dragon Ball donde muestro una tabla de personajes y detalles individuales.

## Tecnologias usadas:
- Backend: Python + FastApi
- Frontend: Vue.js 3 + Taildwindcss
- Contenedor: Docker Compose

## Ejecucion:

Para poder revisar este pequeño proyecto debes tener instalado Docker y ejecutar:

docker compose ip --build

## Estructura:

```text
dragonball-project/
│
├── backend/                # Lógica del Servidor (FastAPI)
│   ├── main.py            # Endpoints y configuración de CORS
│   ├── requirements.txt   # Librerías (fastapi, uvicorn, httpx)
│   └── Dockerfile         # Configuración de imagen Python
│
├── frontend/               # Interfaz de Usuario (Vue.js 3)
│   ├── src/
│   │   ├── components/    # Componentes modulares
│   │   │   └── Modal.vue
│   │   │   └── Tabla.vue
│   │   │   └── Card.vue
│   │   ├── App.vue        # Vista principal y gestión de estado
│   │   └── main.js        # Configuración de entrada
│   ├── index.html         # Template base
│   ├── package.json       # Dependencias de Node
│   ├── tailwind.config.js # Configuración de estilos
│   └── Dockerfile         # Configuración de imagen Node
│
├── .dockerignore          # Archivos excluidos del build de Docker
└── docker-compose.yml     # Orquestador de servicios

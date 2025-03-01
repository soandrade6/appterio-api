Endpoints que expondrá la API y ejemplos de uso

---

## **1️⃣ Usuarios** `/user`

### 📌 **Crear un usuario**

**POST** `/user/`

#### **Request Body**

```json
{
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "password": "password123",
  "role": "cuidador"
}
```

#### **Response**

```json
{
  "id": "cf1541d8-7b09-40f5-b43e-d80a0fde1a85",
  "name": "Juan Pérez",
  "email": "juan@example2.com",
  "role": "cuidador",
  "registration_date": "2025-02-27T23:23:30.621402"
}
```

### 📌 **Obtener un usuario por ID**

**GET** `/user{id}`

#### **Response**

```json
{
  "id": "cf1541d8-7b09-40f5-b43e-d80a0fde1a85",
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "role": "cuidador",
  "registration_date": "2025-02-27T23:23:30.621402"
}
```

### 📌 **Obtener todos los usuarios**

**GET** `/user/`

#### **Response**

```json
[
  {
    "id": "uuid",
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "role": "cuidador",
    "registration_date": "2024-02-05T12:00:00"
  },
  {
    "id": "uuid",
    "name": "María López",
    "email": "maria@example.com",
    "role": "investigador",
    "registration_date": "2024-02-05T12:00:00"
  }
]
```

### 📌 **Obtener todos los investigadores**

**GET** `/user/?role=investigador`

#### **Params**

```
role: str
```

#### **Response**

```json
[
  {
    "id": "uuid",
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "role": "investigador",
    "registration_date": "2024-02-05T12:00:00"
  },
  {
    "id": "uuid",
    "name": "María López",
    "email": "maria@example.com",
    "role": "investigador",
    "registration_date": "2024-02-05T12:00:00"
  }
]
```

### 📌 **Obtener todos los cuidadores**

**GET** `/user/?role=cuidador`

#### **Params**

```
role: str
```

#### **Response**

```json
[
  {
    "id": "uuid",
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "role": "cuidador",
    "registration_date": "2024-02-05T12:00:00"
  },
  {
    "id": "uuid",
    "name": "María López",
    "email": "maria@example.com",
    "role": "cuidador",
    "registration_date": "2024-02-05T12:00:00"
  }
]
```

### 📌 **Editar un usuario**

**PUT** `/user/{id}`

#### **Request Body**

```json
{
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "role": "cuidador"
}
```

#### **Response**

```json
{
  "id": "uuid",
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "role": "cuidador",
  "registration_date": "2024-02-05T12:00:00"
}
```

---

### 📌 **Eliminar un usuario**

**DELETE** `/user/{id}`

#### **Response**

```json
{
  "ok": true
}
```

---

## **2️⃣ Animales** `/animal`

### 📌 **Registrar un animal**

**POST** `/animal/`

#### **Request Body**

```json
{
  "name": "nombre1",
  "species": "Cobaya",
  "sex": "HEMBRA",
  "health_status": "SALUDABLE",
  "weight": 750,
  "date_birth": "2024-02-05", // opcional
  "age": 0,
  "origin": "nacimiento",
  "family": "356A",
  "diet": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos.", // opcional
  "last_observations": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud.", // opcional
  "clinical_signs": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección.", // opcional
  "vaccines": "Rabia, Moquillo, Parvovirus", // opcional
  "parent1_id": "1", // opcional
  "parent2_id": "2", // opcional
  "keeper_id": "c89117c8-00cd-43e2-b163-008254e512e7" // opcional
}
```

#### **Response**

```json
{
  "id": "be0b8b88-a565-4fc6-8c83-f02676966bc2",
  "name": "nombre1",
  "sex": "HEMBRA",
  "species": "Cobaya",
  "health_status": "SALUDABLE"
}
```

### 📌 **Obtener un animal por ID**

**GET** `/animal/detail/{id}`

#### **Response**

```json
{
  "id": "uuid",
  "name": "name1",
  "species": "Cobaya",
  "sex": "HEMBRA",
  "state": "CUIDADO",
  "weight": 750.0,
  "age": 10,
  "origin": "nacimiento",
  "family": "356A",
  "details": {
    "diet": {
      "last_update": "18/02/2024",
      "description": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos."
    },
    "last_observations": {
      "last_update": "20/02/2024",
      "description": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud."
    },
    "clinical_signs": {
      "last_update": "16/02/2024",
      "description": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección."
    },
    "vaccines": {
      "last_update": "14/01/2024",
      "description": "Rabia, Moquillo, Parvovirus"
    }
  },
  "researches": [
    {
      "id": "uuid",
      "title": "Efectos de la dieta en la reproducción de ratones",
      "desciption": "Se estudiará el efecto de la dieta en la reproducción de ratones, con el fin de determinar si la dieta influye en la cantidad de crías.",
      "status": "Abierta"
    },
    {
      "id": "uuid",
      "title": "Efectos de la dieta en la reproducción de ratones",
      "description": "Se estudiará el efecto de la dieta en la reproducción de ratones, con el fin de determinar si la dieta influye en la cantidad de crías.",
      "status": "Cerrada"
    }
  ],
  "procedures": [
    {
      "id": "uuid",
      "title": "Extracción de sangre",
      "desciption": "Toma de muestra para análisis genético",
      "status": "pendiente"
    },
    {
      "id": "uuid",
      "title": "Extracción de sangre",
      "description": "Toma de muestra para análisis genético",
      "status": "cerrado"
    }
  ],
  "parent1_id": "uuid",
  "parent2_id": "uuid",
  "keeper_id": "uuid"
}
```

### 📌 **Obtener todos los animales vivos**

**GET** `/animal/alive`

#### **Response**

```json
[
  {
    "id": "uuid",
    "name": "name1",
    "species": "Raton",
    "sex": "MACHO",
    "health_status": "SALUDABLE"
  },
  {
    "id": "uuid",
    "name": "name2",
    "species": "Cobaya",
    "sex": "HEMBRA",
    "health_status": "CUIDADO"
  }
]
```

### 📌 **Obtener animales de cuidador por userID**

**GET** `/animal/keeper/{user_id}`

#### **Response**

```json
[
  {
    "id": "uuid",
    "name": "name1",
    "species": "Raton",
    "sex": "MACHO",
    "health_status": "SALUDABLE"
  },
  {
    "id": "uuid",
    "name": "name2",
    "species": "Cobaya",
    "sex": "HEMBRA",
    "health_status": "DECESO"
  }
]
```

### 📌 **Obtener animales de investigador por userID**

**GET** `/animal/researcher/{user_id}`

#### **Response**

```json
[
  {
    "id": "uuid",
    "name": "name1",
    "species": "Raton",
    "sex": "MACHO",
    "health_status": "SALUDABLE"
  },
  {
    "id": "uuid",
    "name": "name2",
    "species": "Cobaya",
    "sex": "HEMBRA",
    "health_status": "DECESO"
  }
]
```

### 📌 **Obtener padres y crías por animalID**

**GET** `/animal/family/{animal_id}`

#### **Response**

```json
{
  "parents": {
    "parent1": {
      "id": "uuid",
      "name": "name1",
      "species": "Raton",
      "sex": "MACHO",
      "health_status": "SALUDABLE"
    },
    "padre2": {
      "id": "uuid",
      "name": "name2",
      "species": "Raton",
      "sex": "HEMBRA",
      "health_status": "CUIDADO"
    }
  },
  "offspring": [
    {
      "id": "uuid",
      "name": "name3",
      "species": "Raton",
      "sex": "MACHO",
      "health_status": "SALUDABLE"
    },
    {
      "id": "uuid",
      "name": "name5",
      "species": "Raton",
      "sex": "Hembra",
      "health_status": "DECESO"
    }
  ]
}
```

### Ó

```json
{
  "parents": {
    "parent1": null,
    "parent2": null
  },
  "offspring": [
    {
      "id": "uuid",
      "name": "name3",
      "species": "Raton",
      "sex": "MACHO",
      "health_status": "CUIDADO"
    },
    {
      "id": "uuid",
      "name": "name5",
      "species": "Raton",
      "sex": "HEMBRA",
      "health_status": "DECESO"
    }
  ]
}
```

### 📌 **Actualizar animal**

**PATCH** `/animal/{animal_id}`

#### **Request Body**

```json
{
  "health_status": "CUIDADO", //opcional
  "weight": 750, //opcional
  "age": 10, //opcional
  "diet": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos.", //opcional
  "last_observations": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud.", //opcional
  "clinical_signs": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección.", //opcional
  "vaccines": "Rabia, Moquillo, Parvovirus", //opcional
  "keeper_id": "uuid" //opcional
}
```

#### **Response**

```json
{
  // Misma salida para el caso de GET details
}
```

---

## **3️⃣ Investigaciones** `/research`

### 📌 **Registrar Investigacion**

**POST** `/research/`

#### **Request Body**

```json
{
  "title": "Efectos de la dieta en la reproducción de ratones",
  "description": "Se estudiará el efecto de la dieta en la reproducción de ratones, con el fin de determinar si la dieta influye en la cantidad de crías.",
  "specimen_id": "4a01ab95-32e4-4bde-94d0-8e687d1abb2d",
  "researcher_id": "c89117c8-00cd-43e2-b163-008254e512e7",
  "status": "Abierta"
}
```

#### **Response**

```json
{
  "id": "uuid",
  "title": "Efectos de la dieta en la reproducción de ratones",
  "description": "Se estudiará el efecto de la dieta en la reproducción de ratones, con el fin de determinar si la dieta influye en la cantidad de crías.",
  "specimen_id": "4a01ab95-32e4-4bde-94d0-8e687d1abb2d",
  "researcher_id": "c89117c8-00cd-43e2-b163-008254e512e7",
  "status": "Abierta"
}
```

### 📌 **Actualizar Estado de invesigacion**

**PUT** `/research/{animal_id}`

#### **Request Body**

```json
{
  "status": "Cerrada"
}
```

#### **Response**

```json
[
  {
    "status": "Cerrada"
  }
]
```

---

## **4️⃣ Procedimientos** `/procedure`

### 📌 **Registrar un procedimiento**

**POST** `/procedure/`

#### **Request Body**

```json
{
  "specimen_id": "660e8400-e29b-41d4-a716-556655440001",
  "title": "Vacunación anual",
  "description": "Aplicación de vacuna contra la rabia.",
  "user_id": "550e8400-e29b-41d4-a716-446655440001",
  "status": "Pendiente"
}
```

#### **Response**

```json
{
    "title": "Vacunación anual",
    "description": "Aplicación de vacuna contra la rabia.",
    "specimen_id": "660e8400-e29b-41d4-a716-556655440001",
    "user_id": "550e8400-e29b-41d4-a716-446655440001",
    "status": "Pendiente",
    "id": "d0c24889-5d82-4523-b222-b0c7b033b551"
}
```

### 📌 **Actualizar estado de procedimiento**

**PUT** `/procedure/{id}`

#### **Request Body**

```json
{
  "status": "Hecho"
}
```

#### **Response**

```json
{
  "status": "Hecho"
}
```

### 📌 **Obtener todos los procedimientos de investigador por user_id**

**GET** `/procedure/researcher/{user_id}`

#### **Response**

```json
{
  "id": "uuid",
  "title": "Extracción de sangre",
  "description": "Toma de muestra para análisis genético",
  "status": "pendiente",
  "specimen": { // Falta esto
    "id": "uuid",
    "name": "Nala",
    "sex": "HEMBRA",
    "species": "Panthera leo",
    "health_status": "CUIDADO"
  }
}
```

### 📌 **Obtener todos los procedimientos de investigador por user_id**

**GET** `/procedure/keeper/{user_id}`

#### **Response**

```json
{
  "id": "uuid",
  "title": "Extracción de sangre",
  "description": "Toma de muestra para análisis genético",
  "status": "pendiente",
  "specimen": { // falta esto
    "id": "uuid",
    "species": "Raton",
    "sex": "MACHO",
    "health_status": "SALUDABLE"
  }
}
```

---

## **5️⃣ Solicitudes de Animales** `/request`

### 📌 **Crear una solicitud de animales**

**POST** `/request/`

#### **Request Body**

```json

  {
    "title": "Solicitud de Acceso a León",
    "description": "Requerimos acceso al espécimen Panthera leo para toma de muestras de sangre.",
    "researcher_id": "de69c672-c670-4aab-8b59-5274aac84bd6",
    "keeper_id": "37d4c36e-84e1-438c-b2ef-fbf527d52627",
    "status": "Pendiente"
  }

```

#### **Response**

```json
{
    "title": "Solicitud de Acceso a León",
    "description": "Requerimos acceso al espécimen Panthera leo para toma de muestras de sangre.",
    "researcher_id": "de69c672-c670-4aab-8b59-5274aac84bd6",
    "keeper_id": "37d4c36e-84e1-438c-b2ef-fbf527d52627",
    "status": "Pendiente",
    "id": "c2ae4cac-eb2f-4063-a6b2-1abf7b253ec7"
  }
```

### 📌 **Obtener solicitudes de un investigador**

**GET** `/request/researcher/{user_id}`

#### **Response**

```json
[
    {
        "id": "880e8400-e29b-41d4-a716-777655440009",
        "title": "Solicitud de traslado de espécimen",
        "description": "Solicitud para trasladar un espécimen de jaguar a un hábitat de estudio.",
        "keeper": {
            "id": "550e8400-e29b-41d4-a716-446655440002",
            "name": "María López",
            "email": "maria@example.com",
            "role": "cuidador",
            "registration_date": "2025-02-28T13:22:08.766791"
        },
        "status": "Pendiente"
    },
    {
        "id": "880e8400-e29b-41d4-a716-777655440002",
        "title": "Solicitud de muestra biológica",
        "description": "Solicitud de una muestra de sangre de tortuga marina para análisis genético.",
        "keeper": {
            "id": "550e8400-e29b-41d4-a716-446655440002",
            "name": "María López",
            "email": "maria@example.com",
            "role": "cuidador",
            "registration_date": "2025-02-28T13:22:08.766791"
        },
        "status": "Pendiente"
    }
]
```

### 📌 **Obtener solicitudes de un cuidador**

**GET** `/request/keeper/{user_id}`

#### **Response**

```json
[
    {
        "id": "880e8400-e29b-41d4-a716-777655440009",
        "title": "Solicitud de traslado de espécimen",
        "description": "Solicitud para trasladar un espécimen de jaguar a un hábitat de estudio.",
        "researcher": {
            "id": "550e8400-e29b-41d4-a716-446655440001",
            "name": "Juan Pérez",
            "email": "juan@example.com",
            "role": "investigador",
            "registration_date": "2025-02-28T13:22:08.766791"
        },
        "status": "Pendiente"
    },
    {
        "id": "880e8400-e29b-41d4-a716-777655440002",
        "title": "Solicitud de muestra biológica",
        "description": "Solicitud de una muestra de sangre de tortuga marina para análisis genético.",
        "researcher": {
            "id": "550e8400-e29b-41d4-a716-446655440001",
            "name": "Juan Pérez",
            "email": "juan@example.com",
            "role": "investigador",
            "registration_date": "2025-02-28T13:22:08.766791"
        },
        "status": "Pendiente"
    }
]
```

### 📌 **Actualizar estado de una solicitud**

**PUT** `/request/{id}`

#### **Request Body**

```json
{
    "status": "Hecho"
}
```

#### **Response**

```json
{
    "status": "Hecho"
}
```

---
## **6️⃣ Autenticación** `/auth`

### 📌 **Iniciar sesión**

**POST** `/auth/token`

#### **Request Body**

El endpoint espera datos en formato `application/x-www-form-urlencoded` con los siguientes campos:

- **username**: Correo electrónico del usuario.
- **password**: Contraseña del usuario.

Ejemplo de Request Body:

```
username=juan@example.com&password=password123
```

#### **Response**

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

#### **Ejemplo cURL para iniciar sesión**

```bash
curl -X POST "http://localhost:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=juan@example.com&password=password123"
```


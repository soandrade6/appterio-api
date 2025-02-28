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
  "origin": "nacimiento",
  "family": "356A",
  "diet": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos.", // opcional
  "last_observations": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud.", // opcional
  "clinical_signs": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección.", // opcional
  "vaccines": "Rabia, Moquillo, Parvovirus", // opcional
  "parent1Id": "1", // opcional
  "parent2Id": "2", // opcional
  "keeperId": "c89117c8-00cd-43e2-b163-008254e512e7" // opcional
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
  // Pendiente
  "investigaciones": [
    {
      "id": "uuid",
      "titulo": "Efectos de la dieta en la reproducción de ratones",
      "descripcion": "Se estudiará el efecto de la dieta en la reproducción de ratones, con el fin de determinar si la dieta influye en la cantidad de crías.",
      "estado": "Abierta"
    },
    {
      "id": "uuid",
      "titulo": "Efectos de la dieta en la reproducción de ratones",
      "descripcion": "Se estudiará el efecto de la dieta en la reproducción de ratones, con el fin de determinar si la dieta influye en la cantidad de crías.",
      "estado": "Cerrada"
    }
  ],
  "procedimientos": [
    {
      "id": "uuid",
      "titulo": "Extracción de sangre",
      "descripcion": "Toma de muestra para análisis genético",
      "estado": "pendiente"
    },
    {
      "id": "uuid",
      "titulo": "Extracción de sangre",
      "descripcion": "Toma de muestra para análisis genético",
      "estado": "cerrado"
    }
  ],
  // Fin del pendiente
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
  "health_status": "CUIDADO",
  "weight": 750,
  "age": 10,
  "diet": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos.",
  "last_observations": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud.",
  "clinical_signs": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección.",
  "vaccines": "Rabia, Moquillo, Parvovirus",
  "keeper_id": "uuid"
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

## **4️⃣ Procedimientos** `/procedimientos`

### 📌 **Registrar un procedimiento**

**POST** `/procedimientos/`

#### **Request Body**

```json
{
  "id_animal": "uuid",
  "titulo": "Extracción de sangre",
  "descripcion": "Toma de muestra para análisis genético",
  "estado": "pendiente",
  "investigador_id": "uuid"
}
```

#### **Response**

```json
{
  "id_procedimiento": "uuid",
  "id_animal": "uuid",
  "titulo": "Extracción de sangre",
  "descripcion": "Toma de muestra para análisis genético",
  "estado": "pendiente",
  "investigador_id": "uuid"
}
```

### 📌 **Actualizar estado de procedimiento**

**PUT** `/procedimientos/{procedimiento_id}`

#### **Request Body**

```json
{
  "estado": "Hecho"
}
```

#### **Response**

```json
{
  "estado": "Hecho"
}
```

### 📌 **Obtener todos los procedimientos de investigador por user_id**

**GET** `/procedimientos/investigador/{user_id}`

#### **Response**

```json
{
  "id_procedimiento": "uuid",
  "titulo": "Extracción de sangre",
  "descripcion": "Toma de muestra para análisis genético",
  "estado": "pendiente",
  "specimen": {
    "id": "uuid",
    "species": "Raton",
    "sex": "MACHO"
  }
}
```

### 📌 **Obtener todos los procedimientos de investigador por user_id**

**GET** `/procedimientos/cuidador/{user_id}`

#### **Response**

```json
{
  "id_procedimiento": "uuid",
  "titulo": "Extracción de sangre",
  "descripcion": "Toma de muestra para análisis genético",
  "estado": "pendiente",
  "specimen": {
    "id": "uuid",
    "species": "Raton",
    "sex": "MACHO"
  }
}
```

---

## **5️⃣ Solicitudes de Animales** `/solicitudes`

### 📌 **Crear una solicitud de animales**

**POST** `/solicitudes/`

#### **Request Body**

```json
{
  "titulo": "Nuevo especimen",
  "descripcion": "Se requiere un nuevo especimen para realizar investigaciones",
  "estado": "pendiente",
  "investigador_id": "uuid",
  "cuidador_id": "uuid"
}
```

#### **Response**

```json
{
  "id_solicitud": "uuid",
  "titulo": "Extracción de sangre",
  "descripcion": "Toma de muestra para análisis genético",
  "estado": "pendiente",
  "investigador_id": "uuid",
  "cuidador_id": "uuid"
}
```

### 📌 **Obtener solicitudes de un investigador**

**GET** `/solicitudes/investigador/{user_id}`

#### **Response**

```json
[
  {
    "id_solicitud": "uuid",
    "titulo": "Nuevo especimen",
    "descripcion": "Se requiere un nuevo especimen para realizar investigaciones",
    "estado": "pendiente",
    "cuidador": {
      "id": "uuid",
      "nombre": "Juan Pérez",
      "rol": "cuidador"
    }
  },
  {
    "id_solicitud": "uuid",
    "titulo": "Nuevo especimen",
    "descripcion": "Se requiere un nuevo especimen para realizar investigaciones",
    "estado": "pendiente",
    "cuidador": {
      "id": "uuid",
      "nombre": "María López",
      "rol": "cuidador"
    }
  }
]
```

### 📌 **Obtener solicitudes de un cuidador**

**GET** `/solicitudes/cuidador/{user_id}`

#### **Response**

```json
[
  {
    "id_solicitud": "uuid",
    "titulo": "Nuevo especimen",
    "descripcion": "Se requiere un nuevo especimen para realizar investigaciones",
    "estado": "pendiente",
    "investigador": {
      "id": "uuid",
      "nombre": "Juan Pérez",
      "rol": "cuidador"
    }
  },
  {
    "id_solicitud": "uuid",
    "titulo": "Nuevo especimen",
    "descripcion": "Se requiere un nuevo especimen para realizar investigaciones",
    "estado": "pendiente",
    "investigador": {
      "id": "uuid",
      "nombre": "María López",
      "rol": "cuidador"
    }
  }
]
```

### 📌 **Actualizar estado de una solicitud**

**PUT** `/solicitudes/{solicitud_id}`

#### **Request Body**

```json
{
  "estado": "Hecho"
}
```

#### **Response**

```json
{
  "id_solicitud": "uuid",
  "estado": "Hecho"
}
```

---

## **6️⃣ Autenticación** `/auth`

### 📌 **Iniciar sesión**

**POST** `/auth/login`

#### **Request Body**

```json
{
  "email": "juan@example.com",
  "contraseña": "password123"
}
```

#### **Response**

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

### 📌 **Obtener usuario autenticado**

**GET** `/auth/me`

#### **Response**

```json
{
  "id_usuario": "uuid",
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "rol": "cuidador"
}
```

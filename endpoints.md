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
  "specie": "Cobaya",
  "sex": "Hembra",
  "health_status": "SALUDABLE",
  "weight": 750,
  "date_birth": "2024-02-05",
  "origin": "nacimiento",
  "family": "356A",
  "diet": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos.",
  "last_observations": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud.",
  "clinical_signs": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección.",
  "vaccines": "Rabia, Moquillo, Parvovirus",
  "parent1Id": "1",
  "parent2Id": "2",
  "keeperId": "c89117c8-00cd-43e2-b163-008254e512e7" #opcional
}
```

#### **Response**

```json
{
   "id": "be0b8b88-a565-4fc6-8c83-f02676966bc2",
   "name": "nombre1",
   "specie": "Cobaya"
}
```

### 📌 **Obtener un animal por ID**

**GET** `/animal/detalle/{id}`

#### **Response**

```json
{
  "id": "uuid",
  "species": "Cobaya",
  "sex": "Hembra",
  "state": "CUIDADO",
  "weight": 750,
  "age": 10,
  "origin": "nacimiento",
  "family": "356A",
  "details": {
    "dieta": {
      "lastUpdate": "18/02/2024",
      "description": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos."
    },
    "ultimasObservaciones": {
      "lastUpdate": "20/02/2024",
      "description": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud."
    },
    "signosClinicos": {
      "lastUpdate": "16/02/2024",
      "description": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección."
    },
    "vacunas": {
      "lastUpdate": "14/01/2024",
      "description": "Rabia, Moquillo, Parvovirus"
    }
  },
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
  "parent1Id": 1,
  "parent2Id": 2,
  "keeperId": 1
}
```

### 📌 **Obtener todos los animales vivos**

**GET** `/animal/alive`

#### **Response**

```json
[
  {
    "id": "uuid",
    "species": "Raton",
    "sex": "MACHO",
    "state": "SALUDABLE"
  },
  {
    "id": "uuid",
    "species": "Cobaya",
    "sex": "Hembra",
    "state": "ENFERMO"
  }
]
```

### 📌 **Obtener animales de cuidador por userID**

**GET** `/animal/cuidador/{user_id}`

#### **Request Body**

```json
{
  "uesr_id": "uuid"
}
```

#### **Response**

```json
[
  {
    "id": "uuid",
    "species": "Raton",
    "sex": "MACHO",
    "state": "SALUDABLE"
  },
  {
    "id": "uuid",
    "species": "Cobaya",
    "sex": "Hembra",
    "state": "DESCESO"
  }
]
```

### 📌 **Obtener animales de investigador por userID**

**GET** `/animal/investigador/{user_id}`

#### **Request Body**

```json
{
  "uesr_id": "uuid"
}
```

#### **Response**

```json
[
  {
    "id": "uuid",
    "species": "Raton",
    "sex": "MACHO",
    "state": "SALUDABLE"
  },
  {
    "id": "uuid",
    "species": "Cobaya",
    "sex": "Hembra",
    "state": "DESCESO"
  }
]
```

### 📌 **Obtener padres y crías por animalID**

**GET** `/animales/familia/{animal_id}`

#### **Request Body**

```json
{
  "animal_id": "uuid"
}
```

#### **Response**

```json
{
  "padres": {
    "padre1": {
      "id": "uuid",
      "species": "Raton",
      "sex": "MACHO",
      "state": "SALUDABLE"
    },
    "padre2": {
      "id": "uuid",
      "species": "Raton",
      "sex": "Hembra",
      "state": "DESCESO"
    }
  },
  "crias": [
    {
      "id": "uuid",
      "species": "Raton",
      "sex": "MACHO",
      "state": "SALUDABLE"
    },
    {
      "id": "uuid",
      "species": "Raton",
      "sex": "Hembra",
      "state": "DESCESO"
    }
  ]
}
```

### Ó

```json
{
  "padres": {},
  "crias": [
    {
      "id": "uuid",
      "species": "Raton",
      "sex": "MACHO",
      "state": "SALUDABLE"
    },
    {
      "id": "uuid",
      "species": "Raton",
      "sex": "Hembra",
      "state": "DESCESO"
    }
  ]
}
```

### 📌 **Actualizar animal**

**PUT** `/animales/{animal_id}`

#### **Request Body**

```json
{
  "id": "uuid",
  "state": "ENFERMO",
  "weight": 750,
  "age": 10,
  "dieta": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos.",
  "ultimasObservaciones": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud.",
  "signosClinicos": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección.",
  "vacunas": "Rabia, Moquillo, Parvovirus",
  "keeperId": 1
}
```

#### **Response**

```json
{
  "id": "uuid",
  "state": "ENFERMO",
  "weight": 750,
  "age": 10,
  "dieta": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos.",
  "ultimasObservaciones": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud.",
  "signosClinicos": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección.",
  "vacunas": "Rabia, Moquillo, Parvovirus",
  "keeperId": 1
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

**PUT** `/investigacion/{animal_id}`

#### **Request Body**

```json
{
  "estado": "Cerrada"
}
```

#### **Response**

```json
[
  {
    "estado": "Abierta"
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

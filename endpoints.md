Endpoints que expondrá la API y ejemplos de uso

---

## **1️⃣ Usuarios** `/usuarios`

### 📌 **Crear un usuario**

**POST** `/usuarios/`

#### **Request Body**

```json
{
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "contrasena": "password123",
  "rol": "cuidador"
}
```

#### **Response**

```json
{
  "id_usuario": "uuid",
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "rol": "cuidador",
  "fecha_registro": "2024-02-05T12:00:00"
}
```

### 📌 **Obtener un usuario por ID**

**GET** `/usuarios/{user_id}`

#### **Response**

```json
{
  "id_usuario": "uuid",
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "rol": "cuidador",
  "fecha_registro": "2024-02-05T12:00:00"
}
```

### 📌 **Obtener todos los usuarios**

**GET** `/usuarios/`

#### **Response**

```json
[
  {
    "id_usuario": "uuid",
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "rol": "cuidador",
    "fecha_registro": "2024-02-05T12:00:00"
  },
  {
    "id_usuario": "uuid",
    "nombre": "María López",
    "email": "maria@example.com",
    "rol": "investigador",
    "fecha_registro": "2024-02-05T12:00:00"
  }
]
```

### 📌 **Obtener todos los investigadores**

**GET** `/usuarios/investigadores`

#### **Response**

```json
[
  {
    "id_usuario": "uuid",
    "nombre": "Juan Pérez",
    "rol": "investigador",
  },
  {
    "id_usuario": "uuid",
    "nombre": "María López",
    "rol": "investigador",
  }
]
```

### 📌 **Obtener todos los cuidadores**

**GET** `/usuarios/cuidadores`

#### **Response**

```json
[
  {
    "id_usuario": "uuid",
    "nombre": "Juan Pérez",
    "rol": "cuidador",
  },
  {
    "id_usuario": "uuid",
    "nombre": "María López",
    "rol": "cuidador",
  }
]
```

### 📌 **Editar un usuario**

**PUT** `/usuarios/{user_id}`

#### **Request Body**

```json
{
  "id_usuario": "uuid",
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "contrasena": "password123",
  "rol": "cuidador"
}
```

#### **Response**

```json
{
  "id_usuario": "uuid",
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "rol": "cuidador",
  "fecha_registro": "2024-02-05T12:00:00"
}
```

---

## **2️⃣ Animales** `/animales`

### 📌 **Registrar un animal**

**POST** `/animales/`

#### **Request Body**

```json
{
  "id": "uuid",
  "species": "Cobaya",
  "sex": "Hembra",
  "state": "SALUDABLE",
  "weight": 750,
  "age": 10,
  "origin": "nacimiento",
  "family": "356A",
  "dieta": "Dieta controlada con base en pellets comerciales, con un refuerzo de proteínas mediante el suministro ocasional de insectos secos.",
  "ultimasObservaciones": "Se observa mayor actividad nocturna y una leve reducción en el consumo de alimento. Se continuará monitoreando para detectar posibles cambios en la salud.",
  "signosClinicos": "Estado general saludable. Se observó una pequeña pérdida de pelo en la zona dorsal, sin signos de infección.",
  "vacunas": "Rabia, Moquillo, Parvovirus",
  "parent1Id": 1,
  "parent2Id": 2,
  "keeperId": 1
}
```

#### **Response**

```json
{
  "id_animal": "uuid",
  "nombre": "Ratón A",
  "especie": "Mus musculus"
}
```

### 📌 **Obtener un animal por ID**

**GET** `/animales/detalle/{animal_id}`

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

**GET** `/animales/vivos`

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

**GET** `/animales/cuidador/{user_id}`

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

**GET** `/animales/investigador/{user_id}`

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

### 📌 **Obtener padres y crias por animalID**

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

## **3️⃣ Investigaciones** `/Investigaciones`

### 📌 **Registrar Investigacion**

**POST** `/investigacion/`

#### **Request Body**

```json
{
  "titulo": "Efectos de la dieta en la reproducción de ratones",
  "descripcion": "Se estudiará el efecto de la dieta en la reproducción de ratones, con el fin de determinar si la dieta influye en la cantidad de crías.",
  "especimen_id": "uuid",
  "investigador_id": "uuid",
  "estado": "Abierta"
}
```

#### **Response**

```json
{
  "titulo": "Efectos de la dieta en la reproducción de ratones",
  "descripcion": "Se estudiará el efecto de la dieta en la reproducción de ratones, con el fin de determinar si la dieta influye en la cantidad de crías.",
  "especimen_id": "uuid",
  "investigador_id": "uuid",
  "estado": "Abierta"
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

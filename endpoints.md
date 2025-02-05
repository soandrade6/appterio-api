Posibles endpoints que podría tener la API

---

## **1️⃣ Usuarios** `/usuarios`

### 📌 **Crear un usuario**
**POST** `/usuarios/`

#### **Request Body**
```json
{
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "contraseña": "password123",
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

---

## **2️⃣ Animales** `/animales`

### 📌 **Registrar un animal**
**POST** `/animales/`

#### **Request Body**
```json
{
  "nombre": "Ratón A",
  "especie": "Mus musculus",
  "identificador_unico": "12345",
  "estado_salud": "Saludable",
  "peso": 25.3,
  "fecha_nacimiento": "2023-12-01",
  "origen": "Bioterio local",
  "id_cuidador": "uuid"
}
```

#### **Response**
```json
{
  "id_animal": "uuid",
  "nombre": "Ratón A",
  "especie": "Mus musculus",
  "estado_salud": "Saludable"
}
```

### 📌 **Obtener un animal por ID**
**GET** `/animales/{animal_id}`

#### **Response**
```json
{
  "id_animal": "uuid",
  "nombre": "Ratón A",
  "especie": "Mus musculus",
  "estado_salud": "Saludable"
}
```

---

## **3️⃣ Historial Clínico** `/historial`

### 📌 **Registrar historial clínico**
**POST** `/historial/`

#### **Request Body**
```json
{
  "id_animal": "uuid",
  "detalle": "Peso revisado, sin anomalías",
  "registrado_por": "uuid"
}
```

#### **Response**
```json
{
  "id_historial": "uuid",
  "fecha_registro": "2024-02-05T12:00:00",
  "detalle": "Peso revisado, sin anomalías"
}
```

### 📌 **Obtener historial clínico de un animal**
**GET** `/historial/{animal_id}`

#### **Response**
```json
[
  {
    "id_historial": "uuid",
    "fecha_registro": "2024-02-05T12:00:00",
    "detalle": "Peso revisado, sin anomalías"
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
  "id_investigador": "uuid",
  "tipo_procedimiento": "Extracción de sangre",
  "descripcion": "Toma de muestra para análisis genético",
  "estado": "pendiente"
}
```

#### **Response**
```json
{
  "id_procedimiento": "uuid",
  "tipo_procedimiento": "Extracción de sangre",
  "estado": "pendiente"
}
```

### 📌 **Obtener procedimiento por ID**
**GET** `/procedimientos/{procedimiento_id}`

#### **Response**
```json
{
  "id_procedimiento": "uuid",
  "tipo_procedimiento": "Extracción de sangre",
  "estado": "pendiente"
}
```

---

## **5️⃣ Solicitudes de Animales** `/solicitudes`

### 📌 **Crear una solicitud de animales**
**POST** `/solicitudes/`

#### **Request Body**
```json
{
  "id_investigador": "uuid",
  "especie_requerida": "Mus musculus",
  "cantidad": 10
}
```

#### **Response**
```json
{
  "id_solicitud": "uuid",
  "especie_requerida": "Mus musculus",
  "cantidad": 10,
  "estado": "pendiente"
}
```

### 📌 **Obtener solicitudes de un investigador**
**GET** `/solicitudes/{investigador_id}`

#### **Response**
```json
[
  {
    "id_solicitud": "uuid",
    "especie_requerida": "Mus musculus",
    "cantidad": 10,
    "estado": "pendiente"
  }
]
```

### 📌 **Actualizar estado de una solicitud**
**PUT** `/solicitudes/{solicitud_id}`

#### **Request Body**
```json
{
  "estado": "aprobada"
}
```

#### **Response**
```json
{
  "id_solicitud": "uuid",
  "estado": "aprobada"
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



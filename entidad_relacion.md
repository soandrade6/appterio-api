### **Esquema Entidad-Relación para AppTerio**  
---

## **1. Entidades**  

### **Usuarios (`usuarios`)**  
- **PK:** `id_usuario` (`UUID`)  
- `nombre` (`STRING`)  
- `email` (`STRING`, `UNIQUE`)  
- `contrasena` (`STRING`, `HASHED`)  
- `rol` (`ENUM` → 'cuidador', 'investigador', 'administrador')  
- `fecha_registro` (`DATETIME`)  

---

### **Animales (`animales`)**  
- **PK:** `id_animal` (`UUID`)  
- `nombre` (`STRING`)  
- `especie` (`STRING`)  
- `identificador_unico` (`STRING`, `UNIQUE`)  
- `estado_salud` (`STRING`)  
- `peso` (`FLOAT`)  
- `fecha_nacimiento` (`DATE`)  
- `origen` (`STRING`)  *(nacido en bioterio o adquirido de otro laboratorio)*  
- `id_cuidador` (`UUID`, FK → `usuarios.id_usuario`, NULLABLE)   

---

### **Historial Clínico (`historial_clinico`)**  
- **PK:** `id_historial` (`UUID`)  
- `id_animal` (`UUID`, FK → `animales.id_animal`)  
- `fecha_registro` (`DATETIME`)  
- `detalle` (`TEXT`)  
- `registrado_por` (`UUID`, FK → `usuarios.id_usuario`)  

---

### **Procedimientos (`procedimientos`)**  
- **PK:** `id_procedimiento` (`UUID`)  
- `id_animal` (`UUID`, FK → `animales.id_animal`)  
- `id_investigador` (`UUID`, FK → `usuarios.id_usuario`)  
- `tipo_procedimiento` (`STRING`)  
- `descripcion` (`TEXT`)  
- `estado` (`ENUM` → 'pendiente', 'en curso', 'completado')  
- `fecha_asignacion` (`DATETIME`)  
- `fecha_finalizacion` (`DATETIME`, NULLABLE)  

---

### **Solicitudes de Animales (`solicitudes_animales`)**  
- **PK:** `id_solicitud` (`UUID`)  
- `id_investigador` (`UUID`, FK → `usuarios.id_usuario`)  
- `especie_requerida` (`STRING`)  
- `cantidad` (`INTEGER`)  
- `estado` (`ENUM` → 'pendiente', 'aprobada', 'rechazada')  
- `fecha_solicitud` (`DATETIME`)  
- `fecha_resolucion` (`DATETIME`, NULLABLE)  
- `id_cuidador_responsable` (`UUID`, FK → `usuarios.id_usuario`, NULLABLE)   

---

### **Datos Experimentales (`datos_experimentales`)**  
- **PK:** `id_experimento` (`UUID`)  
- `id_animal` (`UUID`, FK → `animales.id_animal`)  
- `id_investigador` (`UUID`, FK → `usuarios.id_usuario`)  
- `tipo_dato` (`STRING`)  
- `valor` (`TEXT`)  
- `fecha_registro` (`DATETIME`)  

---

### **Gestión de Usuarios y Roles (`roles_usuarios`)**  
- **PK:** `id_rol` (`UUID`)  
- `nombre_rol` (`ENUM` → 'cuidador', 'investigador', 'administrador')  
- `descripcion` (`TEXT`)  

---

### **Registro de Actividades (`actividades`)**  
- **PK:** `id_actividad` (`UUID`)  
- `id_usuario` (`UUID`, FK → `usuarios.id_usuario`)  
- `tipo_actividad` (`STRING`)  
- `fecha_actividad` (`DATETIME`)  

---

## **2. Relaciones**  

| Relación | Tipo |
|----------|------|
| `usuarios` 1 → N `animales` (un cuidador puede manejar múltiples animales) |
| `usuarios` 1 → N `procedimientos` (un investigador puede asignar múltiples procedimientos) |
| `usuarios` 1 → N `solicitudes_animales` (un investigador puede hacer múltiples solicitudes) |
| `usuarios` 1 → N `actividades` (un usuario puede generar múltiples actividades en el sistema) |
| `animales` 1 → N `historial_clinico` (un animal puede tener múltiples registros clínicos) |
| `animales` 1 → N `procedimientos` (un animal puede tener múltiples procedimientos) |
| `animales` 1 → N `datos_experimentales` (un animal puede tener múltiples datos experimentales) |
| `procedimientos` N → 1 `usuarios` (múltiples procedimientos pueden ser asignados por un investigador) |
| `procedimientos` N → 1 `animales` (un animal puede tener múltiples procedimientos) |
| `solicitudes_animales` 1 → 1 `usuarios` (un cuidador puede aceptar/rechazar una solicitud) |
| `solicitudes_animales` N → 1 `usuarios` (un investigador puede hacer múltiples solicitudes) |
| `datos_experimentales` N → 1 `animales` (un animal puede tener múltiples datos experimentales) |
| `datos_experimentales` N → 1 `usuarios` (un investigador puede registrar múltiples datos) |
| `roles_usuarios` 1 → N `usuarios` (un rol puede ser asignado a múltiples usuarios) |
| `actividades` N → 1 `usuarios` (un usuario puede generar múltiples actividades) |

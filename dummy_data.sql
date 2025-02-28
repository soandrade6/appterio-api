-- Insert Users
INSERT INTO "user" (id, name, email, password, role, registration_date) VALUES
  ('550e8400-e29b-41d4-a716-446655440001', 'Juan Pérez', 'juan@example.com', 'hashed_password', 'investigador', NOW()),
  ('550e8400-e29b-41d4-a716-446655440002', 'María López', 'maria@example.com', 'hashed_password', 'cuidador', NOW()),
  ('550e8400-e29b-41d4-a716-446655440003', 'Carlos Ramírez', 'carlos@example.com', 'hashed_password', 'investigador', NOW()),
  ('550e8400-e29b-41d4-a716-446655440004', 'Ana Torres', 'ana@example.com', 'hashed_password', 'investigador', NOW()),
  ('550e8400-e29b-41d4-a716-446655440005', 'Luis Gómez', 'luis@example.com', 'hashed_password', 'cuidador', NOW()),
  ('550e8400-e29b-41d4-a716-446655440006', 'Sofía Herrera', 'sofia@example.com', 'hashed_password', 'investigador', NOW()),
  ('550e8400-e29b-41d4-a716-446655440007', 'Fernando Díaz', 'fernando@example.com', 'hashed_password', 'cuidador', NOW());

-- Insert Animals
INSERT INTO "animal" (id, name, specie, health_status, weight, date_birth, origin, family, diet, last_observations, clinical_signs, vaccines, parent1_id, parent2_id, keeper_id) VALUES
  ('660e8400-e29b-41d4-a716-556655440001', 'Simba', 'León', 'Saludable', 190.5, '2018-05-12', 'África', 'Felidae', 'Carnívoro', 'Ninguna', 'Ninguno', 'Rabia', 'Desconocido', 'Desconocido', '550e8400-e29b-41d4-a716-446655440001'),
  ('660e8400-e29b-41d4-a716-556655440002', 'Dumbo', 'Elefante', 'En tratamiento', 500.0, '2015-08-22', 'Asia', 'Elephantidae', 'Herbívoro', 'Revisión médica reciente', 'Ligera cojera', 'Fiebre Aftosa', 'Desconocido', 'Desconocido', '550e8400-e29b-41d4-a716-446655440002'),
  ('660e8400-e29b-41d4-a716-556655440003', 'Rocky', 'Tigre', 'Saludable', 220.3, '2017-09-10', 'India', 'Felidae', 'Carnívoro', 'Ninguna', 'Ninguno', 'Rabia', 'Desconocido', 'Desconocido', '550e8400-e29b-41d4-a716-446655440005'),
  ('660e8400-e29b-41d4-a716-556655440004', 'Luna', 'Lobo', 'Recuperado', 60.0, '2019-01-15', 'América', 'Canidae', 'Carnívoro', 'Seguimiento post tratamiento', 'Ninguno', 'Moquillo', 'Desconocido', 'Desconocido', '550e8400-e29b-41d4-a716-446655440007'),
  ('660e8400-e29b-41d4-a716-556655440005', 'Coco', 'Mono', 'Saludable', 15.2, '2020-02-05', 'Brasil', 'Cebidae', 'Omnívoro', 'Activo y juguetón', 'Ninguno', 'Hepatitis', 'Desconocido', 'Desconocido', '550e8400-e29b-41d4-a716-446655440001'),
  ('660e8400-e29b-41d4-a716-556655440006', 'Max', 'Perro', 'Observación', 25.3, '2018-11-11', 'México', 'Canidae', 'Carnívoro', 'Leve desnutrición', 'Bajo peso', 'Rabia', 'Desconocido', 'Desconocido', '550e8400-e29b-41d4-a716-446655440002'),
  ('660e8400-e29b-41d4-a716-556655440007', 'Toby', 'Gato', 'Saludable', 6.5, '2021-06-30', 'España', 'Felidae', 'Carnívoro', 'Muy activo', 'Ninguno', 'Leucemia Felina', 'Desconocido', 'Desconocido', '550e8400-e29b-41d4-a716-446655440005');

-- Insert Researches
INSERT INTO "research" (id, title, description, specimen_id, researcher_id, status) VALUES
  ('770e8400-e29b-41d4-a716-666655440001', 'Estudio sobre alimentación en leones', 'Análisis de la dieta y salud de los leones en cautiverio.', '660e8400-e29b-41d4-a716-556655440001', '550e8400-e29b-41d4-a716-446655440003', 'Abierta'),
  ('770e8400-e29b-41d4-a716-666655440002', 'Comportamiento de elefantes', 'Estudio del impacto del hábitat en el comportamiento.', '660e8400-e29b-41d4-a716-556655440002', '550e8400-e29b-41d4-a716-446655440004', 'Abierta');

-- Insert Procedures
INSERT INTO "procedure" (id, title, description, specimen_id, user_id, status) VALUES
  ('880e8400-e29b-41d4-a716-777655440001', 'Vacunación anual', 'Aplicación de vacuna contra la rabia.', '660e8400-e29b-41d4-a716-556655440001', '550e8400-e29b-41d4-a716-446655440001', 'Pendiente'),
  ('880e8400-e29b-41d4-a716-777655440002', 'Control de peso', 'Monitoreo del peso del elefante Dumbo.', '660e8400-e29b-41d4-a716-556655440002', '550e8400-e29b-41d4-a716-446655440002', 'Pendiente');

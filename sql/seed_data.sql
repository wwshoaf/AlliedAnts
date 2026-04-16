/*
Seed realistic sample data
sql/seed_data.sql · fits schema.sql · 10+ rows per table where applicable
*/

INSERT INTO Person (name, phone, email) VALUES
  ('Emily Smith',    '3045550101', 'emily.smith@alliedants.com'),
  ('David Johnson',  '1115550102', 'david.johnson@alliedants.com'),
  ('Sophia Lee',     '4125550103', 'sophia.lee@alliedants.com'),
  ('Michael Brown',  '3015550104', 'michael.brown@alliedants.com'),
  ('Olivia Davis',   '3055550105', 'olivia.davis@alliedants.com'),
  ('Jordan Mills',   '3045550201', 'jordan.mills@gmail.com'),
  ('Alex Turner',    '1165550202', 'alex.turner@gmail.com'),
  ('Priya Patel',    '5525550203', 'priya.patel@gmail.com'),
  ('Sam Nguyen',     '1805550204', 'sam.nguyen@gmail.com'),
  ('Chloe Anderson', '4125550205', 'chloe.anderson@gmail.com'),
  ('Malik Johnson',  '3045550206', 'malik.johnson@gmail.com'),
  ('Elena Vasquez',  '9015550207', 'elena.vasquez@gmail.com'),
  ('Ryan OBrien',    '6875550208', 'ryan.obrien@gmail.com'),
  ('Fatima Hassan',  '6795550209', 'fatima.hassan@gmail.com'),
  ('Tyler Brooks',   '9995550210', 'tyler.brooks@gmail.com');

INSERT INTO Teacher (name, phone, number_of_classes_taught) VALUES
  ('Emily Smith',   '3045550101', 5),
  ('David Johnson', '1115550102', 4),
  ('Sophia Lee',    '4125550103', 6),
  ('Michael Brown', '3015550104', 3),
  ('Olivia Davis',  '3055550105', 7);

INSERT INTO Customer (name, phone, payment_method) VALUES
  ('Jordan Mills',   '3045550201', 'annual'),
  ('Alex Turner',    '1165550202', 'monthly'),
  ('Priya Patel',    '5525550203', 'annual'),
  ('Sam Nguyen',     '1805550204', 'annual'),
  ('Chloe Anderson', '4125550205', 'monthly'),
  ('Malik Johnson',  '3045550206', 'annual'),
  ('Elena Vasquez',  '9015550207', 'monthly'),
  ('Ryan OBrien',    '6875550208', 'monthly'),
  ('Fatima Hassan',  '6795550209', 'annual'),
  ('Tyler Brooks',   '9995550210', 'monthly');

INSERT INTO Class (date, time, class_type, duration, attendance) VALUES
  ('2024-01-10', '09:00:00', 'Yoga',          60, 20),
  ('2024-01-11', '10:30:00', 'Pilates',       45, 18),
  ('2024-01-12', '12:00:00', 'Zumba',         30, 22),
  ('2024-01-13', '14:00:00', 'Spin',          60, 15),
  ('2024-01-14', '16:00:00', 'HIIT',          45, 25),
  ('2024-01-15', '18:00:00', 'Boxing',        30, 19),
  ('2024-01-16', '19:30:00', 'CrossFit',      60, 21),
  ('2024-01-17', '08:00:00', 'Barre',         45, 23),
  ('2024-01-18', '11:00:00', 'Dance Cardio',  30, 17);

INSERT INTO PersonClass (name, phone, date, time) VALUES
  -- Teachers linked to the classes they instruct
  ('Emily Smith',   '3045550101', '2024-01-10', '09:00:00'),
  ('David Johnson', '1115550102', '2024-01-11', '10:30:00'),
  ('Sophia Lee',    '4125550103', '2024-01-12', '12:00:00'),
  ('Michael Brown', '3015550104', '2024-01-13', '14:00:00'),
  ('Olivia Davis',  '3055550105', '2024-01-14', '16:00:00'),
  ('Emily Smith',   '3045550101', '2024-01-15', '18:00:00'),
  ('David Johnson', '1115550102', '2024-01-16', '19:30:00'),
  ('Sophia Lee',    '4125550103', '2024-01-17', '08:00:00'),
  ('Michael Brown', '3015550104', '2024-01-18', '11:00:00'),
  -- Customers attending classes
  ('Jordan Mills',   '3045550201', '2024-01-10', '09:00:00'),
  ('Alex Turner',    '1165550202', '2024-01-10', '09:00:00'),
  ('Priya Patel',    '5525550203', '2024-01-11', '10:30:00'),
  ('Sam Nguyen',     '1805550204', '2024-01-12', '12:00:00'),
  ('Chloe Anderson', '4125550205', '2024-01-14', '16:00:00'),
  ('Malik Johnson',  '3045550206', '2024-01-16', '19:30:00'),
  ('Elena Vasquez',  '9015550207', '2024-01-17', '08:00:00'),
  ('Ryan OBrien',    '6875550208', '2024-01-15', '18:00:00'),
  ('Fatima Hassan',  '6795550209', '2024-01-13', '14:00:00'),
  ('Tyler Brooks',   '9995550210', '2024-01-18', '11:00:00');

INSERT INTO Sale (transaction_id, name, phone, date, time, price) VALUES
  (1,  'Jordan Mills',   '3045550201', '2024-01-10', '09:00:00', 199.99),
  (2,  'Alex Turner',    '1165550202', '2024-01-11', '10:30:00', 500.00),
  (3,  'Priya Patel',    '5525550203', '2024-01-12', '12:00:00',  18.99),
  (4,  'Sam Nguyen',     '1805550204', '2024-01-13', '14:00:00',  18.99),
  (5,  'Chloe Anderson', '4125550205', '2024-01-14', '16:00:00',  15.00),
  (6,  'Malik Johnson',  '3045550206', '2024-01-15', '18:00:00',  20.00),
  (7,  'Elena Vasquez',  '9015550207', '2024-01-16', '19:30:00', 500.00),
  (8,  'Ryan OBrien',    '6875550208', '2024-01-17', '08:00:00',  22.99),
  (9,  'Fatima Hassan',  '6795550209', '2024-01-18', '11:00:00',  23.00),
  (10, 'Tyler Brooks',   '9995550210', '2024-01-10', '09:00:00',  45.00);

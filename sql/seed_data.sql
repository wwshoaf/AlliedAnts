/* 
Seed realistic sample data
sql/seed.sql · reuse data from previous artifacts · 10+ rows per table
*/

INSERT INTO Person (person_id, first_name, last_name, email, phone) VALUES
  (1,  'Emily',    'Smith',     'emily.smith@alliedants.com',    '304-555-0101'),
  (2,  'David',    'Johnson',   'david.johnson@alliedants.com',  '111-555-0102'),
  (3,  'Sophia',   'Lee',       'sophia.lee@alliedants.com',     '412-555-0103'),
  (4,  'Michael',  'Brown',     'michael.brown@alliedants.com',  '301-555-0104'),
  (5,  'Olivia',   'Davis',     'olivia.davis@alliedants.com',   '305-555-0105'),
  (6,  'Jordan',   'Mills',     'jordan.mills@gmail.com',        '304-555-0201'),
  (7,  'Alex',     'Turner',    'alex.turner@gmail.com',         '116-555-0202'),
  (8,  'Priya',    'Patel',     'priya.patel@gmail.com',         '552-555-0203'),
  (9,  'Sam',      'Nguyen',    'sam.nguyen@gmail.com',          '180-555-0204'),
  (10, 'Chloe',    'Anderson',  'chloe.anderson@gmail.com',      '412-555-0205'),
  (11, 'Malik',    'Johnson',   'malik.johnson@gmail.com',       '304-555-0206'),
  (12, 'Elena',    'Vasquez',   'elena.vasquez@gmail.com',       '901-555-0207'),
  (13, 'Ryan',     'OBrien',    'ryan.obrien@gmail.com',         '687-555-0208'),
  (14, 'Fatima',   'Hassan',    'fatima.hassan@gmail.com',       '679-555-0209'),
  (15, 'Tyler',    'Brooks',    'tyler.brooks@gmail.com',        '999-555-0210');

INSERT INTO Teacher (teacher_id, person_id, hire_date, classes_taught) VALUES
  (1, 1, '2020-03-15', 5),
  (2, 2, '2021-06-01', 4),
  (3, 3, '2019-09-10', 6),
  (4, 4, '2022-01-20', 3),
  (5, 5, '2023-04-05', 7);

INSERT INTO Customer (customer_id, person_id, payment_method) VALUES
  (1,  6,  'annual'),
  (2,  7,  'monthly'),
  (3,  8,  'annual'),
  (4,  9,  'annual'),
  (5,  10, 'monthly'),
  (6,  11, 'annual'),
  (7,  12, 'monthly'),
  (8,  13, 'monthly'),
  (9,  14, 'annual'),
  (10, 15, 'monthly');

INSERT INTO Class (date, time, duration, class_type, teacher_id, attendance) VALUES
    ('2024-01-10', '09:00:00', 60, 'Yoga', 101, 20),
    ('2024-01-11', '10:30:00', 45, 'Pilates', 102, 18),
    ('2024-01-12', '12:00:00', 30, 'Zumba', 103, 22),
    ('2024-01-13', '14:00:00', 60, 'Spin', 104, 15),
    ('2024-01-14', '16:00:00', 45, 'HIIT', 105, 25),
    ('2024-01-15', '18:00:00', 30, 'Boxing', 106, 19),
    ('2024-01-16', '19:30:00', 60, 'CrossFit', 107, 21),
    ('2024-01-17', '08:00:00', 45, 'Barre', 108, 23),
    ('2024-01-18', '11:00:00', 30, 'Dance Cardio', 109, 17);

INSERT INTO Sale (date, type, price, payment_method) VALUES
    ('2024-01-10', 'retail', 199.99, 'credit'),
    ('2024-01-11', 'membership', 500.00, 'debit'),
    ('2024-01-12', 'class', 18.99, 'cash'),
    ('2024-01-13', 'class', 18.99, 'credit'),
    ('2024-01-14', 'rental', 15.00, 'debit');
    ('2024-01-15', 'retail', 20.00, 'cash'),
    ('2024-01-16', 'membership', 500.00, 'credit'),
    ('2024-01-17', 'class', 22.99, 'debit'),
    ('2024-01-18', 'class', 23.00, 'cash');
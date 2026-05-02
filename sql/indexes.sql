/* Create non-primary indexes */
-- Drop index to see before an after
DROP INDEX idx_teacher_classes ON Teacher;

-- Check performance by running EXPLAIN before index
EXPLAIN SELECT name, phone, number_of_classes_taught
FROM Teacher
ORDER BY number_of_classes_taught DESC;

-- Index on Teacher.number_of_classes_taught
CREATE INDEX idx_teacher_classes
ON Teacher(number_of_classes_taught);

-- Check performance by running EXPLAIN after index
EXPLAIN SELECT name, phone, number_of_classes_taught
FROM Teacher
ORDER BY number_of_classes_taught DESC;

-- Show the index
SHOW INDEX FROM Teacher;
-- /*
-- Write views, stored procedure/trigger, and transaction
-- sql/views.sql · sql/procedures.sql · trigger: auto-update classes taught
-- */

DROP VIEW IF EXISTS ActiveEnrollments;
DROP VIEW IF EXISTS CustomerPurchaseHistory;
DROP VIEW IF EXISTS TeacherSchedule;

-- View 1: active enrollments
-- show all current student-class pairings with details
-- use in enrollment page and attendance reports
CREATE VIEW ActiveEnrollments AS
SELECT
    pc.name,
    pc.phone,
    p.email,
    c.class_type,
    pc.pc_date,
    pc.pc_time,
    c.duration,
    c.attendance
FROM personclass pc
JOIN person p ON pc.name = p.name AND pc.phone = p.phone
JOIN class c ON pc.pc_date = c.class_date AND pc.pc_time = c.class_time;


-- View 2: Customer purchase history
-- joins person and sale so you can see all sales with buyer info
-- use for customer history report
CREATE VIEW CustomerPurchaseHistory AS
SELECT
    s.transaction_id,
    s.name AS buyer_name,
    s.phone AS buyer_phone,
    p.email,
    s.type AS sale_type,
    s.sale_date,
    s.sale_time,
    s.price,
    s.payment_method,
    s.buyer
FROM sale s
JOIN person p ON s.name = p.name AND s.phone = p.phone
ORDER BY s.sale_date DESC;

-- View 3: Teacher schedule summary
-- shows each teacher with the classes they are scheduled for
-- use for teacher page and reports
CREATE VIEW TeacherSchedule AS
SELECT
    p.name AS teacher_name,
    p.phone,
    p.email,
    t.number_of_classes_taught,
    c.class_date,
    c.class_time,
    c.class_type,
    c.duration
FROM teacher t
JOIN person p ON t.name = p.name AND t.phone = p.phone
JOIN personclass pc ON t.name = pc.name AND t.phone = pc.phone
JOIN class c ON pc.pc_date = c.class_date AND pc.pc_time = c.class_time
ORDER BY c.class_date, c.class_time;

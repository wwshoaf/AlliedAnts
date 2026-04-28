/*
Write views, stored procedure/trigger, and transaction
sql/views.sql · sql/procedures.sql · trigger: auto-update classes taught
*/

-- View 1: active enrollments
-- show all current student-class pairings with details
-- use in enrollment page and attendance reports
CREATE VIEW ActiveEnrollments AS
SELECT
    pc.Name,
    pc.Phone,
    p.Email,
    c.Type AS ClassType,
    pc.Date,
    pc.Time,
    c.Duration,
    pc.Attendance
FROM PersonClass pc
JOIN Person p ON pc.Name = p.Name AND pc.Phone = p.Phone
JOIN Class c ON pc.Date = c.Date AND pc.Time = c.Time;


-- View 2: Customer purchase history
-- joins person and sale so you can see all sales with buyer info
-- use for customer history report
CREATE VIEW CustomerPurchaseHistory AS
SELECT
    s.TransactionNumber,
    s.Name AS BuyerName,
    s.Phone AS BuyerPhone,
    p.Email,
    s.Type AS SaleType,
    s.Date,
    s.Price,
    s.PaymentMethod
FROM Sale s
JOIN Person p ON s.Name = p.Name AND s.Phone = p.Phone
ORDER BY s.Date DESC;

-- View 3: Teacher schedule summary
-- shows each teacher with the classes they are scheduled for
-- use for teacher page and reports
CREATE VIEW TeacherSchedule AS
SELECT
    p.Name AS TeacherName,
    p.Phone,
    p.Email,
    t.NumberOfClassesTaught,
    c.Date,
    c.Time,
    c.Type AS ClassType,
    c.Duration
FROM Teacher t
JOIN Person p ON t.Name = p.Name AND t.Phone = p.Phone
JOIN Class c ON t.Name = c.Name AND t.Phone = c.Phone;
ORDER BY c.Date, c.Time;
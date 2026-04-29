-- EnrollStudent procedure
-- enrolls a student in class and makes sure no duplicates
-- use to insert into PersonClass
-- i.e. CALL EnrollStudent('name', 'xxx-xxx-xxxx', 'date', 'time');
DROP PROCEDURE IF EXISTS EnrollStudent;

CREATE PROCEDURE EnrollStudent(
    IN p_name VARCHAR(100),
    IN p_phone VARCHAR(11),
    IN p_date DATE,
    IN p_time Time
)
BEGIN
    IF EXISTS (
        SELECT 1 FROM PersonClass
        WHERE name = p_name AND phone = p_phone
            AND pc_date = p_date AND pc_time = p_time
    ) THEN 
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Student is already enrolled in this class.';
    ELSE 
        INSERT INTO PersonClass (name, phone, pc_date, pc_time)
        VALUES (p_name, p_phone, p_date, p_time);

        -- increment attendance for the class
        UPDATE Class
        SET attendance = attendance + 1
        WHERE class_date = p_date AND class_time = p_time;

        -- if they are a teacher, then increment their number of classes taught
        IF EXISTS (
            SELECT 1 FROM Teacher
            WHERE name = p_name AND phone = p_phone
        ) THEN
            UPDATE Teacher
            SET number_of_classes_taught = number_of_classes_taught + 1
            WHERE name = p_name AND phone = p_phone;
        END IF;
    END IF;
END 
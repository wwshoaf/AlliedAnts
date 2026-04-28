-- EnrollStudent procedure
-- enrolls a student in class and makes sure no duplicates
-- use to insert into PersonClass
-- i.e. CALL EnrollStudent('name', 'xxx-xxx-xxxx', 'date', 'time');
DELIMITER $$

CREATE PROCEDURE EnrollStudent(
    IN p_name VARCHAR(100),
    IN p_phone VARCHAR(20),
    IN p_date DATE,
    IN p_time Time
)
BEGIN
    IF EXISTS (
        SELECT 1 FROM PersonClass
        WHERE Name = p_name AND Phone = p_phone
            AND Date = p_date AND Time = p_time
    ) THEN 
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Student is already enrolled in this class.';
    ELSE 
        INSERT INTO PersonClass (Name, Phone, Date, Time, Attendance)
        VALUES (p_name, p_phone, p_date, p_time, 0);
    END IF;
END $$

DELIMITER ;

-- Trigger AfterEnrollStudent
-- increments teachers number of classes taught anytime a new row is inserted into PersonClass
DELIMITER $$

CREATE TRIGGER AfterEnrollStudent
AFTER INSERT ON PersonClass
FOR EACH ROW
BEGIN
    UPDATE Teacher 
    SET NumberOfClassesTaught = NumberOfClassesTaught + 1
    WHERE Name = (SELECT Name FROM Class WHERE Date = NEW.Date AND Time = NEW.Time)
        AND Phone = (SELECT Phone FROM Class WHERE Date = NEW.Date AND Time = NEW.Time);
END$$

DELIMITER ;
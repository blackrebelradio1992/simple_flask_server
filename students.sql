-- Create the students table
DROP TABLE IF EXISTS student
COPY students FROM '/Users/frankjr./assignments-2/simple_flask_server/data.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name VARCHAR(200),
    last_name VARCHAR(50),
    age INT,
    grade CHAR(1)
);

-- Insert student data
INSERT INTO students (first_name, last_name, age, grade) VALUES
    ('John', 'Doe', 18, 'A'),
    ('Jane', 'Smith', 19, 'B'),
    ('Bob', 'Johnson', 20, 'C'),
    ('Emily', 'Williams', 18, 'A'),
    ('Michael', 'Brown', 19, 'B');

-- Retrieve student information
SELECT * FROM students;

SELECT first_name, last_name FROM students;

SELECT * FROM students WHERE grade = 'A';

SELECT grade, COUNT(*) as grade_count FROM students GROUP BY grade;

SELECT * FROM students WHERE age BETWEEN 18 AND 19;

SELECT * FROM students ORDER BY last_name;

SELECT * FROM students LIMIT 3;

SELECT * FROM students WHERE grade = 'A' AND age > 18 OR grade = 'B';
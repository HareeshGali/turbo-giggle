CREATE table if not exists Session(hash VARCHAR, expires DATETIME, patientID INTEGER AUTOINCREMENT PRIMARY KEY, active BOOLEAN);

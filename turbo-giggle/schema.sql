CREATE table if not exists Sessions(
  expires DATETIME NOT NULL,
  patientID INTEGER NOT NULL,
  hash TEXT NOT NULL
);

CREATE table if not exists Patients(
  patientID INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL,
  dateofBirth VARCHAR NOT NULL,
  address VARCHAR NOT NULL,
  primaryPhys VARCHAR NOT NULL,
  phoneNum INTEGER NOT NULL,
  medHistory TEXT NOT NULL,
  prescribeMeds TEXT NOT NULL

);

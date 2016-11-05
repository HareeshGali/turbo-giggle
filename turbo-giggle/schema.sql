CREATE table if not exists Sessions(
  expires DATETIME NOT NULL,
  patientID INTEGER NOT NULL,
  active BOOLEAN,
  hash VARCHAR NOT NULL
);

CREATE table if not exists Patients(
  patientID INTEGER PRIMARY KEY AUTOINCREMENT
);

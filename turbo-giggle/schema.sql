CREATE table if not exists Sessions(
  expires DATETIME NOT NULL,
  patientID INTEGER NOT NULL,
  hash TEXT NOT NULL
);

CREATE table if not exists Patients(
  patientID INTEGER PRIMARY KEY AUTOINCREMENT
);

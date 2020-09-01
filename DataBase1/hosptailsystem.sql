create database HosptialSystem;
use HosptialSystem;
create table Specialty (
SpatialyId int auto_increment not null primary key,
SpatialyName varchar(45) not null
);
create table Doctor(
DoctorId int auto_increment not null primary key,
Name varchar(45) not null,
Phone varchar(20),
SpatialyId int not null,
CONSTRAINT SpatialyId FOREIGN KEY (SpatialyId)
REFERENCES Specialty(SpatialyId) ON DELETE CASCADE ON update CASCADE

); 
ALTER TABLE Doctor
ADD Supervisor integer null;

create table Patient(
PatientId int auto_increment not null primary key,
Name varchar(45) not null,
Phone varchar(20) not null,
Email varchar(45),
Address varchar(70) not null,
AddedDate date not null,
DoctorId int not null,
CONSTRAINT DoctorId FOREIGN KEY (DoctorId)
REFERENCES Doctor(DoctorId) ON DELETE CASCADE ON update CASCADE
); 
create table Allergy (
AllergyId int auto_increment not null primary key,
AllergyName varchar(45)
);
create table PatientAllergy (
AllergyId int not null,
PatientId int not null,
CONSTRAINT AllergyId FOREIGN KEY (AllergyId)
REFERENCES Allergy(AllergyId) ON DELETE CASCADE ON update CASCADE,
CONSTRAINT PatientId FOREIGN KEY (PatientId)
REFERENCES Patient(PatientId) ON DELETE CASCADE ON update CASCADE
);
create table Appointment(
AppointmentId int auto_increment not null primary key,
DoctorId_FK int not null,
PatientID_KF int not null,
AppointmentDate date not null,
BloodPressure int not null,
Weight float not null,
TreatmentNotes varchar(100),
CONSTRAINT DoctorId_FK FOREIGN KEY (DoctorId_FK)
REFERENCES Doctor(DoctorId) ON DELETE CASCADE ON update CASCADE,
CONSTRAINT PatientID_KF FOREIGN KEY (PatientID_KF)
REFERENCES Patient(PatientID) ON DELETE CASCADE ON update CASCADE
);
create table Medicine (
MedicineId int auto_increment not null primary key,
MedicineName varchar(50)
);

create table PatientMedicine (
MedicineId int not null,
AppointmentId  int not null,
CONSTRAINT AppointmentId FOREIGN KEY (AppointmentId)
REFERENCES Appointment(AppointmentId) ON DELETE CASCADE ON update CASCADE,
CONSTRAINT MedicineId FOREIGN KEY (MedicineId)
REFERENCES Medicine(MedicineId) ON DELETE CASCADE ON update CASCADE
);

insert into Specialty values(1,'Dermatology') ;
insert into Specialty values(2,'Psychiatry') ;
insert into Specialty values(3,'Oncology') ;
insert into Specialty values(4,'Cardiology') ;
insert into Specialty values(5,'Urology') ;
insert into Specialty values(6,'Pediatrics') ;

insert into Doctor values(1,'Doctor Karen',555-1212,6,null);
insert into Doctor values (2,'Doctor John', 555-2934,2,1);
insert into Doctor values (3,'Doctor Robert', 555-6723,6,1);



insert into Patient values(1,'Patient Dana',444-1212,'P1@email.com ' ,'123 Home St.', 02/01/2019,2);
insert into Patient values(2,'Patient Harry',444-2934,'P2@email.com ' ,'3435 Main St.',7/13/2011,3);
insert into Patient values(3,'Patient Sid',444-2347,'P5@email.com' ,'3435 GOE St.',7/14/2011,2);

insert into Appointment values(1,3,2,07/01/2019,80,65,'Dream to success');
insert into Appointment values(2,3,3,01/04/2019,77,88,'Good heart rate');

insert into Allergy values(1,'Drug');
insert into Allergy values(2,'Food');
insert into Allergy values(3,'Skin');
insert into Allergy values(4,'Asthma');

insert into PatientAllergy values(4,1);
insert into PatientAllergy values(3,2);
insert into PatientAllergy values(3,1);

insert into Medicine values(1,'Ibuprofen');
insert into Medicine values(2,'Omeprazole');
insert into Medicine values(3,'Metoprolol');
insert into Medicine values(4,'Azithromycin');

insert into PatientMedicine values (4,2);
insert into PatientMedicine values (2,1);
insert into PatientMedicine values (3,1);

select * from doctor;
select * from allergy;
select * from appointment;
select * from medicine;
select * from patient;
select * from patientallergy;
select * from patientmedicine;
select * from specialty;

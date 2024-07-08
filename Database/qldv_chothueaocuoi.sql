CREATE DATABASE qldv_chothueaocuoi;

-- Switch to the new database
USE qldv_chothueaocuoi;

-- Create the admin table
CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE khachhang (
	idkhachhang VARCHAR(45) PRIMARY KEY NOT NULL,
	name NVARCHAR(45) NULL,
	ngaysinh DATE NULL,
	sdt VARCHAR(45) NULL,
	diachi NVARCHAR(45) NULL
  );
CREATE TABLE dichvu (
    ma_dv VARCHAR(10) PRIMARY KEY NOT NULL,
    goi_dv VARCHAR(50),
    mo_ta TEXT,
    gia_tien DECIMAL(10)
);
CREATE TABLE LichHen (
    malh VARCHAR(45) PRIMARY KEY NOT NULL,
    tenkh NVARCHAR(45),
    sdt NVARCHAR(20),
    diachi NVARCHAR(45),
    ngayhen DATE NULL,
    trangthai NVARCHAR(50)
);


CREATE TABLE muon_tra (
    mamt VARCHAR(10) PRIMARY KEY NOT NULL,
    idkhachhang VARCHAR(45),
    ma_dv VARCHAR(10),
    ngaymuon DATE,
    ngaytra DATE,
    trangthai NVARCHAR(50)
);

CREATE TABLE hoa_don(
	mahd varchar(10) PRIMARY KEY NOT NULL,
    name Nvarchar(50),
    ngaylapHD DATE,
    usernameNV Nvarchar(50),
    tongtien varchar(15),
    soluong varchar(10)
);


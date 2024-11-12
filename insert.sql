INSERT INTO tipos_platos(tipo_plato_id,tipo_plato_nombre,tipo_plato_icon)
values(1,'Bebida','cup-outline') ,(2,'Comida','bowl-outline');

INSERT INTO platos(plato_nombre,plato_descripcion,plato_precio,tipo_plato_id)
values
('Carne','Carne frita de las mas arrechisima',13, 2),
('Pollo' ,'Pollo frito vale',10,2),
('Agua Panela','Ta fria mrk',1,1),
('Agua','Agua de la llave (no esta fria)',0.3,1);


INSERT INTO mesas(mesa_descripcion) values('MESA 1'),
('MESA 2'), ('MESA 3'), ('MESA 4'), ('MESA 5'), ('MESA 6');

INSERT INTO divisas(divisa_id,divisa_nombre,divisa_relacion)
VALUES(1,'DOLAR',1),(2,'BOLIVAR',36),(3,'COP',3700);

INSERT INTO roles(rol_id,rol_nombre) values(1,'SUPERADMIN'), (2,'ADMIN'), (3,'CAJERA'),(4,'MESERO');

INSERT INTO usuarios(usuario_nombre,usuario_contraseña,usuario_salt,rol_id)
VALUES
('DEVELOPER','b3bfb55cd344de020638b0e9f16a65926dda2b649472e11d53d9df2cb4508f22','0691657c32860ac3364911a723ffe481',1),
('MESERO','4cfaaf74d4a3adffd9819da162e73314faf98d9ada91cb78dd2063dbfb7fefb6','531ba3123572a7ac11a210eef2ac7ec6',4);

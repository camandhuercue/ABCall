--
-- Name: pqrs; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA pqrs;


ALTER SCHEMA pqrs OWNER TO postgres;

CREATE SCHEMA usuarios;


ALTER SCHEMA usuarios OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: comentarios; Type: TABLE; Schema: pqrs; Owner: postgres
--

CREATE TABLE pqrs.comentarios (
    "Id" character varying NOT NULL,
    "Comentario" character varying,
    "FechaCreacion" bigint,
    "Creador" character varying
);


ALTER TABLE pqrs.comentarios OWNER TO postgres;

--
-- Name: pqr; Type: TABLE; Schema: pqrs; Owner: postgres
--

CREATE TABLE pqrs.pqr (
    "Id" integer NOT NULL,
    "Usuario" character varying,
    "Servicio" character varying,
    "Estado" character varying,
    "FechaApertura" bigint,
    "FechaCierre" bigint,
    "Comentarios" character varying
);


ALTER TABLE pqrs.pqr OWNER TO postgres;

--
-- Name: usuarios; Type: TABLE; Schema: usuarios; Owner: postgres
--

CREATE TABLE usuarios.usuarios (
    "Id" bigint NOT NULL,
    "Usuario" character varying,
    "Servicios" character varying,
    "Telefono" bigint,
    "Correo" character varying,
    "PrestadoraServicio" character varying,
    "Empresa" character varying
);


ALTER TABLE usuarios.usuarios OWNER TO postgres;

--
-- Name: pqr_Id_seq; Type: SEQUENCE; Schema: pqrs; Owner: postgres
--

CREATE SEQUENCE pqrs."pqr_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE pqrs."pqr_Id_seq" OWNER TO postgres;

--
-- Name: pqr_Id_seq; Type: SEQUENCE OWNED BY; Schema: pqrs; Owner: postgres
--

ALTER SEQUENCE pqrs."pqr_Id_seq" OWNED BY pqrs.pqr."Id";


--
-- Name: pqr Id; Type: DEFAULT; Schema: pqrs; Owner: postgres
--

ALTER TABLE ONLY pqrs.pqr ALTER COLUMN "Id" SET DEFAULT nextval('pqrs."pqr_Id_seq"'::regclass);


--
-- Data for Name: comentarios; Type: TABLE DATA; Schema: pqrs; Owner: postgres
--

COPY pqrs.comentarios ("Id", "Comentario", "FechaCreacion", "Creador") FROM stdin;
8e9b04bc-319c-4d0b-93e4-1ade15d80749    Este es un caso abierto    1725212370    Agente ABCall
69f63b96-126f-4913-a245-6ab005f12a4e    Apertura de caso.    1723748080    Agente ABCall
e9948354-8ac4-4081-a958-fd31ae084889    Comentario del cliente    1723850125    Jose Marin
1aead604-734d-4bc5-9755-87400bcce92e    Caso cerrado    1723907700    Agente ABCall
0850ff71-40b9-4f23-b018-848171ba733b    Caso abierto    1725203700    Agente ABCall
56809cd9-6af6-47c1-baab-9f9ada0f8a8f    Se cierra el caso por solución    1725204650    Agente ABCall
\.


--
-- Data for Name: pqr; Type: TABLE DATA; Schema: pqrs; Owner: postgres
--

COPY pqrs.pqr ("Id", "Usuario", "Servicio", "Estado", "FechaApertura", "FechaCierre", "Comentarios") FROM stdin;
1    1010101010    Telefonia Móvil    Abierto    1725212370    0    8e9b04bc-319c-4d0b-93e4-1ade15d80749
2    2020202020    Canal Empresarial    Cerrado    1723748080    1723907700    69f63b96-126f-4913-a245-6ab005f12a4e;e9948354-8ac4-4081-a958-fd31ae084889;1aead604-734d-4bc5-9755-87400bcce92e
3    3030303030    Servicios Web    Cerrado    1725203700    1725204650    0850ff71-40b9-4f23-b018-848171ba733b;56809cd9-6af6-47c1-baab-9f9ada0f8a8f
\.


--
-- Data for Name: pqr; Type: TABLE DATA; Schema: pqrs; Owner: postgres
--

COPY usuarios.usuarios ("Id", "Usuario", "Servicios", "Telefono", "Correo", "PrestadoraServicio", "Empresa") FROM stdin;
1010101010    Pedro Lopez    Telefonia Móvil    3132222222    pedro.lopez@cliente1.com    Colombia Telefonos    Cliente1
2020202020    Jose Marin    Canal Empresarial    3201234567    jose.marin@cliente2.com    Comunicaciones Empresariales    Cliente2
3030303030    Pablo Borja    Servicios Web    3500102030    pablo.borja@cliente3.com    Colombia Desarrolla    Cliente3
\.

--
-- Name: pqr_Id_seq; Type: SEQUENCE SET; Schema: pqrs; Owner: postgres
--

SELECT pg_catalog.setval('pqrs."pqr_Id_seq"', 1, true);


--
-- Name: comentarios comentarios_pkey; Type: CONSTRAINT; Schema: pqrs; Owner: postgres
--

ALTER TABLE ONLY pqrs.comentarios
    ADD CONSTRAINT comentarios_pkey PRIMARY KEY ("Id");


--
-- Name: pqr pqr_pkey; Type: CONSTRAINT; Schema: pqrs; Owner: postgres
--

ALTER TABLE ONLY pqrs.pqr
    ADD CONSTRAINT pqr_pkey PRIMARY KEY ("Id");


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: usuarios; Owner: postgres
--

ALTER TABLE ONLY usuarios.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY ("Id");

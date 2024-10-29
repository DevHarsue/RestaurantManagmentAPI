--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Debian 16.3-1.pgdg120+1)
-- Dumped by pg_dump version 16.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: root
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO root;

--
-- Name: pg_stat_statements; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA public;


--
-- Name: EXTENSION pg_stat_statements; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_stat_statements IS 'track planning and execution statistics of all SQL statements executed';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: clientes; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.clientes (
    cliente_id integer NOT NULL,
    cliente_nacionalidad "char" NOT NULL,
    cliente_cedula integer NOT NULL,
    cliente_nombre text NOT NULL,
    cliente_apellido text NOT NULL,
    cliente_telefono text,
    cliente_direccion text
);


ALTER TABLE public.clientes OWNER TO root;

--
-- Name: clientes_cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.clientes_cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clientes_cliente_id_seq OWNER TO root;

--
-- Name: clientes_cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.clientes_cliente_id_seq OWNED BY public.clientes.cliente_id;


--
-- Name: detalles_ordenes_divisas; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.detalles_ordenes_divisas (
    detalle_orden_divisa_id integer NOT NULL,
    orden_id integer NOT NULL,
    divisa_id integer NOT NULL,
    detalle_orden_divisa_cantidad double precision NOT NULL
);


ALTER TABLE public.detalles_ordenes_divisas OWNER TO root;

--
-- Name: detalles_ordenes_divisas_detalle_orden_divisa_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.detalles_ordenes_divisas_detalle_orden_divisa_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.detalles_ordenes_divisas_detalle_orden_divisa_seq OWNER TO root;

--
-- Name: detalles_ordenes_divisas_detalle_orden_divisa_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.detalles_ordenes_divisas_detalle_orden_divisa_seq OWNED BY public.detalles_ordenes_divisas.detalle_orden_divisa_id;


--
-- Name: detalles_ordenes_platos; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.detalles_ordenes_platos (
    detalle_orden_plato_id integer NOT NULL,
    orden_id integer NOT NULL,
    plato_id integer NOT NULL,
    detalle_orden_plato_cantidad integer NOT NULL
);


ALTER TABLE public.detalles_ordenes_platos OWNER TO root;

--
-- Name: detalles_ordenes_platos_detalle_orden_plato_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.detalles_ordenes_platos_detalle_orden_plato_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.detalles_ordenes_platos_detalle_orden_plato_id_seq OWNER TO root;

--
-- Name: detalles_ordenes_platos_detalle_orden_plato_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.detalles_ordenes_platos_detalle_orden_plato_id_seq OWNED BY public.detalles_ordenes_platos.detalle_orden_plato_id;


--
-- Name: divisas; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.divisas (
    divisa_id integer NOT NULL,
    divisa_nombre text NOT NULL,
    divisa_relacion double precision NOT NULL
);


ALTER TABLE public.divisas OWNER TO root;

--
-- Name: divisas_divisa_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.divisas_divisa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.divisas_divisa_id_seq OWNER TO root;

--
-- Name: divisas_divisa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.divisas_divisa_id_seq OWNED BY public.divisas.divisa_id;


--
-- Name: mesas; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.mesas (
    mesa_id integer NOT NULL,
    mesa_descripcion text NOT NULL
);


ALTER TABLE public.mesas OWNER TO root;

--
-- Name: mesas_mesa_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.mesas_mesa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.mesas_mesa_id_seq OWNER TO root;

--
-- Name: mesas_mesa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.mesas_mesa_id_seq OWNED BY public.mesas.mesa_id;


--
-- Name: mesas_ocupadas; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.mesas_ocupadas (
    mesa_id integer NOT NULL,
    orden_id integer NOT NULL
);


ALTER TABLE public.mesas_ocupadas OWNER TO root;

--
-- Name: ordenes; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.ordenes (
    orden_id integer NOT NULL,
    orden_fecha date NOT NULL,
    cliente_id integer
);


ALTER TABLE public.ordenes OWNER TO root;

--
-- Name: ordenes_orden_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.ordenes_orden_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ordenes_orden_id_seq OWNER TO root;

--
-- Name: ordenes_orden_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.ordenes_orden_id_seq OWNED BY public.ordenes.orden_id;


--
-- Name: platos; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.platos (
    plato_id integer NOT NULL,
    plato_nombre text NOT NULL,
    plato_descripcion text NOT NULL,
    plato_precio double precision NOT NULL,
    tipo_plato_id integer NOT NULL
);


ALTER TABLE public.platos OWNER TO root;

--
-- Name: platos_plato_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.platos_plato_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.platos_plato_id_seq OWNER TO root;

--
-- Name: platos_plato_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.platos_plato_id_seq OWNED BY public.platos.plato_id;


--
-- Name: tipos_platos; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.tipos_platos (
    tipo_plato_id integer NOT NULL,
    tipo_plato_nombre text NOT NULL,
    tipo_plato_icon text
);


ALTER TABLE public.tipos_platos OWNER TO root;

--
-- Name: tipos_platos_tipo_plato_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.tipos_platos_tipo_plato_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tipos_platos_tipo_plato_id_seq OWNER TO root;

--
-- Name: tipos_platos_tipo_plato_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.tipos_platos_tipo_plato_id_seq OWNED BY public.tipos_platos.tipo_plato_id;


--
-- Name: vista_platos; Type: VIEW; Schema: public; Owner: root
--

CREATE VIEW public.vista_platos AS
 SELECT p.plato_id,
    p.plato_nombre,
    p.plato_descripcion,
    p.plato_precio,
    tp.tipo_plato_id,
    tp.tipo_plato_icon
   FROM (public.platos p
     JOIN public.tipos_platos tp ON ((p.tipo_plato_id = tp.tipo_plato_id)));


ALTER VIEW public.vista_platos OWNER TO root;

--
-- Name: clientes cliente_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.clientes ALTER COLUMN cliente_id SET DEFAULT nextval('public.clientes_cliente_id_seq'::regclass);


--
-- Name: detalles_ordenes_divisas detalle_orden_divisa_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.detalles_ordenes_divisas ALTER COLUMN detalle_orden_divisa_id SET DEFAULT nextval('public.detalles_ordenes_divisas_detalle_orden_divisa_seq'::regclass);


--
-- Name: detalles_ordenes_platos detalle_orden_plato_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.detalles_ordenes_platos ALTER COLUMN detalle_orden_plato_id SET DEFAULT nextval('public.detalles_ordenes_platos_detalle_orden_plato_id_seq'::regclass);


--
-- Name: divisas divisa_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.divisas ALTER COLUMN divisa_id SET DEFAULT nextval('public.divisas_divisa_id_seq'::regclass);


--
-- Name: mesas mesa_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.mesas ALTER COLUMN mesa_id SET DEFAULT nextval('public.mesas_mesa_id_seq'::regclass);


--
-- Name: ordenes orden_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.ordenes ALTER COLUMN orden_id SET DEFAULT nextval('public.ordenes_orden_id_seq'::regclass);


--
-- Name: platos plato_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.platos ALTER COLUMN plato_id SET DEFAULT nextval('public.platos_plato_id_seq'::regclass);


--
-- Name: tipos_platos tipo_plato_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.tipos_platos ALTER COLUMN tipo_plato_id SET DEFAULT nextval('public.tipos_platos_tipo_plato_id_seq'::regclass);


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (cliente_id);


--
-- Name: detalles_ordenes_divisas detalles_ordenes_divisas_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.detalles_ordenes_divisas
    ADD CONSTRAINT detalles_ordenes_divisas_pkey PRIMARY KEY (detalle_orden_divisa_id);


--
-- Name: detalles_ordenes_platos detalles_ordenes_platos_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.detalles_ordenes_platos
    ADD CONSTRAINT detalles_ordenes_platos_pkey PRIMARY KEY (detalle_orden_plato_id);


--
-- Name: divisas divisas_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.divisas
    ADD CONSTRAINT divisas_pkey PRIMARY KEY (divisa_id);


--
-- Name: mesas_ocupadas mesas_ocupadas_mesa_id_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.mesas_ocupadas
    ADD CONSTRAINT mesas_ocupadas_mesa_id_key UNIQUE (mesa_id);


--
-- Name: mesas_ocupadas mesas_ocupadas_orden_id_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.mesas_ocupadas
    ADD CONSTRAINT mesas_ocupadas_orden_id_key UNIQUE (orden_id);


--
-- Name: mesas mesas_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.mesas
    ADD CONSTRAINT mesas_pkey PRIMARY KEY (mesa_id);


--
-- Name: ordenes ordenes_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.ordenes
    ADD CONSTRAINT ordenes_pkey PRIMARY KEY (orden_id);


--
-- Name: platos platos_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.platos
    ADD CONSTRAINT platos_pkey PRIMARY KEY (plato_id);


--
-- Name: tipos_platos tipos_platos_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.tipos_platos
    ADD CONSTRAINT tipos_platos_pkey PRIMARY KEY (tipo_plato_id);


--
-- Name: detalles_ordenes_divisas detalles_ordenes_divisas_divisa_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.detalles_ordenes_divisas
    ADD CONSTRAINT detalles_ordenes_divisas_divisa_id_fkey FOREIGN KEY (divisa_id) REFERENCES public.divisas(divisa_id);


--
-- Name: detalles_ordenes_divisas detalles_ordenes_divisas_orden_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.detalles_ordenes_divisas
    ADD CONSTRAINT detalles_ordenes_divisas_orden_id_fkey FOREIGN KEY (orden_id) REFERENCES public.ordenes(orden_id);


--
-- Name: detalles_ordenes_platos detalles_ordenes_platos_orden_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.detalles_ordenes_platos
    ADD CONSTRAINT detalles_ordenes_platos_orden_id_fkey FOREIGN KEY (orden_id) REFERENCES public.ordenes(orden_id);


--
-- Name: detalles_ordenes_platos detalles_ordenes_platos_plato_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.detalles_ordenes_platos
    ADD CONSTRAINT detalles_ordenes_platos_plato_id_fkey FOREIGN KEY (plato_id) REFERENCES public.platos(plato_id);


--
-- Name: mesas_ocupadas mesas_ocupadas_mesa_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.mesas_ocupadas
    ADD CONSTRAINT mesas_ocupadas_mesa_id_fkey FOREIGN KEY (mesa_id) REFERENCES public.mesas(mesa_id);


--
-- Name: mesas_ocupadas mesas_ocupadas_orden_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.mesas_ocupadas
    ADD CONSTRAINT mesas_ocupadas_orden_id_fkey FOREIGN KEY (orden_id) REFERENCES public.ordenes(orden_id);


--
-- Name: ordenes ordenes_cliente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.ordenes
    ADD CONSTRAINT ordenes_cliente_id_fkey FOREIGN KEY (cliente_id) REFERENCES public.clientes(cliente_id);


--
-- Name: platos platos_tipo_plato_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.platos
    ADD CONSTRAINT platos_tipo_plato_id_fkey FOREIGN KEY (tipo_plato_id) REFERENCES public.tipos_platos(tipo_plato_id) NOT VALID;


--
-- Name: FUNCTION pg_stat_statements(showtext boolean, OUT userid oid, OUT dbid oid, OUT toplevel boolean, OUT queryid bigint, OUT query text, OUT plans bigint, OUT total_plan_time double precision, OUT min_plan_time double precision, OUT max_plan_time double precision, OUT mean_plan_time double precision, OUT stddev_plan_time double precision, OUT calls bigint, OUT total_exec_time double precision, OUT min_exec_time double precision, OUT max_exec_time double precision, OUT mean_exec_time double precision, OUT stddev_exec_time double precision, OUT rows bigint, OUT shared_blks_hit bigint, OUT shared_blks_read bigint, OUT shared_blks_dirtied bigint, OUT shared_blks_written bigint, OUT local_blks_hit bigint, OUT local_blks_read bigint, OUT local_blks_dirtied bigint, OUT local_blks_written bigint, OUT temp_blks_read bigint, OUT temp_blks_written bigint, OUT blk_read_time double precision, OUT blk_write_time double precision, OUT temp_blk_read_time double precision, OUT temp_blk_write_time double precision, OUT wal_records bigint, OUT wal_fpi bigint, OUT wal_bytes numeric, OUT jit_functions bigint, OUT jit_generation_time double precision, OUT jit_inlining_count bigint, OUT jit_inlining_time double precision, OUT jit_optimization_count bigint, OUT jit_optimization_time double precision, OUT jit_emission_count bigint, OUT jit_emission_time double precision); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.pg_stat_statements(showtext boolean, OUT userid oid, OUT dbid oid, OUT toplevel boolean, OUT queryid bigint, OUT query text, OUT plans bigint, OUT total_plan_time double precision, OUT min_plan_time double precision, OUT max_plan_time double precision, OUT mean_plan_time double precision, OUT stddev_plan_time double precision, OUT calls bigint, OUT total_exec_time double precision, OUT min_exec_time double precision, OUT max_exec_time double precision, OUT mean_exec_time double precision, OUT stddev_exec_time double precision, OUT rows bigint, OUT shared_blks_hit bigint, OUT shared_blks_read bigint, OUT shared_blks_dirtied bigint, OUT shared_blks_written bigint, OUT local_blks_hit bigint, OUT local_blks_read bigint, OUT local_blks_dirtied bigint, OUT local_blks_written bigint, OUT temp_blks_read bigint, OUT temp_blks_written bigint, OUT blk_read_time double precision, OUT blk_write_time double precision, OUT temp_blk_read_time double precision, OUT temp_blk_write_time double precision, OUT wal_records bigint, OUT wal_fpi bigint, OUT wal_bytes numeric, OUT jit_functions bigint, OUT jit_generation_time double precision, OUT jit_inlining_count bigint, OUT jit_inlining_time double precision, OUT jit_optimization_count bigint, OUT jit_optimization_time double precision, OUT jit_emission_count bigint, OUT jit_emission_time double precision) TO root;


--
-- Name: FUNCTION pg_stat_statements_info(OUT dealloc bigint, OUT stats_reset timestamp with time zone); Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON FUNCTION public.pg_stat_statements_info(OUT dealloc bigint, OUT stats_reset timestamp with time zone) TO root;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON SEQUENCES TO root;


--
-- Name: DEFAULT PRIVILEGES FOR TYPES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TYPES TO root;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON FUNCTIONS TO root;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: -; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TABLES TO root;


--
-- PostgreSQL database dump complete
--


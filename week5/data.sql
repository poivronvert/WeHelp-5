--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-1.pgdg110+1)
-- Dumped by pg_dump version 15.3 (Debian 15.3-1.pgdg110+1)

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
-- Name: website; Type: SCHEMA; Schema: -; Owner: demodb01
--

CREATE SCHEMA website;


ALTER SCHEMA website OWNER TO demodb01;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: member; Type: TABLE; Schema: website; Owner: demodb01
--

CREATE TABLE website.member (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    username character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    follower_count integer DEFAULT 0 NOT NULL,
    "time" timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT member_follower_count_check CHECK ((follower_count >= 0))
);


ALTER TABLE website.member OWNER TO demodb01;

--
-- Name: COLUMN member.id; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.member.id IS 'Unique ID';


--
-- Name: COLUMN member.name; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.member.name IS 'Name';


--
-- Name: COLUMN member.username; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.member.username IS 'Username';


--
-- Name: COLUMN member.password; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.member.password IS 'Password';


--
-- Name: COLUMN member.follower_count; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.member.follower_count IS 'Follower Count';


--
-- Name: COLUMN member."time"; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.member."time" IS 'Signup Time';


--
-- Name: member_id_seq; Type: SEQUENCE; Schema: website; Owner: demodb01
--

ALTER TABLE website.member ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME website.member_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: message; Type: TABLE; Schema: website; Owner: demodb01
--

CREATE TABLE website.message (
    id bigint NOT NULL,
    member_id bigint NOT NULL,
    content character varying(255) NOT NULL,
    like_count integer DEFAULT 0 NOT NULL,
    "time" timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT message_like_count_check CHECK ((like_count >= 0))
);


ALTER TABLE website.message OWNER TO demodb01;

--
-- Name: COLUMN message.id; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.message.id IS 'Unique ID';


--
-- Name: COLUMN message.member_id; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.message.member_id IS 'Member ID for Message Sender';


--
-- Name: COLUMN message.content; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.message.content IS 'Content';


--
-- Name: COLUMN message."time"; Type: COMMENT; Schema: website; Owner: demodb01
--

COMMENT ON COLUMN website.message."time" IS 'Publish Time';


--
-- Name: message_id_seq; Type: SEQUENCE; Schema: website; Owner: demodb01
--

ALTER TABLE website.message ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME website.message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: member; Type: TABLE DATA; Schema: website; Owner: demodb01
--

COPY website.member (id, name, username, password, follower_count, "time") FROM stdin;
2	Apple	apple	123	2	2024-04-29 08:03:08.2573
3	Banana	banaba	123	3	2024-04-29 08:03:08.2573
4	Kiwi	kiwi	123	4	2024-04-29 08:03:08.2573
5	Grape	grape	123	5	2024-04-29 08:03:08.2573
1	test2	test	test	1	2024-04-29 07:59:51.130845
\.


--
-- Data for Name: message; Type: TABLE DATA; Schema: website; Owner: demodb01
--

COPY website.message (id, member_id, content, like_count, "time") FROM stdin;
2	1	Hello	10	2024-04-30 07:36:32.190429
3	2	Hello	20	2024-04-30 07:36:32.190429
4	3	Hello	30	2024-04-30 07:36:32.190429
5	4	Hello	40	2024-04-30 07:36:32.190429
6	5	Hello	50	2024-04-30 07:36:32.190429
\.


--
-- Name: member_id_seq; Type: SEQUENCE SET; Schema: website; Owner: demodb01
--

SELECT pg_catalog.setval('website.member_id_seq', 5, true);


--
-- Name: message_id_seq; Type: SEQUENCE SET; Schema: website; Owner: demodb01
--

SELECT pg_catalog.setval('website.message_id_seq', 6, true);


--
-- Name: member member_pkey; Type: CONSTRAINT; Schema: website; Owner: demodb01
--

ALTER TABLE ONLY website.member
    ADD CONSTRAINT member_pkey PRIMARY KEY (id);


--
-- Name: message message_pkey; Type: CONSTRAINT; Schema: website; Owner: demodb01
--

ALTER TABLE ONLY website.message
    ADD CONSTRAINT message_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--


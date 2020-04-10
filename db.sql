--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_content_type VALUES (1, 'auth', 'permission');
INSERT INTO django_content_type VALUES (2, 'auth', 'group');
INSERT INTO django_content_type VALUES (3, 'contenttypes', 'contenttype');
INSERT INTO django_content_type VALUES (4, 'dAuction2', 'user');
INSERT INTO django_content_type VALUES (5, 'dAuction2', 'treatment');
INSERT INTO django_content_type VALUES (6, 'dAuction2', 'auction');
INSERT INTO django_content_type VALUES (7, 'dAuction2', 'group');
INSERT INTO django_content_type VALUES (8, 'dAuction2', 'period');
INSERT INTO django_content_type VALUES (9, 'dAuction2', 'player');
INSERT INTO django_content_type VALUES (10, 'dAuction2', 'page');
INSERT INTO django_content_type VALUES (11, 'dAuction2', 'distribution');
INSERT INTO django_content_type VALUES (12, 'dAuction2', 'player_stats');
INSERT INTO django_content_type VALUES (13, 'dAuction2', 'voucher');
INSERT INTO django_content_type VALUES (14, 'dAuction2', 'voucherre');
INSERT INTO django_content_type VALUES (15, 'dAuction2', 'phase');
INSERT INTO django_content_type VALUES (16, 'dAuction2', 'timer');
INSERT INTO django_content_type VALUES (17, 'dAuction2', 'offer');
INSERT INTO django_content_type VALUES (18, 'dAuction2', 'penalty');
INSERT INTO django_content_type VALUES (19, 'dAuction2', 'question');
INSERT INTO django_content_type VALUES (20, 'dAuction2', 'option_mc');
INSERT INTO django_content_type VALUES (21, 'dAuction2', 'player_questions');
INSERT INTO django_content_type VALUES (22, 'dAuction2', 'player_question_options');
INSERT INTO django_content_type VALUES (23, 'admin', 'logentry');
INSERT INTO django_content_type VALUES (24, 'sessions', 'session');


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO auth_permission VALUES (1, 'Can add permission', 1, 'add_permission');
INSERT INTO auth_permission VALUES (2, 'Can change permission', 1, 'change_permission');
INSERT INTO auth_permission VALUES (3, 'Can delete permission', 1, 'delete_permission');
INSERT INTO auth_permission VALUES (4, 'Can add group', 2, 'add_group');
INSERT INTO auth_permission VALUES (5, 'Can change group', 2, 'change_group');
INSERT INTO auth_permission VALUES (6, 'Can delete group', 2, 'delete_group');
INSERT INTO auth_permission VALUES (7, 'Can add content type', 3, 'add_contenttype');
INSERT INTO auth_permission VALUES (8, 'Can change content type', 3, 'change_contenttype');
INSERT INTO auth_permission VALUES (9, 'Can delete content type', 3, 'delete_contenttype');
INSERT INTO auth_permission VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO auth_permission VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO auth_permission VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO auth_permission VALUES (13, 'Can add treatment', 5, 'add_treatment');
INSERT INTO auth_permission VALUES (14, 'Can change treatment', 5, 'change_treatment');
INSERT INTO auth_permission VALUES (15, 'Can delete treatment', 5, 'delete_treatment');
INSERT INTO auth_permission VALUES (16, 'Can add auction', 6, 'add_auction');
INSERT INTO auth_permission VALUES (17, 'Can change auction', 6, 'change_auction');
INSERT INTO auth_permission VALUES (18, 'Can delete auction', 6, 'delete_auction');
INSERT INTO auth_permission VALUES (19, 'Can add group', 7, 'add_group');
INSERT INTO auth_permission VALUES (20, 'Can change group', 7, 'change_group');
INSERT INTO auth_permission VALUES (21, 'Can delete group', 7, 'delete_group');
INSERT INTO auth_permission VALUES (22, 'Can add period', 8, 'add_period');
INSERT INTO auth_permission VALUES (23, 'Can change period', 8, 'change_period');
INSERT INTO auth_permission VALUES (24, 'Can delete period', 8, 'delete_period');
INSERT INTO auth_permission VALUES (25, 'Can add player', 9, 'add_player');
INSERT INTO auth_permission VALUES (26, 'Can change player', 9, 'change_player');
INSERT INTO auth_permission VALUES (27, 'Can delete player', 9, 'delete_player');
INSERT INTO auth_permission VALUES (28, 'Can add page', 10, 'add_page');
INSERT INTO auth_permission VALUES (29, 'Can change page', 10, 'change_page');
INSERT INTO auth_permission VALUES (30, 'Can delete page', 10, 'delete_page');
INSERT INTO auth_permission VALUES (31, 'Can add distribution', 11, 'add_distribution');
INSERT INTO auth_permission VALUES (32, 'Can change distribution', 11, 'change_distribution');
INSERT INTO auth_permission VALUES (33, 'Can delete distribution', 11, 'delete_distribution');
INSERT INTO auth_permission VALUES (34, 'Can add player_stats', 12, 'add_player_stats');
INSERT INTO auth_permission VALUES (35, 'Can change player_stats', 12, 'change_player_stats');
INSERT INTO auth_permission VALUES (36, 'Can delete player_stats', 12, 'delete_player_stats');
INSERT INTO auth_permission VALUES (37, 'Can add voucher', 13, 'add_voucher');
INSERT INTO auth_permission VALUES (38, 'Can change voucher', 13, 'change_voucher');
INSERT INTO auth_permission VALUES (39, 'Can delete voucher', 13, 'delete_voucher');
INSERT INTO auth_permission VALUES (40, 'Can add voucher re', 14, 'add_voucherre');
INSERT INTO auth_permission VALUES (41, 'Can change voucher re', 14, 'change_voucherre');
INSERT INTO auth_permission VALUES (42, 'Can delete voucher re', 14, 'delete_voucherre');
INSERT INTO auth_permission VALUES (43, 'Can add phase', 15, 'add_phase');
INSERT INTO auth_permission VALUES (44, 'Can change phase', 15, 'change_phase');
INSERT INTO auth_permission VALUES (45, 'Can delete phase', 15, 'delete_phase');
INSERT INTO auth_permission VALUES (46, 'Can add timer', 16, 'add_timer');
INSERT INTO auth_permission VALUES (47, 'Can change timer', 16, 'change_timer');
INSERT INTO auth_permission VALUES (48, 'Can delete timer', 16, 'delete_timer');
INSERT INTO auth_permission VALUES (49, 'Can add offer', 17, 'add_offer');
INSERT INTO auth_permission VALUES (50, 'Can change offer', 17, 'change_offer');
INSERT INTO auth_permission VALUES (51, 'Can delete offer', 17, 'delete_offer');
INSERT INTO auth_permission VALUES (52, 'Can add penalty', 18, 'add_penalty');
INSERT INTO auth_permission VALUES (53, 'Can change penalty', 18, 'change_penalty');
INSERT INTO auth_permission VALUES (54, 'Can delete penalty', 18, 'delete_penalty');
INSERT INTO auth_permission VALUES (55, 'Can add question', 19, 'add_question');
INSERT INTO auth_permission VALUES (56, 'Can change question', 19, 'change_question');
INSERT INTO auth_permission VALUES (57, 'Can delete question', 19, 'delete_question');
INSERT INTO auth_permission VALUES (58, 'Can add option_mc', 20, 'add_option_mc');
INSERT INTO auth_permission VALUES (59, 'Can change option_mc', 20, 'change_option_mc');
INSERT INTO auth_permission VALUES (60, 'Can delete option_mc', 20, 'delete_option_mc');
INSERT INTO auth_permission VALUES (61, 'Can add player_ questions', 21, 'add_player_questions');
INSERT INTO auth_permission VALUES (62, 'Can change player_ questions', 21, 'change_player_questions');
INSERT INTO auth_permission VALUES (63, 'Can delete player_ questions', 21, 'delete_player_questions');
INSERT INTO auth_permission VALUES (64, 'Can add player_ question_ options', 22, 'add_player_question_options');
INSERT INTO auth_permission VALUES (65, 'Can change player_ question_ options', 22, 'change_player_question_options');
INSERT INTO auth_permission VALUES (66, 'Can delete player_ question_ options', 22, 'delete_player_question_options');
INSERT INTO auth_permission VALUES (67, 'Can add log entry', 23, 'add_logentry');
INSERT INTO auth_permission VALUES (68, 'Can change log entry', 23, 'change_logentry');
INSERT INTO auth_permission VALUES (69, 'Can delete log entry', 23, 'delete_logentry');
INSERT INTO auth_permission VALUES (70, 'Can add session', 24, 'add_session');
INSERT INTO auth_permission VALUES (71, 'Can change session', 24, 'change_session');
INSERT INTO auth_permission VALUES (72, 'Can delete session', 24, 'delete_session');


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_permission_id_seq', 72, true);


--
-- Data for Name: dAuction2_treatment; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_treatment" VALUES (2, false, '2017-11-01 09:56:41.85351+00', 4, 4, 4, 0.0177777777770000006, 0, 0, 60, 20, 55, 65, 73, 60, 2.89999999999999991, 60.3999999999999986, 8.69999999999999929, true, 3, 45, 180, 30, 20, 45, 180, 120, 20, 45, 2000, 900, 600, 180, 2, 5, 15, 1, 3.5, 200, 50, 50, 0, 100, 35, 400, 15, 10, 3, false, false, false, false, 1, false, true, true, 8);
INSERT INTO "dAuction2_treatment" VALUES (1, true, '2017-11-01 09:56:41.775997+00', 1, 1, 4, 0.0177777777770000006, 0, 0, 60, 20, 20, 100, 139, 60, 23.0899999999999999, 87, 79, true, 1, 45, 180, 30, 20, 45, 180, 120, 20, 45, 2000, 900, 600, 180, 2, 7, 15, 2, 0.5, 200, 50, 50, 300, 100, 35, 400, 15, 10, 3, false, false, false, false, 1, false, true, true, 0);


--
-- Data for Name: dAuction2_auction; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_auction" VALUES (271420, '2017-11-01 09:56:41.971444+00', '2017-11-10 14:45:17.677722+00', 1500, false, false, false, true, true, true, true, true, 5, false, false, 1, 'data_1', 19, true, true, 60.0985000000000014, 22.624738622799601, 5494.86650000000009, 4954.02920587653989, 106547.801149749997, false, true, true, true, false, true, 35, 22, 0, false, false, false, true, true, true, true, false, false, true, false, false, 0, false, false, false, 1);


--
-- Name: dAuction2_auction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_auction_id_seq"', 1, false);


--
-- Data for Name: dAuction2_distribution; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_distribution" VALUES (14088, 1, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14089, 2, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14090, 3, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14091, 4, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14092, 5, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14093, 6, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14094, 7, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14095, 8, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14096, 9, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14097, 10, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14098, 11, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14099, 12, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14100, 13, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14101, 14, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14102, 15, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14103, 16, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14104, 17, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14105, 18, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14106, 19, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14107, 20, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14108, 21, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14109, 22, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14110, 23, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14111, 24, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14112, 25, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14113, 26, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14114, 27, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14115, 28, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14116, 29, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14117, 30, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14118, 31, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14119, 32, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14120, 33, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14121, 34, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14122, 35, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14123, 36, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14124, 37, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14125, 38, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14126, 39, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14127, 40, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14128, 41, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14129, 42, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14130, 43, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14131, 44, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14132, 45, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14133, 46, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14134, 47, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14135, 48, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14136, 49, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14137, 50, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14138, 51, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14139, 52, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14140, 53, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14141, 54, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14142, 55, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14143, 56, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14144, 57, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14145, 58, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14146, 59, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14147, 60, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14148, 61, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14149, 62, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14150, 63, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14151, 64, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14152, 65, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14153, 66, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14154, 67, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14155, 68, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14156, 69, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14157, 70, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14158, 71, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14159, 72, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14160, 73, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14161, 74, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14162, 75, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14163, 76, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14164, 77, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14165, 78, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14166, 79, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14167, 80, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14168, 81, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14169, 82, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14170, 83, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14171, 84, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14172, 85, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14173, 86, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14174, 87, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14175, 88, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14176, 89, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14177, 90, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14178, 91, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14179, 92, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14180, 93, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14181, 94, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14182, 95, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14183, 96, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14184, 97, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14185, 98, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14186, 99, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14187, 100, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14188, 101, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14189, 102, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14190, 103, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14191, 104, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14192, 105, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14193, 106, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14194, 107, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14195, 108, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14196, 109, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14197, 110, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14198, 111, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14199, 112, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14200, 113, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14201, 114, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14202, 115, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14203, 116, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14204, 117, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14205, 118, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14206, 119, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14207, 120, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14208, 121, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14209, 122, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14210, 123, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14211, 124, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14212, 125, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14213, 126, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14214, 127, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14215, 128, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14216, 129, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14217, 130, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14218, 131, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14219, 132, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14220, 133, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14221, 134, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14222, 135, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14223, 136, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14224, 137, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14225, 138, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14226, 139, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14227, 140, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14228, 141, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14229, 142, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14230, 143, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14231, 144, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14232, 145, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14233, 146, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14234, 147, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14235, 148, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14236, 149, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14237, 150, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14238, 151, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14239, 152, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14240, 153, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14241, 154, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14242, 155, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14243, 156, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14244, 157, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14245, 158, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14246, 159, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14247, 160, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14248, 161, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14249, 162, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14250, 163, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14251, 164, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14252, 165, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14253, 166, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14254, 167, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14255, 168, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14256, 169, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14257, 170, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14258, 171, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14259, 172, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14260, 173, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14261, 174, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14262, 175, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14263, 176, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14264, 177, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14265, 178, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14266, 179, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14267, 180, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14268, 181, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14269, 182, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14270, 183, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14271, 184, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14272, 185, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14273, 186, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14274, 187, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14275, 188, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14276, 189, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14277, 190, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14278, 191, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14279, 192, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14280, 193, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14281, 194, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14282, 195, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14283, 196, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14284, 197, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14285, 198, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14286, 199, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14287, 200, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14288, 201, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14289, 202, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14290, 203, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14291, 204, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14292, 205, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14293, 206, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14294, 207, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14295, 208, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14296, 209, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14297, 210, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14298, 211, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14299, 212, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14300, 213, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14301, 214, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14302, 215, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14303, 216, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14304, 217, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14305, 218, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14306, 219, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14307, 220, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14308, 221, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14309, 222, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14310, 223, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14311, 224, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14312, 225, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14313, 226, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14314, 227, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14315, 228, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14316, 229, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14317, 230, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14318, 231, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14319, 232, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14320, 233, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14321, 234, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14322, 235, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14323, 236, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14324, 237, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14325, 238, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14326, 239, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14327, 240, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14328, 241, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14329, 242, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14330, 243, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14331, 244, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14332, 245, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14333, 246, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14334, 247, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14335, 248, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14336, 249, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14337, 250, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14338, 251, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14339, 252, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14340, 253, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14341, 254, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14342, 255, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14343, 256, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14344, 257, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14345, 258, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14346, 259, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14347, 260, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14348, 261, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14349, 262, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14350, 263, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14351, 264, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14352, 265, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14353, 266, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14354, 267, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14355, 268, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14356, 269, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14357, 270, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14358, 271, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14359, 272, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14360, 273, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14361, 274, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14362, 275, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14363, 276, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14364, 277, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14365, 278, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14366, 279, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14367, 280, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14368, 281, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14369, 282, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14370, 283, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14371, 284, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14372, 285, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14373, 286, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14374, 287, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14375, 288, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14376, 289, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14377, 290, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14378, 291, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14379, 292, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14380, 293, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14381, 294, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14382, 295, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14383, 296, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14384, 297, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14385, 298, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14386, 299, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14387, 300, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14388, 301, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14389, 302, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14390, 303, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14391, 304, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14392, 305, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14393, 306, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14394, 307, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14395, 308, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14396, 309, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14397, 310, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14398, 311, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14399, 312, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14400, 313, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14401, 314, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14402, 315, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14403, 316, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14404, 317, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14405, 318, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14406, 319, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14407, 320, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14408, 321, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14409, 322, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14410, 323, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14411, 324, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14412, 325, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14413, 326, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14414, 327, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14415, 328, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14416, 329, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14417, 330, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14418, 331, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14419, 332, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14420, 333, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14421, 334, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14422, 335, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14423, 336, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14424, 337, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14425, 338, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14426, 339, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14427, 340, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14428, 341, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14429, 342, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14430, 343, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14431, 344, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14432, 345, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14433, 346, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14434, 347, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14435, 348, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14436, 349, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14437, 350, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14438, 351, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14439, 352, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14440, 353, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14441, 354, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14442, 355, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14443, 356, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14444, 357, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14445, 358, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14446, 359, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14447, 360, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14448, 361, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14449, 362, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14450, 363, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14451, 364, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14452, 365, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14453, 366, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14454, 367, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14455, 368, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14456, 369, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14457, 370, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14458, 371, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14459, 372, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14460, 373, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14461, 374, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14462, 375, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14463, 376, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14464, 377, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14465, 378, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14466, 379, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14467, 380, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14468, 381, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14469, 382, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14470, 383, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14471, 384, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14472, 385, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14473, 386, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14474, 387, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14475, 388, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14476, 389, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14477, 390, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14478, 391, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14479, 392, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14480, 393, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14481, 394, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14482, 395, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14483, 396, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14484, 397, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14485, 398, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14486, 399, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14487, 400, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14488, 401, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14489, 402, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14490, 403, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14491, 404, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14492, 405, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14493, 406, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14494, 407, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14495, 408, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14496, 409, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14497, 410, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14498, 411, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14499, 412, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14500, 413, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14501, 414, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14502, 415, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14503, 416, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14504, 417, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14505, 418, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14506, 419, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14507, 420, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14508, 421, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14509, 422, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14510, 423, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14511, 424, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14512, 425, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14513, 426, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14514, 427, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14515, 428, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14516, 429, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14517, 430, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14518, 431, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14519, 432, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14520, 433, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14521, 434, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14522, 435, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14523, 436, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14524, 437, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14525, 438, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14526, 439, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14527, 440, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14528, 441, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14529, 442, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14530, 443, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14531, 444, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14532, 445, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14533, 446, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14534, 447, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14535, 448, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14536, 449, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14537, 450, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14538, 451, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14539, 452, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14540, 453, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14541, 454, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14542, 455, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14543, 456, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14544, 457, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14545, 458, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14546, 459, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14547, 460, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14548, 461, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14549, 462, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14550, 463, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14551, 464, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14552, 465, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14553, 466, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14554, 467, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14555, 468, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14556, 469, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14557, 470, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14558, 471, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14559, 472, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14560, 473, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14561, 474, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14562, 475, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14563, 476, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14564, 477, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14565, 478, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14566, 479, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14567, 480, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14568, 481, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14569, 482, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14570, 483, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14571, 484, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14572, 485, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14573, 486, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14574, 487, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14575, 488, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14576, 489, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14577, 490, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14578, 491, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14579, 492, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14580, 493, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14581, 494, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14582, 495, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14583, 496, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14584, 497, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14585, 498, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14586, 499, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14587, 500, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14588, 501, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14589, 502, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14590, 503, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14591, 504, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14592, 505, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14593, 506, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14594, 507, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14595, 508, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14596, 509, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14597, 510, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14598, 511, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14599, 512, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14600, 513, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14601, 514, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14602, 515, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14603, 516, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14604, 517, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14605, 518, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14606, 519, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14607, 520, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14608, 521, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14609, 522, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14610, 523, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14611, 524, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14612, 525, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14613, 526, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14614, 527, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14615, 528, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14616, 529, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14617, 530, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14618, 531, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14619, 532, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14620, 533, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14621, 534, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14622, 535, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14623, 536, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14624, 537, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14625, 538, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14626, 539, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14627, 540, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14628, 541, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14629, 542, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14630, 543, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14631, 544, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14632, 545, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14633, 546, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14634, 547, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14635, 548, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14636, 549, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14637, 550, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14638, 551, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14639, 552, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14640, 553, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14641, 554, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14642, 555, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14643, 556, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14644, 557, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14645, 558, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14646, 559, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14647, 560, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14648, 561, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14649, 562, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14650, 563, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14651, 564, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14652, 565, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14653, 566, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14654, 567, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14655, 568, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14656, 569, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14657, 570, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14658, 571, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14659, 572, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14660, 573, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14661, 574, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14662, 575, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14663, 576, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14664, 577, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14665, 578, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14666, 579, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14667, 580, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14668, 581, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14669, 582, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14670, 583, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14671, 584, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14672, 585, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14673, 586, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14674, 587, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14675, 588, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14676, 589, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14677, 590, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14678, 591, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14679, 592, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14680, 593, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14681, 594, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14682, 595, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14683, 596, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14684, 597, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14685, 598, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14686, 599, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14687, 600, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14688, 601, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14689, 602, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14690, 603, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14691, 604, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14692, 605, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14693, 606, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14694, 607, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14695, 608, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14696, 609, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14697, 610, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14698, 611, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14699, 612, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14700, 613, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14701, 614, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14702, 615, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14703, 616, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14704, 617, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14705, 618, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14706, 619, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14707, 620, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14708, 621, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14709, 622, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14710, 623, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14711, 624, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14712, 625, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14713, 626, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14714, 627, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14715, 628, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14716, 629, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14717, 630, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14718, 631, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14719, 632, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14720, 633, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14721, 634, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14722, 635, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14723, 636, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14724, 637, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14725, 638, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14726, 639, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14727, 640, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14728, 641, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14729, 642, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14730, 643, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14731, 644, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14732, 645, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14733, 646, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14734, 647, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14735, 648, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14736, 649, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14737, 650, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14738, 651, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14739, 652, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14740, 653, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14741, 654, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14742, 655, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14743, 656, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14744, 657, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14745, 658, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14746, 659, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14747, 660, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14748, 661, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14749, 662, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14750, 663, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14751, 664, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14752, 665, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14753, 666, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14754, 667, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14755, 668, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14756, 669, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14757, 670, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14758, 671, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14759, 672, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14760, 673, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14761, 674, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14762, 675, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14763, 676, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14764, 677, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14765, 678, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14766, 679, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14767, 680, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14768, 681, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14769, 682, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14770, 683, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14771, 684, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14772, 685, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14773, 686, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14774, 687, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14775, 688, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14776, 689, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14777, 690, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14778, 691, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14779, 692, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14780, 693, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14781, 694, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14782, 695, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14783, 696, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14784, 697, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14785, 698, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14786, 699, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14787, 700, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14788, 701, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14789, 702, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14790, 703, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14791, 704, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14792, 705, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14793, 706, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14794, 707, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14795, 708, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14796, 709, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14797, 710, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14798, 711, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14799, 712, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14800, 713, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14801, 714, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14802, 715, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14803, 716, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14804, 717, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14805, 718, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14806, 719, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14807, 720, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14808, 721, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14809, 722, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14810, 723, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14811, 724, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14812, 725, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14813, 726, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14814, 727, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14815, 728, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14816, 729, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14817, 730, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14818, 731, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14819, 732, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14820, 733, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14821, 734, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14822, 735, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14823, 736, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14824, 737, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14825, 738, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14826, 739, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14827, 740, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14828, 741, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14829, 742, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14830, 743, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14831, 744, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14832, 745, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14833, 746, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14834, 747, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14835, 748, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14836, 749, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14837, 750, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14838, 751, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14839, 752, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14840, 753, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14841, 754, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14842, 755, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14843, 756, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14844, 757, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14845, 758, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14846, 759, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14847, 760, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14848, 761, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14849, 762, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14850, 763, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14851, 764, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14852, 765, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14853, 766, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14854, 767, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14855, 768, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14856, 769, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14857, 770, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14858, 771, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14859, 772, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14860, 773, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14861, 774, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14862, 775, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14863, 776, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14864, 777, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14865, 778, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14866, 779, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14867, 780, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14868, 781, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14869, 782, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14870, 783, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14871, 784, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14872, 785, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14873, 786, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14874, 787, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14875, 788, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14876, 789, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14877, 790, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14878, 791, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14879, 792, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14880, 793, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14881, 794, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14882, 795, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14883, 796, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14884, 797, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14885, 798, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14886, 799, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14887, 800, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14888, 801, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14889, 802, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14890, 803, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14891, 804, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14892, 805, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14893, 806, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14894, 807, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14895, 808, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14896, 809, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14897, 810, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14898, 811, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14899, 812, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14900, 813, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14901, 814, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14902, 815, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14903, 816, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14904, 817, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14905, 818, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14906, 819, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14907, 820, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14908, 821, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14909, 822, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14910, 823, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14911, 824, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14912, 825, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14913, 826, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14914, 827, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14915, 828, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14916, 829, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14917, 830, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14918, 831, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14919, 832, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14920, 833, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14921, 834, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14922, 835, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14923, 836, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14924, 837, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14925, 838, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14926, 839, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14927, 840, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14928, 841, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14929, 842, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14930, 843, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14931, 844, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14932, 845, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14933, 846, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14934, 847, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14935, 848, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14936, 849, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14937, 850, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14938, 851, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14939, 852, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14940, 853, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14941, 854, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14942, 855, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14943, 856, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14944, 857, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14945, 858, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14946, 859, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14947, 860, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14948, 861, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14949, 862, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14950, 863, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14951, 864, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14952, 865, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14953, 866, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14954, 867, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14955, 868, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14956, 869, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14957, 870, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14958, 871, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14959, 872, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14960, 873, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14961, 874, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14962, 875, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14963, 876, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14964, 877, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14965, 878, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14966, 879, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14967, 880, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14968, 881, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14969, 882, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14970, 883, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14971, 884, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14972, 885, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14973, 886, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14974, 887, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14975, 888, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14976, 889, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14977, 890, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14978, 891, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14979, 892, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14980, 893, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14981, 894, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14982, 895, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14983, 896, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14984, 897, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14985, 898, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14986, 899, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14987, 900, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14988, 901, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14989, 902, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14990, 903, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14991, 904, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14992, 905, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14993, 906, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14994, 907, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14995, 908, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14996, 909, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14997, 910, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14998, 911, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (14999, 912, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15000, 913, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15001, 914, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15002, 915, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15003, 916, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15004, 917, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15005, 918, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15006, 919, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15007, 920, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15008, 921, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15009, 922, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15010, 923, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15011, 924, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15012, 925, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15013, 926, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15014, 927, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15015, 928, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15016, 929, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15017, 930, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15018, 931, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15019, 932, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15020, 933, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15021, 934, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15022, 935, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15023, 936, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15024, 937, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15025, 938, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15026, 939, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15027, 940, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15028, 941, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15029, 942, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15030, 943, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15031, 944, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15032, 945, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15033, 946, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15034, 947, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15035, 948, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15036, 949, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15037, 950, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15038, 951, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15039, 952, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15040, 953, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15041, 954, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15042, 955, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15043, 956, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15044, 957, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15045, 958, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15046, 959, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15047, 960, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15048, 961, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15049, 962, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15050, 963, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15051, 964, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15052, 965, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15053, 966, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15054, 967, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15055, 968, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15056, 969, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15057, 970, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15058, 971, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15059, 972, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15060, 973, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15061, 974, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15062, 975, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15063, 976, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15064, 977, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15065, 978, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15066, 979, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15067, 980, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15068, 981, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15069, 982, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15070, 983, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15071, 984, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15072, 985, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15073, 986, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15074, 987, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15075, 988, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15076, 989, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15077, 990, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15078, 991, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15079, 992, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15080, 993, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15081, 994, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15082, 995, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15083, 996, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15084, 997, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15085, 998, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15086, 999, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15087, 1000, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15088, 1001, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15089, 1002, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15090, 1003, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15091, 1004, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15092, 1005, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15093, 1006, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15094, 1007, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15095, 1008, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15096, 1009, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15097, 1010, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15098, 1011, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15099, 1012, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15100, 1013, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15101, 1014, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15102, 1015, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15103, 1016, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15104, 1017, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15105, 1018, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15106, 1019, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15107, 1020, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15108, 1021, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15109, 1022, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15110, 1023, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15111, 1024, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15112, 1025, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15113, 1026, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15114, 1027, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15115, 1028, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15116, 1029, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15117, 1030, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15118, 1031, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15119, 1032, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15120, 1033, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15121, 1034, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15122, 1035, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15123, 1036, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15124, 1037, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15125, 1038, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15126, 1039, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15127, 1040, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15128, 1041, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15129, 1042, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15130, 1043, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15131, 1044, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15132, 1045, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15133, 1046, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15134, 1047, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15135, 1048, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15136, 1049, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15137, 1050, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15138, 1051, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15139, 1052, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15140, 1053, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15141, 1054, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15142, 1055, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15143, 1056, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15144, 1057, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15145, 1058, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15146, 1059, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15147, 1060, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15148, 1061, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15149, 1062, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15150, 1063, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15151, 1064, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15152, 1065, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15153, 1066, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15154, 1067, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15155, 1068, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15156, 1069, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15157, 1070, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15158, 1071, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15159, 1072, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15160, 1073, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15161, 1074, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15162, 1075, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15163, 1076, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15164, 1077, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15165, 1078, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15166, 1079, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15167, 1080, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15168, 1081, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15169, 1082, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15170, 1083, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15171, 1084, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15172, 1085, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15173, 1086, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15174, 1087, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15175, 1088, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15176, 1089, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15177, 1090, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15178, 1091, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15179, 1092, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15180, 1093, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15181, 1094, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15182, 1095, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15183, 1096, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15184, 1097, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15185, 1098, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15186, 1099, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15187, 1100, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15188, 1101, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15189, 1102, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15190, 1103, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15191, 1104, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15192, 1105, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15193, 1106, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15194, 1107, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15195, 1108, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15196, 1109, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15197, 1110, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15198, 1111, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15199, 1112, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15200, 1113, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15201, 1114, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15202, 1115, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15203, 1116, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15204, 1117, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15205, 1118, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15206, 1119, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15207, 1120, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15208, 1121, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15209, 1122, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15210, 1123, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15211, 1124, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15212, 1125, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15213, 1126, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15214, 1127, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15215, 1128, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15216, 1129, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15217, 1130, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15218, 1131, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15219, 1132, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15220, 1133, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15221, 1134, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15222, 1135, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15223, 1136, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15224, 1137, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15225, 1138, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15226, 1139, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15227, 1140, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15228, 1141, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15229, 1142, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15230, 1143, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15231, 1144, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15232, 1145, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15233, 1146, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15234, 1147, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15235, 1148, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15236, 1149, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15237, 1150, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15238, 1151, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15239, 1152, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15240, 1153, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15241, 1154, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15242, 1155, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15243, 1156, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15244, 1157, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15245, 1158, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15246, 1159, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15247, 1160, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15248, 1161, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15249, 1162, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15250, 1163, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15251, 1164, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15252, 1165, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15253, 1166, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15254, 1167, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15255, 1168, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15256, 1169, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15257, 1170, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15258, 1171, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15259, 1172, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15260, 1173, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15261, 1174, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15262, 1175, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15263, 1176, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15264, 1177, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15265, 1178, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15266, 1179, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15267, 1180, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15268, 1181, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15269, 1182, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15270, 1183, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15271, 1184, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15272, 1185, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15273, 1186, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15274, 1187, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15275, 1188, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15276, 1189, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15277, 1190, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15278, 1191, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15279, 1192, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15280, 1193, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15281, 1194, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15282, 1195, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15283, 1196, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15284, 1197, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15285, 1198, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15286, 1199, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15287, 1200, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15288, 1201, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15289, 1202, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15290, 1203, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15291, 1204, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15292, 1205, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15293, 1206, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15294, 1207, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15295, 1208, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15296, 1209, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15297, 1210, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15298, 1211, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15299, 1212, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15300, 1213, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15301, 1214, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15302, 1215, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15303, 1216, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15304, 1217, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15305, 1218, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15306, 1219, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15307, 1220, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15308, 1221, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15309, 1222, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15310, 1223, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15311, 1224, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15312, 1225, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15313, 1226, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15314, 1227, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15315, 1228, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15316, 1229, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15317, 1230, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15318, 1231, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15319, 1232, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15320, 1233, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15321, 1234, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15322, 1235, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15323, 1236, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15324, 1237, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15325, 1238, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15326, 1239, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15327, 1240, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15328, 1241, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15329, 1242, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15330, 1243, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15331, 1244, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15332, 1245, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15333, 1246, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15334, 1247, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15335, 1248, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15336, 1249, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15337, 1250, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15338, 1251, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15339, 1252, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15340, 1253, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15341, 1254, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15342, 1255, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15343, 1256, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15344, 1257, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15345, 1258, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15346, 1259, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15347, 1260, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15348, 1261, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15349, 1262, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15350, 1263, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15351, 1264, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15352, 1265, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15353, 1266, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15354, 1267, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15355, 1268, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15356, 1269, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15357, 1270, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15358, 1271, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15359, 1272, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15360, 1273, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15361, 1274, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15362, 1275, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15363, 1276, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15364, 1277, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15365, 1278, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15366, 1279, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15367, 1280, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15368, 1281, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15369, 1282, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15370, 1283, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15371, 1284, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15372, 1285, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15373, 1286, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15374, 1287, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15375, 1288, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15376, 1289, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15377, 1290, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15378, 1291, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15379, 1292, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15380, 1293, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15381, 1294, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15382, 1295, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15383, 1296, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15384, 1297, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15385, 1298, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15386, 1299, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15387, 1300, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15388, 1301, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15389, 1302, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15390, 1303, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15391, 1304, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15392, 1305, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15393, 1306, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15394, 1307, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15395, 1308, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15396, 1309, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15397, 1310, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15398, 1311, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15399, 1312, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15400, 1313, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15401, 1314, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15402, 1315, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15403, 1316, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15404, 1317, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15405, 1318, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15406, 1319, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15407, 1320, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15408, 1321, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15409, 1322, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15410, 1323, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15411, 1324, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15412, 1325, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15413, 1326, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15414, 1327, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15415, 1328, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15416, 1329, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15417, 1330, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15418, 1331, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15419, 1332, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15420, 1333, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15421, 1334, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15422, 1335, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15423, 1336, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15424, 1337, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15425, 1338, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15426, 1339, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15427, 1340, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15428, 1341, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15429, 1342, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15430, 1343, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15431, 1344, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15432, 1345, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15433, 1346, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15434, 1347, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15435, 1348, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15436, 1349, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15437, 1350, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15438, 1351, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15439, 1352, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15440, 1353, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15441, 1354, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15442, 1355, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15443, 1356, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15444, 1357, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15445, 1358, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15446, 1359, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15447, 1360, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15448, 1361, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15449, 1362, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15450, 1363, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15451, 1364, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15452, 1365, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15453, 1366, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15454, 1367, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15455, 1368, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15456, 1369, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15457, 1370, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15458, 1371, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15459, 1372, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15460, 1373, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15461, 1374, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15462, 1375, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15463, 1376, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15464, 1377, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15465, 1378, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15466, 1379, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15467, 1380, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15468, 1381, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15469, 1382, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15470, 1383, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15471, 1384, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15472, 1385, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15473, 1386, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15474, 1387, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15475, 1388, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15476, 1389, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15477, 1390, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15478, 1391, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15479, 1392, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15480, 1393, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15481, 1394, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15482, 1395, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15483, 1396, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15484, 1397, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15485, 1398, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15486, 1399, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15487, 1400, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15488, 1401, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15489, 1402, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15490, 1403, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15491, 1404, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15492, 1405, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15493, 1406, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15494, 1407, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15495, 1408, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15496, 1409, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15497, 1410, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15498, 1411, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15499, 1412, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15500, 1413, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15501, 1414, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15502, 1415, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15503, 1416, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15504, 1417, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15505, 1418, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15506, 1419, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15507, 1420, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15508, 1421, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15509, 1422, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15510, 1423, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15511, 1424, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15512, 1425, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15513, 1426, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15514, 1427, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15515, 1428, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15516, 1429, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15517, 1430, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15518, 1431, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15519, 1432, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15520, 1433, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15521, 1434, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15522, 1435, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15523, 1436, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15524, 1437, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15525, 1438, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15526, 1439, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15527, 1440, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15528, 1441, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15529, 1442, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15530, 1443, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15531, 1444, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15532, 1445, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15533, 1446, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15534, 1447, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15535, 1448, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15536, 1449, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15537, 1450, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15538, 1451, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15539, 1452, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15540, 1453, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15541, 1454, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15542, 1455, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15543, 1456, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15544, 1457, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15545, 1458, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15546, 1459, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15547, 1460, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15548, 1461, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15549, 1462, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15550, 1463, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15551, 1464, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15552, 1465, 87, 11706, 1018422, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15553, 1466, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15554, 1467, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15555, 1468, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15556, 1469, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15557, 1470, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15558, 1471, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15559, 1472, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15560, 1473, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15561, 1474, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15562, 1475, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15563, 1476, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15564, 1477, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15565, 1478, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15566, 1479, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15567, 1480, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15568, 1481, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15569, 1482, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15570, 1483, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15571, 1484, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15572, 1485, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15573, 1486, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15574, 1487, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15575, 1488, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15576, 1489, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15577, 1490, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15578, 1491, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15579, 1492, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15580, 1493, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15581, 1494, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15582, 1495, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15583, 1496, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15584, 1497, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15585, 1498, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15586, 1499, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15587, 1500, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15588, 1501, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15589, 1502, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15590, 1503, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15591, 1504, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15592, 1505, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15593, 1506, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15594, 1507, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15595, 1508, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15596, 1509, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15597, 1510, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15598, 1511, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15599, 1512, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15600, 1513, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15601, 1514, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15602, 1515, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15603, 1516, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15604, 1517, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15605, 1518, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15606, 1519, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15607, 1520, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15608, 1521, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15609, 1522, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15610, 1523, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15611, 1524, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15612, 1525, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15613, 1526, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15614, 1527, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15615, 1528, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15616, 1529, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15617, 1530, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15618, 1531, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15619, 1532, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15620, 1533, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15621, 1534, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15622, 1535, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15623, 1536, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15624, 1537, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15625, 1538, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15626, 1539, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15627, 1540, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15628, 1541, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15629, 1542, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15630, 1543, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15631, 1544, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15632, 1545, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15633, 1546, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15634, 1547, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15635, 1548, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15636, 1549, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15637, 1550, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15638, 1551, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15639, 1552, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15640, 1553, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15641, 1554, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15642, 1555, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15643, 1556, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15644, 1557, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15645, 1558, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15646, 1559, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15647, 1560, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15648, 1561, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15649, 1562, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15650, 1563, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15651, 1564, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15652, 1565, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15653, 1566, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15654, 1567, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15655, 1568, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15656, 1569, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15657, 1570, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15658, 1571, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15659, 1572, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15660, 1573, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15661, 1574, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15662, 1575, 72, 6635, 477720, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15663, 1576, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15664, 1577, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15665, 1578, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15666, 1579, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15667, 1580, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15668, 1581, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15669, 1582, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15670, 1583, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15671, 1584, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15672, 1585, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15673, 1586, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15674, 1587, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15675, 1588, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15676, 1589, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15677, 1590, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15678, 1591, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15679, 1592, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15680, 1593, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15681, 1594, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15682, 1595, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15683, 1596, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15684, 1597, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15685, 1598, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15686, 1599, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15687, 1600, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15688, 1601, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15689, 1602, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15690, 1603, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15691, 1604, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15692, 1605, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15693, 1606, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15694, 1607, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15695, 1608, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15696, 1609, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15697, 1610, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15698, 1611, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15699, 1612, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15700, 1613, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15701, 1614, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15702, 1615, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15703, 1616, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15704, 1617, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15705, 1618, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15706, 1619, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15707, 1620, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15708, 1621, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15709, 1622, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15710, 1623, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15711, 1624, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15712, 1625, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15713, 1626, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15714, 1627, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15715, 1628, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15716, 1629, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15717, 1630, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15718, 1631, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15719, 1632, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15720, 1633, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15721, 1634, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15722, 1635, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15723, 1636, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15724, 1637, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15725, 1638, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15726, 1639, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15727, 1640, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15728, 1641, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15729, 1642, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15730, 1643, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15731, 1644, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15732, 1645, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15733, 1646, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15734, 1647, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15735, 1648, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15736, 1649, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15737, 1650, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15738, 1651, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15739, 1652, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15740, 1653, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15741, 1654, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15742, 1655, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15743, 1656, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15744, 1657, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15745, 1658, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15746, 1659, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15747, 1660, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15748, 1661, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15749, 1662, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15750, 1663, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15751, 1664, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15752, 1665, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15753, 1666, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15754, 1667, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15755, 1668, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15756, 1669, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15757, 1670, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15758, 1671, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15759, 1672, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15760, 1673, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15761, 1674, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15762, 1675, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15763, 1676, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15764, 1677, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15765, 1678, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15766, 1679, 92, 13843, 1273556, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15767, 1680, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15768, 1681, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15769, 1682, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15770, 1683, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15771, 1684, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15772, 1685, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15773, 1686, 82, 9802, 803764, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15774, 1687, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15775, 1688, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15776, 1689, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15777, 1690, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15778, 1691, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15779, 1692, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15780, 1693, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15781, 1694, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15782, 1695, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15783, 1696, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15784, 1697, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15785, 1698, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15786, 1699, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15787, 1700, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15788, 1701, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15789, 1702, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15790, 1703, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15791, 1704, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15792, 1705, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15793, 1706, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15794, 1707, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15795, 1708, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15796, 1709, 66, 5111, 337326, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15797, 1710, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15798, 1711, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15799, 1712, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15800, 1713, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15801, 1714, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15802, 1715, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15803, 1716, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15804, 1717, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15805, 1718, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15806, 1719, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15807, 1720, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15808, 1721, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15809, 1722, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15810, 1723, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15811, 1724, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15812, 1725, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15813, 1726, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15814, 1727, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15815, 1728, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15816, 1729, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15817, 1730, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15818, 1731, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15819, 1732, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15820, 1733, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15821, 1734, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15822, 1735, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15823, 1736, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15824, 1737, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15825, 1738, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15826, 1739, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15827, 1740, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15828, 1741, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15829, 1742, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15830, 1743, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15831, 1744, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15832, 1745, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15833, 1746, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15834, 1747, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15835, 1748, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15836, 1749, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15837, 1750, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15838, 1751, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15839, 1752, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15840, 1753, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15841, 1754, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15842, 1755, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15843, 1756, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15844, 1757, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15845, 1758, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15846, 1759, 89, 12532, 1115348, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15847, 1760, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15848, 1761, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15849, 1762, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15850, 1763, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15851, 1764, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15852, 1765, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15853, 1766, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15854, 1767, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15855, 1768, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15856, 1769, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15857, 1770, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15858, 1771, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15859, 1772, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15860, 1773, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15861, 1774, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15862, 1775, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15863, 1776, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15864, 1777, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15865, 1778, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15866, 1779, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15867, 1780, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15868, 1781, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15869, 1782, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15870, 1783, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15871, 1784, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15872, 1785, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15873, 1786, 68, 5589, 380052, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15874, 1787, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15875, 1788, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15876, 1789, 43, 1413, 60759, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15877, 1790, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15878, 1791, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15879, 1792, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15880, 1793, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15881, 1794, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15882, 1795, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15883, 1796, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15884, 1797, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15885, 1798, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15886, 1799, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15887, 1800, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15888, 1801, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15889, 1802, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15890, 1803, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15891, 1804, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15892, 1805, 84, 10536, 885024, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15893, 1806, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15894, 1807, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15895, 1808, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15896, 1809, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15897, 1810, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15898, 1811, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15899, 1812, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15900, 1813, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15901, 1814, 57, 3292, 187644, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15902, 1815, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15903, 1816, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15904, 1817, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15905, 1818, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15906, 1819, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15907, 1820, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15908, 1821, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15909, 1822, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15910, 1823, 79, 8765, 692435, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15911, 1824, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15912, 1825, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15913, 1826, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15914, 1827, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15915, 1828, 96, 15728, 1509888, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15916, 1829, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15917, 1830, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15918, 1831, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15919, 1832, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15920, 1833, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15921, 1834, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15922, 1835, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15923, 1836, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15924, 1837, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15925, 1838, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15926, 1839, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15927, 1840, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15928, 1841, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15929, 1842, 27, 349, 9423, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15930, 1843, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15931, 1844, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15932, 1845, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15933, 1846, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15934, 1847, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15935, 1848, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15936, 1849, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15937, 1850, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15938, 1851, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15939, 1852, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15940, 1853, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15941, 1854, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15942, 1855, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15943, 1856, 98, 16732, 1639736, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15944, 1857, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15945, 1858, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15946, 1859, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15947, 1860, 36, 829, 29844, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15948, 1861, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15949, 1862, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15950, 1863, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15951, 1864, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15952, 1865, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15953, 1866, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15954, 1867, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15955, 1868, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15956, 1869, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15957, 1870, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15958, 1871, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15959, 1872, 51, 2358, 120258, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15960, 1873, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15961, 1874, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15962, 1875, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15963, 1876, 44, 1514, 66616, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15964, 1877, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15965, 1878, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15966, 1879, 39, 1054, 41106, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15967, 1880, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15968, 1881, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15969, 1882, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15970, 1883, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15971, 1884, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15972, 1885, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15973, 1886, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15974, 1887, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15975, 1888, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15976, 1889, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15977, 1890, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15978, 1891, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15979, 1892, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15980, 1893, 35, 762, 26670, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15981, 1894, 29, 433, 12557, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15982, 1895, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15983, 1896, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15984, 1897, 71, 6362, 451702, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15985, 1898, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15986, 1899, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15987, 1900, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15988, 1901, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15989, 1902, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15990, 1903, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15991, 1904, 76, 7804, 593104, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15992, 1905, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15993, 1906, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15994, 1907, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15995, 1908, 41, 1225, 50225, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15996, 1909, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15997, 1910, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15998, 1911, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (15999, 1912, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16000, 1913, 38, 975, 37050, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16001, 1914, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16002, 1915, 31, 529, 16399, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16003, 1916, 48, 1966, 94368, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16004, 1917, 90, 12959, 1166310, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16005, 1918, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16006, 1919, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16007, 1920, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16008, 1921, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16009, 1922, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16010, 1923, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16011, 1924, 45, 1619, 72855, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16012, 1925, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16013, 1926, 50, 2222, 111100, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16014, 1927, 24, 245, 5880, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16015, 1928, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16016, 1929, 22, 189, 4158, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16017, 1930, 40, 1137, 45480, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16018, 1931, 80, 9102, 728160, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16019, 1932, 85, 10917, 927945, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16020, 1933, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16021, 1934, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16022, 1935, 25, 277, 6925, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16023, 1936, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16024, 1937, 21, 164, 3444, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16025, 1938, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16026, 1939, 91, 13396, 1219036, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16027, 1940, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16028, 1941, 34, 698, 23732, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16029, 1942, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16030, 1943, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16031, 1944, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16032, 1945, 97, 16225, 1573825, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16033, 1946, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16034, 1947, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16035, 1948, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16036, 1949, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16037, 1950, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16038, 1951, 74, 7203, 533022, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16039, 1952, 67, 5346, 358182, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16040, 1953, 63, 4445, 280035, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16041, 1954, 26, 312, 8112, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16042, 1955, 49, 2091, 102459, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16043, 1956, 69, 5840, 402960, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16044, 1957, 32, 582, 18624, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16045, 1958, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16046, 1959, 73, 6915, 504795, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16047, 1960, 100, 17777, 1777700, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16048, 1961, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16049, 1962, 70, 6097, 426790, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16050, 1963, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16051, 1964, 75, 7499, 562425, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16052, 1965, 23, 216, 4968, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16053, 1966, 77, 8116, 624932, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16054, 1967, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16055, 1968, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16056, 1969, 54, 2799, 151146, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16057, 1970, 52, 2499, 129948, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16058, 1971, 53, 2646, 140238, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16059, 1972, 86, 11307, 972402, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16060, 1973, 33, 638, 21054, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16061, 1974, 60, 3839, 230340, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16062, 1975, 28, 390, 10920, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16063, 1976, 62, 4236, 262632, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16064, 1977, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16065, 1978, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16066, 1979, 30, 479, 14370, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16067, 1980, 61, 4035, 246135, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16068, 1981, 58, 3468, 201144, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16069, 1982, 81, 9447, 765207, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16070, 1983, 55, 2957, 162635, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16071, 1984, 47, 1845, 86715, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16072, 1985, 88, 12115, 1066120, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16073, 1986, 20, 142, 2840, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16074, 1987, 37, 900, 33300, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16075, 1988, 46, 1730, 79580, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16076, 1989, 95, 15242, 1447990, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16077, 1990, 59, 3651, 215409, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16078, 1991, 42, 1317, 55314, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16079, 1992, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16080, 1993, 56, 3122, 174832, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16081, 1994, 94, 14765, 1387910, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16082, 1995, 65, 4882, 317330, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16083, 1996, 83, 10165, 843695, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16084, 1997, 93, 14299, 1329807, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16085, 1998, 78, 8436, 658008, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16086, 1999, 64, 4660, 298240, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16087, 2000, 99, 17249, 1707651, true, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16088, 1, 22, 189, 0, false, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16089, 2, 67, 5346, 0, false, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16090, 3, 52, 2499, 0, false, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16091, 4, 46, 1730, 0, false, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16092, 5, 37, 900, 0, false, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16093, 6, 70, 6097, 0, false, 271420);
INSERT INTO "dAuction2_distribution" VALUES (16094, 7, 43, 1413, 0, false, 271420);


--
-- Name: dAuction2_distribution_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_distribution_id_seq"', 16094, true);


--
-- Data for Name: dAuction2_group; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_group" VALUES (22, 1, 271420);


--
-- Name: dAuction2_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_group_id_seq"', 22, true);


--
-- Data for Name: dAuction2_period; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_period" VALUES (46, 3, '2017-11-10 14:34:08.863753+00', false, 271420);
INSERT INTO "dAuction2_period" VALUES (47, 4, '2017-11-10 14:34:09.014975+00', false, 271420);
INSERT INTO "dAuction2_period" VALUES (48, 5, '2017-11-10 14:34:09.152332+00', false, 271420);
INSERT INTO "dAuction2_period" VALUES (49, 6, '2017-11-10 14:34:09.284886+00', false, 271420);
INSERT INTO "dAuction2_period" VALUES (50, 7, '2017-11-10 14:34:09.380685+00', false, 271420);
INSERT INTO "dAuction2_period" VALUES (44, 1, '2017-11-10 14:41:00.061317+00', true, 271420);
INSERT INTO "dAuction2_period" VALUES (45, 2, '2017-11-10 14:41:00.119102+00', false, 271420);


--
-- Data for Name: dAuction2_phase; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_phase" VALUES (35, 1, true, 1, false, false, '2017-11-10 14:34:23.447254+00', 271420, 44);
INSERT INTO "dAuction2_phase" VALUES (36, 2, true, 1, false, true, '2017-11-10 14:39:02.405696+00', 271420, 44);
INSERT INTO "dAuction2_phase" VALUES (37, 1, false, 1, false, false, '2017-11-10 14:41:00.113034+00', 271420, 45);


--
-- Data for Name: dAuction2_user; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_user" VALUES (3, 'plain$$u03', NULL, false, 'u03', '', '', '', false, true, '2017-11-01 09:56:42.810801+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (4, 'plain$$u04', NULL, false, 'u04', '', '', '', false, true, '2017-11-01 09:56:42.87625+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (5, 'plain$$u05', NULL, false, 'u05', '', '', '', false, true, '2017-11-01 09:56:42.906702+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (6, 'plain$$u06', NULL, false, 'u06', '', '', '', false, true, '2017-11-01 09:56:42.928679+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (7, 'plain$$u07', NULL, false, 'u07', '', '', '', false, true, '2017-11-01 09:56:42.989395+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (8, 'plain$$u08', NULL, false, 'u08', '', '', '', false, true, '2017-11-01 09:56:43.026792+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (9, 'plain$$u09', NULL, false, 'u09', '', '', '', false, true, '2017-11-01 09:56:43.043213+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (10, 'plain$$u10', NULL, false, 'u10', '', '', '', false, true, '2017-11-01 09:56:43.061384+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (11, 'plain$$u11', NULL, false, 'u11', '', '', '', false, true, '2017-11-01 09:56:43.121786+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (12, 'plain$$u12', NULL, false, 'u12', '', '', '', false, true, '2017-11-01 09:56:43.144808+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (13, 'plain$$u13', NULL, false, 'u13', '', '', '', false, true, '2017-11-01 09:56:43.173477+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (14, 'plain$$u14', NULL, false, 'u14', '', '', '', false, true, '2017-11-01 09:56:43.197209+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (15, 'plain$$u15', NULL, false, 'u15', '', '', '', false, true, '2017-11-01 09:56:43.243925+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (16, 'plain$$u16', NULL, false, 'u16', '', '', '', false, true, '2017-11-01 09:56:43.270218+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (17, 'plain$$u17', NULL, false, 'u17', '', '', '', false, true, '2017-11-01 09:56:43.3009+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (18, 'plain$$u18', NULL, false, 'u18', '', '', '', false, true, '2017-11-01 09:56:43.344892+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (19, 'plain$$u19', NULL, false, 'u19', '', '', '', false, true, '2017-11-01 09:56:43.372157+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (20, 'plain$$u20', NULL, false, 'u20', '', '', '', false, true, '2017-11-01 09:56:43.440826+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (21, 'plain$$u21', NULL, false, 'u21', '', '', '', false, true, '2017-11-01 09:56:43.463653+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (22, 'plain$$u22', NULL, false, 'u22', '', '', '', false, true, '2017-11-01 09:56:43.539593+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (23, 'plain$$u23', NULL, false, 'u23', '', '', '', false, true, '2017-11-01 09:56:43.567135+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (24, 'plain$$u24', NULL, false, 'u24', '', '', '', false, true, '2017-11-01 09:56:43.593567+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (25, 'plain$$u25', NULL, false, 'u25', '', '', '', false, true, '2017-11-01 09:56:43.636253+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (26, 'plain$$u26', NULL, false, 'u26', '', '', '', false, true, '2017-11-01 09:56:43.66151+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (27, 'plain$$u27', NULL, false, 'u27', '', '', '', false, true, '2017-11-01 09:56:43.685184+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (28, 'plain$$u28', NULL, false, 'u28', '', '', '', false, true, '2017-11-01 09:56:43.744154+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (29, 'plain$$u29', NULL, false, 'u29', '', '', '', false, true, '2017-11-01 09:56:43.769274+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (30, 'plain$$u30', NULL, false, 'u30', '', '', '', false, true, '2017-11-01 09:56:43.796043+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (31, 'plain$$u31', NULL, false, 'u31', '', '', '', false, true, '2017-11-01 09:56:43.853147+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (32, 'plain$$u32', NULL, false, 'u32', '', '', '', false, true, '2017-11-01 09:56:43.945266+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (33, 'plain$$u33', NULL, false, 'u33', '', '', '', false, true, '2017-11-01 09:56:43.973872+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (34, 'plain$$u34', NULL, false, 'u34', '', '', '', false, true, '2017-11-01 09:56:43.997932+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (35, 'plain$$u35', NULL, false, 'u35', '', '', '', false, true, '2017-11-01 09:56:44.061271+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (36, 'plain$$u36', NULL, false, 'u36', '', '', '', false, true, '2017-11-01 09:56:44.089478+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (37, 'plain$$u37', NULL, false, 'u37', '', '', '', false, true, '2017-11-01 09:56:44.161329+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (38, 'plain$$u38', NULL, false, 'u38', '', '', '', false, true, '2017-11-01 09:56:44.182109+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (39, 'plain$$u39', NULL, false, 'u39', '', '', '', false, true, '2017-11-01 09:56:44.262041+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (40, 'plain$$u40', NULL, false, 'u40', '', '', '', false, true, '2017-11-01 09:56:44.285109+00', 1, false, false, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (99, 'plain$$admin', '2017-11-01 09:56:50.808262+00', true, 'admin', '', '', '', true, true, '2017-11-01 09:56:42.68941+00', 1, false, true, false, '2002-12-04 00:00:00+00', -1, '');
INSERT INTO "dAuction2_user" VALUES (2, 'plain$$u02', '2017-11-09 15:41:18.683772+00', false, 'u02', '', '', '', false, true, '2017-11-01 09:56:42.790143+00', 5, false, true, false, '2002-12-04 00:00:00+00', -1, '0.5');
INSERT INTO "dAuction2_user" VALUES (1, 'plain$$u01', '2017-11-09 15:41:11.124435+00', false, 'u01', '', '', '', false, true, '2017-11-01 09:56:42.732017+00', 5, false, true, false, '2002-12-04 00:00:00+00', -1, '0.5');


--
-- Data for Name: dAuction2_player; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_player" VALUES (200, 5, 2, 1, false, 0, 1, false, 0, 0, 0, true, '', 0, '2002-12-04 00:00:00+00', 1, 1, 858, 2070, 0, 858, 1, 1, 858, 0, 0, true, '', '', true, 0, false, 0, 0, 0, '', '', 271420, 22, 1, 0, 1716);
INSERT INTO "dAuction2_player" VALUES (199, 5, 2, 1, false, 0, 1, false, 0, 0, 0, true, '', 0, '2002-12-04 00:00:00+00', 1, 0, 1160, 930, 0, 1160, 1, 1, 1160, 0, 0, true, '', '', true, 0, false, 0, 0, 0, '', '', 271420, 22, 2, 0, 580);


--
-- Data for Name: dAuction2_offer; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_offer" VALUES (724, '2017-11-10 14:39:22.030495+00', '2017-11-10 14:39:21.954883+00', 0, false, true, false, 0, 22, 100, 100, 2200, 271420, 22, 36, 199);
INSERT INTO "dAuction2_offer" VALUES (723, '2017-11-10 14:39:13.110982+00', '2017-11-10 14:39:21.954894+00', 1, false, true, false, 0, 22, 100, 100, -2200, 271420, 22, 36, 200);


--
-- Name: dAuction2_offer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_offer_id_seq"', 724, true);


--
-- Data for Name: dAuction2_question; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_question" VALUES (1, 'Given the distribution in the picture below, what is the probability that the MARKET UNITS DEMANDED is equal or larger than 60?', 'y', 'staticfiles/images/DR_M60_SD20.jpg', '419', '751', 1);
INSERT INTO "dAuction2_question" VALUES (2, 'When drawing the MARKET UNITS REQUIRED from the distribution below, what is the probability that an outcome between 40 and 80 is chose?', 'y', 'staticfiles/images/DR_M60_SD20.jpg', '419', '751', 1);
INSERT INTO "dAuction2_question" VALUES (3, 'What is the expected number of MARKET UNITS DEMANDED for the distribution below? In other words, what is the average of MARKET UNITS DEMANDED if we drew this number many times randomly from the distribution below?', 'y', 'staticfiles/images/DR_M60_SD20.jpg', '419', '751', 1);
INSERT INTO "dAuction2_question" VALUES (4, 'What is approximately (allowing for a possible rounding error) the expected price for the distribution of prices below? In other words, what is the average of prices if we drew them many times randomly from the distribution below?', 'y', 'staticfiles/images/DR_M60_SD20.jpg', '419', '751', 1);
INSERT INTO "dAuction2_question" VALUES (5, 'Look at the Offer Overview in the picture below. Given the offers at this moment, what is the cheapest price for which you can buy 1 unit?', 'y', 'staticfiles/images/testing01.png', '440', '360', 1);
INSERT INTO "dAuction2_question" VALUES (6, 'Look at the Offer Overview in the picture below. Given the offers at this moment, what is the highest price for which you can sell 1 unit?', 'y', 'staticfiles/images/testing01.png', '500', '400', 1);
INSERT INTO "dAuction2_question" VALUES (7, 'Look at the Offer Overview in the picture below. Given the offers at this moment, what is the cheapest price for which you can buy 1 unit?', 'y', 'staticfiles/images/testing02.png', '500', '400', 1);
INSERT INTO "dAuction2_question" VALUES (8, 'Look at the Offer Overview in the picture below. Given the offers at this moment, what is the highest price for which you can sell 1 unit?', 'y', 'staticfiles/images/testing02.png', '500', '400', 1);
INSERT INTO "dAuction2_question" VALUES (9, 'Look at the Offer Overview in the picture below. Given the offers at this moment, if I submit a SELL offer of 3 units for a price of 1, how many units do I sell?', 'y', 'staticfiles/images/testing02.png', '500', '400', 1);
INSERT INTO "dAuction2_question" VALUES (10, 'Look at the Offer Overview in the picture below. Given the offers at this moment, we determined before that if I submit a SELL offer of 3 units for a price of 1, I will sell 3 units. For what price(s) will I sell these 3 units?', 'y', 'staticfiles/images/testing02.png', '500', '450', 1);
INSERT INTO "dAuction2_question" VALUES (11, 'Look at the Offer Overview in the picture below. Given the offers at this moment, if I submit a BUY offer of 2 units for a price of 7, how many units do I buy?', 'y', 'staticfiles/images/testing02.png', '500', '450', 1);
INSERT INTO "dAuction2_question" VALUES (12, 'Look at the Offer Overview in the picture below. Given the offers at this moment, we determined before that if I submit a BUY offer of 2 units for a price of 7, I will buy 2 units. For what price(s) will I buy these 2 units?', 'y', 'staticfiles/images/testing02.png', '500', '450', 1);
INSERT INTO "dAuction2_question" VALUES (13, 'Look at the Offer Overview in the picture below. Given the offers at this moment, if I submit a BUY offer of 5 units for a price of 7, what will be the result?', 'y', 'staticfiles/images/testing02.png', '500', '450', 1);
INSERT INTO "dAuction2_question" VALUES (14, 'Look at the Earnings Overview for the first 10 units in the picture below. At the moment the Retailer hasn''t bought any units now. If the Retailer now successfully buys 5 units, what will be the number of the last unit that will be used (and thus marked with a cross)? (Thus, give the highest unit number that will still have a cross).', 'y', 'staticfiles/images/testing13.png', '400', '300', 1);
INSERT INTO "dAuction2_question" VALUES (15, 'Look at the Production Cost for the first 10 units in the picture below. If the Producer now successfully BUYS 2 units, what will be the number of the last unit that will be used (and marked with a cross)? (Thus, give the highest unit number that will still have a cross).', 'y', 'staticfiles/images/testing14.png', '400', '300', 1);
INSERT INTO "dAuction2_question" VALUES (16, 'Look at the Earnings Overview for the first 10 units in the picture below. If the Retailer now successfully SELLS 5 units, what will then be the number of his/her FIRST unit?', 'y', 'staticfiles/images/testing15.png', '400', '300', 1);
INSERT INTO "dAuction2_question" VALUES (17, 'Look at the Earnings Overview for the first 10 units in the picture below. If the Retailer now successfully buys 5 units, what will be the number of the last unit that will be used (and marked with a cross)? (Thus, give the highest unit number that will still have a cross).', 'y', 'staticfiles/images/testing16.png', '400', '300', 1);
INSERT INTO "dAuction2_question" VALUES (18, 'If in a round the MARKET UNITS DEMANDED is equal to 42, and there are four Retailers, what will be the UNITS DEMANDED for the retailers?', '', '', '250', '500', 1);
INSERT INTO "dAuction2_question" VALUES (19, 'If in Stage 2 a Retailer has bought (or a Producer has sold) more units than the number of UNITS DEMANDED. What can the Retailer (or Producer) do to increase profits?', '', '', '250', '500', 1);


--
-- Data for Name: dAuction2_option_mc; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_option_mc" VALUES (1, 1, '0%', false, 'As you can see in the graph, it happens frequently that the number of required units is larger than 60. Thus 0% cannot be correct.', '', '125', '500', 1);
INSERT INTO "dAuction2_option_mc" VALUES (2, 2, '25%', false, 'As you can see in the graph, the area on the right of 60 is as large as the area to the left of 60.', '', '125', '500', 1);
INSERT INTO "dAuction2_option_mc" VALUES (3, 3, '50%', true, 'As you can see in the graph, the area on the right of 60 is as large as the area to the left of 60. The probability of the number of required units being equal or larger than 60 is therefore 50%', '', '125', '500', 1);
INSERT INTO "dAuction2_option_mc" VALUES (4, 4, '75%', false, 'As you can see in the graph, the area on the right of 60 is as large as the area to the left of 60.', '', '125', '500', 1);
INSERT INTO "dAuction2_option_mc" VALUES (5, 5, '100%', false, 'As you can see in the graph, it happens frequently that the number of required units is smaller than 60. Thus 100% cannot be correct.', '', '125', '500', 1);
INSERT INTO "dAuction2_option_mc" VALUES (6, 1, '20%', false, 'The probability mass of outcomes between 40 and 80 is more than 20% of the total probability mass.', '', '125', '500', 2);
INSERT INTO "dAuction2_option_mc" VALUES (7, 2, '30%', false, 'The probability mass of outcomes between 40 and 80 is more than 30% of the total probability mass.', '', '125', '500', 2);
INSERT INTO "dAuction2_option_mc" VALUES (8, 3, '40%', false, 'The probability mass of outcomes between 40 and 80 is more than 40% of the total probability mass.', '', '125', '500', 2);
INSERT INTO "dAuction2_option_mc" VALUES (9, 4, '50%', true, 'The probability mass of outcomes between 40 and 80 is half the probability mass of the all outcomes (between 20 and 100). The probability of an outcome between 40 and 80 is thus indeed 50 %.', '', '125', '500', 2);
INSERT INTO "dAuction2_option_mc" VALUES (10, 5, '60%', false, 'The probability mass of outcomes between 40 and 80 is less than 60% of the total probability mass.', '', '125', '500', 2);
INSERT INTO "dAuction2_option_mc" VALUES (11, 1, '40', false, 'Look for the average value in the distribution below.', '', '125', '500', 3);
INSERT INTO "dAuction2_option_mc" VALUES (12, 2, '50', false, 'Look for the average value in the distribution below.', '', '125', '500', 3);
INSERT INTO "dAuction2_option_mc" VALUES (13, 3, '60', true, '', '', '125', '500', 3);
INSERT INTO "dAuction2_option_mc" VALUES (14, 4, '70', false, 'Look for the average value in the distribution below.', '', '125', '500', 3);
INSERT INTO "dAuction2_option_mc" VALUES (15, 5, '80', false, 'Look for the average value in the distribution below.', '', '125', '500', 3);
INSERT INTO "dAuction2_option_mc" VALUES (16, 1, '17', false, 'Look for the average value in the distribution below.', '', '125', '500', 4);
INSERT INTO "dAuction2_option_mc" VALUES (17, 2, '52', false, '', '', '125', '500', 4);
INSERT INTO "dAuction2_option_mc" VALUES (18, 3, '87', true, '', '', '125', '500', 4);
INSERT INTO "dAuction2_option_mc" VALUES (19, 4, '121', false, 'Look for the average value in the distribution below.', '', '125', '500', 4);
INSERT INTO "dAuction2_option_mc" VALUES (20, 1, '1', false, 'As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 1.', '', '125', '500', 5);
INSERT INTO "dAuction2_option_mc" VALUES (21, 2, '2', false, 'As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 2.', '', '125', '500', 5);
INSERT INTO "dAuction2_option_mc" VALUES (22, 3, '4', false, 'As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 4.', '', '125', '500', 5);
INSERT INTO "dAuction2_option_mc" VALUES (23, 4, '6', true, 'As you want to buy, you need to look in the column with the SELL offers. As you can see, the cheapest offer is indeed for a price of 6.', '', '125', '500', 5);
INSERT INTO "dAuction2_option_mc" VALUES (24, 5, '7', false, 'As you want to buy, you need to look in the column with the SELL offers. There are indeed two units on offer for a price of 7, but 7 is not the cheapest price among all SELL offers.', '', '125', '500', 5);
INSERT INTO "dAuction2_option_mc" VALUES (25, 6, '8', false, 'As you want to buy, you need to look in the column with the SELL offers. There are indeed two units on offer for a price of 8, but 8 is not the cheapest price among all SELL offers.', '', '125', '500', 5);
INSERT INTO "dAuction2_option_mc" VALUES (26, 1, '1', false, 'As you want to sell, you need to look in the column with the BUY offers. There is indeed one units asked for a price of 1, but 1 is not the highest price among all BUY offers.', '', '125', '500', 6);
INSERT INTO "dAuction2_option_mc" VALUES (27, 2, '2', false, 'As you want to sell, you need to look in the column with the BUY offers. There is indeed one units asked for a price of 2, but 2 is not the highest price among all BUY offers.', '', '125', '500', 6);
INSERT INTO "dAuction2_option_mc" VALUES (28, 3, '4', true, 'As you want to sell, you need to look in the column with the BUY offers. As you can see, the most expensive BUY offer has indeed a price of 4.', '', '125', '500', 6);
INSERT INTO "dAuction2_option_mc" VALUES (29, 4, '6', false, 'As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of 6.', '', '125', '500', 6);
INSERT INTO "dAuction2_option_mc" VALUES (30, 5, '7', false, 'As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of 7.', '', '125', '500', 6);
INSERT INTO "dAuction2_option_mc" VALUES (31, 6, '8', false, 'As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of 8.', '', '125', '500', 6);
INSERT INTO "dAuction2_option_mc" VALUES (32, 1, '1', false, 'As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 1.', '', '125', '500', 7);
INSERT INTO "dAuction2_option_mc" VALUES (33, 2, '2', false, 'As you want to buy, you need to look in the column with the SELL offers. As you can see, there are no SELL offers with a price of 2.', '', '125', '500', 7);
INSERT INTO "dAuction2_option_mc" VALUES (34, 3, '4', true, 'As you want to buy, you need to look in the column with the SELL offers. As you can see, the cheapest offer is indeed for a price of 4.', '', '125', '500', 7);
INSERT INTO "dAuction2_option_mc" VALUES (35, 4, '5', false, 'As you want to buy, you need to look in the column with the SELL offers. There are indeed two units on offer for a price of 5, but 5 is not the cheapest price among all SELL offers.', '', '125', '500', 7);
INSERT INTO "dAuction2_option_mc" VALUES (36, 5, '7', false, 'As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of 7.', '', '125', '500', 6);
INSERT INTO "dAuction2_option_mc" VALUES (37, 1, '1', false, 'As you want to sell, you need to look in the column with the BUY offers. There is indeed one units asked for a price of 1, but 1 is not the highest price among all BUY offers.', '', '125', '500', 8);
INSERT INTO "dAuction2_option_mc" VALUES (38, 2, '2', false, 'As you want to sell, you need to look in the column with the BUY offers. As you can see, the most expensive BUY offer has indeed a price of 2.', '', '125', '500', 8);
INSERT INTO "dAuction2_option_mc" VALUES (39, 3, '4', true, 'As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of 4.', '', '125', '500', 8);
INSERT INTO "dAuction2_option_mc" VALUES (40, 4, '5', false, 'As you want to sell, you need to look in the column with the BUY offers. As you can see, there are no BUY offers with a price of 5.', '', '125', '500', 8);
INSERT INTO "dAuction2_option_mc" VALUES (41, 1, '1 unit', false, 'The price for which you make your SELL offer is equal or lower than all the three offers in the BUY column of the Offers Overview. Your SELL offer can thus be matched to more than 1 unit.', '', '125', '500', 9);
INSERT INTO "dAuction2_option_mc" VALUES (42, 2, '2 units', false, 'The price for which you make your SELL offer is equal or lower than all the three offers in the BUY column of the Offers Overview. Your SELL offer can thus be matched to more than 2 units.', '', '125', '500', 9);
INSERT INTO "dAuction2_option_mc" VALUES (43, 3, '3 units', true, 'The price for which you make your SELL offer is equal or lower than all the three offers in the BUY column of the Offers Overview. You thus indeed sell all your 3 units.', 'staticfiles/images/testing02_ answer08.png', '400', '300', 9);
INSERT INTO "dAuction2_option_mc" VALUES (44, 1, 'for a price of 1', false, 'When you submit an offer, you get the best price for all the units that can be matched. In the BUY column are also units with a price of 2, so you must get a price of 2 for some of your units.', '', '125', '500', 10);
INSERT INTO "dAuction2_option_mc" VALUES (45, 2, 'for a price of 2', false, 'In the BUY column are only 2 units with a price of 2, so you cannot get a price of 2 for all your 3 units.', '', '125', '500', 10);
INSERT INTO "dAuction2_option_mc" VALUES (46, 3, '1 unit for a price of 1 and 2 units for a price of 2', true, 'When you submit an offer, you get the best price for all the units that can be matched. In the BUY column there are 2 units with a price of 2 and 1 unit with a price of 1.', '', '125', '500', 10);
INSERT INTO "dAuction2_option_mc" VALUES (47, 4, '2 units for a price of 1 and 1 unit for a price of 2', false, 'When you submit an offer, you get the best price for all the units that can be matched. In the BUY column are 2 units with a price of 2, so you must get a price of 2 for at least 2 of your units.', '', '125', '500', 10);
INSERT INTO "dAuction2_option_mc" VALUES (48, 1, 'no units', false, 'The price for which you make your BUY offer is equal or higher than all the three offers in the SELL column of the Offers Overview. Your BUY offer can thus be matched at least to 1 unit.', '', '125', '500', 11);
INSERT INTO "dAuction2_option_mc" VALUES (49, 2, '1 unit', false, 'The price for which you make your BUY offer is equal or higher than all the three offers in the BUY column of the Offers Overview. Your BUY offer can thus be matched to at least 2 units.', '', '125', '500', 11);
INSERT INTO "dAuction2_option_mc" VALUES (50, 3, '2 units', true, 'The price for which you make your BUY offer is equal or higher than all the three offers in the BUY column of the Offers Overview. You thus indeed buy all your 2 units.', 'staticfiles/images/testing02_ answer10.png', '400', '300', 11);
INSERT INTO "dAuction2_option_mc" VALUES (51, 1, 'for a price of 7', false, 'When you submit an offer, you get the best price for all the units that can be matched. In the SELL column are also units with a price of 4, so you must get a price of 4 for some of your units.', '', '125', '500', 12);
INSERT INTO "dAuction2_option_mc" VALUES (52, 2, 'for a price of 4', false, 'In the SELL column is only 1 unit with a price of 4, so you cannot get a price of 4 for both your 2 units.', '', '125', '500', 12);
INSERT INTO "dAuction2_option_mc" VALUES (53, 3, 'for a price of 5', false, 'When you submit an offer, you get the best price for all the units that can be matched. In the SELL column are also units with a price of 4, so you must get a price of 4 for some of your units.', '', '125', '500', 12);
INSERT INTO "dAuction2_option_mc" VALUES (54, 4, '1 units for a price of 4 and 1 unit for a price of 5', true, 'When you submit an offer, you get the best price for all the units that can be matched. In the SELL column is 1 unit with a price of 4, so you must get a price of 4 for 1 unit. The second unit is then bought at the slightly worse (but still acceptable) price of 5.', '', '125', '500', 12);
INSERT INTO "dAuction2_option_mc" VALUES (55, 1, 'I buy the 3 units on offer.', false, 'You submit a BUY offer for 5 units, while there are only 3 units in total in the SELL column. You thus buy 3 units and the two units that are left over are put into the Offer Overview.', '', '125', '500', 13);
INSERT INTO "dAuction2_option_mc" VALUES (56, 2, 'I buy the 3 units on offer and I post a BUY offer for 2 units for a price of 7.', true, 'You submit a BUY offer for 5 units, while there are only 3 units in total in the SELL column. You thus buy 3 units and the two units that are left over a put into the Offer Overview for a price of 7.', 'staticfiles/images/testing02_ answer12.png', '400', '300', 13);
INSERT INTO "dAuction2_option_mc" VALUES (57, 3, 'I post a BUY offer for 5 units for a price of 7.', false, 'You submit a BUY offer for 5 units for a price of 7. They can thus be matched with the 3 units in the SELL column. Only the remaining 2 units are posted as your BUY offer.', '', '125', '500', 13);
INSERT INTO "dAuction2_option_mc" VALUES (58, 1, '1', false, 'The Retailer bought 5 units, thus the number of units must be higher.', '', '125', '500', 14);
INSERT INTO "dAuction2_option_mc" VALUES (59, 2, '2', false, 'The Retailer bought 5 units, thus the number of units must be higher.', '', '125', '500', 14);
INSERT INTO "dAuction2_option_mc" VALUES (60, 3, '3', false, 'The Retailer bought 5 units, thus the number of units must be higher.', '', '125', '500', 14);
INSERT INTO "dAuction2_option_mc" VALUES (61, 4, '4', false, 'The Retailer bought 5 units, thus the number of units must be higher.', '', '125', '500', 14);
INSERT INTO "dAuction2_option_mc" VALUES (62, 5, '5', true, 'The Retailer bought 5 units, thus the number of units is indeed 5.', 'staticfiles/images/testing14.png', '300', '200', 14);
INSERT INTO "dAuction2_option_mc" VALUES (63, 6, '6', false, 'The Retailer bought 5 units, thus the number of units must be lower.', '', '125', '500', 14);
INSERT INTO "dAuction2_option_mc" VALUES (64, 1, '1', false, 'The Producer bought only 2 units, thus the number of units must be higher.', '', '125', '500', 15);
INSERT INTO "dAuction2_option_mc" VALUES (65, 2, '2', false, 'The Producer bought only 2 units, thus the number of units must be higher.', '', '125', '500', 15);
INSERT INTO "dAuction2_option_mc" VALUES (66, 3, '3', true, 'The Producer bought 2 units, thus the number of used units is now indeed 3.', 'staticfiles/images/testing15.png', '300', '200', 15);
INSERT INTO "dAuction2_option_mc" VALUES (67, 4, '4', false, 'The Producer bought 2 units, thus the number of units must be lower.', '', '125', '500', 15);
INSERT INTO "dAuction2_option_mc" VALUES (68, 5, '5', false, 'The Producer bought 2 units, thus the number of units must be lower than before.', '', '125', '500', 15);
INSERT INTO "dAuction2_option_mc" VALUES (69, 1, '-2', true, 'The Retailer sold 5 units, thus the number of used units is now indeed -2. (The Retailer has in effect borrowed 2 units)', 'staticfiles/images/testing16.png', '350', '250', 16);
INSERT INTO "dAuction2_option_mc" VALUES (70, 2, '-1', false, 'The Retailer sold 5 units, thus the number of units must be lower.', '', '125', '500', 16);
INSERT INTO "dAuction2_option_mc" VALUES (71, 3, '0', false, 'There are no units with 0 as an index', '', '125', '500', 16);
INSERT INTO "dAuction2_option_mc" VALUES (72, 4, '1', false, 'The Retailer sold 5 units, thus the number of units must be lower.', '', '125', '500', 16);
INSERT INTO "dAuction2_option_mc" VALUES (73, 5, '2', false, 'The Retailer sold 5 units, thus the number of units must be lower.', '', '125', '500', 16);
INSERT INTO "dAuction2_option_mc" VALUES (74, 1, '-1', false, 'The Retailer bought 5 units, thus the number of used units must be higher.', '', '125', '500', 17);
INSERT INTO "dAuction2_option_mc" VALUES (75, 2, '0', false, 'There are no units with 0 as an index', '', '125', '500', 17);
INSERT INTO "dAuction2_option_mc" VALUES (76, 3, '1', false, 'The Retailer bought 5 units, thus the number of used units must be higher.', '', '125', '500', 17);
INSERT INTO "dAuction2_option_mc" VALUES (77, 4, '2', false, 'The Retailer bought 5 units, thus the number of used units must be higher.', '', '125', '500', 17);
INSERT INTO "dAuction2_option_mc" VALUES (78, 5, '3', true, 'The Retailer bought 5 units, thus the number of used units is now indeed 3. Two out of the 5 units are used to give back the borrowed two units (unit number 0 and number -1). Only the remaining three units contribute to the Earnings ', 'staticfiles/images/testing17.png', '300', '250', 17);
INSERT INTO "dAuction2_option_mc" VALUES (79, 1, 'each Retailer has 10 as UNITS DEMANDED.', false, 'This is incorrect as then only 40 out of the total of 43 units would be divided over the Retailers.', '', '125', '500', 18);
INSERT INTO "dAuction2_option_mc" VALUES (80, 2, 'two Retailers each have 10 and the two remaining Retailers each 11 as UNITS DEMANDED.', true, 'This is correct as the MARKET UNITS DEMANDED is divided as equally as possible over the Retailers', '', '125', '500', 18);
INSERT INTO "dAuction2_option_mc" VALUES (81, 3, 'one Retailer has zero and the three remaining retailers have 14 as UNITS DEMANDED.', false, 'The MARKET UNITS DEMANDED is divided as equally as possible over the Retailers.', '', '125', '500', 18);
INSERT INTO "dAuction2_option_mc" VALUES (82, 4, 'The UNITS DEMANDED cannot be determined in this case', false, 'The UNITS DEMANDED can be determined.', '', '125', '500', 18);
INSERT INTO "dAuction2_option_mc" VALUES (83, 1, 'The Retailer (or Producer) can offer to sell (buy back) the excess of units in Stage 2 until the Retailer (or Producer) has exactly the same number as UNITS DEMANDED.', true, 'This is correct. A Retailer will not be credited for holding extra units above the UNITS DEMANDED, and can thus earn some extra profit by selling the extra units. A Producer that has sold more units than the number of UNITS DEMANDED increases his profit by buying back units when the price for these units is below the Producer''s production costs.', '', '125', '500', 19);
INSERT INTO "dAuction2_option_mc" VALUES (84, 2, 'When a Retailers (or Producer) has more units than the number of UNITS DEMANDED in Stage 2, nothing can be done and the Retailer (or Producer) must just accept that they lose a little bit of profit here.', false, 'This is incorrect as both Retailers and Producers are allowed to sell and buy in both Stage 1 and Stage 2. They can thus try to change the number of units sold or bought until it is EXACTLY equal to the number of UNITS DEMANDED is divided as equally as possible over the Retailers', '', '125', '500', 19);
INSERT INTO "dAuction2_option_mc" VALUES (85, 3, 'This is incorrect as both Retailers and Producers are allowed to sell and buy in both Stage 1 and Stage 2. They can thus try to change the number of units sold or bought until it is EXACTLY equal to the number of UNITS DEMANDED is divided as equally as possible over the Retailers.', false, 'The MARKET UNITS DEMANDED is divided as equally as possible over the Retailers.', '', '125', '500', 19);
INSERT INTO "dAuction2_option_mc" VALUES (86, 4, 'A Producer can always still in Stage 2 offer to buy back the excess units. However, a Retailer in Stage 2 cannot reduce the number of units it bought by offering to sell units.', false, 'This is incorrect as both Retailers and Producers are allowed to sell and buy in both Stage 1 and Stage 2. They can thus try to change the number of units sold or bought until it is EXACTLY equal to the number of UNITS DEMANDED is divided as equally as possible over the Retailers.', '', '125', '500', 19);


--
-- Name: dAuction2_option_mc_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_option_mc_id_seq"', 86, true);


--
-- Data for Name: dAuction2_page; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_page" VALUES (514, 'instructions/pages/page01.html', 1, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (515, 'instructions/pages/page02.html', 2, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (516, 'instructions/pages/page03.html', 3, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (517, 'instructions/pages/page04.html', 4, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (518, 'instructions/pages/page05.html', 5, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (519, 'instructions/pages/page06.html', 6, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (520, 'instructions/pages/page07.html', 7, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (521, 'instructions/pages/page08.html', 8, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (522, 'instructions/pages/page09.html', 9, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (523, 'instructions/pages/page10.html', 10, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (524, 'instructions/pages/page11.html', 11, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (525, 'instructions/pages/page12.html', 12, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (526, 'instructions/pages/page13.html', 13, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (527, 'instructions/pages/page14.html', 14, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (528, 'instructions/pages/page15.html', 15, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (529, 'instructions/pages/page16.html', 16, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (530, 'instructions/pages/page17.html', 17, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (531, 'instructions/pages/page18.html', 18, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (532, 'instructions/pages/page19.html', 19, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (533, 'instructions/pages/page20.html', 20, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (534, 'instructions/pages/page21.html', 21, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (535, 'instructions/pages/page22.html', 22, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (536, 'instructions/pages/page23.html', 23, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (537, 'instructions/pages/page24.html', 24, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (538, 'instructions/pages/page25.html', 25, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (539, 'instructions/pages/page26.html', 26, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (540, 'instructions/pages/page27.html', 27, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (541, 'instructions/pages/page28.html', 28, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (542, 'instructions/pages/page29.html', 29, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (543, 'instructions/pages/page30.html', 30, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (544, 'instructions/pages/page31.html', 31, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (545, 'instructions/pages/page32.html', 32, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (546, 'instructions/pages/page33.html', 33, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (547, 'instructions/pages/page34.html', 34, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (548, 'instructions/pages/page35.html', 35, 1, 271420);
INSERT INTO "dAuction2_page" VALUES (549, 'instructions/pages_summary/page01.html', 1, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (550, 'instructions/pages_summary/page02.html', 2, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (551, 'instructions/pages_summary/page03.html', 3, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (552, 'instructions/pages_summary/page04.html', 4, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (553, 'instructions/pages_summary/page05.html', 5, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (554, 'instructions/pages_summary/page06.html', 6, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (555, 'instructions/pages_summary/page07.html', 7, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (556, 'instructions/pages_summary/page08.html', 8, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (557, 'instructions/pages_summary/page09.html', 9, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (558, 'instructions/pages_summary/page12.html', 10, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (559, 'instructions/pages_summary/page13.html', 11, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (560, 'instructions/pages_summary/page18.html', 12, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (561, 'instructions/pages_summary/page19.html', 13, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (562, 'instructions/pages_summary/page20.html', 14, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (563, 'instructions/pages_summary/page25.html', 15, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (564, 'instructions/pages_summary/page26.html', 16, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (565, 'instructions/pages_summary/page27.html', 17, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (566, 'instructions/pages_summary/page28.html', 18, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (567, 'instructions/pages_summary/page29.html', 19, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (568, 'instructions/pages_summary/page33.html', 20, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (569, 'instructions/pages_summary/page34.html', 21, 0, 271420);
INSERT INTO "dAuction2_page" VALUES (570, 'instructions/pages_summary/page35.html', 22, 0, 271420);


--
-- Name: dAuction2_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_page_id_seq"', 570, true);


--
-- Data for Name: dAuction2_player_stats; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_player_stats" VALUES (573, '2017-11-10 14:34:08.74496+00', 1, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 45, 200);
INSERT INTO "dAuction2_player_stats" VALUES (574, '2017-11-10 14:34:08.779205+00', 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 45, 199);
INSERT INTO "dAuction2_player_stats" VALUES (575, '2017-11-10 14:34:08.87735+00', 1, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 46, 200);
INSERT INTO "dAuction2_player_stats" VALUES (576, '2017-11-10 14:34:08.984261+00', 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 46, 199);
INSERT INTO "dAuction2_player_stats" VALUES (577, '2017-11-10 14:34:09.022962+00', 1, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 47, 200);
INSERT INTO "dAuction2_player_stats" VALUES (578, '2017-11-10 14:34:09.080458+00', 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 47, 199);
INSERT INTO "dAuction2_player_stats" VALUES (579, '2017-11-10 14:34:09.17867+00', 1, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 48, 200);
INSERT INTO "dAuction2_player_stats" VALUES (580, '2017-11-10 14:34:09.257528+00', 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 48, 199);
INSERT INTO "dAuction2_player_stats" VALUES (581, '2017-11-10 14:34:09.297181+00', 1, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 49, 200);
INSERT INTO "dAuction2_player_stats" VALUES (582, '2017-11-10 14:34:09.36053+00', 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 49, 199);
INSERT INTO "dAuction2_player_stats" VALUES (583, '2017-11-10 14:34:09.388897+00', 1, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 50, 200);
INSERT INTO "dAuction2_player_stats" VALUES (584, '2017-11-10 14:34:09.407856+00', 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, -1, -1, 35, 0, 0, 0, 0, 271420, 22, 50, 199);
INSERT INTO "dAuction2_player_stats" VALUES (571, '2017-11-10 14:34:08.557413+00', 1, 22, -2200, 0, 0, 3058, 858, 0, 0, 0, 0, 1, -1, -1, -1, 0, 22, 0, 0, 0, 271420, 22, 44, 200);
INSERT INTO "dAuction2_player_stats" VALUES (572, '2017-11-10 14:34:08.637875+00', 0, 22, 2200, 0, 1040, 0, 1160, 0, 0, 0, 0, 1, -1, -1, -1, 0, 22, 0, 0, 0, 271420, 22, 44, 199);


--
-- Data for Name: dAuction2_penalty; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: dAuction2_penalty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_penalty_id_seq"', 314, true);


--
-- Name: dAuction2_period_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_period_id_seq"', 50, true);


--
-- Name: dAuction2_phase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_phase_id_seq"', 37, true);


--
-- Name: dAuction2_player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_player_id_seq"', 200, true);


--
-- Data for Name: dAuction2_player_questions; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_player_questions" VALUES (2547, false, 0, false, false, 199, 1);
INSERT INTO "dAuction2_player_questions" VALUES (2548, false, 0, false, false, 200, 1);
INSERT INTO "dAuction2_player_questions" VALUES (2549, false, 0, false, false, 199, 2);
INSERT INTO "dAuction2_player_questions" VALUES (2550, false, 0, false, false, 200, 2);
INSERT INTO "dAuction2_player_questions" VALUES (2551, false, 0, false, false, 199, 3);
INSERT INTO "dAuction2_player_questions" VALUES (2552, false, 0, false, false, 200, 3);
INSERT INTO "dAuction2_player_questions" VALUES (2553, false, 0, false, false, 199, 4);
INSERT INTO "dAuction2_player_questions" VALUES (2554, false, 0, false, false, 200, 4);
INSERT INTO "dAuction2_player_questions" VALUES (2555, false, 0, false, false, 199, 5);
INSERT INTO "dAuction2_player_questions" VALUES (2556, false, 0, false, false, 200, 5);
INSERT INTO "dAuction2_player_questions" VALUES (2557, false, 0, false, false, 199, 6);
INSERT INTO "dAuction2_player_questions" VALUES (2558, false, 0, false, false, 200, 6);
INSERT INTO "dAuction2_player_questions" VALUES (2559, false, 0, false, false, 199, 7);
INSERT INTO "dAuction2_player_questions" VALUES (2560, false, 0, false, false, 200, 7);
INSERT INTO "dAuction2_player_questions" VALUES (2561, false, 0, false, false, 199, 8);
INSERT INTO "dAuction2_player_questions" VALUES (2562, false, 0, false, false, 200, 8);
INSERT INTO "dAuction2_player_questions" VALUES (2563, false, 0, false, false, 199, 9);
INSERT INTO "dAuction2_player_questions" VALUES (2564, false, 0, false, false, 200, 9);
INSERT INTO "dAuction2_player_questions" VALUES (2565, false, 0, false, false, 199, 10);
INSERT INTO "dAuction2_player_questions" VALUES (2566, false, 0, false, false, 200, 10);
INSERT INTO "dAuction2_player_questions" VALUES (2567, false, 0, false, false, 199, 11);
INSERT INTO "dAuction2_player_questions" VALUES (2568, false, 0, false, false, 200, 11);
INSERT INTO "dAuction2_player_questions" VALUES (2569, false, 0, false, false, 199, 12);
INSERT INTO "dAuction2_player_questions" VALUES (2570, false, 0, false, false, 200, 12);
INSERT INTO "dAuction2_player_questions" VALUES (2571, false, 0, false, false, 199, 13);
INSERT INTO "dAuction2_player_questions" VALUES (2572, false, 0, false, false, 200, 13);
INSERT INTO "dAuction2_player_questions" VALUES (2573, false, 0, false, false, 199, 14);
INSERT INTO "dAuction2_player_questions" VALUES (2574, false, 0, false, false, 200, 14);
INSERT INTO "dAuction2_player_questions" VALUES (2575, false, 0, false, false, 199, 15);
INSERT INTO "dAuction2_player_questions" VALUES (2576, false, 0, false, false, 200, 15);
INSERT INTO "dAuction2_player_questions" VALUES (2577, false, 0, false, false, 199, 16);
INSERT INTO "dAuction2_player_questions" VALUES (2578, false, 0, false, false, 200, 16);
INSERT INTO "dAuction2_player_questions" VALUES (2579, false, 0, false, false, 199, 17);
INSERT INTO "dAuction2_player_questions" VALUES (2580, false, 0, false, false, 200, 17);
INSERT INTO "dAuction2_player_questions" VALUES (2581, false, 0, false, false, 199, 18);
INSERT INTO "dAuction2_player_questions" VALUES (2582, false, 0, false, false, 200, 18);
INSERT INTO "dAuction2_player_questions" VALUES (2583, false, 0, false, false, 199, 19);
INSERT INTO "dAuction2_player_questions" VALUES (2584, false, 0, false, false, 200, 19);


--
-- Data for Name: dAuction2_player_question_options; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: dAuction2_player_question_options_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_player_question_options_id_seq"', 1, false);


--
-- Name: dAuction2_player_questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_player_questions_id_seq"', 2584, true);


--
-- Name: dAuction2_player_stats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_player_stats_id_seq"', 584, true);


--
-- Name: dAuction2_question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_question_id_seq"', 1, false);


--
-- Data for Name: dAuction2_timer; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_timer" VALUES (1, false, false, 1510324905, 45, false, 1510324887, 999);


--
-- Name: dAuction2_timer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_timer_id_seq"', 1, false);


--
-- Name: dAuction2_treatment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_treatment_id_seq"', 1, false);


--
-- Data for Name: dAuction2_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: dAuction2_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_user_groups_id_seq"', 1, false);


--
-- Name: dAuction2_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_user_id_seq"', 1, false);


--
-- Data for Name: dAuction2_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: dAuction2_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_user_user_permissions_id_seq"', 1, false);


--
-- Data for Name: dAuction2_voucher; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_voucher" VALUES (246, 1, 0, 0, 271420);
INSERT INTO "dAuction2_voucher" VALUES (247, 2, 0.100000000000000006, 0.100000000000000006, 271420);
INSERT INTO "dAuction2_voucher" VALUES (248, 3, 0.400000000000000022, 0.300000000000000044, 271420);
INSERT INTO "dAuction2_voucher" VALUES (249, 4, 1.10000000000000009, 0.700000000000000067, 271420);
INSERT INTO "dAuction2_voucher" VALUES (250, 5, 2.80000000000000027, 1.70000000000000018, 271420);
INSERT INTO "dAuction2_voucher" VALUES (251, 6, 5.80000000000000071, 3.00000000000000044, 271420);
INSERT INTO "dAuction2_voucher" VALUES (252, 7, 10.7000000000000011, 4.90000000000000036, 271420);
INSERT INTO "dAuction2_voucher" VALUES (253, 8, 18.1999999999999993, 7.49999999999999822, 271420);
INSERT INTO "dAuction2_voucher" VALUES (254, 9, 29.2000000000000028, 11.0000000000000036, 271420);
INSERT INTO "dAuction2_voucher" VALUES (255, 10, 44, 14.7999999999999972, 271420);
INSERT INTO "dAuction2_voucher" VALUES (256, 11, 65, 21, 271420);
INSERT INTO "dAuction2_voucher" VALUES (257, 12, 92, 27, 271420);
INSERT INTO "dAuction2_voucher" VALUES (258, 13, 127, 35, 271420);
INSERT INTO "dAuction2_voucher" VALUES (259, 14, 171, 44, 271420);
INSERT INTO "dAuction2_voucher" VALUES (260, 15, 225, 54, 271420);
INSERT INTO "dAuction2_voucher" VALUES (261, 16, 291, 66, 271420);
INSERT INTO "dAuction2_voucher" VALUES (262, 17, 371, 80, 271420);
INSERT INTO "dAuction2_voucher" VALUES (263, 18, 465, 94, 271420);
INSERT INTO "dAuction2_voucher" VALUES (264, 19, 580, 115, 271420);
INSERT INTO "dAuction2_voucher" VALUES (265, 20, 710, 130, 271420);
INSERT INTO "dAuction2_voucher" VALUES (266, 21, 865, 155, 271420);
INSERT INTO "dAuction2_voucher" VALUES (267, 22, 1040, 175, 271420);
INSERT INTO "dAuction2_voucher" VALUES (268, 23, 1245, 205, 271420);
INSERT INTO "dAuction2_voucher" VALUES (269, 24, 1475, 230, 271420);
INSERT INTO "dAuction2_voucher" VALUES (270, 25, 1735, 260, 271420);
INSERT INTO "dAuction2_voucher" VALUES (271, 26, 2030, 295, 271420);
INSERT INTO "dAuction2_voucher" VALUES (272, 27, 2360, 330, 271420);
INSERT INTO "dAuction2_voucher" VALUES (273, 28, 2730, 370, 271420);
INSERT INTO "dAuction2_voucher" VALUES (274, 29, 3145, 415, 271420);
INSERT INTO "dAuction2_voucher" VALUES (275, 30, 3600, 455, 271420);
INSERT INTO "dAuction2_voucher" VALUES (276, 31, 4100, 500, 271420);
INSERT INTO "dAuction2_voucher" VALUES (277, 32, 4660, 560, 271420);
INSERT INTO "dAuction2_voucher" VALUES (278, 33, 5270, 610, 271420);
INSERT INTO "dAuction2_voucher" VALUES (279, 34, 5940, 670, 271420);
INSERT INTO "dAuction2_voucher" VALUES (280, 35, 6670, 730, 271420);


--
-- Name: dAuction2_voucher_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_voucher_id_seq"', 280, true);


--
-- Data for Name: dAuction2_voucherre; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO "dAuction2_voucherre" VALUES (78, '1', 139, '139', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (79, '2', 278, '139', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (80, '3', 417, '139', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (81, '4', 556, '139', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (82, '5', 695, '139', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (83, '...', 834, '139', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (84, '<i>UNITS DEMANDED</i>', 834, '139', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (85, '<i>UNITS DEMANDED</i> + 1', 0, '0', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (86, '<i>UNITS DEMANDED</i> + 2', 0, '0', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (87, '<i>UNITS DEMANDED</i> + 3', 0, '0', 271420);
INSERT INTO "dAuction2_voucherre" VALUES (88, '<i>UNITS DEMANDED</i> + ...', 0, '0', 271420);


--
-- Name: dAuction2_voucherre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('"dAuction2_voucherre_id_seq"', 88, true);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('django_content_type_id_seq', 24, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_migrations VALUES (1, 'contenttypes', '0001_initial', '2017-11-01 09:52:26.025317+00');
INSERT INTO django_migrations VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2017-11-01 09:52:26.267182+00');
INSERT INTO django_migrations VALUES (3, 'auth', '0001_initial', '2017-11-01 09:52:26.424668+00');
INSERT INTO django_migrations VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2017-11-01 09:52:26.451678+00');
INSERT INTO django_migrations VALUES (5, 'auth', '0003_alter_user_email_max_length', '2017-11-01 09:52:26.478008+00');
INSERT INTO django_migrations VALUES (6, 'auth', '0004_alter_user_username_opts', '2017-11-01 09:52:26.502091+00');
INSERT INTO django_migrations VALUES (7, 'auth', '0005_alter_user_last_login_null', '2017-11-01 09:52:26.526751+00');
INSERT INTO django_migrations VALUES (8, 'auth', '0006_require_contenttypes_0002', '2017-11-01 09:52:26.535024+00');
INSERT INTO django_migrations VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2017-11-01 09:52:26.570056+00');
INSERT INTO django_migrations VALUES (10, 'auth', '0008_alter_user_username_max_length', '2017-11-01 09:52:26.596215+00');
INSERT INTO django_migrations VALUES (11, 'dAuction2', '0001_initial', '2017-11-01 09:52:43.734002+00');
INSERT INTO django_migrations VALUES (12, 'admin', '0001_initial', '2017-11-01 09:52:57.698894+00');
INSERT INTO django_migrations VALUES (13, 'admin', '0002_logentry_remove_auto_add', '2017-11-01 09:52:57.828228+00');
INSERT INTO django_migrations VALUES (14, 'sessions', '0001_initial', '2017-11-01 09:52:57.91852+00');
INSERT INTO django_migrations VALUES (15, 'dAuction2', '0002_auto_20171109_1653', '2017-11-10 10:09:13.346486+00');
INSERT INTO django_migrations VALUES (16, 'dAuction2', '0003_auto_20171110_1051', '2017-11-10 14:10:12.916725+00');


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('django_migrations_id_seq', 16, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_session VALUES ('3c92y501ku1fmox3ybivg5i1oo7wxw10', 'NTU5MGY1Y2NmZjYzNTk4MjhiN2YxZmM4NDRmZDk1ZDRiZmYwODMwNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjI4ZDE0Yzk4MTJlZjczNTQwMWU0ODNkODZlZTQzNjE5ODMyMTRkYjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI5OSJ9', '2017-11-15 09:56:50.819649+00');
INSERT INTO django_session VALUES ('ycaplfv0k2bxzhtef3l0otdvpgi58hjz', 'MTZjYmQ1OGYxNzlkOTYwMzc4MjIwMzVjZjkyODA3ZDY2MTA5NTFlMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImJiOWQ4MDEyM2JjMTBiMDU3MTVhMzhlMzhkNjBhOThiMzhmN2Q2MjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwidXNlcm5hbWUiOiJ1MDEifQ==', '2017-11-15 09:57:08.046449+00');
INSERT INTO django_session VALUES ('spncsscg963b7ut4kuoj2usjl6ht1f38', 'YzgyZjRhYzliNmZhNjY2ZWNkMTU5ZTNjOTJmYjE4YzU3Yjc4OWM4ZDp7Il9hdXRoX3VzZXJfaGFzaCI6ImQyZGJjNTU4NmU2ZWFjY2Y2NDUxOGMwNWRkNGVkY2E3ODFiYWJhOTkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIiwidXNlcm5hbWUiOiJ1MDIifQ==', '2017-11-15 09:57:14.320383+00');
INSERT INTO django_session VALUES ('98zflzje7pf2wbrhnp5g0ue8k3xqdf8c', 'N2Y1ZDVkMWQ3Zjc3ZWI3NTc1ZDE1MzQ3MjlhODA1OTZjZTM4YzU1MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiYmI5ZDgwMTIzYmMxMGIwNTcxNWEzOGUzOGQ2MGE5OGIzOGY3ZDYyMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2017-11-23 15:41:11.135001+00');
INSERT INTO django_session VALUES ('6c6iqbpnn8fdzyz5n7emwog3jipbz196', 'Yzg4NzE0ZjRhNTJkMzJkODAwMjBiMWExZTU1ZWM0YjE0NDU0ZDNjYTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDJkYmM1NTg2ZTZlYWNjZjY0NTE4YzA1ZGQ0ZWRjYTc4MWJhYmE5OSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2017-11-23 15:41:18.690502+00');


--
-- PostgreSQL database dump complete
--


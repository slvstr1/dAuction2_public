ALTER SYSTEM SET shared_buffers TO '612MB';
ALTER SYSTEM SET effective_cache_size TO '612MB';
ALTER SYSTEM SET maintenance_work_mem TO '312MB';
CREATE ROLE :user WITH LOGIN PASSWORD :'passwd';
CREATE DATABASE dauction2 OWNER :user;
GRANT ALL PRIVILEGES ON DATABASE dauction2 TO :user;


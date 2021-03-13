"""
Create tables for users
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
        CREATE TABLE media_types (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT NOW(),
            primary key(id)
        );
    """, ignore_errors='rollback'),
    step("""
        INSERT INTO media_types (id, name)
        VALUES (1, 'Kakao')
    """, ignore_errors='rollback'),
    step("""
        CREATE TABLE users (
            id INT NOT NULL AUTO_INCREMENT,
            email VARCHAR(200) NOT NULL,
            media_type_id INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT NOW(),
            primary key(id),
        CONSTRAINT users_media_type_id_fkey FOREIGN KEY (media_type_id) REFERENCES media_types(id)
        );
    """, ignore_errors='rollback')
]

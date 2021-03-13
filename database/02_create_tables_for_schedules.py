"""
Create tables for schedules
"""

from yoyo import step

__depends__ = {'01_create_tables_for_users'}

steps = [
        step("""
            CREATE TABLE schedule_categories (
                id INT NOT NULL AUTO_INCREMENT,
                category VARCHAR(50),
                created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                user_id INT NOT NULL,
                CONSTRAINT schedule_categories_user_id_fkey FOREIGN KEY (user_id) REFERENCES users (id),
                primary key (id)
            );
        """),
        step("""
            CREATE TABLE schedules (
                id INT NOT NULL AUTO_INCREMENT,
                content VARCHAR (100) NOT NULL,
                user_id INT NOT NULL,
                start_time TIMESTAMP NOT NULL,
                end_time TIMESTAMP NOT NULL,
                schedule_category_id INT NOT NULL,
                duration INT NOT NULL,
                memo VARCHAR (1000),
                created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                CONSTRAINT schedules_user_id_fkey FOREIGN KEY (user_id) REFERENCES users (id),
                CONSTRAINT schedules_schedule_category_id_fkey FOREIGN KEY (schedule_category_id) REFERENCES schedule_categories (id),
                primary key (id)
            );
        """)
]

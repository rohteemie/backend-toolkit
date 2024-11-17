#!/usr/bin/python3
"""
SQLDBStorage Module using SQLAlchemy

This module provides a storage engine for managing database interactions
in Python applications using SQLAlchemy. It supports basic CRUD operations,
object retrieval by ID, and counting objects in the database.

How to Use:
1. Set up your MySQL database and ensure it is accessible.
2. Create environment variables:
   - MYSQL_USER: Your MySQL username.
   - MYSQL_PWD: Your MySQL password.
   - MYSQL_HOST: Your database host (default: localhost).
   - MYSQL_DB: Your database name.
   - ENV: Set to 'test' for testing to drop tables on initialization.
3. Define your models in the `models/` directory.
4. Import and initialize `DBStorage` in your application:
   ```python
   from storage.db_storage import DBStorage
   storage = DBStorage()
   storage.reload()
   ```
5. Use the provided methods (e.g., `all`, `new`, `save`, `delete`) to interact
   with your database.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

# below are place holders for the classes that you will define
# from models.auth import Auth
# from models.general_model general_model


# Dictionary mapping class names to classes based on your definition
# classes = {
#     "auth": Auth,
#     "user": user
# }


class DBStorage:
    """Interacts with the MySQL database using SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine and session."""
        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_HOST = getenv('MYSQL_HOST', 'localhost')
        MYSQL_DB = getenv('MYSQL_DB')
        ENV = getenv('ENV')

        if not all([MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB]):
            raise ValueError("Missing one or more required environment variables for database connection")

        # Create the engine
        self.__engine = create_engine(
            f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}/{MYSQL_DB}',
            pool_pre_ping=True
        )

        # Drop tables in test environment
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects of a specific class or all classes.

        Args:
            cls: The class or class name to query (optional).

        Returns:
            A dictionary of objects.
        """
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            if cls is None:
                raise ValueError("Invalid class name provided")
            objs = self.__session.query(cls).all()
            return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

        # Query all classes
        all_objs = {}
        for class_name, class_type in classes.items():
            objs = self.__session.query(class_type).all()
            for obj in objs:
                key = f"{type(obj).__name__}.{obj.id}"
                all_objs[key] = obj
        return all_objs

    def new(self, obj):
        """Add the object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session."""
        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieve an object by class and ID.

        Args:
            cls: The class or class name of the object.
            id: The ID of the object.

        Returns:
            The object, or None if not found.
        """
        if isinstance(cls, str):
            cls = classes.get(cls)
        if cls is None:
            return None

        return self.__session.query(cls).filter_by(id=id).first()

    def count(self, cls=None):
        """
        Count the number of objects in storage.

        Args:
            cls: The class or class name to count (optional).

        Returns:
            The number of objects.
        """
        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            if cls is None:
                raise ValueError("Invalid class name provided")
            return self.__session.query(cls).count()

        # Count all objects across all classes
        return sum(self.__session.query(cls).count() for cls in classes.values())

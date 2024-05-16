Data Management Console
Overview
Welcome to the Data Management Console project! This project provides a robust command-line interface (CLI) for creating, managing, and persisting objects. The console offers a powerful storage engine, enabling easy manipulation of objects without worrying about the underlying storage mechanisms.

Features
Create Your Data Model: Define and customize your data models to suit your application's needs.
Object Management: Create, update, delete, and manage objects seamlessly through the console.
Persistent Storage: Store and persist objects in a JSON file for consistent and reliable data management.
Storage Abstraction: Interact with objects through the console, front-end, or REST API without concerning yourself with the details of data storage and persistence.
Getting Started
Prerequisites
Ensure you have the following installed on your machine:

Python 3.7 or higher
Git (for version control)
Installation
Clone the repository:

git clone https://github.com/your-username/data-management-console.git
cd data-management-console
Install dependencies:

pip install -r requirements.txt
Usage
To start the console, run:

python console.py
Once the console is running, you can use the following commands:

Create an object:

create <ObjectName> <attribute1=value1> <attribute2=value2> ...
Update an object:

update <ObjectName> <object_id> <attribute1=value1> <attribute2=value2> ...
Delete an object:

destroy <ObjectName> <object_id>
Show an object:

show <ObjectName> <object_id>
List all objects:

all <ObjectName>
Storage System
The storage engine provides a critical abstraction layer between your objects and their storage mechanism. By default, objects are stored in a JSON file, but this design allows for easy changes to the storage type without modifying the entire codebase.

Example Commands
Create a new user:

create User name="John Doe" email="john.doe@example.com"
Update user information:

update User 1234 name="Jane Doe"
Delete a user:

destroy User 1234
Show user details:

show User 1234
List all users:

all User
Persisting Data
All objects are stored and persisted in a JSON file (storage.json). The storage engine handles all the complexities of reading from and writing to this file, ensuring data integrity and persistence across sessions.

Extending the Project
Future enhancements might include:

Front-End Integration: Develop a front-end interface for interacting with the objects.
REST API: Build a REST API to enable remote access and management of objects.
Alternative Storage Systems: Implement additional storage options such as SQL databases or NoSQL databases.
Conclusion
This project provides a flexible and powerful way to manage data models and objects. With a focus on abstraction and ease of use, it simplifies the complexities of data persistence and management, making it a valuable tool for developers.

Feel free to contribute to the project by submitting issues or pull requests. Happy coding!

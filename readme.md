# CandidateFinder REST API 
Backend REST API for finding finding suitable candidates based on job description and candidate skill.
Tech Stack:
  - Python
  - Flask
  - SQLAlchemy
  - Marshmellow
  - SQLite
  - flassger (flask swagger)

### How to create Database if needed (Python)

```python
from app import create_app
from models.database import db
# Create new DB
db.create_all(app=create_app()) 
# Delete DB
db.drop_all(app=create_app()) # in order to delete existing database
```
 
 
 Start Server - 2 Options
  1. flask run
  2. python app.py


To view all of options the API has to offer, go to [Swagger Documentation](http://127.0.0.1:5000/apidocs/)

![alt text](https://github.com/OhadVal/CandidateFinder-Rest-API/blob/master/Swagger.png?raw=true)
  
 

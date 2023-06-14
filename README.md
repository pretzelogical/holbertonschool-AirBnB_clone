# holbertonschool-AirBnB_clone
## Aaron & Wyatt


![hbnb-logo](./hbnb.png)

This project is a command interpreter for a backend of of an AirBnB like website.

## Example
```
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create BaseModel
b17ce628-7d36-4a43-925d-9508ee873284
(hbnb) all
[BaseModel] (b17ce628-7d36-4a43-925d-9508ee873284) {'id': 'b17ce628-7d36-4a43-925d-9508ee873284', 'created_at': datetime.datetime(2023, 6, 13, 19, 17, 3, 251233), 'updated_at': datetime.datetime(2023, 6, 14, 0, 17, 3, 251259)}

(hbnb) show BaseModel b17ce628-7d36-4a43-925d-9508ee873284
[BaseModel] (b17ce628-7d36-4a43-925d-9508ee873284) {'id': 'b17ce628-7d36-4a43-925d-9508ee873284', 'created_at': datetime.datetime(2023, 6, 13, 19, 17, 3, 251233), 'updated_at': datetime.datetime(2023, 6, 14, 0, 17, 3, 251259)}

(hbnb) update BaseModel b17ce628-7d36-4a43-925d-9508ee873284 str "the string"
(hbnb) show BaseModel b17ce628-7d36-4a43-925d-9508ee873284
[BaseModel] (b17ce628-7d36-4a43-925d-9508ee873284) {'id': 'b17ce628-7d36-4a43-925d-9508ee873284', 'created_at': datetime.datetime(2023, 6, 13, 19, 17, 3, 251233), 'updated_at': datetime.datetime(2023, 6, 14, 0, 17, 3, 251259), 'str': 'the string'}

(hbnb) destroy BaseModel b17ce628-7d36-4a43-925d-9508ee873284
(hbnb) all
```

## Testing

Testing can be done using the followinf comman
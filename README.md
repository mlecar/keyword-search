# Keyword search

Find keyword ids

### Configuration file
First create a file config.ini with the following properties:
```
[default]
keyword_service_url = {keyword_service_endpoint} 
source_file = {source_file_with_keywords}
target_file = {name_of_target_file}
body = {fixed_body_parameters}
```

### How to execute?
```
$> python keywords-id-search.py
```


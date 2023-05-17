< form
action = "/your-name/"
action = "/your-lastname/"
method = "post" >
< label
for ="your_name" > Your name: < / label >
for ="your_lastname" > Your lastname: < / label >
< input
id = "your_name"
id = "your_lastname"
type = "text"
name = "your_name"
name = "your_lastname"
value = "{{ current_name }}" >
value = "{{ current_lastname }}" >
< input
type = "submit"
value = "OK" >
< / form >
#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">

  <p>?</p>
 </body>
</html>
"""
new_template = []
for line in template.split("\n"):
    if "?" in line:
        for key, value in page.items():
            if key in line:
                line = line.replace("?", value)
                break
    new_template.append(line + "\n")
    
f = open("index.html", mode = "wt", encoding = "UTF-8")
f.writelines(new_template)
f.close()

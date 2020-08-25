favourite_language = {"bob": "python", "juan": "java",
                      "pepe": "c", "rodolfo": "python"}

for name, language in favourite_language.items():
    print(name.title() + "'s favourite language is " +
        language.title() + ".")
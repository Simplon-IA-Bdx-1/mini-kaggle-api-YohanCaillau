# mini-kaggle-api-YohanCaillau
mini-kaggle-api-YohanCaillau created by GitHub Classroom

1. **requirements.txt** contient les librairies nécessaires 
2. **split.py** permet de séparer le fichier trainfull de kaggle en 80% (train.csv) et 20% (test2.csv)
3. **predict.py** permet d'entrainer un modèle sklearn  SGDClassifier et de récupérer les prédictions dans test2-predictions.csv
4. **api.py** permet de faire appel à Flask pour obtenir l'AUC avec l'interface en ligne ou via une requête curl:

curl --request POST 
--url 'http://127.0.0.1:5000/submit_api' 
--header 'accept: multipart/form-data' 
-F 'file=@test2-predictions.csv'

5. **request.py** permet de faire une requête directe à l'URL avec la librairie requests
ATTENTION: Pour charger les fichiers csv le chemin d'accès est un chemin absolu, il faut donc le modifier pour pouvoir charger les fichiers.

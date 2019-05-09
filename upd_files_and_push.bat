xcopy C:\Users\Christian\PycharmProjects\database_setup /S /E /F /EXCLUDE:exclude_from_copy.txt
git add .
git commit -m "auto-updates"
git push -u origin master

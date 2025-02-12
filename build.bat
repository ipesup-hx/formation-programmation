@echo off
chcp 65001
echo Conversion des notebooks...
for %%F in (*.ipynb) do (
    echo %%F
    jupyter nbconvert --to slides "%%F"
    if errorlevel 1 (
        echo Erreur lors de la conversion de %%F
    )
)
echo Conversion terminée
echo Déploiement sur GitHub Pages...
git add -A
git commit --amend --no-edit
git push --force
echo Déploiement terminé
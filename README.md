# Selenium_Testing
BDD-GIT-ALLURE-BEHAVE-UNITTEST-PYTHON-FLASK


login/pass Testing using Selenium
https://opensource-demo.orangehrmlive.com/index.php/auth/login
<br>
<BR>
BEHAVE: <BR>
https://behave.readthedocs.io/en/latest/ <BR>
behave --include ____.feature <BR>
behave -i ____ <BR>
<br>
ALLURE: <BR> https://github.com/allure-framework <br>
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/ 
<br>
pytest -v -s --alluredir="/PycharmProjects/alluretest/reports" alluretest/test_orangehrm.py     (stworzenie raportow) <br>
lub <br>
behave -f allure_behave.formatter:AllureFormatter -o raport ./features <br>
-w konsoli ./allure serve + podajemy sciezke do folderu z raportami  (z folderu allure)
<br>
PYTEST:
-w target podac pelna sciezke
pytest -v -s alluretest/test_orangehrm.py
<br>
Przedstawienie - udostepnienie wynikow jako strona - link:
https://app.netlify.com/    (wrzucic caly folder temp - allure-report z terminala po odpaleniu)
<br><br>
GITHUB: <BR>
settings > SSH Keys > add 
<br>
ssh-keygen -t ed25519 -C "your_email@example.com"
<br>
created 2 files: priv and public key
<br>
add public one to github
<br><br>
Github token 
settings > developer settings > personal token > tokens classic
<br><br>
LINUX: <br>
ls <br>
ls -la <br>
mkdir – stworzenie katalogu <br>
cd .. <br>
rm _nazwa_ - usuniecie <br>
pwd – wyswietla biezacy katalog <br>
file nazwa pliku – pokazuje typ pliku <br>
cp _skad_  _dokad_ : z -R kopiuje pliki wewnatrz katalogow  <br>
mv – przenosi pliki <br>
find __ - wyszukuje <br>
du – pokazuje wielkosc pliku lub katalogu <br>
df- pokazuje uzycie dysku (procesow) <br>
date – pokazuje date <br>
uptime -czas pracy <br>
passwd - zmiana hasla <br>
uname -a  : wersja systemu <br>
chmod np. 750 katalog(lub plik) -R – zmiana uprawnien konta/uzytkownika, praw dostepu (-R)  <br>
chown KONTO NAZWA PLIKU - zmiana uprawnien plikow, zmiana wlasciciela, nadanie uprawnien (z -R nie tylko katalog ale do wszystkich elementow w katalogu) <br>
sh – np. ‘sh jmeter‘  uruchamia(wykonuje) plik lub ./jmeter <br>
pycharm -  ./pycharm.sh  w folderze bin
<br><br>
GIT: <br>
1. git clone |URL| <br>
2. cd |folder| <br>
3. git status <br>
4. git add |nazwa pliku| <br>
5. git commit -m |tekst| <br>
5. git push <br> <br>
mkdir git_test(users>x)>cd..>git config --global user.name "github_username"|git config --global user.email "email_address">git clone repository_url>cd..>git remote -v>git status <br>
gitbash > wejsc w branch (przeciagnac do okienka)  <br>
git log - Check out the Git logs <br>
git rebase -i <numer commita>   - erase the commit from history <br>
git reset –hard HEAD~1  - remove the latest commit <br>
git add ___  (sledzenie pliku-dodaje do indeksu) kolor czerwony <br>
git commit -m „____”   (zapisanie zmian do repo z message/wiadomoscia) <br>
git status <br>
git remote add origin link_to_your_remote_repository (polaczenie ze zdalnym repo) <br>
git push origin master  (lub develop/bdd wyslanie do	repo/utworzenie. 					Może być konieczne najpierw checkout) <br>
git pull origin master (pobranie z repo) <br>
git flow feature publish ___  -  publikacja zmian na gitlab /serwerze/ <br>
git flow feature start ____  - utworzenie i przejscie do galezi <br>
git flow feature finish ____  -  polaczenie z galezia develop i usuniecie swojej <br>
git branch  - pokazuje dostepne galezie <br>
git checkout – zmiana galezi <br>
git checkout -b ___    - tworzy i przelacza do nowej galezi <br>
git merge  - polaczenie dwoch galezi <br>
git-pull  - pobranie i integracja <br>
git push  aktualizuje zdalne repo (wysyla zmiany) <br>
git remote  - wyswietla zdalne repozytoria <br>
git flow init  - inicjuje gitflow <br>
git clone ___ (adres url) (git config --global url.https://github.com/.insteadOf git://github.com/)<br>

<br>
PYTHON/FLASK: <br>
pipenv shell – uruchomienie wirtualnego srodowiska <br>
flask run – produkcyjna wersja/ python manage.py run  -  do http://localhost:5000/api/ <br>
export FLASK_ENV=development   /   export FLASK_APP=hello.py (do pliku)<br>
flask run <br>
docker-compose up mariadb rabbitmq – uruchomienie rabbit i docker <br>
python manage.py behave – odpalenie testow  (z pipenv shell) <br>
pipenv install –dev    instalcja paczek developerskich <br>



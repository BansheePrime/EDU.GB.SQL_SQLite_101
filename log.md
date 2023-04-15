adding to ~/.bashrc
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi

git clone https://github.com/BansheePrime/EDU.GB.SQL_SQLite_101.git

sudo apt install python3-venv
python3 -m venv sqlite3

sudo apt install sqlite
sqlite3 --version

pip list --outdated

source ./sqlite3/bin/activate

pip list --outdated
python3 -m pip install --upgrade {package_name}

python3 ./db_init.py

sql.toad.cz/?


# serial2sql

Read data from serial port a write into database, also can save an sql script to run later or csv files.

## Installation

Need to install dependencies, use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies

```bash
pip install mysql-connector-python
pip install pySerial
```

## Configure

Edit the config.json according to your installation a needs:

```json
{
    "port":"COM3",
    "baudrate": 115200,
    "credentials" : {
    "host":"localhost",
    "database":"data",
    "user":"root",
    "password":"",
    "raise_on_warnings": "True"
    },
    "tableName": "datos1",
    "fields": [
        { "name":"indice","type":"INT(10)" },
        { "name":"valor","type":"INT(10)" }
    ]
}
```

## Use

Once you edit config.json just, on terminal run:
```terminal
python serial2sql.py
```

Also you can save an sql file to run later with -o parameter:
```terminal
python serial2sql.py -o output.sql
```

Or just save to csv file:
```terminal
python serial2sql.py -o output.csv
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
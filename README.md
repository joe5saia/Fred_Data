# irates

Downloads FRED data and saves it as a CSV

## How to Run
This project can be run as a docker container or as a standalone project. All the required code and files are in the `code` directory. 

### Standalone Method
`pull_fred.py` contains the functions and script to call them. If not running as a docker container there are some paths that need to be adjusted. You may also need to create an output directory to save the data in. The file `requirements.txt` has the required packages for running `pull_fred.py`. If using pip, you can install them with `pip3 install --user -r requirements.txt`. 

### Docker Method
The `code` directory also contains a Docker file that builds a simple container and runs the python script. `run_docker.sh` is a shell script that builds the container and then runs it. the `-v` flags tell docker to make a volume mount so that the script can readand write from/to the local machine running the container. The format for this is `-v <local/dir>:<container/dir>`. Modify the local directory to point to where you need it to on your machine. 

## FRED API
The script uses the FRED API to download a good chunck of its data. You might need a new API key which you can get [from the St. Louis Fed here](https://research.stlouisfed.org/docs/api/api_key.html)

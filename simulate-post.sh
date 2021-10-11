echo "Simulating login with username=$1 and password=$2"
curl -k -s -m .1 -d "username=$1&password=$2" https://localhost:4433/submit
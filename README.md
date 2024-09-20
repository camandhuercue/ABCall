# ABCall

sudo docker network create -d bridge my-bridge-network --subnet=172.16.0.0/24

sudo docker image build -t graphql .

sudo docker image build -t postgres .

sudo docker image build -t web .

sudo docker run --name some-postgres --network my-bridge-network -d postgres

sudo docker run --name graphql --network my-bridge-network -d graphql

sudo docker run --name web --network my-bridge-network -p 5000:5000 web

post 

{
    "user": {
        "algo": "importante"
    }
}

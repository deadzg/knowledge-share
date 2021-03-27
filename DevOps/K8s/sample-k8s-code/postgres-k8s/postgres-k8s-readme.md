# Steps to setup Postgres and Login:
Navigate to the script folder from root: `cd DevOps/K8s/sample-k8s-code/postgres-k8s` 
Setup postgres: `sh run-script.sh`
Exec into pod: `k exec -it my-postgres-db-0 sh`
Login to postgres: `psql -h localhost -U postgres -d postgres -p 5432`
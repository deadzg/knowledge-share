# Maven Basic Commands

- Build Java Project: `mvn clean install`
- Build without Skip Testcases : `mvn clean install -DskipTests`
- Run single class unit testcases: `mvn -Dtest=<testclass_name> test` 
Eg: mvn -Dtest=UserServiceDaoImpl test
- Dependency tree of an artifact: `mvn dependency:tree`

Installing Jenkins in AWS:

1. Login to ec2 machine you want to install the jenkins

2. Update the yum packages: sudo yum update

3. Install java8: sudo yum install java-1.8.0

4. Add jenkins repository to yum repos: sudo wget -O /etc/yum.repos.d/jenkins.repo 
http://pkg.jenkins-ci.org/redhat/jenkins.repo

5. Import key: sudo rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key

6. Install jenkins: sudo yum install jenkins

7. Start jenkins: sudo service jenkins start

8. Get Admin Password: sudo cat /var/lib/jenkins/secrets/initialAdminPassword

9. Add your IP to Inbound rules for custom tcp port: 8080

10. Access Dashboard: http://<public-ip>:8080/
Eg: http://ec2-341-172-109-177.compute-1.amazonaws.com:8080/

11. Install git : sudo yum install git

12. Restart server: sudo service jenkins stop ; sudo service jenkins start
Install

13. Install Maven:
sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo

sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo

sudo yum install -y apache-maven

mvn --version

14. UI Settings:
Click on manage jenkins -> Global tool configuration
Add git
Add mvn

Install Publish Over SSH from Manage plugin
- Add pemfile of the server where deployement needs to be done

Go to dashboard -> Click on New Item -> Give name <mastermindds3> -> Select free style project

15. In Configure of project:
Git configuration
	https://giturl
Creds: username/<personal access token for git>
Specify branch : /develop

16. Under build:
Execute shell
mvn clean install -DskipTests

17. Post Build Action:
Select SSH publisher:
Select the server where the artifact needs to be deployed
In transfer set add: 

Source Files: target/*.war

Exec Command:
cd /home/ec2-user

touch deploy-status.txt

echo "NEW_BUILD" >> deploy-status.txts

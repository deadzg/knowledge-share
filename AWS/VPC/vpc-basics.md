# VPC
- Lets you provision a logically isolated section of the AWS cloud where you can launch AWS resources in virtual network that you define. 
- You have a complete control over your networking environment including selection of your own ip address range, creation of subnets and configuration of route tables  and network gateways.
- Cusomize the n/w config
- You can create HVPN ie Hardware VPN - Connection b/n corporate cloud and your VPC and leverage the cloud as an extension of your coporate datacenter
- VPC do not span Regions, but can span AZ
- By default all subnet(private/public) can route traffic between each other by default since they are connected to main route table by default


## CIDR Convention

201.239.0.0/16 (16 bits identified the network)
193.239.32.0/20 (20 bits identified the network)
193.239.32.115/32 Identifies a specific host - Complete Ip address followed by /32 identifies complete host

What is 10/8, 172.16/12, 192.168/16
10.0.0.0/16 is the largest network size, thus we use it

- Public subnets mean they are internet accesible. We can put webservices, bastion host/jump host etc
- Private subnets means they are not internet accesible. We can put db service, app service etc
- Security groups, Network ACL, Route tables can span subnets
- Each subnet maps directly to one AZ
- Cannot span subnet across multiple AZ
- Can an AZ have multiple subnets? Yes
- You can add one or more subnets in each Availability Zone
- If a subnet doesn't have a route to the Internet gateway, the subnet is known as a private subnet.
- If a subnet's traffic is routed to an Internet gateway, the subnet is known as a public subnet.
- If a subnet doesn't have a route to the Internet gateway, but has its traffic routed to a virtual private gateway for a VPN connection, the subnet is known as a VPN-only subnet. 
- By default 5 VPC’s are allowed in each AWS region
- In your VPC, if you use private IPv4 address for data transfer between EC2 instances in two different availability zones in a region then intra region data transfer pricing applies


## Egress-only Internet gateway
An egress-only Internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows outbound communication over IPv6 from instances in your VPC to the Internet, and prevents the Internet from initiating an IPv6 connection with your instances. It’s only used for IPv6 traffic

## Subnets
What can you do with your subnets:
- Launch instances into a subnet of your choosing
- Assign custom ip address ranges in each subnet
- Configure route tables b/n subnets. These table defines whether the subnet will be private or public.
- Create internet gateway and attach it to vpc. Only one internet gateway per vpc. Cannot attach multiple gateways to a vpc
- Much better security over AWS resources
- Instance security groups. By default http is allowed out of security group. It’s stateful ie. if you create inbound http. outbound will be automatically created
- When I create a new security group, all outbound traffic is allowed by default - Yes
- Subnet ACLs, also called stateless. So if we create a rule HTTP traffic into our ACL, we need to create another rule allowing traffic outside ACL
- A subnet can only be associated with one route table at a time, but you can associate multiple subnets with the same route table

## Default VPC vs Custom VPC
Default VPC is user friendly, allowing you to immediately deploy instances
All subnets in default VPC have a route out to the internet(ie. public)
Each EC2 instances has both a public and private IP address. You can configure to keep only private / public addresses.
If you delete the default VPC, the only way to get it back is to contact AWS

## Exam Tips
- Think of a VPC as a logical datacenter in AWS
- VPC consists of IGW’s(Internet Gateways), Route tables, N/w ACL, Subnets, Security groups
1 subnet = 1AZ
Security groups are stateful and N/w ACL are stateless
NO TRANSITIVE PEERING

### Build your own custom VPC
Is VPC region based? If yes what if I change the region of my AWS account? Will it impact the vpc created?Yes it’s region based. If you change the region, you wont be able to see vpc. You need to switch back to that region. No it wont imapct vpc created.
What is the default vpc?
When we create a vpc, subnet and gateway is not created by default, but route tables , security groups and n/w ACLs does gets created

Each subnet we create, 3 addresses are reserved by default by aws. So in all 251 is available.   .1, .2, .3 are reserved

Whenver u create a subnet, by default it will always be associated with the main route table. Thus we don’t want a route out to our main route table because everything will be public.

Thus we need to create a new route table with the route out on it.

Build Custom VPC
A subnet can only be associated with one route table at a time, but you can associate multiple subnets with the same route tableWebserver: Private Ip: 10.0.2.243,  Public IP : 
13.126.78.159
MySQL server : Private IP : 
10.0.1.237

## NAT Instances and NAT gateway
- NAT instance is literally an ec2 instance. 
- Amazon recommends to enable HTTP and HTTPS for NAT instances
- For NAT gateway we don’t have to select a SG , but for NAT instances we do need to
- With NAT gateway we don’t have to disable source destination check, but in NAT instance we do
- Amazon maintains the NAT gateway for you
- NAT instance is a single point of failure. We can avoid this by putting the NAT behind an autoscaling group and set the min number to 1
- NAT gateways/instances are always put in the public subnet, and always update route table to point to the internet using the NAT gateways/instances
Refer : http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-comparison.html

- There must be route out for private subnet to NAT instance, in order for this to work
- When you deploy NAT instances, it should have a public IP address
- Amount of traffic the NAT instances support is based on size. If your are bottle necking, increase the instance size
- NAT Gateways scale automatically up to  10Gbps
- No need to patch NAT Gateways
- Automatically assigned public IP to NAT Gateways
- NAT gateways scales across a single AZ and redundancy with in one AZ

## Routing table 
- Each subnet should be connected to a route table.
- The table controls the routing of the subnet.
- One subnet can be connected to only one route table
- A route table can associate with multiple subnet
- VPC comes with a main route table which can be modified
- We can create custom route tables
- If we do not explicitly specify which route table a subnet is connected to , it will connect to the main route table implicitly

## Network ACL vs Security Groups

Comparison of N/w ACL vs SG:
http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html

For SG everything is deny by default, thus it has only allow rules
When we create our VPC a n/w ACL is created by default.
Default n/w ACL , all inbound and outbound traffic allow automatically.
For custom n/w ACL, all inbound and outbound traffic denied by default.
One subnet can only be associated with one n/w ACL
Each subnet in a vpc must be associated with a n/w ACL. Default n/w ACL
Add Ephemeral ports for ACL to work in both inbound and outbound property
Rule with lower number is the priority
ACL has separate inbound and outbound rules. ie. they are stateless
IP address can be blocked using ACL and not SG
Ensure that you place the DENY rules earlier in the table than the ALLOW rules that open the wide range of ephemeral ports.
Security Group consolidates all rules and evaluates all of them before deciding if traffic is allowed

ELB: Elastic Load Balancers
If you want anything highly avialable , if u need atleat two public subnets to configure load balancer

## NAT vs Bastions 
When configuring the NAT, ur machine gets access to internet via NAT instance, but people using internet cannot to ssh or rdp to this host which is sitting in private subnet.  Thus Bastions(JumpBoxes/JumpHosts) comes into play. They allow to ssh or rdp into a bastion and initiate a private connection/nw to private boxes. We need to put Bastion in public subnet. For autoscaling u may need to put bastion instance in two public subnets for HA


## Elastic Network Interfaces(ENI)
It’s a virtual n/w interface that you can attach to an instance in a VPC
It’s available only for instances running in a VPC
You can create ENI, attach it to an instance, detach it from an instance, and attach it to another instance.
When you move a n/w interface from one instance to another, n/w traffic is redirected to the new instance
Each instance in a VPC has a default network interface, called primary network interface(eth0)
You cannot detach a primary netwrok interface, but you can create and attach additional ENI
Max number of ENI you can use varies by instance type

## VPC Peering
- VPC peering is simply a connection between two VPCs that enables you to route traffic between them using private IP addresses
- Instances in either VPC can communicate with each other as if they are within the same network.
- You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account with a single region
- You cannot do VPC peering across multiple regions
- AWS uses the existing infrastruture of a VPC to create a VPC peering connection; it is neither a gateway nor a VPN connection and does not rely on a separate piece of physical hardware
- There is no single point of failure for communication or a bandwidth bottleneck
- Overlapping/Matching CIDR block won’t allow VPC peering For eg: 10.0.0.0/16 and 10.0.0.0/24 can’t peer
- Transitive peering is not supported
- Allows you to connect one VPC with another via a direct route using private IP addresses
- Instances behave as if they were on same private n/w
- You can peer vpc’s with other AWS accounts as well as with other VPC’s in the same account
- Peering is a star configuration ie. 1 central VPC peers with 4 others. NO TRASITIVE PEERING

General Things:
We cannot delete VPC’s until the instances are alive. So terminate the instances before deleting VPC

Same is the case with Load 

## VPC Flow Logs

This feature enables you to capture information about IP traffic going to and from network interfaces in your VPC.  Flowlogs are stored using Cloudwatch logs

Flow logs can help you with a number of tasks; for example, to troubleshoot why specific traffic is not reaching an instance, which in turn can help you diagnose overly restrictive security group rules. You can also use flow logs as a security tool to monitor the traffic that is reaching your instance.

At subnet we need to modify public IP setting ie. Enable Auto-assign public IP, to assing public iP to the EC2 instance belonging to a subnet



FAQs: https://aws.amazon.com/vpc/faqs/
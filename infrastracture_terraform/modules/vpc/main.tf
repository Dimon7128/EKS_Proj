 resource "aws_vpc" "main" {
  cidr_block             = var.cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "main"
  }
}

resource "aws_internet_gateway" "igw" {
    vpc_id = aws_vpc.main.id
		tags = {
    Name = "main-igw"
  }
  }

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "public-rt"
  }
}
resource "aws_route_table_association" "public_a_rt_assoc" {
  subnet_id      = aws_subnet.public_A.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "public_b_rt_assoc" {
  subnet_id      = aws_subnet.public_B.id
  route_table_id = aws_route_table.public_rt.id
}


resource "aws_eip" "nat_eip" {
  domain = "vpc"

  tags = {
    Name = "nat_eip"
  }
}

resource "aws_nat_gateway" "nat_gateway" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = aws_subnet.public_A.id

  tags = {
    Name = "nat_gateway"
  }
}

resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block    = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gateway.id
  }

  tags = {
    Name = "private-rt"
  }
}

resource "aws_route_table_association" "private_a_rt_assoc" {
  subnet_id      = aws_subnet.private_A.id
  route_table_id = aws_route_table.private_rt.id
}

resource "aws_route_table_association" "private_b_rt_assoc" {
  subnet_id      = aws_subnet.private_B.id
  route_table_id = aws_route_table.private_rt.id
}


resource "aws_subnet" "private_B" { 
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.cidr_block_private_B
  availability_zone = var.AZ_B

  tags = {
    Name                               = "private_B"
    "kubernetes.io/cluster/my-cluster" = "owned"
    
  }
}


resource "aws_subnet" "private_A" { 
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.cidr_block_private_A
  availability_zone = var.AZ_A

  tags = {
    Name                               = "private_A"
    "kubernetes.io/cluster/my-cluster" = "owned"
   
  }
}

resource "aws_subnet" "public_A" { 
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.cidr_block_public_A
  availability_zone = var.AZ_A

  tags = {
    Name = "public_A"
  }
}


resource "aws_subnet" "public_B" { 
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.cidr_block_public_B
  availability_zone = var.AZ_B

  tags = {
    Name = "public_B"
  }
}


  



# Define other resources like subnets, IGW, NAT Gateway here, using variables where needed


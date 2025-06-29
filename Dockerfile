# ZERO Platform - Security Tools Container
# © 2025 ZERO Platform. All rights reserved.

FROM kalilinux/kali-rolling

# Update and install basic tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nmap \
    nikto \
    dirb \
    whatweb \
    wpscan \
    masscan \
    hping3 \
    dnsenum \
    snmp \
    hydra \
    john \
    hashcat \
    cewl \
    crunch \
    metasploit-framework \
    apktool \
    aircrack-ng \
    reaver \
    wifite \
    hcxtools \
    bettercap \
    bluez \
    bluez-tools \
    ettercap-text-only \
    dsniff \
    mitmproxy \
    sslstrip \
    netsniff-ng \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install additional tools
RUN pip3 install objection drozer

# Create working directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

# Expose port
EXPOSE 12000

# Run the application
CMD ["python3", "app.py"]
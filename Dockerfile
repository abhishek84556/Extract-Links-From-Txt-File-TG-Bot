FROM anasty17/mltb:latest

# Set the working directory
WORKDIR /app
RUN chmod 777 /app
# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Run the bot
CMD ["python3", "bot.py"]

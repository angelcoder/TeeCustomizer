## Welcome to the TeeCustomizer AI Chatbot!

This chatbot can:

1. **Collect user orders for a customizable t-shirt**  
   Guide users through style, color, size, and printing options, and collect all necessary details.

2. **Answer user questions using FAQs**  
   Provide factual and extensive answers.

3. **Send support requests**  
   Detect user struggles or direct requests and capture key details for the support team.

### Demo (currently running on GCP)
[http://34.123.140.86:8501/](http://34.123.140.86:8501/)

https://github.com/user-attachments/assets/13f3268c-2656-4ece-81cd-93b429ce6818


---

### Running the project locally:

```bash
# Clone the repository
git clone git@github.com:angelcoder/TeeCustomizer.git

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt

# Set up environment variables
touch .env
echo 'OPENAI_API_KEY="YOUR_OPENAI_KEY"' >> .env

# Run the application
chainlit run app.py -w
```
The app will run on [http://localhost:8000](http://localhost:8000).
Alternatively, for running on GCP or any other server, use (port number can be changed):

```bash


python3 -m chainlit run app.py --host 0.0.0.0 --port 8501
```


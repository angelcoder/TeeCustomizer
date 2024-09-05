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


## Next Steps:

1. **Experimenting with self-hosted LM**: using pre-trained models to understand user queries and create simple keyword-based matching for initial versions.

2. **Creating intents and entities** (using RASA). For example:
   - **Intents**: `ask_faq`, `request_support`, `check_product_availability`, `check_sizes`, `check_colors`, `ask_about_shipping`, `ask_about_delivery`...
   - **Entities**: `product_name`, `size`, `color`...

   This will solve an issue that you may encounter: when I write a message with double meaning, the customizations might get mixed up (e.g. I got style: female). But if we strict it down to intent/entity level, that could be avoided

3. **Creating a dialog management**: rules about how the chatbot should respond to different user inputs (also RASA): 

   - **Story**: User asks for sizes  
     **Steps**:  
       - `intent`: `check_sizes`  
       - `action`: `action_check_sizes`

4. **FAQ Handling**: I first tried to match user queries with the closest FAQ entries (I used  [SentenceTransformer](https://huggingface.co/sentence-transformers), however, that required prior intent classification. 
5. **Evaluating chatbot performance**: E2E (End to End) benchmarking as suggested in [this paper](https://arxiv.org/pdf/2308.04624). measuring general performance indicators, like user satisfaction, conversation completion rate (possible after production); setting up analytics, creating tests for measuring the success of intent/entities/other extractions.

If we are talking about  intent recognition, then this can be **precision**, **recall**, and **f1 score**. score for an ML model

6. **Multilingual support** can be done via automatic language detection(langdetect, polyglot) and then their translations, or using Multilingual NLP Models ([mBERT](https://huggingface.co/google-bert/bert-base-multilingual-cased), [XLM-R](https://huggingface.co/FacebookAI/xlm-roberta-base)). I used gpt-4 (you can also play and see that it support ukrainian, I also experimented with spanish and estonian). I googled integration of translation APIs, but won’t it just increase the latency? I would go with the first few suggested approaches.



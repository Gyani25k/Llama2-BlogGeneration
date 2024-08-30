import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import time

@st.cache_resource
def load_llama_model():
    """Load the LLaMa model only once to improve performance."""
    return CTransformers(
        model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={'max_new_tokens': 256, 'temperature': 0.01}
    )

def get_llama_response(input_text, no_words, blog_style):
    """Generate a response from the LLaMa 2 model based on the input parameters."""
    # Load the model
    llm = load_llama_model()

    # Prompt template
    template = """
        Write a blog for a {blog_style} job profile on the topic "{input_text}"
        within {no_words} words.
    """
    
    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )
    
    # Generate the response
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    
    return response

# Streamlit UI setup
st.set_page_config(
    page_title="Generate Blogs Using LlaMa 2",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('Number of Words')
with col2:
    blog_style = st.selectbox(
        'Writing the blog for', 
        (
            'Researchers', 
            'Data Scientist', 
            'Common People', 
            'Students', 
            'Educators', 
            'Entrepreneurs', 
            'Healthcare Professionals', 
            'Engineers', 
            'Marketing Professionals', 
            'Artists', 
            'Technologists'
        ), 
        index=0
    )

submit = st.button("Generate")

# Input validation and response generation with progress timeline
if submit:
    if not input_text:
        st.error("Please enter a blog topic.")
    elif not no_words.isdigit() or int(no_words) <= 0:
        st.error("Please enter a valid number of words.")
    else:
        no_words = int(no_words)  # Convert no_words to an integer
        
        progress_bar_placeholder = st.empty()
        status_placeholder = st.empty()
        
        with st.spinner('Generating your blog...'):
            # Initialize progress bar and status messages
            progress_bar = progress_bar_placeholder.progress(0)
            
            # Step 1: Load model
            status_placeholder.write("🟢 **Step 1: Loading model...**")
            llm = load_llama_model()
            time.sleep(1)  # Simulate model loading
            progress_bar.progress(33)
            
            # Step 2: Pass prompt
            status_placeholder.write("🟠 **Step 2: Passing prompt...**")
            template = """
                Write a blog for a {blog_style} job profile on the topic "{input_text}"
                within {no_words} words.
            """
            prompt = PromptTemplate(
                input_variables=["blog_style", "input_text", "no_words"],
                template=template
            )
            time.sleep(1)  # Simulate prompt preparation
            progress_bar.progress(66)
            
            # Step 3: Create blog
            status_placeholder.write("🔵 **Step 3: Creating blog...**")
            response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
            time.sleep(1)  # Simulate blog creation
            progress_bar.progress(100)
        
        # Clear progress and status once the blog is generated
        progress_bar_placeholder.empty()
        status_placeholder.empty()
        
        # Display the generated blog
        st.write("✅ **Blog created successfully!**")
        st.write(response)

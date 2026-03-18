import streamlit as st
import random
import string
import requests
import io
from PyPDF2 import PdfMerger

# --- NAVIGATION SIDEBAR ---
st.sidebar.title("My Python Portfolio")
project = st.sidebar.radio("Select a Project", [
    "Secret Code Language", 
    "Snake Water Gun Game", 
    "Library Manager", 
    "PDF Merger", 
    "News App", 
    "Water Reminder"
])

# --- PROJECT 1: SECRET CODE ---
if project == "Secret Code Language":
    st.title("🔐 Secret Code Language")
    
    msg = st.text_input("Enter message:")
    mode = st.radio("Action:", ["Coding", "Decoding"])
    
    if st.button("Process Text"):
        words = msg.split(" ")
        new_words = []
        
        def get_chars(): return ''.join(random.choices(string.ascii_lowercase, k=3))

        for word in words:
            if mode == "Coding":
                if len(word) >= 3:
                    res = get_chars() + word[1:] + word[0] + get_chars()
                    new_words.append(res)
                else:
                    new_words.append(word[::-1])
            else: # Decoding
                if len(word) >= 3:
                    st_new = word[3:-3]
                    res = st_new[-1] + st_new[:-1]
                    new_words.append(res)
                else:
                    new_words.append(word[::-1])
        
        st.success(f"Result: {' '.join(new_words)}")

# --- PROJECT 2: SNAKE WATER GUN ---
elif project == "Snake Water Gun Game":
    st.title("🐍 Snake Water Gun")
    
    youDict = {"Snake": 1, "Water": -1, "Gun": 0}
    revDict = {1: "Snake", -1: "Water", 0: "Gun"}
    
    choice = st.selectbox("Your Choice:", ["Snake", "Water", "Gun"])
    if st.button("Play"):
        comp = random.choice([-1, 0, 1])
        you = youDict[choice]
        
        st.write(f"Computer chose: **{revDict[comp]}**")
        
        if comp == you: st.warning("It's a Draw!")
        elif (comp == -1 and you == 1) or (comp == 1 and you == 0) or (comp == 0 and you == -1):
            st.success("You Win! 🎉")
        else:
            st.error("You Lose! 💀")

# --- PROJECT 3: LIBRARY MANAGER ---
elif project == "Library Manager":
    st.title("📚 Library Manager")
    
    # Using Session State to keep the list alive in the browser
    if 'books' not in st.session_state:
        st.session_state.books = ["Harry Potter", "Naruto"]

    new_book = st.text_input("Add a new book:")
    if st.button("Add Book"):
        if new_book:
            st.session_state.books.append(new_book)
            st.rerun()

    st.write(f"Total Books: {len(st.session_state.books)}")
    for b in st.session_state.books:
        st.text(f"📖 {b}")

# --- PROJECT 4: PDF MERGER ---
elif project == "PDF Merger":
    st.title("📄 PDF Merger")
    st.info("Upload multiple PDFs to merge them into one.")
    
    uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type="pdf")
    
    if st.button("Merge PDFs"):
        if uploaded_files:
            merger = PdfMerger()
            for pdf in uploaded_files:
                merger.append(pdf)
            
            output = io.BytesIO()
            merger.write(output)
            st.download_button("Download Merged PDF", data=output.getvalue(), file_name="merged.pdf")
        else:
            st.error("Please upload files first.")

# --- PROJECT 5: NEWS APP ---
elif project == "News App":
    st.title("📰 Real-time News")
    query = st.text_input("Topic (e.g., Cricket, Tech):", "India")
    
    if st.button("Get News"):
        api_key = "dbe57b028aeb41e285a226a94865f7a7"
        url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"
        r = requests.get(url)
        data = r.json()
        
        for art in data.get("articles", [])[:10]:
            st.subheader(art['title'])
            st.write(art['description'])
            st.write(f"[Read more]({art['url']})")
            st.divider()

# --- PROJECT 6: WATER REMINDER ---
elif project == "Water Reminder":
    st.title("💧 Water Reminder")
    st.write("On a browser, we use visual alerts instead of desktop popups.")
    
    minutes = st.number_input("Remind me every (minutes):", min_value=1, value=60)
    if st.button("Start Reminder"):
        st.success(f"Reminder set for every {minutes} minutes!")
        st.toast(f"Stay Hydrated! Next reminder in {minutes} min.")
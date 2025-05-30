import streamlit as st

st.title("Hello, Chai App!")
st.subheader("Brewed Streamlit app.")
st.write("Choose your favourite variety of chai.")
st.text(
    "Welcome to your first Streamlit application. You can use this framework to build interactive web applications with Python"
)

chai = st.selectbox(
    "Your favourite chai",
    ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Lemon Chai", "Green Tea Chai"],
)
st.write(f"You chose: {chai}. Excellent choice!")

st.success("Enjoy your cup of chai! ☕")

if st.button("Make Chai"):
    st.balloons()
    st.write("Chai is being prepared... ☕")
    add_masala = st.checkbox("Add Masala")
    st.write("Masala added! Enjoy your spicy chai!")
else:
    st.write("Chai preparation is on hold. Please click the button to make chai.")
tea_type = st.radio(
    "What type of tea do you prefer?",
    ("Black Tea", "Green Tea", "Herbal Tea", "Keshar Tea", "Milk Tea"),
)
st.write(f"You prefer: {tea_type}. That's a great choice!")

st.title("Chai Preferences")
st.write("Customize your chai experience.")
sugar_level = st.slider("Sugar Level", 0, 10, 5)
st.write(f"Sugar level set to: {sugar_level}")

flavour = st.selectbox(
    "Choose a flavour",
    ["Adrak", "Mint", "Cardamom", "Ginger", "Masala", "Lemon", "Tulsi"],
)
st.write(f"You chose: {flavour}")

cups = st.number_input("Number of cups", min_value=1, max_value=10, value=1)
st.write(f"How many cups will you take {cups} cup(s) of chai.")

name = st.text_input("Enter your name", placeholder="Your Name")
st.write(f"Welcome, {name}!")

dob = st.date_input("Enter your date of birth")
st.write(f"Your date of birth is: {dob}")

st.title("Chai Feedback")
feedback = st.text_area("Share your feedback about the chai app:")
if feedback:
    st.write("Thank you for your feedback!")
    st.write(f"Feedback: {feedback}")
else:
    st.write("No feedback provided yet. Please share your thoughts!")

st.title("Chai Taste Poll")
col1, col2 = st.columns(2)
with col1:
    st.header("Adrak Chai")
    vote1 = st.button("Vote for Adrak Chai?")
with col2:
    st.header("Masala Chai")
    vote2 = st.button("Vote for Masala Chai")

if vote1:
    st.write("You voted for Adrak Chai! A classic choice!")
if vote2:
    st.write("You voted for Masala Chai! A spicy favorite!")

st.image(
    "https://images.unsplash.com/photo-1567922045116-2a00fae2ed03?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8dGVhfGVufDB8fDB8fHww",
    width=200,
    caption="Enjoying a cup of chai!",
)
st.image(
    "https://plus.unsplash.com/premium_photo-1692049123825-8d43174c9c5c?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8dGVhfGVufDB8fDB8fHww",
    width=200,
    caption="Exploring tea gardens with friends!",
)

st.write("Thank you for sharing your chai preferences!")
sidebar_name = st.sidebar.text_input("Enter your name", placeholder="Your Name", key="sidebar_name")
sidebar_tea = st.sidebar.selectbox("Choose your tea", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Lemon Chai", "Green Tea Chai"], key="sidebar_tea")
st.sidebar.write(f"Welcome, {sidebar_name} and your chai is getting ready!")

with st.expander("Show Chai Making Process"):
    st.write("1. Boil water.")
    st.write("2. Add tea leaves and spices.")
    st.write("3. Simmer for a few minutes.")
    st.write("4. Strain and serve hot with milk or lemon.")# Add a new line
    st.write("5. Enjoy your delicious cup of chai!")
st.write("Thank you for using the Chai App!")
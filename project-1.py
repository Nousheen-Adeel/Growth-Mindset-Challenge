import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🔆")
st.header("Welcome to the web")
st.title("🌱 Growth Mindset Challenge")
st.write("An interactive web app to help you develop a growth mindset!")

st.subheader("🚀 What is a Growth Mindset?")
st.write("""
A **Growth Mindset** means believing that intelligence and abilities can improve through dedication, learning, and effort.
Unlike a **Fixed Mindset**, which assumes talent is static, a growth mindset helps you view challenges as opportunities.
""")

st.subheader("💡 Why Should You Adopt a Growth Mindset?")
st.markdown("""
✅ **Embrace Challenges** – Treat difficulties as opportunities to grow.  
✅ **Learn from Mistakes** – Every failure is a stepping stone toward improvement.  
✅ **Stay Persistent** – Keep going even when things get tough.  
✅ **Celebrate Effort** – Success is not just about talent but consistent hard work.  
✅ **Keep an Open Mind** – Be adaptable and always ready to learn new things.
""")

# Interactive Quiz
st.subheader("🧠 Growth Mindset Self-Check")
st.write("Answer the following questions to see how strong your growth mindset is!")

questions = [
    "What do you do when you face a tough challenge?",
    "How do you feel when you make a mistake?",
    "What do you believe about intelligence?",
    "How do you react to criticism?",
    "What do you do when something feels too hard?",
    "How do you view the success of others?",
    "What motivates you to improve?",
    "What do you think about asking for help?",
    "When you fail, what’s your next step?",
    "How do you handle something you’re not good at?"
]

options = [
    ["Give up", "Keep trying and learn from mistakes", "Avoid it"],
    ["Feel like a failure", "Learn from it", "Ignore it"],
    ["It can grow with effort", "It's fixed", "Only some are born smart"],
    ["Feel hurt", "Use it to improve", "Avoid it"],
    ["Avoid it", "Break it down and try", "Wait for someone else to do it"],
    ["Feel jealous", "Feel inspired", "Ignore them"],
    ["Being better than others", "Learning and growth", "Getting rewards"],
    ["It’s weak", "It’s smart", "It’s unnecessary"],
    ["Give up", "Reflect and try again", "Blame others"],
    ["Accept and practice more", "Avoid it", "Feel embarrassed"]
]

score = 0
positive_answers = [
    "Keep trying and learn from mistakes",
    "Learn from it",
    "It can grow with effort",
    "Use it to improve",
    "Break it down and try",
    "Feel inspired",
    "Learning and growth",
    "It’s smart",
    "Reflect and try again",
    "Accept and practice more"
]

for i in range(len(questions)):
    response = st.radio(f"Q{i+1}. {questions[i]}", options[i], index=None, key=f"q{i}")
    if response == positive_answers[i]:
        score += 1

# Result
if score:
    if score >= 8:
        st.success(f"✅ Awesome! You scored {score}/10. You have a strong growth mindset!")
        st.balloons()
    elif score >= 5:
        st.info(f"🌿 You scored {score}/10. You're developing a growth mindset. Keep going!")
    else:
        st.warning(f"💡 You scored {score}/10. There's room to grow. Start embracing challenges!")

# Growth Mindset Score
st.subheader("🌿 Your Self-Rated Growth Mindset Level")
progress = st.slider("How strong do you think your growth mindset is?", 0, 100, 50)
st.progress(progress / 100)
st.write(f"🌱 Your Growth Mindset Level: **{progress}%**")

# Encouragement
st.subheader("🌟 Keep Growing!")
st.write("""
Your journey in education and personal growth is about **progress, not perfection**.
Remember, every effort you put in helps you become **better than yesterday**. Keep learning, keep improving! 🚀
""")

# Footer
st.markdown("---")
st.write("📢 Share your results and challenge your friends to build a growth mindset!")
